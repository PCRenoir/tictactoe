import tkinter as tk

class Jeu:
    def __init__(self):
        self.plateau = [['.' for i in range(3)] for j in range(3)]
        self.player = 0

    def victoire(self, player):
        #test_victoire = liste formée des 3 lignes, 3 colonnes et 2 diagonales du plateau
        test_victoire = [[self.plateau[0][0], self.plateau[0][1], self.plateau[0][2]],
        [self.plateau[1][0], self.plateau[1][1], self.plateau[1][2]], 
        [self.plateau[2][0], self.plateau[2][1], self.plateau[2][2]], 
        [self.plateau[0][0], self.plateau[1][0], self.plateau[2][0]], 
        [self.plateau[0][1], self.plateau[1][1], self.plateau[2][1]], 
        [self.plateau[0][2], self.plateau[1][2], self.plateau[2][2]], 
        [self.plateau[0][0], self.plateau[1][1], self.plateau[2][2]], 
        [self.plateau[2][0], self.plateau[1][1], self.plateau[0][2]]] 
        if [player, player, player] in test_victoire:
            return True
        else:
            return False


def affiche_grille():
    dessin.create_line(100, 0, 100, 300, fill= 'black', width = 2)
    dessin.create_line(200, 0, 200, 300, fill= 'black', width = 2)
    dessin.create_line(0, 100, 300, 100, fill= 'black', width = 2)
    dessin.create_line(0, 200, 300, 200, fill= 'black', width = 2)

def clicjeu(event):
    if game.player % 2 == 0 :   #game.player % 2 -> donne le n° du joueur en fct du nbre de coups
        couleur = 'red'   #j0 = red
    else:
        couleur = 'blue'  #j1 = blue
    # position du pointeur de la souris
    X = event.x
    Y = event.y
    if not(game.victoire(game.player % 2)) and game.player < 9:
        affiche_cercle(X,Y,couleur)
        if game.victoire(game.player % 2):
            victoire = 'Joueur ' + str((game.player % 2) + 1) + ' gagne !'  #texte en cas de victoire
            label = tk.Label(fen, text = victoire)
            label.grid(row = 0, column = 0)
        else :
            game.player += 1
    if game.player == 9 :
        label = tk.Label(fen, text = 'Égalité')
        label.grid(row = 0, column = 0)

def cercle(x,y,color):
    dessin.create_oval(x, y, x + 80, y + 80, width = 2, outline = color)

def affiche_cercle(X,Y,couleur):
    X = X // 100
    Y = Y // 100
    if game.plateau[Y][X] == '.' :
        cercle(100*X + 10, 100*Y + 10, couleur)
        game.plateau[Y][X] = game.player % 2
    else :
        game.player -= 1

################################# Programme Principal
game = Jeu()
fen = tk.Tk()
fen.title('TicTacToe')
dessin = tk.Canvas(fen, width = 300 , height = 300 , bg = 'white', borderwidth = 0, highlightthickness = 0)
dessin.grid(row = 0, column = 0)
dessin.bind('<Button-1>', clicjeu)
affiche_grille()
fen.mainloop()
