from aima.games import Game, GameState

class Trilha(Game):
    def __init__(self):
        """vazio = [(1, 1), (1, 4), (1, 7), (2, 2), (2, 4), (2, 6), (3, 3), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5),
                 (4, 6), (4, 7), (5, 3), (5, 4), (5, 5), (6, 2), (6, 4), (6, 6), (7, 1), (7, 4), (7, 7)]"""
        vazio = [x for x in range(1, 25)]
        self.self.adjacentes = {}
        for x in range(1, 25):
            if (x % 2) == 1:
                if (x % 8) == 1:
                    self.adjacentes.update({x: [x + 1, x + 7]})
                else:
                    self.adjacentes.update({x: [x - 1, x + 1]})
            else:
                if x <= 8:
                    if (x % 8) == 0:
                        self.adjacentes.update({x: [x - 7, x - 1, x + 8]})
                    else:
                        self.adjacentes.update({x: [x - 1, x + 1, x + 8]})
                elif x > 8 and x <= 16:
                    if (x % 8) == 0:
                        self.adjacentes.update({x: [x - 8, x - 7, x - 1, x + 8]})
                    else:
                        self.adjacentes.update({x: [x - 8, x - 1, x + 1, x + 8]})
                else:

                    if (x % 8) == 0:
                        self.adjacentes.update({x: [x - 8, x - 7, x - 1]})
                    else:
                        self.adjacentes.update({x: [x - 8, x - 1, x + 1]})
        self.branco = 9
        self.preto = 9
        self.initial = GameState(to_move='BRANCO', utility=0, board={}, moves=vazio)

    def actions(self, state):
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
        return GameState()

    def utility(self, state, player):
        return state.utility if player == 'BRANCO' else -state.utility

    def terminal_test(self, state):
        return state.utility != 0
