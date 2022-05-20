# PoemGenny

## Description
To combine various Python coding techniques, I created a workflow that will scrape a website, select and organize word text, modify text elements, and re-assemble these words into free-form poetry that would make a Vogon crumble:

*light in the self! 'randomly' sta-star-starving* 

*light in the set! 'autobiography' com-comi-coming* 

*maria hearts triangular sharp! 'biography' ass-assi-assigned* 

*...ibertarianis... ...bertariani... ...ertarian...*

 
## Tech
+ Python3
+ BeautifulSoup

## Usage

### Create your own work!

**1) Select one of the provided options for the url variable (located within the `main` function), or supply your own url (from a website that is safe to scrape)**
```python
url = "http://books.toscrape.com"
# "https://www.rithmschool.com/blog"
# "http://quotes.toscrape.com"
# "http://books.toscrape.com"
```

**2) Run the program (originates via the `main` function)** 

The poem will appear in your console.  
A text file of the poem will be created unless, within the `main` function, the `output_poem(poem)` call is set to `output_poem(poem, False)`.  
As word selection is randomized, re-running the program will create breathtaking new poems from the website text.

