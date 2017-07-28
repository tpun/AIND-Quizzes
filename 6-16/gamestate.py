from copy import deepcopy

class Player:
    def __init__(self, name):
        self.name = name
        self.last_move = None

    def first_move(self):
        return self.last_move == None

    def __repr__(self):
        return 'Player ' + self.name + ', Last Move: ' + str(self.last_move)

class GameState:

    def __init__(self):
        self.board_size = (3, 2)
        self.board = [ (x, y) for x in range(self.board_size[0]) for y in range(self.board_size[1])]
        self.dead_corner = (self.board_size[0]-1, self.board_size[1]-1)
        self.board.remove(self.dead_corner)
        self.players = [ Player('One'), Player('Two') ]

    def forecast_move(self, move):
        """ Return a new board object with the specified move
        applied to the current game state.

        Parameters
        ----------
        move: tuple
            The target position for the active player's next move
        """

        new_board = deepcopy(self)
        active_player = new_board.players[0]
        active_player.last_move = move
        new_board.board.remove(move)

        # Change active player
        new_board.players.pop(0)
        new_board.players.append(active_player)

        return new_board

    def get_legal_moves(self):
        """ Return a list of all legal moves available to the
        active player.  Each player should get a list of all
        empty spaces on the board on their first move, and
        otherwise they should get a list of all open spaces
        in a straight line along any row, column or diagonal
        from their current position. (Players CANNOT move
        through obstacles or blocked squares.) Moves should
        be a pair of integers in (column, row) order specifying
        the zero-indexed coordinates on the board.
        """

        active_player = self.players[0]
        last_move = active_player.last_move

        # You can go anywhere on first move
        if active_player.first_move():
            return self.board

        left  = [ (x, last_move[1]) for x in range(last_move[0]-1, -1, -1)]
        right = [ (x, last_move[1]) for x in range(last_move[0]+1, self.board_size[0])]
        up    = [ (last_move[0], y) for y in range(last_move[1]-1, -1, -1)]
        down  = [ (last_move[0], y) for y in range(last_move[1]+1, self.board_size[1])]
        nw    = [ (x, y) for x in range(last_move[0]-1, -1, -1) for y in range(last_move[1]-1, -1, -1)]
        ne    = [ (x, y) for x in range(last_move[0]+1, self.board_size[0]) for y in range(last_move[1]-1, -1, -1)]
        sw    = [ (x, y) for x in range(last_move[0]-1, -1, -1) for y in range(last_move[1]+1, self.board_size[1])]
        se    = [ (x, y) for x in range(last_move[0]+1, self.board_size[0]) for y in range(last_move[1]+1, self.board_size[1])]
        possible = left + right + up + down + nw + ne + sw + se

        # return ones that are also in the unoccupied space of our board
        return list(set.intersection(*map(set, [possible, self.board])))
