from src.code.process import datasets
from src.code.paths import URI_UNIT
from src.code.modules import convert_int, percent_location
import matplotlib.pyplot as plt
from src.code.configuration_graph import configuration

def doencas_estados_unidos():
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
    
    plt.style.use("ggplot")
    
    plt.xlabel("Doenças mais comuns")
    plt.ylabel("Quantidade de Mortos")

    plt.title("Doenças Estados Unidos 2019")
    
    plt.xticks = rotulos
    
    
      
    plt.bar(x = causas, height= mortes)
    
    plt.show()
    
    soma_mortes = sum(mortes)
    
    pencentual_doencas = []
    
    for i in range(len(mortes)):
        pencentual_doencas.insert(i, percent_location(soma_mortes, mortes[i]))
    
    plt.title("Percentual de doenças EUA")
    plt.pie(pencentual_doencas, labels=mortes)
    plt.legend(rotulos, loc="lower left")
    
    plt.show()


def doencas_brasil():
    dados = pd.read_csv(FOLDER_MAIN + FOLDER_SAUDE + "file.csv")

    aids = 0
    chagas = 0
    tuberculose = 0
    DiarreiaEgastro = 0

    for i in range(16):
        aids += dados["Aids"][i]
        chagas += dados["Doença de Chagas"][i]
        tuberculose += dados["Tuberculose"][i]
        DiarreiaEgastro += dados["Diarréia e gastroenterite de origem infecciosa presumível"][i]

    mt = configuration()

    mt.title("Doenças de 2001 a 2017")

    mt.grid(b=True)
    mt.bar(x=["Aids", "Chagas", "Tuberculose", "Diarréia e gastroenterite de origem infecciosa presumível"],
    height=[aids, chagas, tuberculose, DiarreiaEgastro],
    width=0.4)

    mt.show()