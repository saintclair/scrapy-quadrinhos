# Scrapy Quadrinhos

Crawler that searches for Name, description and link to the 
comic book from the site baixquadrinhos.com **This example is not commercial, just for study purposes**

![Scrapy Quadrinhos](https://www.einerd.com.br/wp-content/uploads/2019/02/Batman-painel-meme-capa.jpg)

## Getting Started

Make your virtual enviroment:

```
virtualenv --python=PATH_VERSION_YOU_PYTHON_3 NAME_ENV

source NAME_ENV/bin/activate
```

### Prerequisites

```
Only Python
```

### Installing

```bash
pip install scrapy

git clone https://github.com/saintclair/scrapy-quadrinhos.git

cd scrapy-quadrinhos
```

## Running

```bash
>> scrapy runspider quadrinhos.py -t json -o quadrinhos.json
```

## Built With

* [Scrapy](https://docs.scrapy.org/en/latest/index.html) - The web crawling/scraping framework used

## License

This project is licensed under the MIT License
