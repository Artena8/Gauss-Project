from random import randint
from tkinter import *
from numpy import linalg

#Création de Matrice aléatoire
def crea_matrice(n):
    """Renvoie une matrice nxn d'entiers entre 1 et 9 choisis au hasard."""
    t = []
    for i in range(n):
        ligne=[]
        for p in range(n):
            ligne.append(randint(1,9))
        t.append(ligne)
    return t

def crea_identite(n):
    """Renvoie une matrice nxn d'entiers entre 1 et 9 choisis au hasard."""
    t = []
    for i in range(n):
        ligne=[]
        for p in range(n):
            if p == i :
                ligne.append(1)
            else: 
                ligne.append(0)
        t.append(ligne)
    return t

def affichage_matrice(M):
    print("Matrice :")
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j],end=' ')
        print()
    return " "

#=========LES OPERATIONS ==================================
def inversion_ligne(la,lb,M):
    M[la],M[lb] = M[lb],M[la]
    return M

def multiplication_ligne(n,la,M):
    for j in range(len(M[0])):
        M[la][j] = M[la][j] * n
    return M

def ajout_ligne(n,la,lb,M):
    for j in range(len(M[0])):
        M[la][j] = M[la][j] + (M[lb][j]* n)
    return M


class GAUSS_GUI():
    def __init__(self):
        """Initialise l'interface."""
        self.window = Tk()  # la fenêtre principale
        self.partie_gauche = Frame(self.window)
        self.partie_gauche.pack(side=LEFT)
        self.partie_droite = Frame(self.window, padx=32, width=256)
        self.partie_droite.pack(side=RIGHT)

        # initialiser la matrice de labels
        self.label_matrix = []
        for i in range(TaiM):
            self.label_matrix.append([])
            for j in range(TaiM):
                self.label_matrix[i].append(Label(self.partie_gauche, text=str(matrice[i][j]),
                                            font=('Courier New', 12),
                                            borderwidth=1, relief=GROOVE,
                                            width=2))
                self.label_matrix[i][j].grid(row=i, column=j)

        # les boutons
        self.btn = Button(self.partie_droite, text='Inverser',
                        command=self.Inversion)
        self.btn.pack(fill=BOTH, expand=1)
        self.btn = Button(self.partie_droite, text='Multiplier',
                        command=self.Multi)
        self.btn.pack(fill=BOTH, expand=1)
        self.btn = Button(self.partie_droite, text='Ajouter',
                        command=self.Ajout)
        self.btn.pack(fill=BOTH, expand=1)

        self.window.title('Gauss')
        self.window.mainloop()

    def Inversion(self):
        LA = int(input('Num 1ere ligne :'))-1
        while LA >= len(matrice):
            print('PRENEZ UNE LIGNE EXISTANTE !')
            LA = int(input('Num 1ere ligne :'))-1

        LB = int(input('Num 2eme ligne :'))-1
        while LB >= len(matrice):
            print('PRENEZ UNE LIGNE EXISTANTE !')
            LB = int(input('Num 2ere ligne :'))-1

        matrice = inversion_ligne(LA,LB,matrice)
        In = inversion_ligne(LA,LB,In)


    def Multi(self):
        LA = int(input('Num ligne :'))-1
        while LA >= len(matrice):
            print('PRENEZ UNE LIGNE EXISTANTE !')
            LA = int(input('Num ligne :'))-1

        nb = int(input('Fois :'))

        matrice = multiplication_ligne(nb,LA,matrice)
        In = multiplication_ligne(nb,LA,In)


    def Ajout(self):
        LA = int(input('Num 1ere ligne :'))-1
        while LA >= len(matrice):
            print('PRENEZ UNE LIGNE EXISTANTE !')
            LA = int(input('Num 1ere ligne :'))-1

        LB = int(input('Num ligne à ajouter :'))-1
        while LB >= len(matrice):
            print('PRENEZ UNE LIGNE EXISTANTE !')
            LB = int(input('Num 2ere ligne :'))-1

        nb = int(input('nombre de fois à ajouter :'))

        matrice = ajout_ligne(nb,LA,LB,matrice)
        In = ajout_ligne(nb,LA,LB,In)


if __name__ == '__main__' :

    #Début du jeux
    fin = False
    TaiM = int(input('Taille de la matrice :'))

    #Les matrices
    matrice = crea_matrice(TaiM)
    resultats = [ randint(-2,100) for i in range(TaiM)]
    print(matrice, resultats)
    In = crea_identite(TaiM)

    matricefin = list(linalg.solve(matrice,resultats))
    print(matricefin)

    GAUSS_GUI()

    '''
    while resultats != matricefin :
        choix = int(input('choix :'))

        if choix == 1 :
            LA = int(input('Num 1ere ligne :'))-1
            while LA >= len(matrice):
                print('PRENEZ UNE LIGNE EXISTANTE !')
                LA = int(input('Num 1ere ligne :'))-1

            LB = int(input('Num 2eme ligne :'))-1
            while LB >= len(matrice):
                print('PRENEZ UNE LIGNE EXISTANTE !')
                LB = int(input('Num 2ere ligne :'))-1

            matrice = inversion_ligne(LA,LB,matrice)
            In = inversion_ligne(LA,LB,In)

        elif choix == 2 :
            LA = int(input('Num ligne :'))-1
            while LA >= len(matrice):
                print('PRENEZ UNE LIGNE EXISTANTE !')
                LA = int(input('Num ligne :'))-1

            nb = int(input('Fois :'))

            matrice = multiplication_ligne(nb,LA,matrice)
            In = multiplication_ligne(nb,LA,In)

        elif choix == 3 :
            LA = int(input('Num 1ere ligne :'))-1
            while LA >= len(matrice):
                print('PRENEZ UNE LIGNE EXISTANTE !')
                LA = int(input('Num 1ere ligne :'))-1

            LB = int(input('Num ligne à ajouter :'))-1
            while LB >= len(matrice):
                print('PRENEZ UNE LIGNE EXISTANTE !')
                LB = int(input('Num 2ere ligne :'))-1

            nb = int(input('nombre de fois à ajouter :'))

            matrice = ajout_ligne(nb,LA,LB,matrice)
            In = ajout_ligne(nb,LA,LB,In)

        elif choix == 5 :
            fin = True

        print(" ")
        print(affichage_matrice(matrice))'''