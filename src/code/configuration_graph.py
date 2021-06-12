from src.code.variables import *
import matplotlib.pyplot as mt 

def configuration(
        mat = mt, 
        font_size=FONT_SIZE, 
        weight=FONT_WEIGHT,
        family = FONT

    ):
    mat.style.use("ggplot")
    
    mat.rcParams["font.weight"] = weight
    mat.rcParams['font.size'] = font_size
    mat.rcParams["font.family"] = family
    
    return mat