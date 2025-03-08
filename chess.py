class ChessGame:
    def __init__(self, player1, player2):
        self.board = self.create_board()
        self.players = {'white': player1, 'black': player2}
        self.turn = 'white'

    def create_board(self):
        # Initialize the chess board with pieces
        board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],  # Black major pieces
            ['P'] * 8,                                 # Black pawns
            [' '] * 8,                                 # Empty rows
            [' '] * 8,
            [' '] * 8,
            [' '] * 8,
            ['p'] * 8,                                 # White pawns
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],  # White major pieces
        ]
        return board

    def display_board(self):
        print("  a b c d e f g h")
        for i, row in enumerate(self.board):
            print(f"{8 - i} " + ' '.join(row))
        print()

    def is_valid_move(self, start, end):
        # Basic move validation (expand for full chess rules)
        x1, y1 = start
        x2, y2 = end
        if not (0 <= x1 < 8 and 0 <= y1 < 8 and 0 <= x2 < 8 and 0 <= y2 < 8):
            return False
        piece = self.board[x1][y1]
        if piece == ' ' or (self.turn == 'white' and piece.isupper()) or (self.turn == 'black' and piece.islower()):
            return False
        return True  # Placeholder: Add piece-specific rules here

    def move_piece(self, start, end):
        x1, y1 = start
        x2, y2 = end
        self.board[x2][y2] = self.board[x1][y1]
        self.board[x1][y1] = ' '

    def is_checkmate(self):
        # Simplified placeholder for checkmate detection
        return False

    def play(self):
        print(f"Welcome to Pro Chess! Players: {self.players['white']} (White) vs. {self.players['black']} (Black)")
        self.display_board()
        while True:
            try:
                print(f"{self.players[self.turn]}'s turn ({self.turn.capitalize()} pieces)")
                start = input("Enter the starting position (e.g., e2): ")
                end = input("Enter the ending position (e.g., e4): ")
                start = (8 - int(start[1]), ord(start[0]) - ord('a'))
                end = (8 - int(end[1]), ord(end[0]) - ord('a'))
                
                if not self.is_valid_move(start, end):
                    print("Invalid move, try again.")
                    continue
                
                self.move_piece(start, end)
                if self.is_checkmate():
                    print(f"Checkmate! {self.players[self.turn]} ({self.turn.capitalize()}) wins!")
                    break

                self.turn = 'black' if self.turn == 'white' else 'white'
                self.display_board()
            except KeyboardInterrupt:
                print("\nGame ended by user.")
                break
            except Exception as e:
                print(f"Error: {e}. Try again.")

# Set players' names
player1 = "Vivek"
player2 = "Akhil"

# Start the enhanced chess game
game = ChessGame(player1, player2)
game.play()
