from forex_python.converter import CurrencyRates, CurrencyCodes

c = CurrencyCodes()
cr = CurrencyRates()
fichier = 'historique.txt'
nouvelle_devise = []
taux = []

def enregistrer_historique(fichier, historique):
    with open(fichier, 'a') as file:
        for ligne in historique:
            file.write(f"{ligne}\n")

def charger_historique(fichier):
    historique = []
    with open('historique.txt', 'w') as file:
        pass

    with open(fichier, 'r') as file:
        historique = [ligne.strip() for ligne in file.readlines()]
    return historique


def est_nombre(montant):
    try:
        float(montant)
        return True
    except ValueError:
        return False

def devise_valide(devise_final):
    return c.get_symbol(devise_final) is not None

historique = charger_historique(fichier)

while True:
    option = input("""
            Appuyez sur 'entrée' pour lancer le convertisseur
            Entrez 'h' pour afficher l'historique
            Entrez 'n' pour ajouter une nouvelle devise
            Entrez 'c' pour afficher la liste des devises disponibles
           """)
    if option == '':
        montant = input("Entrez le montant à convertir : ")
        devise_final = input("En quelle devise voulez-vous convertir ? ").upper()

        if est_nombre(montant) and devise_valide(devise_final):
            montant = float(montant)
            converti = cr.convert('EUR', devise_final, montant)
            print(f"{montant} € équivaut à {round(converti, 2)} {c.get_symbol(devise_final)}")

            historique.append(f"=> {montant} € = {round(converti, 2)} {devise_final}")
            enregistrer_historique(fichier, historique)

        elif devise_final in nouvelle_devise:
            montant = float(montant)
            for i in range(len(nouvelle_devise)):
                if devise_final == nouvelle_devise[i]:
                    converti = montant / taux[i]
                    print(f"{montant} € équivaut à {round(converti, 2)} {devise_final}")
                    historique.append(f"=> {montant} € = {round(converti, 2)} {devise_final}")
                    enregistrer_historique(fichier, historique)
                    
        else:
            print("Erreur: Montant non valide.")

    elif option.lower() == 'h':
        print("Historique des résultats:")
        for ligne in historique:
            print(ligne)
    
    elif option.lower() == 'n':
        nom = input("Veuillez entrer le nom de la nouvelle devise: ").upper()
        if nom in nouvelle_devise:
            print(f"{nom} est déjà une nouvelle devise.")
        else:
            valeur = float(input("Veuillez entrer le taux de conversion de la devise: "))
            nouvelle_devise.append(nom)
            taux.append(valeur)

    elif option.lower() == 'c':
        print ("""
                        Liste des monnaies disponible
               
    USD : Dollar américain | JPY : Yen japonais   | MYR : Ringgit malaisien
    CZK : Couronne tchèque | BRL : Réal brésilien | AUD : Dollar australien
    HUF : Forint hongrois  | PLN : Złoty polonais | IDR : Roupie indonésienne
    SEK : Couronne danoise | CHF : Franc suisse   | ISK : Couronne islandaise
    TRY : Livre turque     | PHP : Peso philippin | DKK : Couronne suédoise
    CAD : Dollar canadien  | CNY : Yuan chinois   | NOK : Couronne norvégienne
    INR : Roupie indienne  | RON : Leu roumain    | HKD : Dollar de Hong Kong
    KRW : Won sud-coréen   | MXN : Peso mexicain  | NZD : Dollar néo-zélandais
    BGN : Lev bulgare      | GBP : Livre sterling | SGD : Dollar singapourien
    THB : Baht thaïlandais | ZAR : Rand sud-africain

    """)