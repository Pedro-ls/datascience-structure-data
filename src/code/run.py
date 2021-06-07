from .search import filtro
from .doencas import doencas_estados_unidos
from .imports import *

def espaco():
    print()
    print()


def main(): #-> int:    
    print("Nomes: Jaime Vaz Nogueira, Pedro Henrique da Silva")
    print("Professor: Danilo")

    a = []
    a.sort()
    while True:
        so.system("Clear") or None
        
        print("\033[1;93m")
        print("PROJETO ESTRUTURA DE DADOS")
        print("ADS MATUTINO\n\n")
        print()
        print("AVISO: Digite o numero 0 ou um numero negativo para encerrar o programa")
        print()
        print("Opções:")
        print("\t1. - Mostrar resultados populacional")
        print("\t2. - Mostrar resultados da saúde.")
        print("\t3. - filtro de doenças e paises.")
        print()

        res = 0

        try:
            print()
            res: int = int(input(
                "Insira a opção para mostrar aos resultados das opções [ '1', '2', '3' ], digite números somente: "))
            
            if (res == 0):
                res = 0
            elif(res == ""):
                res = 500
            print()
        except:
            res = 500
            
        if(res > 0):
            if(res == 1):
                print("\033[1;94m")
                so.system("Clear") or None
                print("1.1 - Mostrar Brasil.")
                populacao_brasil()
                print("1.2 - Mostrar Estados Unidos.")
                populacao_state()
                print("1.3 - Mostrar Brasil e Estados Unidos")
                brasil_state()
                espaco()
                populacional()
                espaco()
                input("continuar pressione [enter]")
            elif(res == 2):
                print("\033[1;94m")
                so.system("Clear") or None
                print("2.1 - Mostrar Brasil.")
                
                # colocar aqui a condição do Brasil                
                
                print("2.2 - Mostrar Estados Unidos.")
                
                doencas_estados_unidos()
                
                print("2.3 - Mostrar Brasil e Estados Unidos")
                
                # comparar Estados Unidos e Brasil 
                
                input("continuar pressione [enter]")
            elif(res == 3):
                resposta = True
                
                so.system("Clear") or None

                print("\033[1;93m")                
                while resposta == True:
                    print("insira sua busca: ")
                    print("Para pesquisar sobre paises digite o nome de um pais serão mostradas algumas informações principais dos paises.")
                    print("Para procurar a doença é só digitar a palavra 'doença'")
                    print("exemplo 'doença'")
                    print("Digite sua pesquisa: ", end="")
                    busca = input()
                    
                    filtro(busca)
                    
                    resposta = input("Deseja continuar digite S, para sair N").upper() == "S"
                    so.system("Clear") or None

                    print("\033[1;93m")
                
            elif(res == 500):
                print("\033[1;31m")
                so.system("Clear") or None
                print("você tem que digitar apenas os números indicados")
                input("continuar pressione [enter]")
        else:
            print("\033[1;32m")
            so.system("Clear") or None
            print("FIM DO PROGRAMA ... ")
            print("todos os arquivos estão salvos na pasta output ...")
            print("Obrigado pela Atenção!!!!")

            print("DATASCIENCE PROFESSOR DANILO")

            break
        
    return int(0)