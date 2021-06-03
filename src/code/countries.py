from .imports import *
from src.code.process import datasets

## dados Populacionais

def country(src, nacionalidade):
    
    idade = 0

    PINK:str = str('#EB15E7')
    BLUE:str = str('#2036F7')

    dataframe = datasets(URI_UNIT, src)[0]
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
            mt.bar(x=data["idade"][i], height=data["masculino"][i], color=BLUE)   
            is_girl_or_boy = 0     
        else:
            mt.bar(x=data["idade"][i], height=data["feminino"][i], color=PINK)
            is_girl_or_boy = 1

        print(data["idade"][i], " -> ", data["feminino"][i])
        
        if is_girl_or_boy:
            mt.bar(x=data["idade"][i], height=data["masculino"][i], color=BLUE)

        else:
            mt.bar(x=data["idade"][i], height=data["feminino"][i], color=PINK)

    mt.legend(("Masculino", "Feminino"))

    mt.show()




def populacao_state():
    configuration()
    country("Country United States Population", "americana")


def populacao_brasil():
    configuration()
    country("Brazil Population", "brasileira")


def forr_plot_point(mt:mt, cont, fim, dadosx, dadosy, label, colors):    
    mt.scatter(dadosx[cont], dadosy[cont],color=colors, label=label)
    
    if((fim-1) == cont):
        return mt
    
    return forr_plot_point(mt, cont+1, fim, dadosx, dadosy, label, colors)
    

def populacional():
    # states = FOLDER_MAIN + FOLDER_COUNTRY + "United States of America-2020.csv"
    # brasil = FOLDER_MAIN + FOLDER_COUNTRY + "Brazil-2020.csv"

    # states = pd.read_csv(states)
    # brasil = pd.read_csv(brasil)
    states = datasets(URI_UNIT, "Country United States Population")[0]
    brasil = datasets(URI_UNIT, "Brazil Population")[0]
    
    

    brasil.columns = ["idade", "masculino", "feminino"]
    states.columns = ["idade", "masculino", "feminino"]
    
    brasil = convert_int_populacional(brasil)
    states = convert_int_populacional(states)
    
    
    feminino = states["feminino"][:] + brasil["feminino"][:]
    masculino = states["masculino"][:] + brasil["masculino"][:]
    
    

    feminino_state = sum(states["feminino"][:])
    feminino_brasil = sum(brasil["feminino"][:])

    masculino_state = sum(states["masculino"][:])
    masculino_brasil = sum(brasil["masculino"][:])

    estados_unidos = feminino_state + masculino_state
    brazil = feminino_brasil + masculino_brasil

    masc = masculino_brasil + masculino_state
    fem = feminino_brasil + feminino_state

    soma = masc + fem

    porc_fem = (fem * 100) / soma
    porc_mas = (masc * 100) / soma

    print("Há população do estados unidos é ", estados_unidos)
    print("Há ", feminino_state , "de mulheres nos estados unidos")
    print("Há ", masculino_state , "de homens nos estados unidos")
    print("Há população do Brasil é ", brazil)
    print("Há ", feminino_state , "de mulheres nos estados unidos")
    print("Há ", masculino_state , "de homens nos estados unidos")
    print("A quantidade total de mulheres é ", fem)
    print("A quantidade total de homens é ", masc)
    print("Somando as mulheres e somando os homens dos dois paises conclui que: ")
    if(masc > fem):
        print("Há mais homens que mulheres")
    elif(fem > masc):
        print("Há mais mulheres que homens")
    elif(fem == masc):
        print("Há quantidade de homens é igual a de mulheres")
    print("População dos Estados Unidos e brasil somados é ", soma)
    print(f"Mulheres equivalem a {porc_fem:.2f}% da população.")
    print(f"Homens equivalem a {porc_mas:.2f}% da população.")

    configuration()

    mt.title("comportamento da população do estados unidos conforme a idade passa")

    mt.plot(brasil["idade"], feminino, color="violet")
    mt.plot(brasil["idade"], masculino, color="blue", scaley=False)

    forr_plot_point(mt, cont=0, fim=len(brasil["idade"]), dadosx=brasil["idade"], dadosy=feminino, label="feminino", colors='violet')
    forr_plot_point(mt, cont=0, fim=len(brasil["idade"]), dadosx=brasil["idade"], dadosy=masculino, label="masculino", colors='blue')

    mt.legend(["masculino", "feminino"])


    mt.show()

    mt.title("Comparação da população do estados unidos com a população do Brasil")
    mt.pie([brazil, estados_unidos], labels=[brazil, estados_unidos], colors=("green", "red"))
    mt.rcParams["legend.borderpad"] = 0.1
    mt.rcParams["legend.borderaxespad"] = 26
    mt.legend(("Brasil", "Estados Unidos"))
    mt.show()



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
