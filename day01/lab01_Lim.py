## Trick and explanation of base conversion
## http://www.purplemath.com/modules/base_why.htm

"""convert positive integer to base 2"""
def binarify(num): 
    b = num
    remainder=[]
    while b != 0:
        a = b/2
        remainder.append(b%2)
        b = a
    return "".join(str(i) for i in remainder[::-1])

binarify(4)

"""convert positive integer to a string in any base"""
def int_to_base(num, base):
    b = num
    remainder=[]
    while b != 0:
        a = b/base
        remainder.append(b%base)
        b = a
    return "".join(str(i) for i in remainder[::-1])

int_to_base(5,3)


"""take a string-formatted number and its base and return the base-10 integer"""
def base_to_int(string, base):

    dat = [letter for letter in string]
    dat = dat[::-1]
    dat2= 0
    for i in range(len(dat)):
        dat2 += (base**i) * int(dat[i])
    return dat2

base_to_int('100',2) #it should be 4.


#[i for i in "abc"]
    

"""add two numbers of different bases and return the sum"""
def flexibase_add(str1, str2, base1, base2):
    dat = [letter for letter in str1]
    dat = dat[::-1]
    cat = [letter for letter in str2]
    cat = cat[::-1]
    dat2 = 0
    
    for i in range(len(dat)):
        dat2 += (base1**i) * int(dat[i])
    for j in range(len(cat)):
        dat2 += (base2**j) * int(cat[j]) 
    return dat2

flexibase_add('100','101',2,3)

"""multiply two numbers of different bases and return the product"""
def flexibase_multiply(str1, str2, base1, base2):
    dat = [letter for letter in str1]
    dat = dat[::-1]
    cat = [letter for letter in str2]
    cat = cat[::-1]
    dat2 = 0
    dat3 = 0
    for i in range(len(dat)):
        dat2 = (base1**i) * int(dat[i])
    for j in range(len(cat)):
        dat3 += (base2**j) * int(cat[j]) 
    return dat2*dat3

flexibase_multiply('100','101',2,3)

"""given an integer, return the Roman numeral version"""
def romanify(num):

  
# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.