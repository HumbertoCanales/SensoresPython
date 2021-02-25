import adafruit_dht
import  RPi.GPIO as GPIO
import time

class Sensores():
    def __init__(self):
        self.ultrasonico = 0
        self.temperatura = 0
        self.humedad = 0
        self.pir = 0
    
    def getDistanciapir():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
        GPIO.setup(3, GPIO.OUT)         #LED output pin
        while True:
            i=GPIO.input(11)
            if i==0:                 #When output from motion sensor is LOW
                print("No intruders",i)
                GPIO.output(3, 0)  #Turn OFF LED
            elif i==1:               #When output from motion sensor is HIGH
                print("Intruder detected",i)
                GPIO.output(3, 1)  #Turn ON LED
                return (i)

    def getDistancia():
        sensorultra = Sensores() 
        TRIG = 23
        ECHO = 24
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)
        try:
            GPIO.output(TRIG, GPIO.LOW)
            time.sleep(2)
            GPIO.output(TRIG, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(TRIG, GPIO.LOW)
            pulso_inicio = time.time()
            if GPIO.input(ECHO) == GPIO.HIGH:
                pulso_fin = time.time()
                if GPIO.input(ECHO) == GPIO.LOW:
                    duracion = pulso_fin - pulso_inicio
                    distancia = (34300 * duracion) / 2
                    sensorultra.ultrasonico = distancia
            #print ("Distancia: %.2f cm" % distancia) 
            return(sensorultra.ultrasonico)
        except RuntimeError as error:
            print(error.args[0])
        finally:
            GPIO.cleanup()

    def getTemp_Hum():
        sensortemyhum = Sensores()
        pin = 4
        sensor = adafruit_dht.DHT22(pin)
        try:
            sensortemyhum.humedad = sensor.humidity
            sensortemyhum.temperatura = sensor.temperature 
            arreglo = [sensortemyhum.humedad, sensortemyhum.temperatura]
            return arreglo
            #print('Temperatura={0:0.1f} C  Humedad={1:0.1f}%'.format(temperatura, humedad))
        except RuntimeError as error:
            print(error.args[0])