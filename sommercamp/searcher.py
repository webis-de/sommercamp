from os.path import exists, abspath
from sys import argv
from pyterrier import started, init


if not started():
    init()
from pyterrier import IndexFactory
from pyterrier.batchretrieve import BatchRetrieve
from pyterrier.text import get_text


def search(index_dir, query):
    index = IndexFactory.of(abspath(index_dir))
    searcher = BatchRetrieve(
        index,
        wmodel="BM25",
        num_results=10,
    )

    text_getter = get_text(index, metadata=["url", "title", "text"])

    pipeline = searcher >> text_getter

    results = pipeline.search(query)
    return results


def main():
    index_dir = argv[1]
    query = argv[2]
    if not exists(index_dir):
        exit(1)

    print("Searching...")

    results = search(index_dir, query)

    print(results)


if __name__ == "__main__":
    main()
