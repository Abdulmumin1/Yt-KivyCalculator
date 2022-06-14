from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class Calculator(BoxLayout):
    text_input = ObjectProperty()

    def insert_character(self, char):

        self.text_input.insert_text(char)

    def calculate(self):
        expression = self.text_input.text
        try:
            result = eval(expression)
            self.text_input.text = str(result)
        except:
            self.text_input.text = 'E'

    def clear_input(self):
        self.text_input.text = ''


class CalculatorApp(App):
    def build(self):
        return Calculator()


app = CalculatorApp()
app.run()
