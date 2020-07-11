import time
import sys

numero = 0

###Finite Counter###
if str(sys.argv[2]) == "-c" and numero < int(sys.argv[1]):
    while not numero == int(sys.argv[1]):
        numero = numero + 1
        print("Upper countdown progress : "+str(numero))
elif str(sys.argv[2]) == "-d":
    numero = int(sys.argv[1]) 
    while not numero == 0 :
        print("Countdown progress : "+str(numero))
        numero -= 1

if not str(sys.argv[2]) == "-c" and not str(sys.argv[2]) == "-d":
    print("Argument 1 - Command not reconized.")
