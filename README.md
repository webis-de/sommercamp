# 🏕️ sommercamp

Building a search engine from scratch.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/heinrichreimer/sommercamp?quickstart=1)

This workshop on how to build a search engine is developed by the [Webis group](https://webis.de/) and designed for students of age 14 and above.
It is planned for the [Computer Science Summer Camp 2024](https://www.sommercamp.uni-jena.de/2024) at [Friedrich-Schiller-Universität Jena](https://uni-jena.de/). To sign up, please refer to the [summer camp website](https://sommercamp.uni-jena.de/).

<details>
<summary>Show a screenshot of the search engine.</summary>

![Screenshot of the search engine](documentation/screenshot.png)

</details>

## Installation

The easiest way to start with the workshop is to open this repository in GitHub Codespaces: \
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/heinrichreimer/sommercamp?quickstart=1) \
This will install all necessary software.

Once the editor window has fully loaded (i.e., no progress bars visible; that may take a while), we can start installing the Python software dependencies:> TODO: Python dependencies. To do so, open a terminal (Top menu > Terminal > New terminal) and type:

```shell
pip install -e .
```
(Do not forget the dot `.` at the end of the line 😉)

## Usage

> TODO: Usage intro.

### Scraping a website

https://docs.scrapy.org/en/latest/index.html

> TODO

```shell
scrapy runspider sommercamp/crawler.py -O data/documents.jsonl
```

> TODO: How long does the crawling take?

```shell
du -h data/documents.jsonl
```

### Indexing the crawled websites

https://pyterrier.readthedocs.io/en/latest/terrier-indexing.html

> TODO

```shell
python sommercamp/indexer.py data/documents.jsonl data/index/
```

### Searching the index

https://pyterrier.readthedocs.io/en/latest/terrier-retrieval.html

> TODO

```shell
python sommercamp/searcher.py data/index/ "Informatik"
```

### Creating an interface to the search engine

> TODO

```shell
streamlit run sommercamp/app.py -- data/index/
```

### Extras

> TODO: Some extras that students can implement when they have the standard template ready.

- Search query from URL: https://docs.streamlit.io/library/api-reference/utilities/st.query_params
- Snippets: https://pyterrier.readthedocs.io/en/latest/text.html#query-biased-summarisation-snippets
- UI components: https://docs.streamlit.io/library/api-reference
- Page numbering: https://github.com/Socvest/streamlit-pagination
- Page numbering (alternative): https://medium.com/streamlit/paginating-dataframes-with-streamlit-2da29b080920
- Auto-complete search box: https://github.com/m-wrzr/streamlit-searchbox
- Theming: https://docs.streamlit.io/library/advanced-features/theming
- Emojis: https://share.streamlit.io/streamlit/emoji-shortcodes

## Ideas
- HiWis fragen zum Helfen
