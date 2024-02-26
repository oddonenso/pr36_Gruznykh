from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class CalculatorApp(App):

    def build(self):
        self.expression = ""
        layout = GridLayout(cols=4)

        self.label = Label(text="0", font_size=40, size_hint_y=None, height=100)
        layout.add_widget(self.label)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', '=', '+'
        ]

        for button in buttons:
            layout.add_widget(Button(text=button, on_press=self.on_button_press))

        return layout

    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                self.label.text = str(eval(self.expression))
            except Exception as e:
                self.label.text = "Error"
            self.expression = ""
        else:
            self.expression += instance.text
            self.label.text = self.expression


if __name__ == "__main__":
    CalculatorApp().run()
