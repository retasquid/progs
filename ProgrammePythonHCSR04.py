import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

print("+-----------------------------------------------------------+")
print("|   Mesure de distance par le capteur ultrasonore HC-SR04   |")
print("+-----------------------------------------------------------+")

Trig = 23
Echo = 24

GPIO.setup(Trig,GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)

GPIO.output(Trig, False)

repet = input("Entrez un nombre de repetitions de mesure : ")

for x in range(repet):

   time.sleep(1)

   GPIO.output(Trig, True)
   time.sleep(0.00001)
   GPIO.output(Trig, False)

   while GPIO.input(Echo)==0:  ## Emission de l'ultrason
     debutImpulsion = time.time()

   while GPIO.input(Echo)==1:   ## Retour de l'Echo
     finImpulsion = time.time()

   distance = round((finImpulsion - debutImpulsion) * 340 * 100 / 2, 1)  ## Vitesse du son = 340 m/s

   print("La distance est de : ",distance," cm")

GPIO.cleanup()