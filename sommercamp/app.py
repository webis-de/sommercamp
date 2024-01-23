from os.path import abspath, exists
from sys import argv
from streamlit import text_input, header, title, subheader, container, \
    markdown, link_button, divider, set_page_config

from pyterrier import started, init
if not started():
    init()
from pyterrier import IndexFactory
from pyterrier.batchretrieve import BatchRetrieve
from pyterrier.text import get_text, snippets, sliding, scorer


def app(index_dir: str) -> None:
    set_page_config(
        page_title="Schul-Suchmaschine",
        page_icon="🔍",
        layout="centered",
    )

    title("Schul-Suchmaschine")
    markdown("Hier kannst du unsere neue Schul-Suchmaschine nutzen:")

    query = text_input(
        label="🔍 Suchanfrage",
        placeholder="Suche...",
        value="Schule",
    )
    if query == "":
        markdown("Bitte gib eine Suchanfrage ein.")
        return

    index = IndexFactory.of(abspath(index_dir))
    searcher = BatchRetrieve(index, wmodel="BM25")
    text_getter = get_text(index, metadata=["url", "title", "text"])

    snippets_splitter = sliding(text_attr="text", length=15, prepend_attr=None)
    snippets_scorer = scorer(body_attr="text", wmodel="Tf", takes="docs")
    snippets_getter = snippets(
        snippets_splitter >> snippets_scorer,
        text_attr="text", summary_attr="snippet"
    )

    pipeline = searcher >> text_getter >> snippets_getter

    divider()
    header("Suchergebnisse")

    results = pipeline.search(query)
    if len(results) == 0:
        markdown("Keine Suchergebnisse 🙁")
        return

    markdown(f"{len(results)} Suchergebnisse 🙂")
    for _, row in results.iterrows():
        with container(border=True):
            subheader(row["title"])
            markdown(row["snippet"])
            link_button(
                label="Seite öffnen",
                url=row["url"],
            )


if __name__ == "__main__":
    index_dir = argv[1]

    if not exists(index_dir):
        exit(1)

    app(index_dir)
