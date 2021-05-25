from .imports import *

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