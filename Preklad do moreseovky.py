def Preklad() :
    global i 
    if i in ["A", "a", "Á", "á"]:
        i = ".-"
    elif i in ["B", "b"]:
        i = "-..."
    elif i in ["C", "c", "Č", "č"]:
        i = "-.-."
    elif i in ["D", "d", "Ď", "ď"]:
        i = "-.."
    elif i in ["E", "e", "É", "é", "Ě", "ě"]:
        i = "."
    elif i in ["F", "f"]:
        i = "..-."
    elif i in ["G", "g"]:
        i = "--."
    elif i in ["H", "h"]:
        i = "...."
    elif i in ["I", "i", "Í", "í"]:
        i = ".."
    elif i in ["J", "j"]:
        i = ".---"
    elif i in ["K", "k"]:
        i = "-.-"
    elif i in ["L", "l"]:
        i = ".-.."
    elif i in ["M", "m"]:
        i = "--"
    elif i in ["N", "n", "Ň", "ň"]:
        i = "-."
    elif i in ["O", "o", "Ó", "ó"]:
        i = "---"
    elif i in ["P", "p"]:
        i = ".--."
    elif i in ["Q", "q"]:
        i = "--.-"
    elif i in ["R", "r", "Ř", "ř"]:
        i = ".-."
    elif i in ["S", "s", "Š", "š"]:
        i = "..."
    elif i in ["T", "t", "Ť", "ť"]:
        i = "-"
    elif i in ["U", "u", "Ú", "ú", "Ů", "ů"]:
        i = "..-"
    elif i in ["V", "v"]:
        i = "...-"
    elif i in ["W", "w"]:
        i = ".--"
    elif i in ["X", "x"]:
        i = "-..-"
    elif i in ["Y", "y", "Ý", "ý"]:
        i = "-.--"
    elif i in ["Z", "z", "Ž", "ž"]:
        i = "--.."
    else:
        i = " "

preklad = []

print("Překlad do morzeovi věty")
veta = str(input("Napiště větu: "))
for i in veta:
    Preklad()
    preklad.append(i)
print(preklad)
