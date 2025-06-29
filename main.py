from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Calculator(BoxLayout):
    def button_pressed(self, button_text):
        # Append button text to result display
        current = self.ids.result.text
        self.ids.result.text = current + button_text

    def clear_result(self):
        # Clear the result display
        self.ids.result.text = ''

    def calculate_result(self):
        # Try to evaluate the expression
        try:
            expression = self.ids.result.text
            result = str(eval(expression))
            self.ids.result.text = result
        except:
            self.ids.result.text = 'Error'

class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == '__main__':
    CalculatorApp().run()
