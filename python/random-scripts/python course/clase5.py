#Functions and Functional Programming
#La programacion funcional es un 
#paradigma en el que la programacion 
#se basa casi en su totalidad en funciones, 

def saludar(lang):
    def saludar_es():
        print "Hola"

    def saludar_en():
        print "Hi"

    def saludar_fr():
        print "Salut"

    lang_func = {"es": saludar_es,
                 "en": saludar_en,
                 "fr": saludar_fr}
    return lang_func[lang]

f = saludar("en")
f()



#Classes, Objects and other OOPS concepts