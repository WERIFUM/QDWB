
from typing import List, Dict, Tuple, Set, Optional, Union, Any, NoReturn
from .check import *

class ReferenceEvapotranspiration():
    
    def __init__(self):
        pass
        
    
    def hargreaves_samani(
        tmin : float,
        tmax : float,
        tmean : float,
        ra : float
    ) -> float:
        
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
            Extraterrestrial Radiation [mm/day]
            
        Returns
        -------
        ETo : float
            Reference Crop Evapotranspiration [mm/day]
        """
        
        check_greater_than(
            a=tmin,
            a_name="Tmin",
            b=tmax,
            b_name="Tmax"
        )
        
        check_greater_than(
            a=tmean,
            a_name="Tmean",
            b=tmax,
            b_name="Tmax"
        )
        
        check_greater_than(
            a=tmin,
            a_name="Tmin",
            b=tmean,
            b_name="Tmean"
        )
        
        check_between(
            a=ra,
            min=0,
            max=0.0820 * 24 * 60 * 0.408,
            name="Extraterrestrial Radiation"
        )
        
        return 0.0023 * (tmean + 17.8) * (tmax - tmin) ** 0.5 * ra
    
    
    def fao56_penman_monteith(
        delta,
        rn,
        G,
        gamma,
        tmean,
        u2,
        es,
        ea
    ) -> float:
        
        """
        Description
        -----------
        Estimate reference evapotranspiration (ETo) from a hypothetical
        short grass reference surface using the FAO-56 Penman-Monteith equation.
        **Reference**: Based on equation 6 in Allen et al (1998).
        
        Parameters
        ----------
        delta : float
            Slope of Saturation Vapour Pressure Curve [kPa/Degrees Celsius].
        
        rn : float
            Net Radiation at Crop Surface [MJ m-2 day-1].
        
        G : float
            Soil Heat Flux (G) [MJ m-2 day-1]
            
        gamma : float
            Psychrometric Constant [kPa/Degrees Celsius].
        
        tmean : float
            Mean Daily Temperature [Degrees Celsius]
        
        u2 : float
            Wind Speed at 2m Height [m/s].
        
        es : float
            Saturation Vapour Pressure [kPa].
        
        ea : float
            Actual Vapour Pressure [kPa]
            
        Returns
        -------
        ETo : float
            Reference Crop Evapotranspiration [mm/day]
        """
        
        A = 0.408 * delta * (rn - G)
        B = gamma * (900 / (tmean + 273)) * u2 * (es - ea)
        C = delta + gamma * (1 + 0.34 * u2)
        
        return (A + B) / C
        