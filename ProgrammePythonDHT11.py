import time
import RPi.GPIO as GPIO

PIN_DHT = 4

def lire_donnees_dht11():
    def lire_bit():
        temps_depart = time.time()
        while GPIO.input(PIN_DHT) == GPIO.LOW:
            if time.time() - temps_depart > 0.1:
                return None
        temps_depart = time.time()
        while GPIO.input(PIN_DHT) == GPIO.HIGH:
            if time.time() - temps_depart > 0.1:
                return None
        return time.time() - temps_depart > 0.00005

    donnees = []
    GPIO.setup(PIN_DHT, GPIO.OUT)
    GPIO.output(PIN_DHT, GPIO.LOW)
    time.sleep(0.02)
    GPIO.output(PIN_DHT, GPIO.HIGH)
    GPIO.setup(PIN_DHT, GPIO.IN)
    if lire_bit() is None:
        return None, None
    for i in range(40):
        donnees.append(1 if lire_bit() else 0)
    humidite = int(''.join(map(str, donnees[0:8])), 2)
    temperature = int(''.join(map(str, donnees[16:24])), 2)
    return temperature, humidite

def configurer_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

def nettoyer_gpio():
    GPIO.cleanup()

def principal():
    configurer_gpio()
    try:
        while True:
            temperature, humidite = lire_donnees_dht11()
            if temperature is not None and humidite is not None:
                print("Température: {:.1f}°C, Humidité: {:.1f}%".format(temperature, humidite))
            else:
                print("Erreur lors de la lecture du capteur.")
            time.sleep(2)
    except KeyboardInterrupt:
        print("Arrêt du programme par l'utilisateur.")
    finally:
        nettoyer_gpio()

if __name__ == "__main__":
    principal()