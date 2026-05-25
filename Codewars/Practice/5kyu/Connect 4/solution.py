class Connect4():

    def __init__(self):
        self.board = [
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]
        ]
        self.count = 1
        self.player = 0
        self.is_game_over = False

    def check_win(self):
        rows = len(self.board)
        cols = len(self.board[0])
        
        # check 4 in a row
        for r in range(rows):
            for c in range(cols):
                test = self.board[r][c]
                if test == 0:
                    continue
                    
                # horizontal
                if c + 3 < cols:
                    if test == self.board[r][c+1] == self.board[r][c+2] == self.board[r][c+3]:
                        return test

                # vertical
                if r + 3 < rows:
                    if test == self.board[r+1][c] == self.board[r+2][c] == self.board[r+3][c]:
                        return test

                # diagonal right
                if r + 3 < rows and c + 3 < cols:
                    if test == self.board[r+1][c+1] == self.board[r+2][c+2] == self.board[r+3][c+3]:
                        return test

                # diagonal left
                if r + 3 < rows and c - 3 >= 0:
                    if test == self.board[r+1][c-1] == self.board[r+2][c-2] == self.board[r+3][c-3]:
                        return test
        return 0
    
    def play(self, col):
        # game status check
        if self.is_game_over == True:
            return "Game has finished!"
        
        # full check
        if self.board[0][col] != 0:
            return f"Column full!"
        
        # indificate player
        if self.count % 2 == 0:
            self.player = 2
        else:
            self.player = 1
        
        # update turn
        for i in reversed(self.board):
            if i[col] == 0:
                i[col] = self.player
                break
        
        # turn count
        self.count += 1
        
        # result
        winner = self.check_win()
        if winner != 0:
            self.is_game_over = True
            return f"Player {self.player} wins!"
        else:
            return f"Player {self.player} has a turn"
