


from os.path import abspath, exists
from sys import argv
from streamlit import (text_input, header, title, subheader, container, markdown, link_button, divider, set_page_config)
from pyterrier import started, init


if not started():
    init()
from pyterrier import IndexFactory
from pyterrier.batchretrieve import BatchRetrieve
from pyterrier.text import get_text


def app(index_dir):

    set_page_config(
        page_title="Remchingen Suchmaschine",
        layout="centered",
    )

    title("Suchmaschine von Remchingen 🏘")
    markdown("Hier kannst viele Informationen zur Gemeinde Remchingen finden.")

    query = text_input(
        label="Suchanfrage",
        placeholder="Suche...",
        value="",
    )

    if query == "":
        markdown("Bitte gib eine Suchanfrage ein.")
        return

    index = IndexFactory.of(abspath(index_dir))

    searcher = BatchRetrieve(
        index,
        wmodel="BM25",
        num_results=10,
    )

    pyterrier.text.snippets(text_scorer_pipe, text_attr='text', summary_attr='summary', num_psgs=5, joinstr='...')

    text_getter = get_text(index, metadata=["url", "title", "text"])

    pipeline = searcher >> text_getter

    results = pipeline.search(query)

    divider()
    header("Suchergebnisse")

    if len(results) == 0:
        markdown("Keine Suchergebnisse.")
        return

    markdown(f"{len(results)} Suchergebnisse.")

    for _, row in results.iterrows():
        with container(border=True):
            subheader(row["title"])
            text = row["text"]
            text = text[:500]
            text = text.replace("\n", " ")
            markdown(text)
            link_button("Seite öffnen", url=row["url"])


def main():
    index_dir = argv[1]
    if not exists(index_dir):
        exit(1)
    app(index_dir)


if __name__ == "__main__":
    main()
