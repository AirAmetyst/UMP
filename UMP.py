import speech_recognition as sr
import RPi.GPIO as GPIO
from time import sleep
Motor1A = 24
Motor1B = 25
Motor1E = 26
Motor2A = 17
Motor2B = 27
Motor2E = 22

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)
    GPIO.setup(Motor2A, GPIO.OUT)
    GPIO.setup(Motor2B, GPIO.OUT)
    GPIO.setup(Motor2E, GPIO.OUT)
def forward():
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)


def backward():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)


def stop():
    GPIO.cleanup()


rec = sr.Recognizer()
rec.pause_threshold = 0.5


def listen_command():
    try:
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = rec.listen(source=mic)
            query = rec.recognize_google(audio_data=audio, language='ru-RU').lo >


        return query
    except sr.UnknownValueError:
        return "Didn't catch"


def main():
    query = listen_command()
    print(query)
    if query == "forward":
        setup()
        forward()
        sleep(5)
        stop()


main()

