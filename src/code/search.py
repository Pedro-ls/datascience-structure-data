import pandas as pd

from pandas.core.series import Series

from .paths import URI_UNIT

from .process import datasets


def informacoes(aviso):
    
    tables = []

    data = []

    if aviso == 1:

        tables.insert(0, "Country United States Population")

    elif(aviso == 2):

        tables.insert(1, "Brazil Population")

    elif(aviso == 3):

        tables.insert(1, "Brazil Population")

        tables.insert(0, "Country United States Population")

    elif(aviso == 4):

        tables.insert(2, "Doencas Estados Unidos 2019-2020")

        tables.insert(3, "dados 2019 doencas Brasil")
    
    for table in tables:

        data.append(datasets(URI_UNIT,table)[0])
        
    return data
    
def success(busca):

    print("Você digitou: ", busca, " os resultados encontrados foram esses abaixo:")    



def show_countries(array):
    
        idade:Series = array[0]["Age"]
    
        masculino:Series = pd.to_numeric(array[0]["M"])
    
        feminino:Series = pd.to_numeric(array[0]["F\n"])
        
        total_masc = masculino.sum()
    
        total_fem = feminino.sum()
        
        maior_fem = feminino.max()
    
        menor_fem = feminino.min()
    
        maior_mas = masculino.max()
    
        menor_mas = masculino.min()
    
        mediana = masculino.median()
        
        
        dfboolean:Series = masculino == mediana
                
        for i in range(len(masculino)):
    
            if masculino[i] == menor_mas:
    
                idadeMasMenor = i
    
            if feminino[i] == menor_fem:
    
                idadeFemMenor = i
    
            if masculino[i] == maior_mas:
    
                idadeMasMaior = i
    
            if feminino[i] == maior_fem:
    
                idadeFemMaior = i
                
        indice = "False"

        for i, value in enumerate(dfboolean):
    
            if value == True:
    
                indice = i    
                
        if indice != "False":
    
            print(f"A mediana se localiza na idade {idade[indice]} e ela é {mediana}")
        
        print(f"O total de Homens é {total_masc}")
    
        print(f"O total de mulheres é {total_fem}")
    
        print(f"O total de pessoas é {total_masc + total_fem}")
    
        print()
    
        print("Maximos de idade da população e quantidade")
    
        print(f"A faixa de idade {idade[idadeMasMaior]} de idade, apresentou maior quantidade de pessoas do sexo masculino, cerca de {masculino[idadeMasMaior]}")
        
        print(f"A faixa de idade {idade[idadeFemMaior]} de idade, apresentou maior quantidade de pessoas do sexo feminino, cerca de {feminino[idadeFemMaior]}")
        
        print()
        
        print("Minimos de idade da população e quantidade")
        
        print(f"A faixa de idade {idade[idadeMasMenor]} de idade, apresentou menor quantidade de pessoas do sexo masculino, cerca de {masculino[idadeMasMenor]}")
        
        print(f"A faixa de idade {idade[idadeFemMenor]} de idade, apresentou menor quantidade de pessoas do sexo feminino, cerca de {feminino[idadeFemMenor]}")
        
        print()
        
        print("MOSTRANDO")
        
        print(" Idade", "    ", "Masculino", "    ", "Feminino")
        
        for i in range(len(idade)):
        
            print(" ", idade[i], "    ",masculino[i], "    ", feminino[i]) 



def filtro(busca:str):
    
    busca = busca.lower()
    
    if(busca in ["eua", "usa"]):
        
        array = informacoes(1)
        
        success(busca)
        
        show_countries(array)     
        

        
    elif(busca in ["brasil", "brazil"]):
        
        array = informacoes(2)
        
        success(busca)
        
        show_countries(array)
        
    elif(busca in ["doenca", "doença", "enfermidade", "problema"]):
        
        array = informacoes(4)
        
        success(busca)
        
        dataframe0:pd.DataFrame = array[0]
        
        dataframe1:pd.DataFrame = array[1]
        
        coluna_nova = dataframe0.columns[2].replace("\n", "")  
        
        colunas = [dataframe0.columns[0], dataframe0.columns[1], coluna_nova]
        
        dataframe0.columns = colunas
              
        dataframe1.insert(1, column="ANO", value=["2019"] * 28)
        
        dataframe1.columns = colunas
        
        dataframe1["PAIS"] = ["BRASIL"] * 28
        
        dataframe0["PAIS"] = ["EUA"] * 16
        
        df_data = pd.concat([dataframe0, dataframe1], ignore_index=True)
        
        print()
        print("DOENÇAS DISPONIVEIS")
        print()
        print(df_data["CAUSA DA MORTE"])
        chave = True
        while chave == True:
            
            searchBusca = str(input("Digite o nome da doença: ")).strip()
            
            resultado = df_data.loc[df_data["CAUSA DA MORTE"] == searchBusca.lower()]
            
            print(resultado)
            chave = str(input("deseja digitar outra doença digite S para Sim, qualquer outra tecla para não")).upper() == "S"
    else:
    
        print("nenhuma informação encontrada:")