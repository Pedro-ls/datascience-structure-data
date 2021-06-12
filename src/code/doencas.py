import pandas as pd
from src.code.search import uniao_bases_saude_eua_brasil
from src.code.process import datasets
from src.code.paths import URI_UNIT
from src.code.modules import convert_int, percent_location, tira_acento
import matplotlib.pyplot as plt

from pandas.core.series import Series
from src.code.configuration_graph import configuration

def doencas_estados_unidos():
    
    plt.figure(figsize=(12, 11))
   
    configuration()

    dataset = datasets(src=URI_UNIT, busca="Doencas Estados Unidos 2019-2020")

    data = dataset[0]

    coluna_incidentes = "TOTAL DE MORTOS\n"

    coluna_incidentes_new = "TOTAL DE MORTOS"

    new_index = list(range(0,15))

    data = data.drop(2)

    data.index = new_index

    deaths = convert_int(data[coluna_incidentes])

    data = data.drop(coluna_incidentes, axis=1)

    data[coluna_incidentes_new] = deaths

    anos = data["ANO"]
    
    mortes = []
    causas = []
    
    for i, valor in enumerate(anos):
        if(valor == "2019"): 
            causas.append(data["CAUSA DA MORTE"][i])
            mortes.append(data["TOTAL DE MORTOS"][i])
    
    
    rotulos = ["doenças do coração",
    "cancer",
    "alzheimer",
    "diabetes",
    "infruenza e pneumunia",
    "doença de kidney",
    "doenças respiratorias cronicas"]

    
    plt.xlabel = "Doenças mais comuns"
    plt.ylabel = "Quantidade de Mortos"

    plt.title("Doenças Estados Unidos 2019")
    
    plt.xticks = rotulos
    
    plt.bar(x = rotulos, height= mortes)
    
    plt.legend(loc="lower left")
    
    plt.tight_layout()
    
    plt.show()
    
    plt.figure(figsize=(12, 10))
    
    soma_mortes = sum(mortes)
    
    pencentual_doencas = []
    
    print(f"TOTAL DE MORTOS: por doenças é {soma_mortes}")
    
    for i in range(len(mortes)):
        pencentual_doencas.insert(i, percent_location(soma_mortes, mortes[i]))
    
    plt.title("Percentual de doenças EUA")
    plt.pie(pencentual_doencas, labels=mortes)
    plt.legend(rotulos, loc="lower left")
    
    plt.tight_layout()
    
    plt.show()
    

def percentual (total, elem, lista_nova, cont):
    perc = (elem * 100) / total

    formatacao = "{0:.2f}"

    retorno = formatacao.format(perc)

    lista_nova.insert(cont, retorno)

    return cont + 1


def doencas_ordenada(data, ord_data):
    vetor = [] 

    for i in ord_data:
        vetor.append(data["Causas"][i])

    return vetor 


def doencas_valores_ordenada(data, ord_data):
    vetor = [] 

    for i in ord_data:
        vetor.append(data["Quantidade de mortos\n"][i])

    return vetor



def arr(soma, doencas_valores_menor_vetor):
    vetor1 = []
    cont = 0
    for i in doencas_valores_menor_vetor:
        cont = percentual(soma, i, vetor1, cont)
    
    return vetor1



