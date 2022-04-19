"""
Library of Functions for Estimating Reference Crop Evapotransporation (ETo)
copyright: (c) 2022 by Pooya shirazi.
"""

from convert import radiation2evaporation
import math

from check import (
    check_julian_day,
    check_latitude_radians,
    check_solar_declination_radians,
    check_sunset_hour_angle_radians
)


# Solar Constant [ MJ m-2 min-1]
SOLAR_CONSTANT = 0.0820



def solar_declination(day_of_year):
    """
    Description
    -----------
    Calculate Solar declination from Day of the Year.
    **Reference**: Based on Equation 24 in Allen et al (1998).

    Parameters
    ----------
    day_of_year : int
        Day of Year - Between 1 and 365 or 366.

    Returns
    -------
    solar_dec : float
        Solar Declination [radians]
    """
    check_julian_day(day_of_year)

    return 0.409 * math.sin(((2.0 * math.pi / 365.0) * day_of_year - 1.39))



def inverse_relative_distance_earth_sun(day_of_year):
    """
    Description
    -----------
    Calculate the Inverse Relative Distance Between Earth and Sun from Day of the Year.
    **Reference**: Based on Equation 23 in Allen et al (1998).

    Parameters
    ----------
    day_of_year : int
        Day of Year - Between 1 and 365 or 366.

    Returns
    -------
    irdes : float
        Inverse Relative Distance Between Earth and Sun [radians]
    """
    check_julian_day(day_of_year)

    return 1 + (0.033 * math.cos((2.0 * math.pi / 365.0) * day_of_year))



def sunset_hour_angle(latitude, solar_dec):
    """
    Description
    -----------
    Calculate Sunset Hour Angle (*Ws*) from Latitude and Solar Declination.
    **Reference**: Based on Equation 25 in Allen et al (1998).

    Parameters
    ----------
    latitude : float
        Latitude [radians], Should Be Negative if it in the Southern Hemisphere, Positive if in the Northern Hemisphere.
    
    solar_dec : float
        Solar Declination [radians]
        *NOTE*: Can Be Calculated Using ``solar_declination()``

    Returns
    -------
    sha : float
        Sunset Hour Angle [radians]
    """
    check_latitude_radians(latitude)
    check_solar_declination_radians(solar_dec)

    cos_sha = -math.tan(latitude) * math.tan(solar_dec)

    # Domain of acos is -1 <= x <= 1 Radians
    return math.acos(min(max(cos_sha, -1.0), 1.0))



def extraterrestrial_radiation(latitude, solar_dec, sha, irdes):
    """
    Description
    -----------
    Estimate Daily Extraterrestrial Radiation (Top of the Atmosphere Radiation).
    **Reference**: Based on Equation 21 in Allen et al (1998).

    Parameters
    ----------
    latitude : float
        Latitude [radians], Should Be Negative if it in the Southern Hemisphere, Positive if in the Northern Hemisphere.
    
    solar_dec : float
        Solar Declination [radians]
        *NOTE*: Can Be Calculated Using ``solar_declination()``
    
    sha : float
        Sunset Hour Angle [radians]
        *NOTE*: Can Be Calculated Using ``sunset_hour_angle()``

    irdes : float
        Inverse Relative Distance Earth-Sun [radians]
        *NOTE*: Can Be Calculated Using ``inverse_relative_distance_earth_sun()``

    Returns
    -------
    Ra : float
        Daily Extraterrestrial Radiation [MJ m-2 day-1]
    """
    check_latitude_radians(latitude)
    check_solar_declination_radians(solar_dec)
    check_sunset_hour_angle_radians(sha)

    tmp1 = (24.0 * 60.0) / math.pi
    tmp2 = sha * math.sin(latitude) * math.sin(solar_dec)
    tmp3 = math.cos(latitude) * math.cos(solar_dec) * math.sin(sha)
    return tmp1 * SOLAR_CONSTANT * irdes * (tmp2 + tmp3)



def hargreaves_samani(tmin, tmax, tmean, ra):
    """
    Description
    -----------
    Estimate Reference Crop Evapotranspiration (ETo) Using the Hargreaves and Samani Method.
    **Reference**: Based on Equation 4 in Hargreaves and Samani (1985).

    Parameters
    ----------
    tmin : float
        Minimum Daily Temperature [Degrees Celsius]
    
    tmax : float
        Maximum Daily Temperature [Degrees Celsius]
    
    tmean : float
        Mean Daily Temperature [Degrees Celsius]
    
    ra : float
        Extraterrestrial Radiation [MJ/m2/day]
        *NOTE*: Can Be Calculated Using ``extraterrestrial_radiation()``

    Returns
    -------
    ETo : float
        Reference Crop Evapotranspiration [mm/day]
    """
    return 0.0023 * (tmean + 17.8) * (tmax - tmin) ** 0.5 * radiation2evaporation(ra)

