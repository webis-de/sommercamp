# Hier importieren wir die benötigten Softwarebibliotheken.
from os.path import exists, abspath
from sys import argv
from pyterrier import started, init
# Die PyTerrier-Bibliothek muss zuerst gestartet werden,
# um alle seine Bestandteile importieren zu können.
if not started():
    init()
from pyterrier import IndexFactory
from pyterrier.batchretrieve import BatchRetrieve
from pyterrier.text import get_text


# In dieser Funktion öffnen wir den Index und suchen darin 
# nach der gegebenen Suchanfrage ("query").
def search(index_dir, query):
    # Öffne den Index.
    index = IndexFactory.of(abspath(index_dir))
    # Initialisiere den Such-Algorithmus. 
    searcher = BatchRetrieve(
        index,
        # Der bekannteste Suchalgorithmus heißt "BM25".
        wmodel="BM25",
        # Und es sollen bis zu 10 Ergebnisse zurückgegeben werden.
        num_results=10,
    )
    # Initialisiere ein Modul, was den Text 
    # der gefundenen Dokumente aus dem Index lädt.
    text_getter = get_text(index, metadata=["url", "title", "text"])
    # Baue nun die "Pipeline" für die Suche zusammen: 
    # Zuerst suchen, dann Text abrufen.
    pipeline = searcher >> text_getter
    # Führe die Such-Pipeline aus und suche nach der Suchanfrage (query).
    results = pipeline.search(query)
    return results


# Die Hauptfunktion, die beim Ausführen der Datei aufgerufen wird.
def main():
    # Lade den Pfad zum Index aus dem ersten Kommandozeilen-Argument.
    index_dir = argv[1]
    # Lade die Suchanfrage aus dem zweiten Kommandozeilen-Argument.
    query = argv[2]

    # Wenn es noch keinen Index gibt, können wir nichts zurückgeben.
    if not exists(index_dir):
        exit(1)

    print("Searching...")
    # Rufe die Such-Funktion von oben auf.
    results = search(index_dir, query)
    # Gib die Suchergebnisse im Terminal aus.
    print(results)

if __name__ == "__main__":
    main()
