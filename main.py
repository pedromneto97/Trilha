# Interface gráfica
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from Trilha import Trilha


class Jogo(GridLayout):
    def __init__(self, **kwargs):
        super(Jogo, self).__init__(**kwargs)
        # Cria 7 colunas
        self.cols = 7

        # Cria a estrutura do jogo
        self.cria()

        # Instancia o jogo
        self.trilha = Trilha()
        self.estado = self.trilha.initial

    def cria(self):
        # Linha 1
        self.add_widget(Button(on_press=self.btn, id='1'))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Button(on_press=self.btn, id='2'))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Button(on_press=self.btn, id='3'))
        # Linha 2
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(Button(on_press=self.btn, id='9'))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Button(on_press=self.btn, id='10'))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Button(on_press=self.btn, id='11'))
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        # Linha 3
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(Button(on_press=self.btn, id='17'))
        self.add_widget(Button(on_press=self.btn, id='18'))
        self.add_widget(Button(on_press=self.btn, id='19'))
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        # Linha 4
        self.add_widget(Button(on_press=self.btn, id='8'))
        self.add_widget(Button(on_press=self.btn, id='16'))
        self.add_widget(Button(on_press=self.btn, id='24'))
        self.add_widget(Label(text=''))
        self.add_widget(Button(on_press=self.btn, id='20'))
        self.add_widget(Button(on_press=self.btn, id='12'))
        self.add_widget(Button(on_press=self.btn, id='4'))
        # Linha 5
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(Button(on_press=self.btn, id='23'))
        self.add_widget(Button(on_press=self.btn, id='22'))
        self.add_widget(Button(on_press=self.btn, id='22'))
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        # Linha 6
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(Button(on_press=self.btn, id='15'))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Button(on_press=self.btn, id='14'))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Button(on_press=self.btn, id='13'))
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        # Linha 7
        self.add_widget(Button(on_press=self.btn, id='7'))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Button(on_press=self.btn, id='6'))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Button(on_press=self.btn, id='5'))

    def btn(self, button):
        id = int(button.id)
        button.background_color = [5, 5, 5, 5]
        self.estado = self.trilha.result(self.estado, id)
        print(self.estado)


class MyApp(App):
    def build(self):
        return Jogo()


if __name__ == '__main__':
    MyApp().run()
