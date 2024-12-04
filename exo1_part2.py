with open("input.txt", "r") as f: # Permet de lire un fichier texte en lecture
    lines = f.readlines() # récupère la liste de toutes les lignes contenues dans le fichier
    partie_de_droite=[]
    partie_de_gauche=[]
    res=0
    for line in lines: # Pour chaque ligne de la liste "lines"
        a, b = line.split() # split les données comme ce qu'on a vu sur les chaînes de caractères
        # à vous de jouer :)
        partie_de_droite.append(a)
        partie_de_gauche.append(b)
    
    def nb_occurences(chiffre,liste):
        cp=0
        for i in range(len(liste)):
            if chiffre==liste[i]:
                cp+=1
        return cp
    
    def crealiste_car(string):
        res=[]
        for i in (string):
            res.append(int(i))
        return res
    
    res=0
    for i in range(len(partie_de_droite)):

        liste_int_partie_droite=crealiste_car(partie_de_droite[i])
        liste_int_partie_gauche=crealiste_car(partie_de_gauche[i])
        
        for element in liste_int_partie_gauche:
            res+=(nb_occurences(element,liste_int_partie_droite)*element)
        print(res)
    
    


