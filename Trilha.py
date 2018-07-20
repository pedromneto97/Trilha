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
        """Retorna todos os movimentos possíveis no momento"""
        return state.moves

    def result(self, state, move):
        """Deve retornar o estado que ficará o jogo quando uma é aplicado um movimento a um estado anterior"""
        # Movimentos ilegais não tem efeitos
        if move not in state.moves:
            return state
        # Copia o tabuleiro
        board = state.board.copy()
        utility = 0
        # Jogadas
        moves = []
        # Procura uma substring e verifica caso seja a vez de alguém remover a peça
        p = str.find(state.to_move, "_REMOVE")
        if p != -1:
            # Remove a peça do tabuleiro
            del (board[move])
            # Define quem é o próximo a jogar
            if state.to_move[:p] == "BRANCO":
                to_move = "PRETO"
            else:
                to_move = "BRANCO"
            # Verifica se alguém ganhou com essa jogada
            utility = self.compute_utility(board, state.to_move[:p])
        # Caso não seja para remover a peça
        else:
            # Verifica ainda tem peça para jogar no tabuleiro
            if board[state.to_move] < 9:
                board[move] = state.to_move
                board[state.to_move] = board[state.to_move] + 1
            # Caso já tenham sido jogadas as peças, então é para mover uma peça no tabuleiro
            else:
                # Define o destino
                board[move[1]] = state.to_move
                # Remove da origem
                del (board[move[0]])
            # Define quem é o próximo a jogar
            if state.to_move == "BRANCO":
                if self.verifica_trinca(state, move):
                    to_move = "BRANCO_REMOVE"
                else:
                    to_move = "PRETO"
            else:
                if self.verifica_trinca(state, move):
                    to_move = "PRETO_REMOVE"
                else:
                    to_move = "BRANCO"
        # Define os próximos movimentos
        p = str.find(to_move, "_REMOVE")
        # Caso o próximo movimento seja de remover
        if p != -1:
            # POS é o número no tabuleiro e to é quem jogou
            for pos, to in board.items():
                # Caso o estado seja "BRANCO_REMOVE" procura todas as peças preta
                if not to == to_move[:p]:
                    moves.append(pos)
        # Caso o próximo movimento seja só colocar uma peça no tabuleiro
        elif board[to_move] < 9:
            moves = self.vazios(board)
        # Caso o próximo movimento seja movimentar uma peça no tabuleiro
        else:
            jogadas = []
            vazios = self.vazios(board)
            for pos, to in board.items():
                if to == to_move:
                    # Salva todas as jogadas do próximo a mover a peça
                    jogadas.append(pos)
            # Verifica cada jogada
            for jogada in jogadas:
                # Pega os adjacentes de cada jogada
                adjacente = self.adjacentes[jogada]
                # Verifica em cada adjacente se ele está vazio
                for a in adjacente:
                    if a in vazios:
                        # Salva um tuple contendo (ORIGEM,DESTINO)
                        moves.append((jogada, a))
        return GameState(to_move=to_move, utility=utility, board=board, moves=moves)

    def utility(self, state, player):
        """Retorna o estado final para o jogador. 0 se o jogo não acabou, 1 se o player passado ganhou ou -1 se ele
        perdeu"""
        return state.utility if player == 'BRANCO' else -state.utility

    def terminal_test(self, state):
        """Retorna verdadeiro se é o estado final do jogo"""
        return state.utility != 0

    def compute_utility(self, board, player):
        """Verifica se ouve algum ganhador"""
        if board[player] < 9:
            return 0
        cont = 0
        for pos, to in board.items():
            if to == player:
                cont = cont + 1
        if cont < 3:
            return -1 if player == "BRANCO" else +1
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
            elif (move + 1) in state.board.keys() and state.board[move + 1] == state.to_move and (
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

    def vazios(self, board):
        vazios = []
        for x in range(1, 25):
            if x not in board.keys():
                vazios.append(x)
        return vazios
