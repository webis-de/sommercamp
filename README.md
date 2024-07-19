# 🏕️ sommercamp

Baue dir deine eigene Suchmaschine.

[![In GitHub Codespaces öffnen](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new/webis-de/sommercamp?quickstart=1)

Dieser Workshop zum wurde entwickelt von der [Webis-Gruppe](https://webis.de/) für Schüler:innen ab 14 Jahren. Er findet beispielsweise beim [Informatik Sommercamp](https://sommercamp.uni-jena.de/) der [Friedrich-Schiller-Universität Jena](https://uni-jena.de/) statt.

<small>Tipp: Wir bieten auch einen inhaltsgleichen [englischen Kurs](https://github.com/webis-de/summercamp) an.</small>

<details>
<summary>Screenshot der Suchmaschine</summary>

![Screenshot der Suchmaschine](documentation/screenshot.png)

</details>

## Installation

Um die Suchmaschine zu bauen, musst du zunächst einige Programme und Software-Bibliotheken installieren.
Diese brauchst du im späteren Verlauf.

**Fertige Entwicklungsumgebung**
Am einfachsten startest du mit einer fertigen Entwicklungsumgebung, wo alles bereits installiert ist oder automatisch nach installiert wird.

Klicke dazu auf die folgende Schaltfläche:

[![In GitHub Codespaces öffnen](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new/webis-de/sommercamp?quickstart=1)

In dem Fenster, das sich dann öffnet, hast du zwei Optionen:

1. Wähle entweder eine schon laufende Entwicklungsumgebung aus (falls du vorher schon eine erstellt hattest).
2. Oder klicke auf die grüne Schaltfläche <kbd>Create new codespace</kbd>, um eine neue Entwicklungsumgebung zu erstellen.

Es öffnet sich ein Browser-Fenster mit der Entwicklungsumgebung.
Warte bitte eine Weile (bis zu 5 Minuten), bis keine Fortschrittsanzeigen mehr zu sehen sind. Solange werden noch automatisch alle benötigten Software-Bibliotheken installiert.

Dein Browserfenster sollte nun in etwa so aussehen und eine Liste mit Dateien anzeigen:
![Screenshot von GitHub Codespaces](docs/screenshot-codespace.png)

_Tipp:_ Falls du später Software-Abhängigkeiten veränderst, kannst du die Software-Bibliotheken jederzeit neu installieren. Öffne dazu zuerst eine Kommandozeile in der Entwicklungsumgebung.

Klicke dazu auf die drei Striche (![Menü-Button in GitHub Codespaces](docs/screenshot-codespace-menu-button.png)) und dann im Menü "Terminal" auf "New Terminal". Es öffnet sich nun eine Kommandozeile im unteren Bereich des Bildschirms.

Dort gib folgendes ein, um die benötigte Software neu zu installieren:

```shell
pip install -e ./
```

<details><summary><strong>Manuelle Installation</strong></summary>

_Wichtig:_ Die Anleitung zur manuellen Installation ist etwas für erfahrenere Progrmmierer.
Normalerweise solltest du lieber die fertige Entwicklungsumgebung benutzen, wie oben beschrieben.
In den folgenden Abschnitten gehen wir davon aus, dass du ein Linux-Betriebssystem hast. Wenn du ein anderes Betriebssystem hast, frag bitte nach.

Zur manuellen Installation, lade dir zuerst [Python 3.11](https://python.org/downloads/) herunter und installiere es auf deinem PC.

Dann kannst du eine virtuelle Umgebung erstellen. So kannst du Software installieren, ohne andere Programme auf deinem Computer zu beeinflussen. Öffne dazu die Kommandozeile deines PCs in diesem Ordner und gib folgendes ein:

```shell
python3.11 -m venv ./venv/
```

Nachdem du so eine virtuelle Umgebung erstellt hast, musst du diese noch aktivieren:

```shell
source ./venv/bin/activate
```

Nun erscheint im Terminal vor jeder Eingabezeile die Bezeichnung `(venv)`, wodurch du siehst, dass die virtuelle Umgebung aktiviert ist.

Als letztes musst du noch die benötigten Software-Bibliotheken installieren:

```shell
pip install -e ./
```

</details>

Das wars, du kannst nun mit dem ["Crawlen"](#eine-webseite-crawlen) starten.

## Eine Webseite "crawlen"

Für deine Suchmaschine brauchst du zuerst eine Sammlung von Dokumenten, die du durchsuchen willst.

Bei Websuchmaschinen sind das eine oder mehrere Webseiten.
(Bei Google/Bing sind es fast alle bekannten Webseiten.)
Wir wollen aber klein starten und erstmal eine Webseite deiner Wahl durchsuchbar machen.
Wie wäre es denn zum Beispiel mit der Webseite deiner Schule, deines Sportvereins?

Wir wollen also den Text und ein paar zusätzliche Daten zu allen Seiten eines Webauftritts abspeichern. Das nennt man "Crawlen" und das Programm, was das tut, heißt "Crawler" oder "Spider". **TODO Folien.**
Damit wir nicht alles von Null auf selbst programmieren müssen, nutzen wir die [Software-Bibliothek "Scrapy"](https://docs.scrapy.org/en/latest/index.html) für das Crawlen.

Erstelle eine neue neue Datei `crawler.py` im Verzeichnis `sommercamp/` und schreibe darin diesen Quellcode:

<details><summary><strong>Quellcode für `sommercamp/crawler.py`</strong></summary>

```python
# Hier importieren wir die benötigten Softwarebibliotheken.
from resiliparse.extract.html2text import extract_plain_text
from scrapy import Spider, Request
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.http.response.html import HtmlResponse


class SchoolSpider(Spider):
    # Gib hier dem Crawler einen eindeutigen Name,
    # der beschreibt, was du crawlst.
    name = "school"

    start_urls = [
        # Gib hier mindestens eine (oder mehrere) URLs an,
        # bei denen der Crawler anfangen soll,
        # Seiten zu downloaden.
        "https://wilhelm-gym.de/",
    ]
    link_extractor = LxmlLinkExtractor(
        # Beschränke den Crawler, nur Links zu verfolgen,
        # die auf eine der gelisteten Domains verweisen.
        allow_domains=["wilhelm-gym.de"],
    )
    custom_settings = {
        # Identifiziere den Crawler gegenüber den gecrawlten Seiten.
        "USER_AGENT": "Sommercamp (https://uni-jena.de)",
        # Der Crawler soll nur Seiten crawlen, die das auch erlauben.
        "ROBOTSTXT_OBEY": True,
        # Frage zu jeder Zeit höchstens 4 Webseiten gleichzeitig an.
        "CONCURRENT_REQUESTS": 4,
        # Verlangsame den Crawler, wenn Webseiten angeben,
        # dass sie zu oft angefragt werden.
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_TARGET_CONCURRENCY": 1,
        # Frage nicht zwei mal die selbe Seite an.
        "HTTPCACHE_ENABLED": True,
    }

    def parse(self, response):
        if not isinstance(response, HtmlResponse):
            # Die Webseite ist keine HTML-Webseite, enthält also keinen Text.
            return
        
        # Speichere die Webseite als ein Dokument in unserer Dokumentensammlung.
        yield {
            # Eine eindeutige Identifikations-Nummer für das Dokument.
            "docno": str(hash(response.url)),
            # Die URL der Webseite.
            "url": response.url,
            # Der Titel der Webseite aus dem <title> Tag im HTML-Code.
            "title": response.css("title::text").get(),
            # Der Text der Webseite.
            # Um den Hauptinhalt zu extrahieren, benutzen wir
            # eine externe Bibliothek.
            "text": extract_plain_text(response.text, main_content=True),
        }

        # Finde alle Links auf der aktuell betrachteten Webseite.
        for link in self.link_extractor.extract_links(response):
            if link.text == "":
                # Ignoriere Links ohne Linktext, z.B. bei Bildern.
                continue
            # Für jeden gefundenen Link, stelle eine Anfrage zum Crawling.
            yield Request(link.url, callback=self.parse)
```

</details>

Alle Zeilen, die mit einem `#` beginnen, sind Kommentare. Diese Zeilen brauchst du nicht abschreiben, sondern kannst sie weglassen.
Dabei solltest du einige Dinge beachten:

- _Name_: Gib deinem Crawler einen Namen (`name`), der nur aus Buchstaben besteht, z.B., `"school"`.
- _Start-URLs_: Damit der Crawler die ersten Links finden kann, gib mindestens eine URL für den Start an (`start_urls`).
- _Link-Einstellungen_: Für das Auslesen neuer Links, konfiguriere den Link-Extraktor (`link_extractor`). Zum Beispiel, kannst du das Crawling auf Domains beschränken.
- _Weitere Einstellungen_: Außerdem sind noch weitere Einstellungen wichtig (`custom_settings`). Wir wollen "höflich" sein und keine Webseite mit Anfragen überlasten. Dazu identifiziert sich der Crawler (`"USER_AGENT"`) und stellt nur begrenzt viele Anfragen gleichzeitig (`"CONCURRENT_REQUESTS"`).
- _Dokument speichern_: Wir speichern für jede Webseite ein Dokument ab (`yield { ... }`), bei dem wir den Text und andere Metadaten in einem "Dictionary" abspeichern. Gib dabei eine eindeutige Dokumentenkennung (`"docno"`), die URL (`"url"`), den Titel (`"title"`) und den Inhalt (`"text"`) der Webseite an.
- _Links verfolgen_: Um weitere, verlinkte Webseiten zu Crawlen stelle eine neue Anfrage `Request` für jeden Link, den der Link-Extraktor gefunden hat.

Nun kannst du den Crawler starten.
Öffne dazu zuerst eine Kommandozeile in der Entwicklungsumgebung.

Klicke dazu auf die drei Striche (![Menü-Button in GitHub Codespaces](docs/screenshot-codespace-menu-button.png)) und dann im Menü "Terminal" auf "New Terminal". Es öffnet sich nun eine Kommandozeile im unteren Bereich des Bildschirms.

Dort tippe folgendes ein:

```shell
scrapy runspider sommercamp/crawler.py --output data/documents.jsonl
```

Die Zeile startet den Crawler und fängt an, die gecrawlten Dokumente (Webseiten-Inhalte) in die Datei [`documents.jsonl`](data/documents.jsonl) im Verzeichnis `data/` zu schreiben. Schau gerne mal rein, indem du [hier](data/documents.jsonl) klickst. Was komisch aussieht, ist ein strukturiertes Datenformat, bei dem in jeder Zeile ein Dokument steht.

Du kannst die Anzahl der Dokumente jederzeit zählen, indem du zuerst ein weiteres Terminal öffnest (Plus-Symbol in der Terminal-Ansicht; ![Weiteres Terminal öffnen in GitHub Codespaces](docs/screenshot-codespace-add-terminal.png)) und dann folgendes eintippst:

```shell
wc -l data/documents.jsonl
```

Die Zahl in der Ausgabe gibt an, wie viele Dokumente du bisher gecrawlt hast.

## Die heruntergeladenen Webseiten indizieren

Damit die heruntergeladenen Webseiten durchsuchbar werden, müssen wir daraus einen "invertierten Index" erstellen. **TODO Folien.**

Dazu benutzen wir wieder eine Software-Bibliothek, [PyTerrier](https://pyterrier.readthedocs.io/en/latest/terrier-indexing.html).

Erstelle eine neue neue Datei `indexer.py` im Verzeichnis `sommercamp/` und schreibe darin diesen Quellcode:

<details><summary><strong>Quellcode für `sommercamp/indexer.py`</strong></summary>

```python
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
```

</details>

Das Python-Programm zum Indexer kannst du dann ausführen, indem du folgendes in dein Terminal eintippst:

```shell
python sommercamp/indexer.py data/documents.jsonl data/index/
```

Wenn du nun einmal in das [Daten-Verzeichnis](data/) guckst, siehst du, dass dort ein neues [Verzeichnis `data/index/`](data/index/) angelegt wurde, in dem sich der Index befindet.
Leider kannst du in diese Index-Dateien nicht rein gucken, weil es Binärdateien sind (bestehend nur aus Einsen und Nullen).
Du kannst aber mit diesen Befehlen im Terminal vergleichen, wie viel Speicherplatz der Index im Vergleich zur Dokumentensammlung verbraucht:

```shell
du -s -h data/documents.jsonl
du -s -h data/index/
```

Tatsächlich ist der invertierte Index ungefähr so groß wie die gecrawlte Dokumenten-Sammlung.

## Im Index suchen

Jetzt wird es richtig spannend: Wir wollen in dem gerade erstellten Index nach Suchbegriffen suchen.


https://pyterrier.readthedocs.io/en/latest/terrier-retrieval.html

> TODO

```shell
python sommercamp/searcher.py data/index/ "Informatik"
```

## Eine Benutzeroberfläche für die Suchmaschine erstellen

> TODO

```shell
streamlit run sommercamp/app.py -- data/index/
```

> TODO: Port veröffentlichen für andere?

## Extras

> TODO: Einige Extras, die Schüler:innen implementieren können, wenn sie die Standardfunktionen fertig haben.

- [Kurz-Zusammenfassungen ("Snippets")](https://pyterrier.readthedocs.io/en/latest/text.html#query-biased-summarisation-snippets)
- [Komponenten für die Benutzeroberfläche](https://docs.streamlit.io/library/api-reference)
- [Seitennummerierung](https://github.com/Socvest/streamlit-pagination)
- [Seitennummerierung (Alternative)](https://medium.com/streamlit/paginating-dataframes-with-streamlit-2da29b080920)
- [Auto-Vervollständigung in der Such-Leiste](https://github.com/m-wrzr/streamlit-searchbox)
- [Design der Benutzeroberfläche](https://docs.streamlit.io/library/advanced-features/theming)
- [Emojis](https://share.streamlit.io/streamlit/emoji-shortcodes)

## Für Lehrende

<details><summary><strong>Hinweise nur für Lehrende</strong></summary>

Dieses Code-Repository richtet sich an Schüler:innen ab Klasse **TODO**. Wir geben uns Mühe, die Inhalte so einfach wie möglich darzustellen, aber natürlich gibt es noch Raum für Verbesserungen. Wenn du selbst Lehrer:in oder Dozent:in bist, kannst du uns helfen, indem du uns entweder [Ideen oder Wünsche schreibst](https://github.com/webis-de/sommercamp/issues/new) oder selbst bei der Entwicklung unterstützt.
Dazu erläutern wir im Folgenden die Grundstruktur des Code-Repositorys.

Das Repository ist in verschiedene Branches aufgeteilt, die den Start "von Null auf" und die vier Teilziele des Sommercamp-Workshops darstellen:

- `main`: Start "von Null auf", der normale Ablauf des Workshops.
- `crawler`: Fertige Crawler-Implementation, falls Schüler:innen beim Programmieren des Crawlers nicht mitkommen.
- `indexer`: Fertige Indexer-Implementation, falls Schüler:innen beim Programmieren des Indexers nicht mitkommen.
- `searcher`: Fertige Suche-Implementation, falls Schüler:innen beim Programmieren des Such-Algorithmus' nicht mitkommen.
- `app`: Fertige App-Implementation der Web-Oberfläche für die Suchmaschine, falls Schüler:innen beim Programmieren der App nicht mitkommen.

Außer des `main` Branches, der den regulären Start des Workshops darstellt, sind die restlichen vier Branches so angelegt, dass Schüler:innen jederzeit durch Mergen auf den jeweils nächsten Implementierungsstand springen können, falls sie sonst den Anschluss an andere Workshop-Teilnehmende verlieren.

(Weitere Branches enthalten Implementierungsideen und Extras, die schnelle Schüler:innen individuell implementieren können: **TODO: Liste**)

Die vier Teilziele finden sich außerdem in der Benennung der Dateien im Python-Modul `sommercamp` wieder.

Wir bitten dich, bei neuen Beiträgen zu diesem Repository, Bezeichner im Code (Variablennamen, Klassen, etc.) mit englischen Namen zu bennenen, aber erklärende Kommentare in deutsch zu verfassen, damit auch Schüler:innen aus früheren Klassenstufen die Inhalte grob verstehen können.

</details>

## Lizenz

Der Quellcode in diesem Repostitory ist unter der [MIT Lizenz](https://choosealicense.com/licenses/mit/) lizensiert. Kursinhalte werden unter der [CC BY 4.0 Lizenz](https://creativecommons.org/licenses/by/4.0/) zur Verfügung gestellt.
Bitte verweise auf dieses Repository, wenn du Inhalte daraus verwendest.
