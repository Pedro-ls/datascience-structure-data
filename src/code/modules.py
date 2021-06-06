import pandas as pd

def convert_int_populacional(data:pd.DataFrame):
    data["masculino"] = pd.to_numeric(data["masculino"])
    data["feminino"] = pd.to_numeric(data["feminino"])
    
    return data


def convert_int(data:pd.DataFrame, column = ""):
    if column == "":
        return pd.to_numeric(data)
    else:
        return pd.to_numeric(data[column])
    

def percent_location(valor_total, value):
    """ 
        100     valor_total
         x         value
    """
    
    perc = (100 * value) / valor_total

    return perc
    