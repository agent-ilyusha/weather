# -- coding: utf-8


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from main import func_return_values, func_temperature_today


Window.title = "Прогноз погоды"
Window.clearcolor = (255, 255, 255, 1)



class MyApp(App):

    # переменные
    def __init__(self):
        super().__init__()
        self.layout_temp = GridLayout(cols=3)
        self.layout_but_inp = GridLayout(cols=2, row_force_default=True, row_default_height=100)
        self.button = Button(text="Нажми на меня")
        self.button.bind(on_press=self.on_text)
        self.city_input = TextInput(multiline=False, hint_text="Введите город")

        self.values_list = list()
        self.city = ""

        self.layout_but_inp.add_widget(self.city_input)
        self.layout_but_inp.add_widget(self.button)

    # функция для кнопки
    def on_text(self, *args):
        self.layout_temp.clear_widgets()
        self.values_list = func_return_values(func_temperature_today(self.city_input.text))
        hour = 0
        for i in range(8):
            self.layout_temp.add_widget(Label(text=str(hour), font_size=20, color=(0, 0, 0, 1)))
            self.layout_temp.add_widget(Label(text=self.values_list[0][i], font_size=20, color=(0, 0, 0, 1)))
            self.layout_temp.add_widget(Label(text=self.values_list[1][i], font_size=20, color=(0, 0, 0, 1)))
            hour += 3

    # Чарли и фабрика по созданию виджетов
    def build(self):
        box = BoxLayout(orientation='vertical', row_force_default=True)
        box.add_widget(self.layout_but_inp)
        box.add_widget(self.layout_temp)
        return box


my_app = MyApp()

if __name__ == "__main__":
    my_app.run()
