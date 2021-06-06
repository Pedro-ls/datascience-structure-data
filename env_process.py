def paths():
    txt = open("env")
    
    var = []
    
    for i in txt:
        valor = i.split("=")[1]
        var.append({"valor": valor})

    return var

