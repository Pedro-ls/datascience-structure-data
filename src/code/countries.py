from pandas.core.frame import DataFrame
from .modules import convert_int
from .imports import *
from src.code.process import datasets


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

    print("O maior valor dentro da população feminina ",nacionalidade," é ", dataframe.feminino.max())
    print("O maior valor dentro da população masculina ",nacionalidade, " é ", dataframe.masculino.max())
    print()
    print("O valor minimo dentro da população ",nacionalidade," feminina é ", dataframe.feminino.min())
    print("O valor minimo dentro da população ",nacionalidade, " masculina é ", dataframe.masculino.min())


    is_girl_or_boy = 0 # girl = 1, boy = 0

    for i in range(len(dataframe)):
        if data["masculino"][i] > data["feminino"][i]:
            mt.bar(x=data["idade"][i], height=data["masculino"][i], color=BLUE)   
            is_girl_or_boy = 0     
        else:
            mt.bar(x=data["idade"][i], height=data["feminino"][i], color=PINK)
            is_girl_or_boy = 1

        print("Idade: ", data["idade"][i])

        print("Quantidade de mulheres ", data["feminino"][i])

        print("Quantidade de homens ", data["masculino"][i])

        print()

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


def ordena_por_campo(data, campo):
    return data.sort_values(by=campo, ignore_index=True)


def recebe_data():
    states = datasets(URI_UNIT, "Country United States Population")[0]

    brasil = datasets(URI_UNIT, "Brazil Population")[0]

    brasil.columns = ["idade", "masculino", "feminino"]
    
    states.columns = ["idade", "masculino", "feminino"]
    
    brasil = convert_int_populacional(brasil)
    
    states = convert_int_populacional(states)
    
    
    copy_brasil = brasil["masculino"] + brasil["feminino"]
    copy_states = states["masculino"] + states["feminino"]
    idades = brasil["idade"]
    
    df = DataFrame()
    
    df["Idade"] = idades
    df["BRASIL"] = copy_brasil
    df["EUA"] = copy_states
    
    return [brasil, states, df]


def populacional():
    
    brasil = recebe_data()[0]
    states = recebe_data()[1]
    
    print("ORDENAÇÂO POPULACIONAL")
    
    print()
    
    print()
    
    print("ORDENAÇÂO BRASIL")
    
    print()
    
    print("ORDENADO POR HOMENS")
    
    print(ordena_por_campo(brasil, "masculino"))
    
    print("ORDENADO POR MULHERES")
    
    print(ordena_por_campo(brasil, "feminino"))
    
    print()
    print()
    
    print("ORDENAÇÂO EUA(ESTADOS UNIDOS DA AMERICA)")
    
    print()
    
    print("ORDENADO POR HOMENS")
    
    print(ordena_por_campo(states, "masculino"))
    
    print("ORDENADO POR MULHERES")
    
    print(ordena_por_campo(states, "feminino"))
    
    print()
    
    print()
    
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
    
    print()
    
    print("Há ", feminino_state , "de mulheres nos Estados Unidos")
    
    print("Há ", masculino_state , "de homens nos Estados Unidos")
    
    print()
    
    print("Há população do Brasil é ", brazil)
    
    print()
    
    print("Há ", feminino_brasil, "de mulheres nos Brasil")
    
    print("Há ", masculino_brasil , "de homens nos Brasil")
    
    print()
    
    print("A quantidade total de mulheres nos dois paises é", fem)
    
    print("A quantidade total de homens nos dois paises é ", masc)
    
    print()
    
    print("Somando as mulheres e somando os homens dos dois paises conclui que: ")
    
    if(masc > fem):
    
        print("Há mais homens que mulheres")
    
    elif(fem > masc):
    
        print("Há mais mulheres que homens")
    
    elif(fem == masc):
    
        print("Há quantidade de homens é igual a de mulheres")

    print()

    print("População dos Estados Unidos e brasil somados é ", soma)

    print()
    
    print(f"Mulheres equivalem a {porc_fem:.2f}% da população.")
    
    print(f"Homens equivalem a {porc_mas:.2f}% da população.")
    
    print()
    print("media masculino brasil é ", brasil["masculino"].mean())
    print()
    print("A mediana masculino brasil é ", brasil["masculino"].median())
    print()
    print("A disvio padrão masculino brasil é ", brasil["masculino"].std())
    print()
    print()
    print("media feminino brasil é ", brasil["feminino"].mean())
    print()
    print("A mediana feminino brasil é ", brasil["feminino"].median())
    print()
    print("A disvio padrão feminino brasil é ", brasil["feminino"].std())
       
    print()    
    print()
    
    print()
    print("media masculino Estados Unidos da América é ", states["masculino"].mean())
    print()
    print("A mediana masculino Estados Unidos da América é ", states["masculino"].median())
    print()
    print("A disvio padrão masculino Estados Unidos da América é ", states["masculino"].std())
    print()
    print()
    print("media feminino Estados Unidos da América é ", states["feminino"].mean())
    print()
    print("A mediana feminino Estados Unidos da América é ", states["feminino"].median())
    print()
    print("A disvio padrão feminino Estados Unidos da América é ", states["feminino"].std())

    configuration()

    mt.title("comportamento da população dos dois paises conforme a idade passa (Brasil e EUA)")
    
    


    mt.plot(brasil["idade"], feminino, color="violet")
    
    mt.plot(brasil["idade"], masculino, color="blue", scaley=False)

    forr_plot_point(mt, cont=0, fim=len(brasil["idade"]), dadosx=brasil["idade"], dadosy=feminino, label="feminino", colors='violet')
    
    forr_plot_point(mt, cont=0, fim=len(brasil["idade"]), dadosx=brasil["idade"], dadosy=masculino, label="masculino", colors='blue')

    mt.legend(["feminino", "masculino"])

    mt.show()
    
    mt.title("Comparação da população do estados unidos com a população do Brasil")
    
    mt.pie([brazil, estados_unidos], labels=[brazil, estados_unidos], colors=("green", "red"))
    
    mt.rcParams["legend.borderpad"] = 0.1
    
    mt.rcParams["legend.borderaxespad"] = 26
    
    mt.legend(("Brasil", "Estados Unidos"))

    mt.show()


def brasil_state(mt = mt):

    configuration()
    
    brasil = datasets(URI_UNIT, "Brazil Population")[0]

    states = datasets(URI_UNIT, "Country United States Population")[0]
    
    brasil.columns = ("idade", "masculino", "feminino")

    states.columns = ("idade", "masculino", "feminino")
    
    mt.title("População brasileira e americana")
    
    mt.xlabel("Idade de 0 a mais de 100 anos")

    mt.ylabel("População (escala real atravez da formula y x 10000000)")
    
    total_fem = (sum(convert_int(states["feminino"])) + sum(convert_int(brasil["feminino"])))

    total_masc = (sum(convert_int(states["masculino"])) + sum(convert_int(brasil["masculino"])))
        
    mt.bar(x="Feminino", height=total_fem)

    mt.bar(x="Masculino", height=total_masc)
    
    mt.xlabel = "Idades"

    mt.ylabel = "Quantidade população"

    mt.show()