from os.path import exists, abspath
from json import loads
from shutil import rmtree
from sys import argv
from typing import Any, Iterator

from pyterrier import started, init
if not started():
    init()
from pyterrier.io import autoopen
from pyterrier.index import IterDictIndexer


def iterate_documents(documents_file: str) -> Iterator[dict[str, Any]]:
    with autoopen(documents_file, "rt") as lines:
        for line in lines:
            document = loads(line)
            yield document


def index(documents_file: str, index_dir: str) -> None:
    print("Indexing...")
    indexer = IterDictIndexer(
        abspath(index_dir),
        meta={"docno": 36, "url": 256, "title": 256, "text": 10_000},
    )
    indexer.index(iterate_documents(documents_file))


if __name__ == "__main__":
    documents_file = argv[1]
    index_dir = argv[2]

    if exists(index_dir):
        rmtree(index_dir)

    index(documents_file, index_dir)
