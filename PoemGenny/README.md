# PoemGenny

## Description
To combine various Python coding techniques, I created a workflow that will scrape a website, select and organize word text, modify text elements, and re-assemble these words into free-form poetry that would make a Vogon crumble:
```python
light in the self! 'randomly' sta-star-starving 

light in the set! 'autobiography' com-comi-coming 

maria hearts triangular sharp! 'biography' ass-assi-assigned 

...ibertarianis... ...bertariani... ...ertarian... 
```
 
## Tech
+ Python3
+ BeautifulSoup

## Usage

### Create your own work!

**1) Pick a url (from a website that is safe to scrape) or select one of the provided options for the url variable**
```python
url = "http://books.toscrape.com"
# "https://www.rithmschool.com/blog"
# "http://quotes.toscrape.com"
# "http://books.toscrape.com"
```

**2) To view output of the 'clean' function, the following can be un-commented** 
```python
# print("Website text minus potential adjectives/verbs: ")
# for item in others_list:
#     print(item) 
# print("Potential adjectives: ")
# for item in adj_list:
#     print(item)
# print("Potential verbs: ")
# for item in verb_list:
#     print(item)
# print("Longest word: ", longest_word)
```

**3) To view output of the 'modify_words' function, the following may be un-commented**
```python
# for item in poem_depot:
#     print(item) 
```

**4) To run the program, ensure the following is uncommented, and output will also be saved to a .txt file for posterity.  
As word selection is randomized, re-running the program will create breathtaking new poems from the website text.**
```python
for item in poem[0:6]:
    res = item.get_string()
    print(res, end = ' ')
#    save_string("test.txt", res)
print('\n')
for item in poem[6:12]:
    res = item.get_string()
    print(res, end = ' ')
#    save_string("test.txt", res)
print('\n') 
for item in poem[12:18]:
    res = item.get_string()
    print(res, end = ' ')
#    save_string("test.txt", res)
print('\n')   
for item in poem[18:24]:
    res = item.get_string()
    print(res, end = ' ')
#    save_string("test.txt", res)
```
