from src.code.variables import *
import matplotlib.pyplot as mt 

def configuration(
        mat = mt, 
        color_background=BLACK,
        color_y=WHITE, 
        color_x=WHITE, 
        font_size=FONT_SIZE, 
        weight=FONT_WEIGHT,
        color_title=WHITE,
        line = WHITE,
        background = GRAY,
        family = FONT,
        color_legend = WHITE,
        hatch_color = WHITE,
        label_color = WHITE
    ):
    mat.style.use("ggplot")
    mat.rcParams['xtick.color'] = color_x
    mat.rcParams['ytick.color'] = color_y
    mat.rcParams["font.weight"] = weight
    mat.rcParams["figure.facecolor"] = color_background
    mat.rcParams['font.size'] = font_size
    mat.rcParams["axes.titlecolor"] = color_title
    mat.rcParams["axes.edgecolor"] = line
    mat.rcParams["axes.facecolor"] = background
    mat.rcParams['axes.titlepad'] = 10.0
    mat.rcParams["font.family"] = family
    mat.rcParams["hatch.color"] = hatch_color
    mat.rcParams["text.color"] = color_legend
    mat.rcParams["axes.labelcolor"] = label_color
    
    return mat