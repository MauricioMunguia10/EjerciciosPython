#Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
#separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
print("\nCesta de compras\n")
cesta=input("Ingrese lps elementos de la cesta de compras separados por comas:")
print("La lista de compras es:\n")
for n in cesta.split(', '):
    print(n)