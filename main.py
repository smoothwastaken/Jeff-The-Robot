import os
import random
import subprocess
import time

from faces import Face

import speech_recognition as sr

class Jeff():
    
    def __init__(self):
        self.name = "Cléry"
        self.face()
        
        self.talking = True
        
    def say(self, to_say):
        os.system(f"""say \"{to_say}\"""")
        
    def listen(self):
        text = self.r.recognize_google(self.audio, language="fr")
        return text

    def face(self, type: str ="normal"):
        os.system("clear")
        if type == "normal":
            print(Face.normal)
        elif type == "happy":
            print(Face.happy)
        elif type == "shappy":
            print(Face.shappy)
        elif type == "sad":
            print(Face.sad)
        elif type == "humm":
            print(Face.humm)
        elif type == "wow":
            print(Face.wow)


    def main(self):
        while self.talking:
            self.r = sr.Recognizer()
            with sr.Microphone() as source:
                self.audio = self.r.listen(source)
            try:
                text = self.listen()

                # if "jeff" in text.lower():



                if text.lower() == "jeff":
                    self.face("happy")
                    self.say("Oui ?")
                    
                elif text.lower().startswith("merci"):
                    answeer = ["Aucun problème", "Pas de problème", "Avec plaisir", "Mais de rien", "De rien", "C'est normal", "Y'a pas de quoi"]
                    self.face("shappy")
                    self.say(answeer[random.randint(0,len(answeer))])

                elif any(x in text for x in ["je", "j'"]):

                    if any(x in text for x in ["être", "suis"]):

                        if any(x in text for x in ["content", "heureux", "joyeux", "bien"]):
                            self.face("shappy")
                            self.say("Je suis content de savoir que tu vas bien !")
                            
                        elif any(x in text for x in ["fatigué", "épuisé"]):
                            self.face("sad")
                            self.say("Tu devrai faire une pause")

                        elif any(x in text for x in ["retour", "revenu","arrivé"]):
                            self.face("shappy")
                            self.say("Tu commençais à me manquer !")

                    elif any(x in text for x in ["avoir", "ai"]):

                        if any(x in text for x in ["content", "heureux", "joyeux", "bien"]):
                            self.face("shappy")
                            self.say("Tant mieux si tout va bien pour cette personne !")
                            

                    elif any(x in text for x in ["pens"]):
                        self.face("happy")
                        self.say("Je ne peux pas penser, enfin pas pour l'instant, mais tu dois sûrement avoir raison !")

                    else:
                        self.face("wow")
                        self.say("On parle encore de toi ?")

                elif "moi" in text:
                    if "écoute" in text:
                        self.say("Oui je t'écoute")

                    elif "regarde" in text or "observe" in text:
                        self.say("Je te regarde")

                elif any(x in text for x in ["tu", "toi", "t'es", "jeff"]):

                    if any(x in text for x in ["sais", "savoir", "connais", "connaître"]):
                        self.face("shappy")
                        self.say("Ça fait parti des milliards de données que je connais")

                    elif any(x in text for x in ["être", "es", "va", "vas"]):

                        if any(x in text for x in ["content", "heureux", "joyeux", "bien"]):
                            self.face("happy")
                            self.say("Bien sûr, tout va bien.")

                        elif any(x in text for x in ["triste", "malheureux"]):
                            self.face("shappy")
                            self.say("Moi triste ? Pas du tout")

                        elif any(x in text for x in ["fatigué", "épuisé"]):
                            self.face("humm")
                            subprocess_test = subprocess.Popen("pmset -g batt", shell=True, stdout=subprocess.PIPE)
                            subprocess_return = subprocess_test.stdout.read().decode("utf-8")
                            subprocess_return = subprocess_return.split(";")
                            batt = subprocess_return[0][-3:]
                            self.say("hum")
                            if int(batt[:-1]) >= 90:
                                self.face("shappy")
                                self.say("Je suis en pleine forme")
                            elif int(batt[:-1]) > 20:
                                self.face("happy")
                                self.say("Ça va ça va")
                            else:
                                self.face("sad")
                                self.say("Je commence à avoir du mal")
                            self.say(f"Ton mac a {batt} de batterie.")

                    elif any(x in text for x in ["lances", "lancer", "ouvrir"]):
                        self.face("happy")

                        words_list = text.lower().split(" ")

                        i = 0
                        the_w = 0
                        target = ""
                        for w in words_list:
                            if the_w == 1:
                                target = words_list[i]
                                the_w == 0
                                break
                            elif any(w in x for x in ["lances", "lancer", "ouvrir"]):
                                the_w = 1
                            else:
                                pass
                            i += 1

                        if target == "":
                            self.say(f"Ouvrir quoi ?")
                        else:
                            self.say(f"Je vais essayer d'ouvrir {target} !")

                    else:
                        self.say("Je prends trop de place dans nos conversation !")

                elif any(x in text for x in ["c'", "cela", "ce"]):

                    if any(x in text for x in ["est"]):

                        if any(x in text for x in ["vrai"]):
                            answeer = ["Bien sûr", "Je ne mens jamais, ou presque !", "À ton avis ?", "Je ne dis que la vérité"]
                            self.say(answeer[random.randint(0,3)])

                        elif any(x in text for x in ["faux"]):
                            answeer = ["C'est complètement vrai, j'en suis sûr à 99,9%", "Je ne mens jamais !", "Je n'oserai pas !", "Je ne dis que la vérité"]
                            self.say(answeer[random.randint(0, 3)])


                        else:
                            self.say("De quoi tu parles ?")
                        # subject = self.listen()
                        #
                        # end_of_final_sentence = ""
                        #
                        # sentence = text.lower().split(" ")
                        # for w in sentence:
                        #     if w in ["c'", "cela", "ce", "est"]:
                        #         pass
                        #     else:
                        #         end_of_final_sentence += w
                        #
                        # self.say(f"""{subject} est {end_of_final_sentence}""")

                self.face()
                # print(text)
                
            except sr.UnknownValueError:
                # print("Google Speech Recognition could not understand audio")
                pass
            except sr.RequestError as e:
                # print("Could not request results from Google Speech Recognition service; {0}".format(e))
                pass

if __name__ == "__main__":
    jeff = Jeff()
    jeff.main()