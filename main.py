from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from calculator_logic import evaluate_expression


class Calculator(BoxLayout):

    def button_pressed(self, button_text):
        current = self.ids.result.text
        self.ids.result.text = current + button_text

    def clear_result(self):
        self.ids.result.text = ''

    def calculate_result(self):
        self.ids.result.text = evaluate_expression(self.ids.result.text)


class CalculatorApp(App):

    def build(self):
        return Calculator()


if __name__ == '__main__':
    CalculatorApp().run()
