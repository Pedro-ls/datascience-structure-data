from .imports import *
from .process import datasets

def country(src, nacionalidade):
    
    idade = 0

    PINK:str = str('#EB15E7')
    BLUE:str = str('#2036F7')

    dataframe = datasets(URI_UNIT, src)
    dataframe.columns = ["idade", "masculino", "feminino"]

    dataframe = convert_int_populacional(dataframe)
    print(dataframe)

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

        print(data["idade"][i], " -> ", data["feminino"][i])
        
        if is_girl_or_boy:
            bar = mt.bar(x=data["idade"][i], height=data["masculino"][i], color=BLUE)

        else:
            bar = mt.bar(x=data["idade"][i], height=data["feminino"][i], color=PINK)

    mt.legend(("Masculino", "Feminino"))

    mt.show()




def populacao_state():
    configuration()
    country("Country United States Population", "americana")


def populacao_brasil():
    configuration()
    country("Brazil Population", "brasileira")
