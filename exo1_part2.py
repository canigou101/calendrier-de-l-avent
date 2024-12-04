with open("input.txt", "r") as f: # Permet de lire un fichier texte en lecture
    lines = f.readlines() # récupère la liste de toutes les lignes contenues dans le fichier
    partie_de_droite=[]
    partie_de_gauche=[]
    res=0
    for line in lines: # Pour chaque ligne de la liste "lines"
        a, b = line.split() # split les données comme ce qu'on a vu sur les chaînes de caractères
        # à vous de jouer :)
        partie_de_droite.append(int(a))
        partie_de_gauche.append(int(b))
    
    def nb_occurences(chiffre,liste):
        cp=0
        for i in range(len(liste)):
            if chiffre==liste[i]:
                cp+=1
        return cp
    
    res=0
    for element in partie_de_gauche:
        res+=(nb_occurences(element,partie_de_droite)*element)
    print(res)
    
    


