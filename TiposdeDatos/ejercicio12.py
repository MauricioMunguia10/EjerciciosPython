#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
#Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
#Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace 
#por no ser fresca y el coste final total.

print("\nPanaderia\n")
diahoy=int(input("Ingrese los panes vendidos del dia:"))
diaant=int(input("Ingrese los panes vendidos del dia anterior:"))
totaldia=round(diahoy*3.49,2)
totalayer=round(diaant*3.49*0.4,2)
total=totaldia+totalayer
new_template="""
Panes               Descuento    Total
Del dia:{dia}             0%        {totaldia}€
De ayer:{ayer}            60%       {totalayer}€

TOTAL                           {total}€
"""
print(new_template.format(dia=diahoy,ayer=diaant,totaldia=totaldia,totalayer=totalayer,total=total))