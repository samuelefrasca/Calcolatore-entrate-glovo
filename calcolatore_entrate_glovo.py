# CALCOLATORE ENTRATE GLOVO
# FASE 1: QUANTE ENTRATE HAI IN TOTALE
# FASE 2: QUANTE SONO MANCE
# FASE 3: RIMUOVERE IL 20% DAL TOTALE TOGLIENDO LE MANCE
# FASE 4: MOSTRARE PAGAMENTO + MANCE

import os

print("CALCOLATORE ENTRATE GLOVO")
while True:
    try:
        entrate_lordo = input("Entrate complessive: ")
        if entrate_lordo.lower() == "":
            entrate_lordo = 0.0
        else:
            entrate_lordo=float(entrate_lordo)
            if entrate_lordo < 0:
                print("Le entrate complessive non possono essere minori di 0. Riprova.")
                continue

        mance = input("Mance (Premi INVIO per proseguire): ")
        if mance.lower() == "":
            mance = 0.0
        else:
            mance = float(mance)
            if mance < 0:
                print("Le mance non possono essere minori di 0. Riprova.")
                continue

        contanti1_input = input("Prelievo quotidiano maturato (Premi INVIO per proseguire): ")
        if contanti1_input.lower() == "":
            contanti1 = 0.0
        else:
            contanti1 = float(contanti1_input)
            if contanti1 < 0:
                print("Il prelievo quotidiano maturato non può essere minore di 0. Riprova.")
                continue

        contanti2_input = input("Prelievo di fine periodo (Premi INVIO per proseguire): ")
        if contanti2_input.lower() == "":
            contanti2 = 0.0
        else:
            contanti2 = float(contanti2_input)
            if contanti2 < 0:
                print("Il prelievo di fine periodo non può essere minore di 0. Riprova.")
                continue

    except ValueError:
        os.system('cls')
        print("Per favore inserisci un valore numerico valido.")
        continue

    contanti = contanti1 + contanti2
    entrate_senza_mance = entrate_lordo - mance
    entrate_netto = entrate_senza_mance * 0.8
    entrate_totali = entrate_netto + mance
    senza_contanti = entrate_totali - contanti

    print(f"\nIl tuo guadagno lordo è stato: {entrate_lordo:.2f}€")
    print(f"Di cui mance: {mance:.2f}€")
    print(f"Il tuo guadagno senza mance: {entrate_senza_mance:.2f}€")
    print(f"Le tue entrate nette (20% va in Ritenuta d'acconto) sono: {entrate_netto:.2f}€")
    print(f"TOTALE ENTRATE: {entrate_totali:.2f}€")
    print(f"Hai avuto {contanti:.2f}€ entrate in contanti")
    print(f"BONIFICO: {senza_contanti:.2f}€")

    while True:
        restart = input("\nVuoi fare altro? Digita:\n1 - Continua\n2 - Esci\nScelta: ").strip()
        if restart == "1":
            os.system('cls')
            break
        elif restart == "2":
            print("Grazie per aver utilizzato il Calcolatore Entrate Glovo!")
            exit()
        else:
            print("Inserisci un valore valido (1 o 2).")