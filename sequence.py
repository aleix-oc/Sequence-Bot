import random

class Player:

    def __init__(self, color, board):
        self.color = color
        self.deck= self.take_hand(board.deck)

    def take_hand(self, board.deck):
        hand = []

        for _ in range(7):
            card = random.choice(board.deck)
            hand.append(card)
            board.deck.remove(card)
        
        return hand



class Board:

    def __init__(self):
        self.cards = [
            ["T", "D6", "D7", "D8", "D9", "D10", "DQ", "DK", "DA", "T"],
            ["D5", "H3", "H2", "S2", "S3", "S4", "S5", "S6", "S7", "CA"],
            ["D4", "H4", "DK", "DA", "CA", "CK", "CQ", "C10", "S8", "CK"],
            ["D3", "H5", "DQ", "HQ", "H10", "H9", "H8", "C9", "S9", "CQ"],
            ["D2", "H6", "D10", "HK", "H3", "H2", "H7", "C9", "S10", "C10"],
            ["SA", "H7", "D9", "HA", "H4", "H5", "H6", "C7", "SQ", "C9"],
            ["SK", "H8", "D8", "C2", "C3", "C4", "C5", "C6", "SK", "C8"],
            ["SQ", "H9", "D7", "D6", "D5", "D4", "D3", "D2", "SA", "C7"],
            ["S10", "H10", "HQ", "HK", "HA", "C2", "C3", "C4", "C5", "C6"],
            ["T", "S9", "S8", "S7", "S6", "S5", "S4", "S3", "S2", "T"]
        ]

        self.colors = [["E"]*10]*10

        self.deck = [card for row in self.cards for card in row]
        
        self.card_pos = {}

        for i, row in enumerate(self.cards):
            for j, card in enumerate(row):
                if card != "T":
                    if card not in self.card_pos:
                        self.card_pos[card] = []
                    self.card_pos[card].append((i, j))

    def dfs(color,i,j,count):
        if self.colors[i][j] != color:
            return False
        count += 1
        if count == 5:
            return True
        if j < 9 and dfs(color,i,j+1,count):
            return True
        if i < 9 and j > 0 and dfs(color,i+1,j-1,count):
            return True
        if i < 9 and dfs(color,i+1,j,count):
            return True
        if i < 9 and j < 9 and dfs(color,i+1,j+1,count):
            return True
        return False

    def check_win(color):
        for i in range(10):
            for j in range(10):
                if dfs(color,i,j,0):
                    return True
        return False

