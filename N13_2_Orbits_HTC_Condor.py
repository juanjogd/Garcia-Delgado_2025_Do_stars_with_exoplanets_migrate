#!/usr/bin/env python
# coding: utf-8

import numpy             as np
import pandas            as pd
from astropy import units as astro_units


def internal_loop(resample_size_01, resample_size_02, period, ncores, data, i):
    import galpy
    from galpy.orbit import Orbit as orbit
    from galpy.potential.mwpotentials import McMillan17 as mcmillan
    from galpy.util.conversion import get_physical as gp

    from astropy.coordinates import SkyCoord as astro_coord
    from astropy.time import Time as astro_time

    orbits = {}
    orbits['CNAME']                 = []
    orbits['distance']              = []
    orbits['ang_moment_x_lx']       = []
    orbits['ang_moment_y_ly']       = []
    orbits['ang_moment_z_lz']       = []
    orbits['action_radial_jr']      = []
    orbits['action_azimuthal_jphi'] = []
    orbits['action_vertical_jz']    = []
    orbits['helio_x']               = []
    orbits['helio_y']               = []
    orbits['helio_z']               = []
    orbits['energy_tot_e']          = []
    orbits['energy_z_ez']           = []
    orbits['energy_r_er']           = []
    orbits['lsr_vel_u']             = []
    orbits['lsr_vel_v']             = []
    orbits['lsr_vel_w']             = []
    orbits['lsr_vel_uw']            = []
    orbits['vel_x_vx']              = []
    orbits['vel_y_vy']              = []
    orbits['vel_z_vz']              = []
    orbits['vel_r_vr']              = []
    orbits['vel_phi_vphi']          = []
    orbits['eccentricity']          = []
    orbits['rperi']                 = []
    orbits['rapoa']                 = []
    orbits['zmax']                  = []
    orbits['rguiding']              = []

    # setting the data in order to resample the stars -------------------------------------------------------------
    # first we need to estimate the covariance among the parameters -----------------------------------------------
    cov_data = data[['ra', 'dec', 'pmra', 'pmdec', 'RV', 'distance_50.']].iloc[i].copy().to_numpy()
    cov_data_err = data[['ra_error', 'dec_error', 'pmra_error', 'pmdec_error', 'RV error',
                         'distance_sigma']].iloc[i].copy().to_numpy()
    # generating the row-shaped data as described here: -----------------------------------------------------------
    # https://numpy.org/doc/stable/reference/generated/numpy.cov.html ---------------------------------------------

    cov_rows = []
    for covariates in range(cov_data.size):
        ## resampling each star in the individual parameters given their errors -----------------------------------
        rows = np.random.normal(cov_data[covariates], cov_data_err[covariates], resample_size_01)
        if covariates == 0:
            cov_rows = rows
        else:
            cov_rows = np.row_stack([cov_rows, rows])

    # calculating the covariance ----------------------------------------------------------------------------------
    covariance = np.cov(cov_rows)

    # resampling the star considering that this is a multivariate normal distribution (which may not be true) -----
    resample = np.random.multivariate_normal(mean=cov_data, cov=covariance, size=resample_size_02)
    resample_df = pd.DataFrame(resample, columns=['ra', 'dec', 'pmra', 'pmdec', 'RV', 'distance'])
    cname = np.full(shape=resample_size_02, fill_value=np.array(data['CNAME'].iloc[i]))
    resample_df.insert(0, 'CNAME', cname)

    # running the orbits integration for the resampled data for each star -----------------------------------------
    for r in range(resample_size_02):
        if resample_df['distance'].iloc[r] < 0:
            print(r"Object %d has distance<0 (CNAME=%s)" % (r, resample_df['CNAME'].iloc[r]))
        else:

            current_star_coord = astro_coord(ra=resample_df['ra'].iloc[r] * astro_units.degree,
                                             dec=resample_df['dec'].iloc[r] * astro_units.degree,
                                             pm_ra_cosdec=(resample_df['pmra'].iloc[r] *
                                                           astro_units.mas / astro_units.year),
                                             pm_dec=resample_df['pmdec'].iloc[r] * astro_units.mas / astro_units.year,
                                             radial_velocity=(resample_df['RV'].iloc[r] *
                                                              astro_units.km / astro_units.s),
                                             distance=resample_df['distance'].iloc[r] * astro_units.pc,
                                             frame='icrs', obstime=astro_time("J2016.0", format="jyear_str"))
            estimated_orbit = orbit(current_star_coord, **gp(mcmillan))

            estimated_orbit.integrate(period, mcmillan, method='dop853_c', numcores=ncores)

            ## appending results to dictionary --------------------------------------------------------------------
            orbits['CNAME'].append(resample_df['CNAME'].iloc[r])  # object identifier
            orbits['distance'].append(resample_df['distance'].iloc[r])  # resampled distance
            orbits['ang_moment_x_lx'].append(estimated_orbit.L()[0])  # angular momentum (x-axis)
            orbits['ang_moment_y_ly'].append(estimated_orbit.L()[1])  # angular momentum (y-axis)
            orbits['ang_moment_z_lz'].append(estimated_orbit.L()[2])  # angular momentum (z-axis)
            orbits['action_radial_jr'].append(estimated_orbit.jr())  # radial action
            orbits['action_azimuthal_jphi'].append(estimated_orbit.jp())  # azimuthal action
            orbits['action_vertical_jz'].append(estimated_orbit.jz())  # vertical action
            orbits['helio_x'].append(estimated_orbit.helioX())  # heliocentric cartesian dist. (x-axis)
            orbits['helio_y'].append(estimated_orbit.helioY())  # heliocentric cartesian dist. (y-axis)
            orbits['helio_z'].append(estimated_orbit.helioZ())  # heliocentric cartesian dist. (z-axis)
            orbits['energy_tot_e'].append(estimated_orbit.E())  # total energy
            orbits['energy_z_ez'].append(estimated_orbit.Ez())  # partitioned energy (z-axis)
            orbits['energy_r_er'].append(estimated_orbit.ER())  # partitioned energy (r-axis)
            orbits['lsr_vel_u'].append(estimated_orbit.U())  # local standard of rest vel (u-axis)
            orbits['lsr_vel_v'].append(estimated_orbit.V())  # local standard of rest vel (v-axis)
            orbits['lsr_vel_w'].append(estimated_orbit.W())  # local standard of rest vel (w-axis)
            orbits['lsr_vel_uw'].append(np.sqrt(estimated_orbit.U()**2 + estimated_orbit.W()**2))  # local standard of rest vel (uw-plane)
            orbits['vel_x_vx'].append(estimated_orbit.vx())  # mw cartesian velocity (x-axis)
            orbits['vel_y_vy'].append(estimated_orbit.vy())  # mw cartesian velocity (y-axis)
            orbits['vel_z_vz'].append(estimated_orbit.vz())  # mw cartesian velocity (y-axis)
            orbits['vel_r_vr'].append(estimated_orbit.vR())  # radial velocity
            orbits['vel_phi_vphi'].append(estimated_orbit.vphi())  # azimuthal velocity
            orbits['eccentricity'].append(estimated_orbit.e())  # eccentricity
            orbits['rperi'].append(estimated_orbit.rperi())  # radius of periapsis
            orbits['rapoa'].append(estimated_orbit.rap())  # radius of apoapsis
            orbits['zmax'].append(estimated_orbit.zmax())  # highest point in z-axis
            orbits['rguiding'].append(estimated_orbit.rguiding())  # theoretical circular radius w/ equiv.
            ## length of elliptical (real) orbit
    return orbits


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("index", help="index of the star in the file", type=int)
    parser.add_argument("--file-input", help="input file", default='orbits_HTC.csv')
    parser.add_argument("--resample-size1", default=100)
    parser.add_argument("--resample-size2", default=100)
    parser.add_argument("--ncores", default=24)
    parser.add_argument("--prefix-output", default="orbits")

    args = parser.parse_args()

    index = args.index
    file_input = args.file_input
    resample_size_01 = args.resample_size1
    resample_size_02 = args.resample_size2
    ncores = args.ncores

    file_output = f'{args.prefix_output}_{resample_size_01}x{resample_size_02}_index{index:05d}.csv'

    data = pd.read_csv(file_input)
    period = np.linspace(0, 10, 51) * astro_units.Gyr
    orbits = internal_loop(resample_size_01, resample_size_02, period, ncores, data, index)
    orbits_df = pd.DataFrame(orbits)
    orbits_df.to_csv(file_output, index=False)


if __name__ == '__main__':
    main()
