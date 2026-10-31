# Threat Feed Parser

Summarize a local plain-text feed export by line tags and record status; does not extract or validate indicators.

## Requirements
Python 3.10+, standard library only.

## Usage
`python threatfeed_parser.py sample.txt`

The program reads a local text file only. It performs no network requests, scanning, or enrichment. Treat output as a summary, not a security verdict.

## Tests
`python -m unittest discover -s tests -v`
