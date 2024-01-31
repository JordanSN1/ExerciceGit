while True:
    nombreUtilisateur = int(input("Entrez un nombre: "))

    for i in range(1, 11):
        print(f"{nombreUtilisateur} x {i} = {nombreUtilisateur * i}")

    continuer = input("Voulez-vous recommencer le programme ? (Y/N): ").upper()
    if continuer != 'Y':
        break