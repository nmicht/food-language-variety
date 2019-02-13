# Food names distribution

A map to display distribution of food names using their synonyms in different regions.

Currently available for English and Spanish.


## Technologies
- Python
- Wikipedia API
- Beautiful Soup

## Authors
[@nmicht](https://github.com/nmicht/)
[@jbrew](https://github.com/jbrew/)

## To-Do

- Clean up synonyms
    - ~remove s, us, species, botany~
    - regularize capitalization
    - *remove single-synonym lists from synonyms*
- ~Add key into the file of the found_words~
- Run for counties/cities/farms in us, mx, es, and uk
	- ~counties in uk~
	- counties in us
	- ~states in mx~
	- ~provinces in es~
- Fix accented letters in file writing
- Map coordinates with words in a map
    - main_key --> [ (coord, names), (coord, names) ...]
