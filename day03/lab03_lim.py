import string
## 1. write tests in lab03_tests.py
## 2. then code for the following functions

## Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Presumably your code won't work for an int
## raise a built-in (or custom!) exception if fed an int


## make all characters capitalized
def shout(txt):
    if type(txt)!=str:
        raise TypeError, "Not string."
    else:
       ex = txt
       txt2=ex.upper()
       return txt2


## reverse all characters in string
def reverse(txt):
    if type(txt)!=str:
        raise TypeError, "Not string."
    else:
       ex = txt
       txt= ex[::-1]
       return txt

   
## reverse word order in string
def reversewords(txt):
    if type(txt)!=str:
        raise TypeError, "Not string."
    else:
       ex = txt
       ex = ex.split()
       ex.reverse()  #?? 
       result = " ".join(ex)
       return result

reversewords("order pizza now")

## reverses letters in each word
def reversewordletters(txt):
    if type(txt)!=str:
        raise TypeError, "Not string."
    else:
       ex = txt
       ex = ex.split()
       ex
       mine=[]
       for i in ex: 
           mine.append(i[::-1])
       return mine

reversewordletters("order pizza now")

## change text to piglatin.. google it! 
def piglatin(txt):
    if type(txt)!=str:
        raise TypeError, "Not string."
    else:
 
        ex = list(txt)
 
        vowels = ['a', 'e', 'i', 'o', 'u']
        first_v = []
        for i in ex:
            if i in vowels:
                first_v.append(i)
                num= ex.index(i)
                break
        back= ex[num:len(ex)]

        before=ex[0:num]
        back.extend(ex[0:num])
        back.extend("ay")
        print ''.join(back)




                

            
        






## Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.
 
string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]


		
			
			
			
			
			
			

