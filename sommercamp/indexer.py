# Hier importieren wir die benötigten Softwarebibliotheken.
from os.path import exists, abspath
from json import loads
from shutil import rmtree
from sys import argv
from pyterrier import started, init
# Die PyTerrier-Bibliothek muss zuerst gestartet werden,
# um alle seine Bestandteile importieren zu können.
if not started():
    init()
from pyterrier.index import IterDictIndexer


# Diese Funktion liest jedes Dokument aus der Dokumenten-Sammlung ein
# und gibt es als Python-Objekt zurück.
def iterate_documents(documents_file):
    # Öffne die Datei (Dateiname aus `documents_file`) im Lesemodus.
    with open(documents_file, "rt") as lines:
        # Schleife, die jede Zeile einzeln einliest.
        for line in lines:
            # Lade das Dokument aus der Zeile als Python-Objekt.
            document = loads(line)
            # Gib die URL im Terminal aus, sodass du
            # den Fortschritt beim Indizieren siehst.
            print(document["url"])
            yield document


# Diese Funktion indiziert die Dokumente aus der Dokumenten-Sammlung
# und speichert den Index an der angegebenen Stelle ab.
def index(documents_file, index_dir):
    # Erzeuge hier den Indexer von PyTerrier.
    indexer = IterDictIndexer(
        # Der Pfad, wo der Index gespeichert werden soll.
        abspath(index_dir),
        # Die maximale Länge in Buchstaben für jedes Feld im Index.
        # (Die Werte unten sollten locker reichen.)
        meta={
            "docno": 100,
            "url": 1000,
            "title": 1000,
            "text": 100_000,
        },
    )
    # Starte das Indizieren.
    indexer.index(iterate_documents(documents_file))


# Die Hauptfunktion, die beim Ausführen der Datei aufgerufen wird.
def main():
    # Lade den Pfad zur Dokumenten-Sammlung aus dem
    # ersten Kommandozeilen-Argument.
    documents_file = argv[1]
    # Lade den Pfad zum Index aus dem zweiten Kommandozeilen-Argument.
    index_dir = argv[2]

    # Wenn du schon vorher etwas indiziert hattest, lösche den alten Index.
    if exists(index_dir):
        rmtree(index_dir)

    # Rufe die Index-Funktion von oben auf.
    index(documents_file, index_dir)


if __name__ == "__main__":
    main()
