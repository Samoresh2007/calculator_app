from main import Calculator

def test_addition():
    calc = Calculator()
    calc.ids = {'result': type('obj', (object,), {'text': ''})()}
    calc.button_pressed('1')
    calc.button_pressed('+')
    calc.button_pressed('2')
    calc.calculate_result()
    assert calc.ids['result'].text == '3'
