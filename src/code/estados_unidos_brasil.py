from .imports import *
from .process import datasets

def forr_plot_point(mt:mt, cont, fim, dadosx, dadosy, label, colors):    
    mt.scatter(dadosx[cont], dadosy[cont],color=colors, label=label)
    
    if((fim-1) == cont):
        return mt
    
    return forr_plot_point(mt, cont+1, fim, dadosx, dadosy, label, colors)


def convert_int_populacional(data:pd.DataFrame):
    data["masculino"] = pd.to_numeric(data["masculino"])
    data["feminino"] = pd.to_numeric(data["feminino"])
    
    return data
    

def populacional():
    # states = FOLDER_MAIN + FOLDER_COUNTRY + "United States of America-2020.csv"
    # brasil = FOLDER_MAIN + FOLDER_COUNTRY + "Brazil-2020.csv"

    # states = pd.read_csv(states)
    # brasil = pd.read_csv(brasil)
    states = datasets(URI_UNIT, "Country United States Population")
    brasil = datasets(URI_UNIT, "Brazil Population")
    
    

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
    
