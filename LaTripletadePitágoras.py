
import math


"""
Una tripleta de Pitágoras es una serie de tres números enteros, a < b < c, donde:
a 2 + b 2 = c 2
Por ejemplo, 3 2 + 4 2 = 5 2 ∴ 9 + 16 = 25.
Existe solo una tripleta de Pitágoras para la cual a + b + c = 1000.
¿Cuál es el producto de abc?
"""

def pitagoras(perimetro):

    for i in range(perimetro):
        for k in range(perimetro):
            if (  i + k + math.sqrt( (i**2) + (k**2) ) == 1000  ): 
                if (i !=0 and k != 0):
                   c = math.sqrt(i**2 + k**2)
                   print ("\n")
                   print ("Una tripleta de Pitágoras es una serie de tres números enteros, a < b < c, donde:")
                   print ("a^2 + b^2 = c^2")
                   print ("Por ejemplo, 3^2 + 4^2 = 5^2 ∴ 9 + 16 = 25.")
                   print ("Existe solo una tripleta de Pitágoras para la cual a + b + c = 1000.")
                   print ("¿Cuál es el producto de abc?")
                   print ("\n")
                   print ("solucion : ")
                   print ("\n")
                   print ("a =", i, ",", "b =", k, "c =", int(c))  
                   print ("\n")
                   print (i, "+", k, "+", int(c), "=", (i+k+int(c)))
                   print ("\n")
                   print ("############################")
                   print ("\n")
                   return 


pitagoras(1000)
