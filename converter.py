import pandas as pd
import os

# Chiede all'utente di inserire il percorso della cartella
folder = input("Inserisci il percorso della cartella con i file .xlsx: ").strip()

# Controlla se il percorso esiste
if not os.path.isdir(folder):
    print("Errore: La cartella specificata non esiste.")
else:
    # Elenca tutti i file .xlsx nella cartella
    for filename in os.listdir(folder):
        if filename.endswith('.xlsx'):
            file_path = os.path.join(folder, filename)  # Percorso completo

            # Leggi il file .xlsx
            df = pd.read_excel(file_path)

            # Salva come .csv con lo stesso nome
            new_filename = os.path.splitext(filename)[0] + '.csv'
            df.to_csv(os.path.join(folder, new_filename), index=False)

            print(f"Convertito: {filename} -> {new_filename}")

print("Conversione completata!")
