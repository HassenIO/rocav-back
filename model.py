import pandas as pd

def model(compTerit,specialite,domaine):
    dataFinal = pd.read_csv("./dataFinal.csv", sep=",")
     ###### listes des compétences,spécialités et domaines possibles
    compTerritPossibles=[x for x in dataFinal.columns if ('CT_LWord_' in x)]
    specialitePossibles=[x for x in dataFinal.columns if ('SpecLWord_' in x)]
    domainesPossibles=[x for x in dataFinal.columns if ('DomainLW_' in x)]
    compTerit='CT_LWord_'+compTerit.upper()
    specialite='SpecLWord_'+specialite
    domaine='DomainLW_'+domaine
    if (compTerit in compTerritPossibles)&(specialite in specialitePossibles)&(domaine in domainesPossibles):
        dataPossibles= dataFinal[(dataFinal[compTerit]>0)&(dataFinal[specialite]>0)]
        domaineColonne='nb_missions_'+domaine.replace("DomainLW_", "")
        dataPossibles['Taux_missions_Accomplies']=dataPossibles['nb_mission']/max(dataPossibles['nb_mission'])
        dataPossibles['Taux_missions_Domaine_Accomplies']=dataPossibles[domaine]/sum(dataPossibles[domaine])
        dataPossibles[domaineColonne]=dataPossibles[domaine].astype(int)
        criteres=dataPossibles['Taux de reussite']+dataPossibles['Taux Part reussite']-dataPossibles['Taux_Echec']+dataPossibles['Taux_missions_Accomplies']+dataPossibles['Taux_missions_Domaine_Accomplies']
        if (len(dataPossibles)>1):         
            dataPossibles['Critères']=(criteres-min(criteres))/float(max(criteres)-min(criteres))
            dataSorted=dataPossibles.sort_values(by=['Critères'],ascending=False)
            return dataSorted[['AvocatId','nameAvocat','Critères',domaineColonne,'Partenaire', 'Côut']]
        elif (len(dataPossibles)==1):
            dataPossibles['Critères']=1
            return dataPossibles[['AvocatId','nameAvocat','Critères',domaineColonne,'Partenaire', 'Côut']]
        else:
            return pd.DataFrame()
