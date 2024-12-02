with open("input.txt", "r") as f: # Permet de lire un fichier texte en lecture
    lines = f.readlines() # récupère la liste de toutes les lignes contenues dans le fichier
    res=0
    tempA = []
    tempB = []
    for line in lines: # Pour chaque ligne de la liste "lines"
        a, b = line.split() # split les données comme ce qu'on a vu sur les chaînes de caractères
        # à vous de jouer :)
        tempA.append(int(a))
        tempB.append(int(b))
        
        
    def est_min(a,b):
        if a<=b:
            return True
        return False
        
        
        
    temp1=[]
    tempA.sort()
    tempB.sort()
    for i in range(len(tempA)):
        if est_min(tempA[i],tempB[i])==True:
            temp1.append(tempB[i]-tempA[i])
        else : 
           temp1.append(tempA[i]-tempB[i])
    res+=sum(temp1)
    print(res)