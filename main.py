# Interface gráfica
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from Trilha import Trilha


class Jogo(GridLayout):
    def __init__(self, **kwargs):
        super(Jogo, self).__init__(**kwargs)
        self.padding = 10
        # Cria 7 colunas
        self.cols = 7

        # Cria a estrutura do jogo
        self.cria()

        self.anterior = 0

        # Instancia o jogo
        self.trilha = Trilha()
        self.estado = self.trilha.initial
        # setrecursionlimit(1000000)

    def cria(self):
        # Linha 1
        self.btn_list = []
        for x in range(1, 25):
            self.btn_list.append(Button(on_press=self.btn, id=str(x)))
        self.add_widget(self.btn_list[0])
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(self.btn_list[1])
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(self.btn_list[2])
        # Linha 2
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(self.btn_list[8])
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(self.btn_list[9])
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(self.btn_list[10])
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        # Linha 3
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(self.btn_list[16])
        self.add_widget(self.btn_list[17])
        self.add_widget(self.btn_list[18])
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        # Linha 4
        self.add_widget(self.btn_list[7])
        self.add_widget(self.btn_list[15])
        self.add_widget(self.btn_list[23])
        self.add_widget(Label(text=''))
        self.add_widget(self.btn_list[19])
        self.add_widget(self.btn_list[11])
        self.add_widget(self.btn_list[3])
        # Linha 5
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(self.btn_list[22])
        self.add_widget(self.btn_list[21])
        self.add_widget(self.btn_list[20])
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        # Linha 6
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        self.add_widget(self.btn_list[14])
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(self.btn_list[13])
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(self.btn_list[12])
        self.add_widget(Label(text='[color=ffffff]|[/color]', markup=True))
        # Linha 7
        self.add_widget(self.btn_list[6])
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(self.btn_list[5])
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(Label(text='[color=ffffff]-------[/color]', markup=True))
        self.add_widget(self.btn_list[4])

    def btn(self, button):
        id = int(button.id)
        if len(self.estado.moves) > 0 and isinstance(self.estado.moves[0], tuple):
            if self.anterior == 0:
                if id in self.estado.board.keys() and self.estado.board[id] == self.estado.to_move:
                    self.anterior = id
                    button.background_color = [3, 2, 2, 3]
            else:
                id = (self.anterior, id)
                if self.estado.to_move == "BRANCO":
                    self.btn_list[self.anterior - 1].background_color = [5, 5, 5, 5]
                else:
                    self.btn_list[self.anterior - 1].background_color = [0, 0, 1, 2]
                self.anterior = 0
        if id in self.estado.moves:
            if self.estado.board['REMOVE'] == 1:
                button.background_color = [1, 1, 1, 1]
            elif self.estado.to_move == "BRANCO":
                if isinstance(id, tuple):
                    self.btn_list[id[0] - 1].background_color = [1, 1, 1, 1]
                button.background_color = [5, 5, 5, 5]
            else:
                if isinstance(id, tuple):
                    self.btn_list[id[0] - 1].background_color = [1, 1, 1, 1]
                button.background_color = [0, 0, 1, 2]
            self.estado = self.trilha.result(self.estado, id)
            print(self.estado)
            # a = minimax_decision(self.estado, self.trilha)
            # print(a)


class MyApp(App):
    def build(self):
        return Jogo()


if __name__ == '__main__':
    MyApp().run()
