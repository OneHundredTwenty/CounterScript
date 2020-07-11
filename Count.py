import time
import sys

###Why the variables are not in english ###

numero = 0 ###This transtale to number by the way###

if str(sys.argv[2]) == "-u" and numero < int(sys.argv[1]):
    while not numero == int(sys.argv[1]):
        numero = numero + 1
        print("Upper countdown - "+str(numero))
elif str(sys.argv[2]) == "-d":
    numero = int(sys.argv[1]) 
    while not numero == 0 :
        print("Countdown - "+str(numero))
        numero -= 1

if not str(sys.argv[2]) == "-u" and not str(sys.argv[2]) == "-d":
    print("Argument 2 - Argument not reconized or not registred .")