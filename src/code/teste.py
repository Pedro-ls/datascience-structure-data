import pandas as pd

data1 = [
["CAUSA", "ANO", "QTD"],
["TETSE", "2020", 2000],
["TETSE", "2020", 2000],
["TETSE", "2020", 2000],
["TETSE", "2020", 2000],
["TETSE", "2020", 2000],
["TETSE", "2020", 2000],
["TETSE", "2020", 2000],
["TETSE", "2020", 2000],
["TETSE", "2020", 2000],
]
data2 = [
["TETSE", "2019", 3000],
["TETSE", "2019", 3000],
["TETSE", "2019", 3000],
["TETSE", "2019", 3000],
["TETSE", "2019", 3000],
["TETSE", "2019", 3000],
["TETSE", "2019", 3000],
["TETSE", "2019", 3000],
]


data1 = pd.DataFrame(data1, columns=["CAUSA", "ANO", "QTD"])
data2 = pd.DataFrame(data2, columns=["CAUSA", "ANO", "QTD"])

print(pd.concat([data1, data2], ignore_index=True))
