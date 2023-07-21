#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from bardapi import Bard
import os
import speech_recognition as sr

os.environ['_BARD_API_KEY']="Put Here your Bard 'API' key"

class Recognizer:
    message = ""
    node = "/speech"
    trainingMessages = ["De ahora en adelante eres pepper, el robot de softbank", "De ahora en adelante si no sabes una respuesta responde \"No se la respuesta, preguntale a mi supervisor\""]
    r = sr.Recognizer()

    def __init__(self):
        pass

    def training(self):
        for message in self.trainingMessages:
            rospy.loginfo(message)
            reply = Bard().get_answer(message)['content']
            rospy.loginfo(reply)

    def voiceRecognition(self):
        with sr.Microphone() as source:
            rospy.loginfo("Di algo...")
            audio = self.r.listen(source)
            try:
                rospy.loginfo("Reconociendo...")
                texto = self.r.recognize_google(audio, language="ES")
                rospy.loginfo("Texto reconocido: " + texto)
                reply = Bard().get_answer(texto)['content']
                rospy.loginfo("Bard: %s", reply)
                return reply

            except sr.UnknownValueError:
                rospy.loginfo("No se pudo reconocer el audio")
                return "Lo siento no te entendí"

            except sr.RequestError as e:
                rospy.loginfo("Error al enviar la solicitud a la API de Google: {0}".format(e))
                return "Lo siento, hubo un error al calcular tu respuesta"

    def pepperPublisher(self):
        pub = rospy.Publisher('/speech', String, queue_size=10)
        rospy.init_node('pepperPub', anonymous=True)
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            message = self.voiceRecognition()
            rospy.loginfo(message)
            pub.publish(message)
            rate.sleep()

if __name__ == "__main__":
    recognition = Recognizer()

    recognition.training()
    recognition.pepperPublisher()
