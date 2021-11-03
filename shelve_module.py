import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
shelfFile['cats']
shelfFile = shelve.open('mydata')
shelfFile['cats']
shelfFile.close()






'''Just like dictionaries, shelf values have keys() and values() methods that
will return list-like values of the keys and values in the shelf. Since these
methods return list-like values instead of true lists, you should pass them
to the list() function to get them in list form. Enter the following into the
interactive shell:'''

shelfFile = shelve.open('mydata')
list(shelfFile.keys())
list(shelfFile.values())
shelfFile.close()