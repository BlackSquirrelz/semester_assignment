# 2020-05-05 UZH CALR

## GIT Repository for Syntactic Parsing

## Team:

- Ariana Dragusha
- Rodolfo Miranda Chavez
- Tobias Weisskopf

## Assignment:

The final project will be prepared in groups of 3-4 people. The project requires an application
of the corpus processing or annotation methods covered in the course on the Horizons
corpus, published in English, German and French. Each group will prepare a presentation
introducing their topic and prepare a project report describing the details of the selected
processing and annotation methods and an analysis of the linguistic features of the resulting
methods.


Each group will prepare a 15-min. presentation describing
1. The description of the chosen application
2. The general processing or analysis system to be implemented
3. The required methods used in the system
4. Challenges relevant to the application or different methods
5. Outcomes of the project and potential usage in linguistic studies or language and
media technolgy.




## Installation

```
$ python3 -m pip install -r requirements.txt
```
---

## Introduction
What is parsing and why do we do it?
  (Syntactic) Parsing:
    To parse -> to break down a text into its parts-of-speech 
    and reveal syntactic relationships

  Parse trees / treebanks are useful for:
    Machine translation
    Speech recognition
    Question answering
    Grammar checking
    Information extraction
    Speech synthesis
    

## Presentation:

01. Description of Chosen Application




### Methodology

02. General Processing or Analysis System to be Implemented
  Data Retrieval
    Take data
    Store to DB
  Data Parsing
    Run parsing per language / and different parser
    Store accuracy of parser in the database
    Displaying a parse tree
    Display accuracy of parsing in graph

03. Required Methods Used

04. Challenges

04.1 - Challenge
    Multilingual Dataset (DE, FR, EN)
    Parsers may be better at specific languages which one to choose
    Selecting a representative set of texts to annotate
    
04.2 - Method
    Team members annotate texts based on their mother tongue
    Selected multiple parsers for testing
    Comparison between parser and language

05. Outcomes of the Project

Below table is a proposal on how to compare the parsers to each other and to the languages.
The same annotated text is provided to all parsers. With this approach we want to find the most specialised parser, and the best allrounder.

In the evaulation we have implemented a percentage against baseline, with baseline being the Stanford Parser

Language | Stanford Parser | AllenNLP Parser | spaCy Parser 
---------|-----------------|-----------------|-------------
DE|X|X|X
EN|X|X|X
FR|X|X|X


05.1 To run the GUI we need to first start the server.
First open a terminal, and start the virtual environment in the semester_assignment directory

On that branch you can see the GUI by doing the following:

```
$ source ../venv/bin/activate
$ export FLASK_APP=run.py 
$ export FLASK_DEBUG=1
$ flask run
```
Now you can go to a sensible webbrowser and go to this location:
http://localhost:8000/

or 

http://127.0.0.1:8000/

    
## Corpus Source: 

https://www.horizons-mag.ch/

## References:

A comprehensive list of dependencies used can be found on the GitHub repository of this project in the “requirements.txt” file. 

https://www.nltk.org/book/ch08.html

https://www.tutorialspoint.com/natural_language_processing/natural_language_processing_syntactic_analysis.htm

https://en.wikipedia.org/wiki/Parsing

https://www.oxfordhandbooks.com/view/10.1093/oxfordhb/9780198568971.001.0001/oxfordhb-9780198568971-e-017

https://www.sciencedirect.com/science/article/pii/B9780123693747500134

### Further Reading:

Parsing Algorithms - https://tomassetti.me/guide-parsing-algorithms-terminology/
Blog - http://nlpprogress.com/english/constituencyparsing.html 
Blog http://nlpprogress.com/english/dependencyparsing.html 
Book - https://web.stanford.edu/jurafsky/slp3/12.pdf ; https://web.stanford.edu/jurafsky/slp3/13.pdf ; https://web.stanford.edu/jurafsky/slp3/14.pdf ; https://web.stanford.edu/jurafsky/slp3/15.pdf
NLTK Parsing - https://www.nltk.org/book/ch08.html
Stanford Parser - https://nlp.stanford.edu/software/lex-parser.shtml

### More Reading:

Abeille, A. (Ed.). (2012). Treebanks: Building and Using Parsed Corpora ´ (Vol. 20). Springer Science & Business Media. Aepli, N. (2018). Parsing Approaches for Swiss German (Doctoral dissertation, University of Zurich).

## Known Issues

Please see Issue Tab of this project.