def doencas_brasil():
    
    configuration()
    
    plt.figure(figsize=(8, 9))

    dataset = datasets(src=URI_UNIT, busca="dados 2019 doencas Brasil")

    data = dataset[0]

    data["Quantidade de mortos\n"] = pd.to_numeric(data["Quantidade de mortos\n"])

    data["Causas"] = data["Causas"].apply(tira_acento)

    plt.title("Doenças Brasil 2019 (Quantidade de Mortos)")


    plt.barh(data["Causas"], data["Quantidade de mortos\n"], align="center")

    plt.tight_layout()
    plt.autoscale()
    plt.margins(0.01)
    
    plt.show()
    
    soma = data["Quantidade de mortos\n"].sum()
    mediana = data["Quantidade de mortos\n"].median()
    media = data["Quantidade de mortos\n"].mean()
    disvio = data["Quantidade de mortos\n"].std()
    variancia = data["Quantidade de mortos\n"].var()
    minimo = data["Quantidade de mortos\n"].min()
    maximo = data["Quantidade de mortos\n"].max()

    print(f"A quantidade de mortos somados é {soma}")
    print(f"A quantidade de mortos mediana é {mediana}")
    print(f"A quantidade de mortos media é {media}")
    print(f"O desvio padrão destes dados é {disvio}")
    print(f"A variância destes dados é {variancia}")

    mais = data.loc[data["Quantidade de mortos\n"] == maximo]
    menos = data.loc[data["Quantidade de mortos\n"] == minimo]

    doenca_mais = mais["Causas"][27].replace("Ã§", "ç").replace("Ã£", "ã")
    doenca_menos = menos["Causas"][6]
    
    plt.xlabel = "posição dos pontos"
    plt.ylabel = "localização dos valores"

    print(f"A doença {doenca_menos} é com menos mortes, tendo {minimo} de mortes")
    print(f"As {doenca_mais} é com mais mortes, tendo {maximo} de mortes")

    plt.figure(figsize=(12, 10))
    
    plt.title("Valores maximos, medios e minimos para doenças no Brasil")
    
    plt.scatter(["valor minimo", "valor medio", "valor maximo"], [minimo, mediana, maximo])
    plt.plot(["valor minimo", "valor medio", "valor maximo"], [minimo, mediana, maximo])

    plt.scatter(["valor minimo", "valor medio", "valor maximo"], [minimo, media, maximo])
    plt.plot(["valor minimo", "valor medio", "valor maximo"], [minimo, media, maximo])

    plt.legend(["Com mediana", "Com media"], loc = "lower right")
    
    plt.tight_layout()    
    
    plt.show()

    ordenado = data["Quantidade de mortos\n"].sort_values()

    grafico_vector_25_menores = []
    grafico_vector_25_maiores = []
    grafico_vector_25_menores2 = []
    grafico_vector_25_maiores2 = []

    i = 0
    while i <= 27:

        if i == 7:
            c = 0
        if i == 14:
            t = 0
        if i == 21:
            k = 0
            

        if(i <= 6):
            grafico_vector_25_menores.insert(i, ordenado.index[i])
            
        elif(i <= 13):
            grafico_vector_25_maiores.insert(c, ordenado.index[i])
            c += 1
            
        elif(i <= 20):
            grafico_vector_25_menores2.insert(t, ordenado.index[i])
            t += 1
            
        elif(i <= 27):
            grafico_vector_25_maiores2.insert(k, ordenado.index[i])
            k += 1
            
        
        i+=1



    doencas_menor_vetor = doencas_ordenada(data, grafico_vector_25_menores)
    doencas_maior_vetor =doencas_ordenada(data, grafico_vector_25_maiores)

    doencas_menor_vetor2 = doencas_ordenada(data, grafico_vector_25_menores2)
    doencas_maior_vetor2 =doencas_ordenada(data, grafico_vector_25_maiores2)

    soma1 = sum(grafico_vector_25_menores)
    soma2 = sum(grafico_vector_25_maiores)
    soma3 = sum(grafico_vector_25_menores2)
    soma4 = sum(grafico_vector_25_maiores2)


    vetor1 = arr(soma1, grafico_vector_25_menores)
    vetor2 = arr(soma2, grafico_vector_25_maiores)

    vetor3 = arr(soma3, grafico_vector_25_menores2)
    vetor4 = arr(soma4, grafico_vector_25_maiores2)

    plt.figure(figsize=[12, 10])

    plt.subplot(2, 2, 1)

    plt.title(f"25% das informações BRASIL DOENÇAS 01")

    plt.pie(vetor1, labels=vetor1)

    plt.legend(doencas_menor_vetor, loc="center")

    plt.subplot(2, 2, 2)

    plt.title(f"25% das informações BRASIL DOENÇAS 02")

    plt.pie(vetor2, labels=vetor2)

    plt.legend(doencas_maior_vetor, loc="center")

    plt.subplot(2, 2, 3)

    plt.title(f"25% das informações BRASIL DOENÇAS 03")

    plt.pie(vetor3, labels=vetor3)

    doencas_menor_vetor2[3] = "sistema nervoso"

    plt.legend(doencas_menor_vetor2, loc="center")

    plt.subplot(2, 2, 4)

    plt.title(f"25% das informações BRASIL DOENÇAS 04")

    plt.pie(vetor4, labels=vetor4)

    doencas_maior_vetor2[1] = "doença respitatoria"
    doencas_maior_vetor2[6] = "doença coração"
    doencas_maior_vetor2[2] = "pressão alta"


    plt.legend(doencas_maior_vetor2, loc="center")

    plt.tight_layout()

    plt.show()



