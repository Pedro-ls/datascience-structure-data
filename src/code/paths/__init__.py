from env_process import paths

FOLDER_MAIN:str = paths()[0]["valor"]
FOLDER_OUTPUT:str = paths()[1]["valor"]
URI_UNIT:str = paths()[2]["valor"].replace("Ã¡", "á")