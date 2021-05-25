from pandas.core.frame import DataFrame
from src.code.variables import ROW_COUNTRY
from src.code.paths import URI_UNIT

def process(src):
    
    tables = []
    
    file = open(src, "r")
    
    instance_file = list(file)
    
    indices = []
    sum_plus = 0

    
    for i, l in enumerate(instance_file):
        b = l[0:18] == ROW_COUNTRY

        if(b):
            content = l[18:]
            tables.append({ "indice" : i, "table": content })
            
            indices.append(i)
            
            instance_file[i] = "NEW TABLE"
            
            sum_plus += 1
    
    lines = []
    
    qtd_tables = len(indices)
    
    for i in range(qtd_tables):
        
        
        if i == qtd_tables:
            total = (indices[i] - indices[i - 1]) - 1
            lines.append(total)
        elif i < qtd_tables - 1:
            total = (indices[i + 1] - indices[i]) - 1
            
            lines.append(total)
    
    
    for i in range(qtd_tables - 1):
        values = []
        for v in range(indices[i] + 1, (indices[i] + lines[i]) + 1):
            values.append(instance_file[v])
        
        tables[i]["data"] = values
        tables[i]["columns"] = values[0]
    
    del tables[-1]
    
    
    
    return tables


def datasets(src:str="", busca:str = ""):
    array_dataframe = process(src)
    
    disc = ""
    for i in range(len(array_dataframe)):
        data = str(array_dataframe[i]['table']).replace("\n", "")
        if data == busca:           
            
            disc = array_dataframe[i]['data']
    
    
    row_colunas = disc[0]
    
    array_dados = []
    for d in range(len(disc)):
        array_dados.append(disc[d].split(","))
    
    del array_dados[0]
    
    colunas = str(row_colunas).split(",")
    
    data = DataFrame(array_dados, columns=colunas)
    
    tamanho = len(data.columns) - 1

    value = data.columns[tamanho]

    for i, c in enumerate(data[value]):
        data[value][i] = float(c.replace("\n", ""))

    return data
    
