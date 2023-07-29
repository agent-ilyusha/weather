# -- coding: utf-8

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput




class TestApp(App):

    def __init__(self):
        super().__init__()
        self.button = Button(text='press me')
        self.button.bind(on_press=self.drop_down_list_button)
        self.lay = BoxLayout(orientation='vertical')
        self.lay.add_widget(self.button)
        self.button.bind(on_press=self.drop_down_list_button)


    def drop_down_list_button(self, *args):
        self.lay.clear_widgets()
        list_name_button = ['первая  кнопка', 'вторая кнопка']
        list_button = list()

        for el in list_name_button:
            list_button.append(Button(text=el))



        for b in list_button:
            b.bind(on_press=self.change_of_day)
            self.lay.add_widget(b)

    def change_of_day(self, *args):
        self.lay.clear_widgets()
        self.lay.add_widget(self.button)
        self.button.bind(on_press=self.drop_down_list_button)

    def build(self):
        grid_lay = GridLayout(cols=3)
        grid_lay.add_widget(TextInput(hint_text='hello_world'))
        grid_lay.add_widget(Button(text='Press me'))
        grid_lay.add_widget(self.lay)
        return grid_lay


app = TestApp()

if __name__ == '__main__':
    app.run()
