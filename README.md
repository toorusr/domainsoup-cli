# Domainsouper CLI 🍜
> A commandline tool for souping domain names

###### Status
[![domainsoup-cli](https://img.shields.io/badge/struct-working-green.svg)](https://github.com/toorusr/domainsoup-cli/tree/master/struct)
[![README.md](https://img.shields.io/badge/README.md-incomplete-yellow.svg)](https://github.com/toorusr/domainsoup-cli/tree/master/README.md)


## Features
- Check a lot of domains
- Generate domainnames
- 3 letter domain checking

## Get started
###### Setup
1. Make sure you have [python3.x](https://www.python.org/downloads/) installed and the [tqdm](https://github.com/tqdm/tqdm) module.
2. Copy this repository to your machine. (`git clone https://github.com/toorusr/domainsoup-cli`)

###### Run souper
1. Navigate in the cloned repositorys `src/` folder.
2. Run the souper by executing it with python3.
```bash
python3 souper.py
```

###### Run parser
Because the souper outputs every domain and its availability to a big file, we can easily parse this data.
You can do this by using the `parser.py`.

```bash
python3 parser.py $domain_file
```

###### Configuration
There is not really any configuration possible right now, but you can easily change the sourcecode on you behalve. It's indeed not so complicated.

## License
[MIT](https://github.com/toorusr/domainsoup-cli/tree/master/LICENSE)
