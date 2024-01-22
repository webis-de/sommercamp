# 🏕️ sommercamp

Building a search engine from scratch.

## Installation

> TODO: Dev container.

> TODO: Python dependencies.

```shell
pip install -e .
```

## Usage

> TODO: Usage intro.

### Scraping a website

> TODO

```shell
scrapy runspider sommercamp/crawler.py -O data/documents.jsonl
```

### Indexing the crawled websites

> TODO

```shell
python sommercamp/indexer.py data/documents.jsonl data/index/
```

### Searching the index

> TODO

```shell
python sommercamp/searcher.py data/index/ "Informatik"
```

### Creating an interface to the search engine

> TODO

### Extras

> TODO: Some extras that students can implement when they have the standard template ready.