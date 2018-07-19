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
        self.adjacentes = {}
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
        """Estado inicial"""
        self.initial = GameState(to_move="BRANCO", utility=0, board={"BRANCO": 0, "PRETO": 0}, moves=vazio)

    def actions(self, state):
        """Deve retornar uma lista de movimentos disponíveis neste ponto, assim temos vários casos.
            - Quando tiver uma peça para jogar
            - Quando colocar três peças adjacentes
            - Quando acabar as peças e poder movimentar uma peça no tabuleiro caso tenha espaço nas adjacências
            """
        return state.moves
        # Procura uma substring
        p = str.find(state.to_move, "_REMOVE")
        # Caso encontre
        if p != -1:
            jogadas = []
            # POS é o número no tabuleiro e to é quem jogou
            for pos, to in state.board.items():
                # Caso o estado seja "BRANCO_REMOVE" procura todas as peças preta
                if not to == state.to_move[:p]:
                    jogadas.append(pos)
            # Retorna todas as peças possíveis de serem removidas
            return jogadas
        # Jogadas já feitas
        jogadas = []
        # POS é o número no tabuleiro e to é quem jogou
        for pos, to in state.board.items():
            if to == state.to_move:
                jogadas.append(pos)
        # Verifica se tem menos de 9 peças de quem está jogando no tabuleiro
        if state.board[state.to_move] < 9:
            # Retorna todos os espaços vazios
            return state.moves
        else:
            moves = []
            for jogada in jogadas:
                adjacente = self.adjacentes[jogada]
                for a in adjacente:
                    if a in state.moves:
                        # Salva um tuple contendo (ORIGEM,DESTINO)
                        moves.append((jogada, a))
            # Retorna os movimentos disponíveis para mover a peça de uma casa a outra
            return moves

    def result(self, state, move):
        """Deve retornar o estado que ficará o jogo quando uma é aplicado um movimento a um estado anterior"""
        # Movimentos ilegais não tem efeitos
        if move not in state.moves:
            return state
        # Próximo a mover
        to_move = ""
        # Copia o tabuleiro
        board = state.board.copy()
        utility = 0
        # Jogadas
        moves = []
        # Procura uma substring
        p = str.find(state.to_move, "_REMOVE")
        if p != -1:
            del (board[move])
            if state.to_move[:p] == "BRANCO":
                to_move = "PRETO"
            else:
                to_move = "BRANCO"
        else:
            if board[state.to_move] < 9:
                board[move] = state.to_move
                board[state.to_move] = board[state.to_move] + 1
            else:
                board[move[1]] = state.to_move
                del (board[move[0]])
            if state.to_move == "BRANCO":
                to_move = "PRETO"
            else:
                to_move = "BRANCO"

        return GameState(to_move=to_move, utility=utility, board=board, moves=moves)

    def utility(self, state, player):
        """Retorna o estado final para o jogador. 0 se o jogo não acabou, 1 se o player passado ganhou ou -1 se ele
        perdeu"""
        return state.utility if player == 'BRANCO' else -state.utility

    def terminal_test(self, state):
        """Retorna verdadeiro se é o estado final do jogo"""
        return state.utility != 0

    def compute_utility(self, state):
        """Verifica se ouve algum ganhador"""
        return 0

    def verifica_trinca(self, state, move):
        """Verifica se houve alguma trinca com o movimento"""
        adjacente = self.adjacentes[move]
        # Caso move seja ímpar
        if (move % 2) == 1:
            # Verifica se é 1,9 ou 17
            if (move % 8) == 1:
                if ((move + 1) in state.board.keys() and state.board[move + 1] == state.to_move and (
                        move + 2) in state.board.keys() and state.board[move + 2] == state.to_move) or (
                        (move + 7) in state.board.keys() and state.board[move + 7] == state.to_move and (
                        move + 6) in state.board.keys() and state.board[move + 6] == state.to_move):
                    return True
                else:
                    return False
            elif ((move - 1) in state.board.keys() and state.board[move - 1] == state.to_move and (
                    move - 2) in state.board.keys() and state.board[move - 2] == state.to_move) or (
                    (move + 1) in state.board.keys() and state.board[move + 1] == state.to_move and (
                    move + 2) in state.board.keys() and state.board[move + 2] == state.to_move):
                return True
            else:
                return False
        # Caso par
        else:
            if (move % 8) == 0:
                if (move - 7) in state.board.keys() and state.board[move - 7] == state.to_move and (
                        move - 1) in state.board.keys() and state.board[move - 1] == state.to_move:
                    return True
            if move <= 8:
                if (move + 8) in state.board.keys() and state.board[move + 8] == state.to_move and (
                        move + 16) in state.board.keys() and state.board[move + 16] == state.to_move:
                    return True
                else:
                    return False
            # De 9 até 16
            elif move > 8 and move <= 16:
                if (move - 8) in state.board.keys() and state.board[move - 8] == state.to_move and (
                        move + 8) in state.board.keys() and state.board[move + 8] == state.to_move:
                    return True
                else:
                    return False
            # De 17 até 24
            else:
                if (move - 8) in state.board.keys() and state.board[move - 8] == state.to_move and (
                        move - 16) in state.board.keys() and state.board[move - 16] == state.to_move:
                    return True
                else:
                    return False
