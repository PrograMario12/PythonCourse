trad = {
    "buen": "good", 
    "día": "morning", 
    "noche": "night", 
    "gracias": "thanks", 
    "hola": "hello"
}
frase = "hola buen día"
 
frase_trad = []
for palabra in frase.split():
    frase_trad.append(trad.get(palabra))
 
print(' '.join(frase_trad))