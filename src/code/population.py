from .process import datasets
from .imports import *
def sobrepor_barras(mt, data, pais):
    is_girl_or_boy = 0 # girl = 1, boy = 0

    for i in range(len(pais)):
        if data["masculino"][i] > data["feminino"][i]:
            mt.bar(x=data["idade"][i], height=data["masculino"][i], color=BLUE)   
            is_girl_or_boy = 0     
        elif data["masculino"][i] < data["feminino"][i]:
            mt.bar(x=data["idade"][i], height=data["feminino"][i], color=PINK)
            is_girl_or_boy = 1

        
        if is_girl_or_boy == 1:
            mt.bar(x=data["idade"][i], height=data["masculino"][i], color=BLUE)
        elif is_girl_or_boy == 0:
            mt.bar(x=data["idade"][i], height=data["feminino"][i], color=PINK)

    return mt



def brasil_state(mt = mt):
    configuration()
    idade = 0

    brasil = datasets(URI_UNIT, "Brazil Population")
    states = datasets(URI_UNIT, "Country United States Population")
    brasil.columns = ["idade", "masculino", "feminino"]
    states.columns = ["idade", "masculino", "feminino"]
    brasil["feminino"]
    states["masculino"]
    idade = []
    masculino = []
    feminino = []
    data = {
        "idade": idade,
        "masculino": masculino,
        "feminino": feminino
    }
    mt.title("População Americana, por idade e sexo")
    mt.xlabel("Idade de 0 a mais de 100 anos")
    mt.ylabel("População (escala real atravez da formula y x 10000000)")
    
    for i in range(len(brasil)):
        idade.insert(i, brasil.idade[i])
        masculino.insert(i,brasil.masculino[i])
        feminino.insert(i,brasil.feminino[i])
    
    mt = sobrepor_barras(mt, data, brasil)
    mt.legend(("Masculino", "Feminino"))
    mt.show()