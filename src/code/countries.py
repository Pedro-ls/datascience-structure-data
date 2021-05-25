from .imports import *

def country(src, nacionalidade):
    
    idade = 0
    masc = 1
    fem = 2

    PINK:str = str('#EB15E7')
    BLUE:str = str('#2036F7')

    dataframe = pd.read_csv(src)
    dataframe.columns = ["idade", "masculino", "feminino"]


    idade = []
    masculino = []
    feminino = []

    data = {
        "idade": idade,
        "masculino": masculino,
        "feminino": feminino
    }

    mt.title("População "+ nacionalidade +", por idade e sexo")
    mt.xlabel("Idade de 0 a mais de 100 anos")
    mt.ylabel("População (escala real atravez da formula y x 10000000)")

    mt.rcParams["font.size"] = 8.5

    for i in range(len(dataframe)):
        idade.insert(i, dataframe.idade[i])
        masculino.insert(i,dataframe.masculino[i])
        feminino.insert(i,dataframe.feminino[i])

    print(max(data["feminino"][:]))
    print(dataframe.feminino.max())


    is_girl_or_boy = 0 # girl = 1, boy = 0

    for i in range(len(dataframe)):
        if data["masculino"][i] > data["feminino"][i]:
            bar = mt.bar(x=data["idade"][i], height=data["masculino"][i], color=BLUE)   
            is_girl_or_boy = 0     
        else:
            bar = mt.bar(x=data["idade"][i], height=data["feminino"][i], color=PINK)
            is_girl_or_boy = 1


        
        if is_girl_or_boy:
            bar = mt.bar(x=data["idade"][i], height=data["masculino"][i], color=BLUE)

        else:
            bar = mt.bar(x=data["idade"][i], height=data["feminino"][i], color=PINK)

    mt.legend(("Masculino", "Feminino"))

    mt.show()




def populacao_state():
    configuration()
    country(FOLDER_MAIN + FOLDER_COUNTRY + "United States of America-2020.csv", "americana")


def populacao_brasil():
    configuration()
    country(FOLDER_MAIN + FOLDER_COUNTRY + "Brazil-2020.csv", "brasileira")
