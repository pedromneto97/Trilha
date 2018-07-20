# Interface gráfica
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class Jogo(GridLayout):
    def __init__(self, **kwargs):
        super(Jogo, self).__init__(**kwargs)
        # Cria 7 colunas
        self.cols = 7

        # Cria a estrutura do jogo
        self.cria()

    def cria(self):
        # Linha 1
        self.add_widget(Button(text='', on_press=self.btn))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Button(text=''))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Button(text=''))
        # Linha 2
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(Button(text=''))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Button(text=''))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Button(text=''))
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        # Linha 3
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(Button(text=''))
        self.add_widget(Button(text=''))
        self.add_widget(Button(text=''))
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        # Linha 4
        self.add_widget(Button(text=''))
        self.add_widget(Button(text=''))
        self.add_widget(Button(text=''))
        self.add_widget(Label(text=''))
        self.add_widget(Button(text=''))
        self.add_widget(Button(text=''))
        self.add_widget(Button(text=''))
        # Linha 5
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(Button(text=''))
        self.add_widget(Button(text=''))
        self.add_widget(Button(text=''))
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        # Linha 6
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(Button(text=''))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Button(text=''))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Button(text=''))
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        # Linha 7
        self.add_widget(Button(text=''))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Button(text=''))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Button(text=''))

    def btn(self, button):
        button.text = 'AQUI'


class MyApp(App):
    def build(self):
        return Jogo()


if __name__ == '__main__':
    MyApp().run()
