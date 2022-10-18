"""
Internal Validation Functions.
copyright: (c) 2022 by Pooya shirazi.
"""


from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
from convert import degrees2radians


# Internal Constants:

# Latitude
_MINLAT_RADIANS = degrees2radians(-90.0)
_MAXLAT_RADIANS = degrees2radians(90.0)

# Solar Declination
_MINSOLDEC_RADIANS = degrees2radians(-23.5)
_MAXSOLDEC_RADIANS = degrees2radians(23.5)

# Sunset Hour angle
_MINSHA_RADIANS = 0.0
_MAXSHA_RADIANS = degrees2radians(180)



def check_julian_day(
    doy : int
) -> NoReturn:
    
    """
    Description
    -----------
    Check Julian Day of the Year Is Valid.

    Parameters
    ----------
    doy : int
        Julian Day of the Year
    """
    
    if not 1 <= doy <= 366:
        raise ValueError(
            f'Julian Day (doy) Must Be in Range 1-366: {doy}'
        )



def check_latitude_radians(
    latitude : float
) -> NoReturn:
    
    """
    Description
    -----------
    Check Latitude Is Valid.

    Parameters
    ----------
    latitude : float
        Latitude [radians]
    """
    
    if not _MINLAT_RADIANS <= latitude <= _MAXLAT_RADIANS:
        raise ValueError(
            f'Latitude Outside Valid Range {_MINLAT_RADIANS} to { _MAXLAT_RADIANS} radians: {latitude}'
        )



def check_solar_declination_radians(
    sd : float
) -> NoReturn:
    
    """
    Description
    -----------
    Check Solar Declination Is Valid.
    Solar Declination Can Vary Between -23.5 and +23.5 Degrees.
    **Reference**: http://mypages.iit.edu/~maslanka/SolarGeo.pdf

    Parameters
    ----------
    sd : float
        Solar Declination [radians]
    """
    
    if not _MINSOLDEC_RADIANS <= sd <= _MAXSOLDEC_RADIANS:
        raise ValueError(
            f'Solar Declination Outside Valid Range {_MINSOLDEC_RADIANS} to {_MAXSOLDEC_RADIANS} radians: {sd}'
        )



def check_sunset_hour_angle_radians(
    sha : float
) -> NoReturn:
    
    """
    Description
    -----------
    Check Sunset Hour Angle Is Valid.
    Sunset Hour Angle Has the Range 0 to 180 Degrees.
    **Reference**: http://mypages.iit.edu/~maslanka/SolarGeo.pdf

    Parameters
    ----------
    sha : float
        Sunset Hour Angle [radians]
    """
    
    if not _MINSHA_RADIANS <= sha <= _MAXSHA_RADIANS:
        raise ValueError(
            f'Sunset Hour Angle Outside Valid Range {_MINSHA_RADIANS} to {_MAXSHA_RADIANS} radians: {sha}'
        )