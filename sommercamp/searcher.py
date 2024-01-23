from os.path import exists, abspath
from sys import argv

from pyterrier import started, init
if not started():
    init()
from pyterrier import IndexFactory
from pyterrier.batchretrieve import BatchRetrieve
from pyterrier.text import get_text


def search(index_dir: str, query: str) -> None:
    print("Searching...")
    index = IndexFactory.of(abspath(index_dir))
    searcher = BatchRetrieve(index, wmodel="BM25")
    text_getter = get_text(index, metadata=["url", "title", "text"])
    pipeline = searcher >> text_getter
    results = pipeline.search(query)
    print(results.head(10))


if __name__ == "__main__":
    index_dir = argv[1]
    query = argv[2]

    if not exists(index_dir):
        exit(1)

    search(index_dir, query)
