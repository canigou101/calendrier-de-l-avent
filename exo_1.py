with open("input.txt", "r") as f: # Permet de lire un fichier texte en lecture
    lines = f.readlines() # récupère la liste de toutes les lignes contenues dans le fichier
    res=0
    partie_de_gauche = []
    partie_de_droite = []
    for line in lines: # Pour chaque ligne de la liste "lines"
        a, b = line.split() # split les données comme ce qu'on a vu sur les chaînes de caractères
        # à vous de jouer :)
        partie_de_gauche.append(int(a))
        partie_de_droite.append(int(b))
        
        
    def est_min(a,b):
        if a<=b:
            return True
        return False
        
        
        
    temp1=[]
    partie_de_gauche.sort()
    partie_de_droite.sort()
    for i in range(len(partie_de_gauche)):
        if est_min(partie_de_gauche[i],partie_de_droite[i])==True:
            temp1.append(partie_de_droite[i]-partie_de_droite[i])
        else : 
           temp1.append(partie_de_gauche[i]-partie_de_droite[i])
    res+=sum(temp1)
    print(res)