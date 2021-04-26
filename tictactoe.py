import tkinter as tk
import random as rd

class Jeu:
    def __init__(self):
        self.plateau = [['.' for i in range(3)] for j in range(3)]
        self.player = 0

    def victoire(self, player):
        test_victoire = [[self.plateau[0][0], self.plateau[0][1], self.plateau[0][2]],[self.plateau[1][0], self.plateau[1][1], self.plateau[1][2]], [self.plateau[2][0], self.plateau[2][1], self.plateau[2][2]], [self.plateau[0][0], self.plateau[1][0], self.plateau[2][0]], [self.plateau[0][1], self.plateau[1][1], self.plateau[2][1]], [self.plateau[0][2], self.plateau[1][2], self.plateau[2][2]], [self.plateau[0][0], self.plateau[1][1], self.plateau[2][2]], [self.plateau[2][0], self.plateau[1][1], self.plateau[0][2]]] #test_victoire formé des 3 lignes, 3 colonnes et 2 diagonales
        if [player, player, player] in test_victoire:
            return True
        else:
            return False


def affiche_grille():
    dessin.create_line(100, 0, 100, 320, fill= 'black', width = 2)
    dessin.create_line(200, 0, 200, 320, fill= 'black', width = 2)
    dessin.create_line(0, 100, 320, 100, fill= 'black', width = 2)
    dessin.create_line(0, 200, 320, 200, fill= 'black', width = 2)


def clicjeu_h_vs_h(event):
    if game.player % 2 == 0 :
        couleur = 'red'  #j0 = red ->n° pair
    else:
        couleur = 'blue'  #j1 = blue -> n° impair
    # position du pointeur de la souris
    X = event.x // 100
    Y = event.y // 100
    if not(game.victoire(game.player % 2)) and game.player < 9:
        affiche_cercle(X,Y,couleur)
        if game.victoire(game.player % 2):
            victoire = 'Joueur '+str((game.player % 2) + 1)+' gagne !'
            label = tk.Label(fen, text = victoire)
            label.grid(row = 0, column = 0)
        else :
            game.player += 1
    if game.player == 9 :
        label = tk.Label(fen, text = 'Égalité')
        label.grid(row = 0, column = 0)

def color():
    if game.player % 2 == 0 :
        return 'red'
    else:
        return 'blue'

def clicjeu_h_vs_pc(event):
    choix = [0,1,2]
    X = event.x // 100
    Y = event.y // 100
    if not(game.victoire(game.player % 2)) and game.player < 9:
        couleur = color()
        if game.plateau[Y][X] != '.' :
            return None
        affiche_cercle(X,Y,couleur)
        if game.victoire(game.player % 2):
            victoire = 'Joueur humain gagne !'
            label = tk.Label(fen, text = victoire)
            label.grid(row = 0, column = 0)
        game.player += 1
        if game.player < 9 and game.victoire((game.player - 1) % 2) == False:
            X = rd.choice(choix)  #X et Y au hasard
            Y = rd.choice(choix)
            couleur = color()
            while game.plateau[Y][X] != '.':
                X = rd.choice(choix)
                Y = rd.choice(choix)
            affiche_cercle(X,Y,couleur)
            if game.victoire(game.player % 2):
                victoire = 'Ordinateur gagne !'
                label = tk.Label(fen, text = victoire)
                label.grid(row = 0, column = 0)
            game.player += 1
    if game.player >= 9 and not(game.victoire(game.player % 2) or game.victoire((game.player + 1) % 2)):
        label = tk.Label(fen, text = 'Égalité')
        label.grid(row = 0, column = 0)


def cercle(x,y,color):
    dessin.create_oval(x,y,x+80,y+80,width = 2, outline = color)

def affiche_cercle(X,Y,couleur):
    if game.plateau[Y][X] == '.' :
        cercle(100*X+10,100*Y+10, couleur)
        game.plateau[Y][X] = game.player % 2
    else :
        game.player -= 1

###########
game = Jeu()
fen = tk.Tk()
fen.title('TicTacToe')
dessin = tk.Canvas(fen, width = 300 , height = 300 , bg = 'white', borderwidth = 0, highlightthickness = 0)
dessin.grid(row = 0, column = 0)
affiche_grille()
dessin.bind('<Button-1>', clicjeu_h_vs_pc)


fen.mainloop()
