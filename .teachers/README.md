# Für Lehrende

> **Hinweis:** Die nachfolgende Dokumentation richtet sich nur an Lehrende. Wenn du Schüler:in bist, schau bitte in die [Haupt-Dokumentation](../README.md)

Dieses Sommercamp-Workshop richtet sich an Schüler:innen ab 14 Jahren. Alle Inhalte sind für einen leichten Start der noch programmier-unerfahrenen Schüler:innen vorbereitet.

Für Lehrende, die diesen Workshop durchführen wollen, erläutern wir im Folgenden die [Grundstruktur des Code-Repositorys](#repository-struktur), das [Vorgehen](#workshop-start), wie du deinen Workshop starten kannst und Tricks, um [ad hoc Schüler:innen zu helfen](#ad-hoc-hilfe).

## Voraussetzungen

Dieser Workshop hat nur einige grundlegende Voraussetzungen:

- Schüler:innen ab 14 Jahre
- Computer (Thin-Clients reichen)
- Web-Browser (empfohlen: Mozilla Firefox)
- GitHub-Account (kann z.B. vorab von den Workshop-Organisator:innen erstellt werden)

Durch die Nutzung von [GitHub Codespaces](https://github.com/features/codespaces) sind weder viel Rechenleistung, Speicherplatz noch ein Webserver nötig.

## Repository-Struktur

Da das Repository darauf ausgelegt ist, dass Schüler:innen es auf GitHub forken, sind alle Dateien im `main`-Branch des Repositorys enthalten.

Im Sommercamp-Workshop arbeiten wir an vier Dateien, die jeweils eins der vier Teilziele des Workshops abdecken:

- [`crawler.py`](crawler.py): Skript zum Crawlen und Text Parsen einer beliebigen (kleinen) Webseite.
- [`indexer.py`](indexer.py): Skript zum erstellen des invertierten Index aus den gecrawlten Dokumenten.
- [`searcher.py`](searcher.py): Skript für die Suche per Terminal.
- [`app.py`](app.py): Streamlit-App mit Web-Oberfläche für die Suchmaschine.

Für den Start des Workshops sind diese vier Python-Skripte `crawler.py`, `indexer.py`, `searcher.py` und `app.py` erst einmal leer. Schüler:innen sollen in diesen selbständig den Python-Code schreiben, wie es in der [Haupt-Dokumentation](../README.md) (und live im Workshop) für sie erläutert wird.

## Workshop-Start

Die Folgenden Schritte sollten die Schüler:innen durchführen, um ihren Arbeitsplatz für die Workshop-Teilnahme vorzubereiten.
Der erste Einstiegs-Vortrag kann dann stattfinden, während die Codespaces der Schüler:innen aufgesetzt werden, um die Wartezeit zu überbrücken.

1. Öffne den Web-Browser (z.B. Mozilla Firefox).
2. Gehe zu [`github.com/login`](https://github.com/login).
3. Logge dich mit Benutzername und Passwort ein.
4. Gehe zu [`github.com/webis-de/sommercamp`](https://github.com/webis-de/sommercamp).
5. Klicke auf <kbd>Fork</kbd>, dann bestätige mit <kbd>Create fork</kbd>.
6. Klicke auf <kbd>Open in GitHub Codespaces</kbd>, dann auf <kbd>Create codespace</kbd> (oder <kbd>Resume this codespace</kbd>).
7. Höre dem Einstiegs-Vortrag zu, während der Codespace aufgesetzt wird.
8. Folge den weiteren Anweisungen aus der [Dokumentation](../README.md).

## Ad hoc Hilfe

Um Lehrenden in Situationen zu helfen, wenn Schüler:innen nicht weiter kommen, sind alle fertigen Skripte jedoch zusätzlich in dem versteckten `.teachers`-Ordner hinterlegt. So kannst du als Lehrende:r direkt die aktuelle Datei eines Schülers mit der Musterlösung vergleichen, indem du folgendes im Terminal eingibst:

```shell
code --diff .teachers/app.py sommercamp/app.py
```

In der Diff-Ansicht, die sich dann öffnet, kannst du die Unterschiede zwischen der Musterlösung und der aktuellen Implementation der Schülerin oder des Schülers sehen.
Per klick auf den Rechtspfeil (→) kannst du auch einzelne Teilabschnitte der Musterlösung direkt übernehmen.

Für die Extras der App stehen im `.teachers`-Ordner außerdem vorgefertigte Implementationen zur Verfügung:

- [`app_pagination.py`](app_pagination.py): Such-App mit Seitennummerierung.
- [`app_snippets.py`](app_snippets.py): Such-App mit Kurzzusammenfassungen (Snippets).

Auch hier kann die Musterlösung leicht mit der aktuellen Lösung der Schülerin / des Schülers verglichen werden, z.B.:

```shell
code --diff .teachers/app_pagination.py sommercamp/app.py
```

## Beitragen

Wir geben uns Mühe, die Inhalte so einfach wie möglich darzustellen, aber natürlich gibt es noch Raum für Verbesserungen. Wenn du selbst Lehrer:in oder Dozent:in bist, kannst du uns helfen, indem du uns entweder [Ideen oder Wünsche schreibst](https://github.com/webis-de/sommercamp/issues/new) oder selbst bei der Entwicklung unterstützt.

Wir bitten dich, bei neuen Beiträgen zu diesem Repository, Bezeichner im Code (Variablennamen, Klassen, etc.) mit englischen Namen zu bennenen, aber erklärende Kommentare in deutsch zu verfassen, damit auch Schüler:innen aus früheren Klassenstufen die Inhalte grob verstehen können.

Ansonsten kannst du zum Entwickeln oder Verbessern genauso im GitHub Codespace arbeiten, wie die Schüler:innen.
