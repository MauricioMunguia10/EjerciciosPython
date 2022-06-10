#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, 
#y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
print("\nBusca letra\n")
sentence=input("Introzca una frase:")
vowel=input("Introduza una vocal:")

print(sentence.replace(vowel.lower(),vowel.upper()))