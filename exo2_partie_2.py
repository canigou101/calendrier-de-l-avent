with open("input_exo2.txt","r") as f:
    lines = f.readlines()
    liste_ligne=[]
    for line in lines: 
        a = line.split()
        liste_ligne.append(a)
    
    def nb_occurences(chiffre,liste):
        cp=0
        for i in range(len(liste)):
            if chiffre==liste[i]:
                cp+=1
        return cp
    
    """
    si nb_occurence >2 next liste
    sinon si nb_occurence <= 2 
    """