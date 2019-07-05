#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

import game

class Piece:
    out = False
    location = []
    index = 0

    def __init__(self):
        self.location = []
        self.location.append(0)
        self.location.append(0)

    def set_location(self, a, b):
        self.location[0] = a
        self.location[1] = b


class Player:
    path = []
    pieces = []
    out = 0
    name = ''

    def __init__(self):
        self.pieces = []
        a = Piece()
        self.pieces.append(a)
        b = Piece()
        self.pieces.append(b)

    def set_name(self, a):
        self.name = a






class Board:
    lists = []

    def __init__(self):
        n = 15
        m = 15
        self.lists = [" "] * n
        for i in range(n):
            self.lists[i] = [' '] * m

    def draw_board(self):
        i = 0
        j = 0
        print('')
        for i in range(0, 15):
            for j in range(0, 15):
                if (j < 6 or j > 8) and (i < 6 or i > 8):
                    self.lists[i][j] = '|#|'
                else:
                    self.lists[i][j] = '   '
                if (i > 5) and (i < 9) and (j > 5) and (j < 9):
                    self.lists[i][j] = '|=|'
                if (i == 7) and (j > 0) and (j < 14):
                    self.lists[i][j] = '|=|'
                if (j == 7) and (i > 0) and (i < 14):
                    self.lists[i][j] = '|=|'
        print('')

    def print_board(self):
        # print(self.players[0].name)
        for i in range(0, 15):
            print(self.lists[i])
        # print('\t\t\t\t\t\t\t\t\t\t\t\t', self.players[1].name )

    pass

    def updates(self, a):
        self.lists[a[0]][a[1]] = ' @ '

    def updates_sp(self, a):
        self.lists[a[0]][a[1]] = '   '

    def update(self, a, b):
        self.lists[a][b] = '   '

    def update_sp(self, a, b):
        self.lists[a][b] = '   '


class Game:
    players = []
    board = Board()
    path1 = [[6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [5, 6], [4, 6], [3, 6], [2, 6], [1, 6], [0, 6], [0, 7], [0, 8],
             [1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 9], [6, 10], [6, 11], [6, 12], [6, 13], [6, 14], [7, 14],
             [8, 14], [8, 13], [8, 12], [8, 11], [8, 10], [8, 9], [9, 8], [10, 8], [11, 8], [12, 8], [13, 8], [14, 8],
             [14, 7], [14, 6], [13, 6], [12, 6], [11, 6], [10, 6], [9, 6], [8, 5], [8, 4], [8, 3], [8, 2], [8, 1],
             [8, 0], [7, 0], [6, 0]]
    path2 = [[8, 13], [8, 12], [8, 11], [8, 10], [8, 9], [9, 8], [10, 8], [11, 8], [12, 8], [13, 8], [14, 8], [14, 7],
             [14, 6], [13, 6], [12, 6], [11, 6], [10, 6], [9, 6], [8, 5], [8, 4], [8, 3], [8, 2], [8, 1], [8, 0],
             [7, 0], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [5, 6], [4, 6], [3, 6], [2, 6], [1, 6], [0, 6],
             [0, 7], [0, 8], [1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 9], [6, 10], [6, 11], [6, 12], [6, 13],
             [6, 14], [7, 14], [8, 14]]

    def __init__(self):
        a = Player()
        a.pieces[0].set_location(6, 1)
        self.players.append(a)
        b = Player()
        a.pieces[1].set_location(9, 13)
        self.players.append(b)
        self.board = Board()
        self.board.draw_board()
        # self.board.print_board()

    def play_game_player1(self):
        a = random.randint(1, 6)
        print(a)
        if a == 6:
            play = self.players[0]
            if play.out < 2:
                play.out = play.out + 1
                index = play.pieces[play.out - 1].index
                play.pieces[play.out - 1].out = True
                self.board.updates(self.path1[index])
                self.board.print_board()
            else:
                index = play.pieces[play.out - 1].index
                index = index + 6
                if index < 52:
                    self.board.updates(self.path1[index])
                    self.board.updates_sp(self.path1[index])
                    play.pieces[play.out - 1].index = index
                    self.board.print_board()

        if a < 6:

            play = self.players[0]
            if play.pieces[play.out - 1].out:
                index = play.pieces[play.out - 1].index
                if index + a < 52:
                    self.board.updates_sp(self.path1[index])
                    index += a
                    self.board.updates(self.path1[index])
                    play.pieces[play.out - 1].index = index
                    self.board.print_board()

    def play_game_player2(self):
        a = random.randint(1, 6)
        print(a)
        if a == 6:
            play = self.players[1]
            if play.out < 2:
                play.out = play.out + 1
                index = play.pieces[play.out - 1].index
                play.pieces[play.out - 1].out = True
                self.board.updates(self.path2[index])
                self.board.print_board()
            else:
                index = play.pieces[play.out - 1].index
                index = index + 6
                if index < 52:
                    self.board.updates(self.path2[index])
                    self.board.updates_sp(self.path2[index])
                    play.pieces[play.out - 1].index = index
                    self.board.print_board()

        if a < 6:
            play = self.players[1]
            if play.pieces[play.out - 1].out:
                index = play.pieces[play.out - 1].index
                if index + a < 52:
                    self.board.updates_sp(self.path2[index])
                    index += a
                    self.board.updates(self.path2[index])
                    play.pieces[play.out - 1].index = index
                    self.board.print_board()


def main():
    games = Game()
    i = 0
    while i < 10:
        print(' ')
        inp=str(input('enter y to roll for player 1 '))
        if inp=='y':
            print("player 1 roll ")
            games.play_game_player1()
            print(' ')
        inp=str(input('enter y to roll for player 2 '))
        if inp=='y':
            print("player 2 roll ")
            games.play_game_player2()
            i = i + 1


if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




