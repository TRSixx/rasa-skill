from mycroft import MycroftSkill, intent_file_handler


class Rasa(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('rasa.intent')
    def handle_rasa(self, message):
        self.speak_dialog('rasa')


def create_skill():
    return Rasa()

