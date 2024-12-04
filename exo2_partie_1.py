with open("input_exo2.txt","r") as f:
    lines = f.readlines()
    liste_ligne=[]
    for line in lines: # Pour chaque ligne de la liste "lines"
        a = line.split()
        liste_ligne.append(int(a))
    
    def nb_occurences(chiffre,liste):
        cp=0
        for i in range(len(liste)):
            if chiffre==liste[i]:
                cp+=1
        return cp
    print(liste_ligne)
    compteur_de_bon_rapport=0
    
    def est_croissante():
    for element in liste_ligne:
        if nb_occurences(element,liste_ligne)==1:
            pass
#faire la diff et cut si c'est pas bon 
