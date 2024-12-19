with open("input_exo2.txt","r") as f:
    lines = f.readlines()
    liste_ligne=[]
    for line in lines: 
        a = line.split()
        liste_ligne.append(a)
    
    nb_rapport_bon=0

    def est_croissante(liste_d_element):
        for i in range(len(liste_d_element)-1):
            if int(liste_d_element[i])>int(liste_d_element[i+1]):
                return 0
        return 1
    
    def différence_entre_deux_sup(liste_d_element):
        for i in range(len(liste_d_element)-1):
            if abs(int(liste_d_element[i])-int(liste_d_element[i+1]))>3 or abs(int(liste_d_element[i])-int(liste_d_element[i+1]))<1 :
                return 0
        return 1
    
    def nb_occurences(chiffre,liste):
        cp=0
        for i in range(len(liste)):
            if chiffre==liste[i]:
                cp+=1
        return cp
    
    def listeOccurence(ligne):
        listeOcc=[]
        for i in range(len(ligne)):
            listeOcc.append(nb_occurences(ligne[i],ligne))
        return listeOcc
    
    for i in range(len(liste_ligne)):
        if (est_croissante(liste_ligne[i])==1 or est_croissante(liste_ligne[i][::-1])==1) and différence_entre_deux_sup(liste_ligne[i])==1:
            nb_rapport_bon+=1
        elif (est_croissante(liste_ligne[i])==0 or est_croissante(liste_ligne[i][::-1])==0) and différence_entre_deux_sup(liste_ligne[i])==0 and max(listeOccurence(liste_ligne[i]))<=2:
            nb_rapport_bon+=1
    print (nb_rapport_bon)