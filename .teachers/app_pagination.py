# Hier importieren wir die benötigten Softwarebibliotheken.
from math import ceil
from os.path import abspath, exists
from sys import argv
from streamlit import (text_input, number_input, header, title, subheader, 
    container, markdown, link_button, divider, set_page_config)
from pyterrier import started, init
# Die PyTerrier-Bibliothek muss zuerst gestartet werden,
# um alle seine Bestandteile importieren zu können.
if not started():
    init()
from pyterrier import IndexFactory
from pyterrier.batchretrieve import BatchRetrieve
from pyterrier.text import get_text


# Diese Funktion baut die App für die Suche im gegebenen Index auf.
def app(index_dir) -> None:

    # Konfiguriere den Titel der Web-App (wird im Browser-Tab angezeigt)
    set_page_config(
        page_title="Schul-Suchmaschine",
        layout="centered",
    )

    # Gib der App einen Titel und eine Kurzbeschreibung:
    title("Schul-Suchmaschine")
    markdown("Hier kannst du unsere neue Schul-Suchmaschine nutzen:")

    # Erstelle ein Text-Feld, mit dem die Suchanfrage (query) 
    # eingegeben werden kann.
    query = text_input(
        label="Suchanfrage",
        placeholder="Suche...",
        value="Schule",
    )

    # Wenn die Suchanfrage leer ist, dann kannst du nichts suchen.
    if query == "":
        markdown("Bitte gib eine Suchanfrage ein.")
        return

    # Öffne den Index.
    index = IndexFactory.of(abspath(index_dir))
    # Initialisiere den Such-Algorithmus. 
    searcher = BatchRetrieve(
        index,
        wmodel="BM25",
        num_results=1000,
    )
    # Führe eine Vorab-Suche durch, um die Gesamtanzahl 
    # der Ergebnisse zu ermitteln.
    all_results = searcher.search(query)
    # Ermittle die Anzahl aller Ergebnisse.
    total_results = len(all_results)

    # Zeige eine Unter-Überschrift vor den Suchergebnissen an.
    divider()
    header("Suchergebnisse")

    # Wenn die Ergebnisliste leer ist, gib einen Hinweis aus.
    if total_results == 0:
        markdown("Keine Suchergebnisse.")
        return

    # Wenn es Suchergebnisse gibt, dann zeige an, wie viele.
    markdown(f"{total_results} Suchergebnisse.")

    # Lege die Seitengröße fest.
    page_size = 10
    # Berechne die Gesamtanzahl der Seiten.
    total_pages = ceil(total_results / page_size)
    # Erstelle ein Eingabe-Feld für die Seitennummer.
    current_page = number_input(
        "Ergebnisseite", min_value=1, max_value=total_pages, step=1,
    )
    # Berechne die Start- und End-Position der anzuzeigenden Dokumente.
    start = page_size * (current_page - 1)
    end = page_size * current_page
    end = min(end, total_results)
    markdown(f"Zeige Ergebnisse {start} bis {end}.")

    # Initialisiere das Modul, zum Abrufen der Texte.
    text_getter = get_text(index, metadata=["url", "title", "text"])
    # Baue die Such-Pipeline zusammen.
    # (Weiter als bis zum letzten anzuzeigenden Dokument musst du nicht suchen.)
    pipeline = (searcher % end) >> text_getter
    # Führe die Such-Pipeline aus und suche nach der Suchanfrage.
    results = pipeline.search(query)
    # Schneide alle Ergebnisse bis zum ersten anzuzeigenden Ergebnis ab.
    results = results[start:]

    # Gib nun der Reihe nach, alle Suchergebnisse aus.
    for _, row in results.iterrows():
        # Pro Suchergebnis, erstelle eine Box (container).
        with container(border=True):
            # Zeige den Titel der gefundenen Webseite an.
            subheader(row["title"])
            # Speichere den Text in einer Variablen (text).
            text = row["text"]
            # Schneide den Text nach 500 Zeichen ab.
            text = text[:500]
            # Ersetze Zeilenumbrüche durch Leerzeichen.
            text = text.replace("\n", " ")
            # Zeige den Dokument-Text an.
            markdown(text)
            # Gib Nutzern eine Schaltfläche, um die Seite zu öffnen.
            link_button("Seite öffnen", url=row["url"])


# Die Hauptfunktion, die beim Ausführen der Datei aufgerufen wird.
def main():
    # Lade den Pfad zum Index aus dem ersten Kommandozeilen-Argument.
    index_dir = argv[1]

    # Wenn es noch keinen Index gibt, kannst du die Suchmaschine nicht starten.
    if not exists(index_dir):
        exit(1)

    # Rufe die App-Funktion von oben auf.
    app(index_dir)


if __name__ == "__main__":
    main()
