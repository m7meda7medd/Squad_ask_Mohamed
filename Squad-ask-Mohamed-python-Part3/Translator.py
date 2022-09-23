def Translation (word) :
    translation = ""
    for i in word :
        if i in "AEOIUaeiou" :
            translation = translation+"V"
        else :
            translation = translation+i.lower()
    return translation         


word=str((input("enter a word to translate:")))
print(Translation(word)) 

         
