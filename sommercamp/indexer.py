from os.path import exists, abspath
from json import loads
from shutil import rmtree
from sys import argv
from pyterrier import started, init

if not started():
    init()

from pyterrier.index import IterDictIndexer


def iterate_documents(documents_file):
    with open(documents_file, "rt") as lines:
        for line in lines:
            document = loads(line)
            print(document["url"])
            yield document


def index(documents_file, index_dir):
    indexer = IterDictIndexer(
       abspath(index_dir),
       meta={
            "docno": 100,
            "url": 1000,
            "title": 1000,
            "text": 100_000,
        },
    )
    indexer.index(iterate_documents(documents_file))


def main():
    documents_file = argv[1]
    index_dir = argv[2]

    if exists(index_dir):
        rmtree(index_dir)

    index(documents_file, index_dir)


if __name__ == "__main__":
    main()
