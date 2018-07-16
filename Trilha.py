from aima.games import Game, GameState


class Trilha(Game):

    def __init__(self):
        """
        Caso utilizar matriz:

        vazio = [(1, 1), (1, 4), (1, 7), (2, 2), (2, 4), (2, 6), (3, 3), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5),
                 (4, 6), (4, 7), (5, 3), (5, 4), (5, 5), (6, 2), (6, 4), (6, 6), (7, 1), (7, 4), (7, 7)]
        """
        # Posições do tabuleiro sem peças
        vazio = [x for x in range(1, 25)]
        # Dicionário com todas as posições e seus adjacentes. Ex: {1: [2,8]}
        self.self.adjacentes = {}
        # Cria os adjacentes
        for x in range(1, 25):
            # Caso x seja ímpar
            if (x % 2) == 1:
                # Verifica se é 1,9 ou 17
                if (x % 8) == 1:
                    self.adjacentes.update({x: [x + 1, x + 7]})
                else:
                    self.adjacentes.update({x: [x - 1, x + 1]})
            # Caso par
            else:
                # 1 até 8
                if x <= 8:
                    if (x % 8) == 0:
                        self.adjacentes.update({x: [x - 7, x - 1, x + 8]})
                    else:
                        self.adjacentes.update({x: [x - 1, x + 1, x + 8]})
                # De 9 até 16
                elif x > 8 and x <= 16:
                    if (x % 8) == 0:
                        self.adjacentes.update({x: [x - 8, x - 7, x - 1, x + 8]})
                    else:
                        self.adjacentes.update({x: [x - 8, x - 1, x + 1, x + 8]})
                # De 17 até 24
                else:
                    if (x % 8) == 0:
                        self.adjacentes.update({x: [x - 8, x - 7, x - 1]})
                    else:
                        self.adjacentes.update({x: [x - 8, x - 1, x + 1]})
        """Quantidade de peças disponíveis para jogar"""
        self.branco = 9
        self.preto = 9
        """Estado inicial"""
        self.initial = GameState(to_move='BRANCO', utility=0, board={}, moves=vazio)

    def actions(self, state):
        """Deve retornar uma lista de movimentos disponíveis neste ponto, assim temos vários casos.
            - Quando tiver uma peça para jogar
            - Quando colocar três peças adjacentes
            - Quando acabar as peças e poder movimentar uma peça no tabuleiro caso tenha espaço nas adjacências
            """
        if state.to_move is 'BRANCO':
            if self.branco > 0:
                return state.moves
            else:
                jogadas = []
                for pos, to in state.board.items():  # for name, age in list.items():  (for Python 3.x)
                    if to == 'BRANCO':
                        jogadas.append(pos)
                moves = []
        elif state.to_move is 'PRETO':
            if self.preto > 0:
                return state.moves
            else:
                return

    def result(self, state, move):
        """Deve retornar o estado que ficará o jogo quando uma é aplicado um movimento a um estado anterior"""
        return GameState()

    def utility(self, state, player):
        """Retorna o estado final para o jogador. 0 se o jogo não acabou, 1 se o player passado ganhou ou -1 se ele
        perdeu"""
        return state.utility if player == 'BRANCO' else -state.utility

    def terminal_test(self, state):
        """Retorna verdadeiro se é o estado final do jogo"""
        return state.utility != 0
