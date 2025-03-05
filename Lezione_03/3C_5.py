nome:str = str(input("Inserire nome: "))
ruolo:str = str(input("Inserire ruolo: "))
eta:int = int(input("Inserire età: "))
utente:dict = {"name": nome, "role": ruolo, "age": eta}

match utente:

    case {"name": nome, "role": "admin", "age": eta}:
        print("Accesso completo a tutte le funzionalità")

    case {"name": nome, "role": "moderatore", "age": eta}:
        print("Può gestire i contenuti ma non modifcare le impostazioni")

    case {"name": nome, "role": "utente", "age": eta}:
        if eta >= 18:
            print("Accesso standard a tutti i servizi")
        else:
            print("Accesso limitato! Alcune funzionalità sono bloccate")

    case {"name": nome, "role": "ospite", "age": eta}:
        print("Accesso ristretto! Solo visualizzazione dei contenuti")

    case _:
        print("Attenzione! Ruolo non riconosciuto! Accesso negato.")
    