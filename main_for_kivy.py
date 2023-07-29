# -- coding: utf-8


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from main import func_temperature_today

Window.title = "title"
Window.size = (1280, 520)
Window.clearcolor = (255, 255, 255, 1)


class My_prognozApp(App):

    # переменные
    def __init__(self):
        super().__init__()
        self.layout_temp = GridLayout(cols=3)
        self.layout_but_inp = GridLayout(cols=3, row_force_default=True, row_default_height=100, size_hint_y=0.3)
        self.lay_button = BoxLayout(orientation='vertical')

        self.button_enter = Button(text="Нажми на меня для подтверждения действий)")
        self.button_for_list = Button(text="Нажми для смены дня)")
        self.button_for_list.bind(on_press=self.drop_down_list_button)
        self.button_enter.bind(on_press=self.for_text)
        self.city_input = TextInput(multiline=False, hint_text="Введите город")

        self.values_list = list()
        self.city = ""
        self.day = 'сегодня'

        self.lay_button.add_widget(self.button_for_list)
        self.layout_but_inp.add_widget(self.city_input)
        self.layout_but_inp.add_widget(self.lay_button)
        self.layout_but_inp.add_widget(self.button_enter)

    # функция для отображения списка дней
    def drop_down_list_button(self, *args):
        self.lay_button.clear_widgets()
        b_today = Button(text='Сегодня')
        b_tomorrow = Button(text='Завтра')

        b_today.bind(on_press=self.change_of_today)
        b_tomorrow.bind(on_press=self.change_of_tomorrow)

        self.lay_button.add_widget(b_today)
        self.lay_button.add_widget(b_tomorrow)

    def change_of_today(self, *args):
        self.lay_button.clear_widgets()
        self.day = 'сегодня'
        self.lay_button.add_widget(self.button_for_list)
        self.button_for_list.bind(on_press=self.drop_down_list_button)

    def change_of_tomorrow(self, *args):
        self.lay_button.clear_widgets()
        self.day = 'завтра'
        self.lay_button.add_widget(self.button_for_list)
        self.button_for_list.bind(on_press=self.drop_down_list_button)

    # функция для кнопки
    def for_text(self, *args):
        self.layout_temp.clear_widgets()
        self.values_list = func_temperature_today(city=self.city_input.text, day=self.day)
        if self.values_list != 0:
            for i in range(8):
                self.layout_temp.add_widget(Label(text=self.values_list[2][i], font_size=20, color=(0, 0, 0, 1),
                                                  halign='left'))
                self.layout_temp.add_widget(Label(text=self.values_list[0][i], font_size=20, color=(0, 0, 0, 1),
                                                  halign='left'))
                self.layout_temp.add_widget(Label(text=self.values_list[1][i], font_size=20, color=(0, 0, 0, 1),
                                                  halign='left'))
        else:
            self.layout_temp.clear_widgets()
            self.layout_temp.add_widget(Label(text='Введи реальный город', font_size=50, color=(0, 0, 0, 1)))
        self.day = 'сегодня'

    # Чарли и фабрика по созданию виджетов
    def build(self) -> BoxLayout:
        box = BoxLayout(orientation='vertical')
        box.size_hint_y = 1
        box.add_widget(self.layout_but_inp)
        box.add_widget(self.layout_temp)
        return box


my_app = My_prognozApp()

if __name__ == "__main__":
    my_app.run()
