with open("input.txt", "r") as f: # Permet de lire un fichier texte en lecture
    lines = f.readlines() # récupère la liste de toutes les lignes contenues dans le fichier
    tempA = []
    res=0
    tempB = []
    for line in lines: # Pour chaque ligne de la liste "lines"
        a, b = line.split() # split les données comme ce qu'on a vu sur les chaînes de caractères
        # à vous de jouer :)
        tempA.append(a)
        tempB.append(b)
    def est_min(a,b):
        if a<=b:
            return True
        return False
    

    
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
    print (int((crealiste_car(tempA[1])[0])))
    
    for j in tempA:
        for i in range(len(j)):
            #print(i)
            temp1=crealiste_car(tempA[i])
            #print(temp1)
            temp2=crealiste_car(tempB[i])
            #temp3=nb_occurences(,)
            res+=((nb_occurences(temp1[i],temp2))*temp1[i])
    print(res)



