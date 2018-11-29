import pandas as pd
import numpy as np

def model1(compTerit,specialite,domaine):
    ###### listes des compétences,spécialités et domaines possibles
    compTerritPossibles=[x for x in dataFinal.columns if ('CT_LWord_' in x)]
    specialitePossibles=[x for x in dataFinal.columns if ('SpecLWord_' in x)]
    domainesPossibles=[x for x in dataFinal.columns if ('DomainLW_' in x)]
    compTerit='CT_LWord_'+compTerit.upper()
    specialite='SpecLWord_'+specialite
    domaine='DomainLW_'+domaine
    if (compTerit in compTerritPossibles)&(specialite in specialitePossibles)&(domaine in domainesPossibles):
        dataPossibles= dataFinal[(dataFinal[compTerit]>0)&(dataFinal[specialite]>0)]
        dataPossibles['Taux_missions_Accomplies']=dataPossibles['nb_mission']/max(dataPossibles['nb_mission']) 
        criteres=dataPossibles['Taux de reussite']+dataPossibles['Taux Part reussite']-dataPossibles['Taux_Echec']+dataPossibles['Taux_missions_Accomplies']
        dataPossibles['Critères']=(criteres)/float(max(criteres))
        dataPossibles['Critères']=(criteres)/float(max(criteres))
        dataSorted=dataPossibles.sort_values(by=['Taux_missions_Accomplies'],ascending=False)
        domaineColonne='nb_missions_'+domaine.replace("DomainLW_", "")
        dataSorted[domaineColonne]=dataPossibles[domaine].astype(int)
        return dataSorted[['AvocatId','Critères',domaineColonne]]