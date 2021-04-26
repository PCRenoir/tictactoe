import tkinter as tk

class Jeu:
    def __init__(self):
        self.plateau = [['.' for i in range(3)] for j in range(3)]
        self.player = 0

    def check_ligne(self,player):
        for i in self.plateau:
            if i[0] == i[1] == i[2] == player :
                return True
        return False

    def check_colonne(self,player):
        for i in range(3):
            if self.plateau[0][i] == self.plateau[1][i] == self.plateau[2][i] == player:
                return True
        return False

    def check_diagonale(self,player):
        if self.plateau[0][0] == self.plateau[1][1] == self.plateau[2][2] == player:
            return True
        if self.plateau[0][2] == self.plateau[1][1] == self.plateau[2][0] == player:
            return True
        return False

    def victoire(self,player):
        if self.check_colonne(player) or self.check_ligne(player) or self.check_diagonale(player):
            return True
        return False



def affiche_grille():
    dessin.create_line(100, 0, 100, 320, fill= 'black', width = 2)
    dessin.create_line(200, 0, 200, 320, fill= 'black', width = 2)
    dessin.create_line(0, 100, 320, 100, fill= 'black', width = 2)
    dessin.create_line(0, 200, 320, 200, fill= 'black', width = 2)


def clicjeu(event):
    if game.player % 2 == 0 :
        couleur = 'red'  #j0 = red
    else:
        couleur = 'blue'  #j1 = blue
    # position du pointeur de la souris
    X = event.x
    Y = event.y
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

def cercle(x,y,color):
    dessin.create_oval(x,y,x+80,y+80,width = 2, outline = color)

def affiche_cercle(X,Y,couleur):
    if 0 <= X <= 98 :
        if 0 <= Y <= 98 :
            if game.plateau[0][0] == '.' :
                cercle(10,10, couleur)
                game.plateau[0][0] = game.player % 2
        elif 100 <= Y <= 198 :
            if game.plateau[1][0] == '.' :
                cercle(10,110, couleur)
                game.plateau[1][0] = game.player % 2
        elif 200 <= Y <= 298 :
            if game.plateau[2][0] == '.' :
                cercle(10,210, couleur)
                game.plateau[2][0] = game.player % 2
    elif 100 <= X <= 198 :
        if 0 <= Y <= 98 :
            if game.plateau[0][1] == '.' :
                cercle(110,10, couleur)
                game.plateau[0][1] = game.player % 2
        elif 100 <= Y <= 198 :
            if game.plateau[1][1] == '.' :
                cercle(110,110, couleur)
                game.plateau[1][1] = game.player % 2
        elif 200 <= Y <= 298 :
            if game.plateau[2][1] == '.' :
                cercle(110,210, couleur)
                game.plateau[2][1] = game.player % 2
    elif 200 <= X <= 298 :
        if 0 <= Y <= 98 :
            if game.plateau[0][2] == '.' :
                cercle(210,10, couleur)
                game.plateau[0][2] = game.player % 2
        elif 100 <= Y <= 198 :
            if game.plateau[1][2] == '.' :
                cercle(210,110, couleur)
                game.plateau[1][2] = game.player % 2
        elif 200 <= Y <= 298 :
            if game.plateau[2][2] == '.' :
                cercle(210,210, couleur)
                game.plateau[2][2] = game.player % 2


###########
game = Jeu()
fen = tk.Tk()
fen.title('TicTacToe')
dessin = tk.Canvas(fen, width = 300 , height = 300 , bg = 'white',borderwidth=0, highlightthickness=0)
dessin.grid(row = 0, column = 0)
dessin.bind('<Button-1>', clicjeu)
affiche_grille()

fen.mainloop()