def data_doencas():
    caminho = URI_UNIT

    configuration()

    df_brasil = datasets(caminho, "dados 2019 doencas Brasil")[0]
    df_eua = datasets(caminho, "Doencas Estados Unidos 2019-2020")[0]

    data = uniao_bases_saude_eua_brasil(df_eua, df_brasil)

    data["TOTAL DE MORTOS"] = pd.to_numeric(data["TOTAL DE MORTOS"])

    data["CAUSA DA MORTE"] = data["CAUSA DA MORTE"].apply(tira_acento)
    
    return data



def doencas_eua_brasil():
    
    data = data_doencas()
    
    dat = data.loc[data["ANO"] == "2019"]

    eua_old:pd.DataFrame = dat.loc[dat["PAIS"] == "EUA"]
    brasil:pd.DataFrame = dat.loc[dat["PAIS"] == "BRASIL"]

    eua_old = eua_old.drop(2)
    eua_old.index = list(range(0, 7))

    brasil = brasil.sort_values("TOTAL DE MORTOS", ignore_index=True)
    eua_old = eua_old.sort_values("TOTAL DE MORTOS", ignore_index=True)

    eua_old:pd.DataFrame = eua_old

    print()
    print()
    print("MORTES DOS ESTADOS UNIDOS E BRASIL ORDENADOS POR QUANTIDADE DE MORTOS DO MENOR PARA O MAIOR NUMERO DE MORTES")
    print()
    print("Brasil: ")
    print(brasil)
    print()
    print("Estados Unidos: ")
    print(eua_old)
    print()
    print()
    
    
    eua = eua_old.copy()

    eua['CAUSA DA MORTE'][1] = "renal"

    eua_doencas = []
    bra_doencas = []
    nome_doencas = []

    # influenza 10
    # pneumunia 25

    infruenza_pneumunia_bra = brasil["TOTAL DE MORTOS"].loc[10] + brasil["TOTAL DE MORTOS"].loc[25]
    infruenza_pneumunia_eua = eua["TOTAL DE MORTOS"].loc[0]

    nome_doencas.insert(0, "Infruenza e pneumunia")
    eua_doencas.insert(0, infruenza_pneumunia_eua)
    bra_doencas.insert(0, infruenza_pneumunia_bra)

    diabetes_eua = eua["TOTAL DE MORTOS"].loc[2]
    diabetes_bra = brasil["TOTAL DE MORTOS"].loc[24]

    nome_doencas.insert(1, "Diabetes")
    eua_doencas.insert(1, diabetes_eua)
    bra_doencas.insert(1, diabetes_bra)

    alzheimer_eua = eua["TOTAL DE MORTOS"].loc[3]
    alzheimer_bra = brasil["TOTAL DE MORTOS"].loc[20]

    nome_doencas.insert(2, "Alzheimer")
    eua_doencas.insert(2, alzheimer_eua)
    bra_doencas.insert(2, alzheimer_bra)

    cancer_eua = eua["TOTAL DE MORTOS"].loc[5]
    cancer_brasil = brasil["TOTAL DE MORTOS"].loc[26]

    nome_doencas.insert(3, "Cancer")
    eua_doencas.insert(3, cancer_eua)
    bra_doencas.insert(3, cancer_brasil)

    coracao_eua = eua["TOTAL DE MORTOS"].loc[6]
    coracao_bra = brasil["TOTAL DE MORTOS"].loc[27]

    nome_doencas.insert(4, "Coração")
    eua_doencas.insert(4, coracao_eua)
    bra_doencas.insert(4, coracao_bra)

    respiracao_eua = eua["TOTAL DE MORTOS"].loc[4]
    respiracao_brasil = brasil["TOTAL DE MORTOS"].loc[22]


    nome_doencas.insert(5, "Respiração(crônico)")
    eua_doencas.insert(5, respiracao_eua)
    bra_doencas.insert(5, respiracao_brasil)


    plt.scatter(nome_doencas, eua_doencas, color="blue")
    plt.scatter(nome_doencas, bra_doencas, color="green")

    plt.plot(nome_doencas, eua_doencas, color="blue", label="EUA")
    plt.plot(nome_doencas, bra_doencas, color="green", label="BRASIL")

    plt.legend(["EUA", "BRASIL"], loc="best")



    plt.show()

    plt.title("Doenças presentes nos dois Paises (EUA e BRASIL)")

    for i in range(6):


        if eua_doencas[i] > bra_doencas[i]:
            plt.bar(nome_doencas[i], eua_doencas[i], label="EUA", color="red", align = "center")
        elif eua_doencas[i] < bra_doencas[i]:
            plt.bar(nome_doencas[i], bra_doencas[i], label="BRASIL", color="green", align = "center")
            
        
        if bra_doencas[i] > eua_doencas[i]:
            plt.bar(nome_doencas[i], eua_doencas[i], label="EUA", color="red", align = "center" )
        elif bra_doencas[i] < eua_doencas[i]:
            plt.bar(nome_doencas[i], bra_doencas[i], label="BRASIL", color="green", align = "center") 
            
    plt.legend(["EUA", "BRASIL"], loc="best")
                

    plt.show()


    eua_doencas:Series = Series(eua_doencas)
    bra_doencas:Series = Series(bra_doencas)


    soma_eua = eua_doencas.sum()
    soma_bra = bra_doencas.sum()

    soma = soma_eua + soma_bra

    print("A soma das doenças analisadas nos EUA é ", soma_eua)
    print("A soma das doenças analisadas no Brasil é ", soma_bra)


    eua_percent = percent_location(soma, eua_doencas.sum())
    bra_percent = percent_location(soma, bra_doencas.sum())

    text_format = "{:.3f}"

    eua_percent = text_format.format(eua_percent)
    bra_percent = text_format.format(bra_percent)
    plt.figure(figsize=[12, 10])

    plt.subplot(1, 2, 1)


    plt.title("Comparação de doenças semelhantes nos EUA e no BRASIL")

    plt.pie([eua_percent, bra_percent], labels = [str(eua_percent)+"%", str(bra_percent)+"%"], colors=["blue", "green"], startangle = 75.0, shadow=True, explode=(0.1, 0), rotatelabels=True)

    plt.legend(["EUA", "BRASIL"], loc="lower left")

    soma_paises = eua_doencas[:] + bra_doencas[:]

    soma_eua_brasil_doencas = soma_paises.sum()

    soma_paises.median()
    soma_paises.mean()

    tamanho_bbrasil = percent_location(soma_eua_brasil_doencas, bra_doencas.sum())
    tamanho_eeua = percent_location(soma_eua_brasil_doencas, eua_doencas.sum())

    plt.subplot(1, 2, 2)

    plt.title("Percentual Estados Unidos e Brasil em algumas doenças semelhantes")

    plt.bar("Percentual (%)", height=tamanho_eeua, color="blue", label="EUA")
    plt.bar("Percentual (%)", height=tamanho_bbrasil, color="green", label="BRASIL")

    plt.ylabel = "percentual de pessoas (%, sabendo que 100% é a soma toria dos dois)"

    plt.legend(loc="lower left")

    plt.margins(x=2)

    plt.tight_layout()

    plt.show()

    plt.figure(figsize=(12, 11))
    
    plt.title("SOMA DA QUANTIDADE DE MORTOS POR DOENÇAS NO ESTADOS UNIDOS E NO BRASIL POR DOENÇA")

    plt.xlabel = "Doenças"
    plt.ylabel = "Quantidade de mortos"
    
    plt.bar(nome_doencas, soma_paises)
    
    plt.legend(loc="best")

    print("SOMA DA QUANTIDADE DE MORTOS POR DOENÇAS NO ESTADOS UNIDOS E NO BRASIL POR DOENÇA")

    for i in range(6):
        print(f"{nome_doencas[i]} no brasil e no Estados Unidos somam {soma_paises[i]:.0f}")

    plt.show()  