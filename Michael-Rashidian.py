#!/usr/bin/python

'''
Revature is building a new API! This API contains functions for validating data, 
solving problems, and encoding data. 

The API consists of 10 functions that you must implement.

Guidelines:
1) Edit the file to match your first name and last name with the format shown.

2) Provide tests in the main method for all functions, We should be able to run
this script and see the outputs in an organized manner.

3) You can leverage the operating system if needed, however, do not use any non
legacy command that solves the problem by just calling the command.

4) We believe in self commenting code, however, provide comments to your solutions
and be organized.

5) Leverage resources online if needed, but remember, be able to back your solutions
up since you can be asked.

6) Plagiarism is a serious issue, avoid it at all costs.

7) Don't import external libraries which are not python native

8) Don't change the parameters or returns, follow the directions.

9) Assignment is optional, but totally recommend to achieve before Monday for practice.

Happy Scripting!

© 2018 Revature. All rights reserved.
'''
	
'''
Use the main function for testing purposes and to show me results for all functions.sort
'''
def main():
	zqd = "Ziquiday"
	x = [1,2,3,4,5,6,7,8,9,0]
	a = [-100,-1,0,1,5,10,50,100,200,1000]
	number=153
	TLA = "Three Letter Acronym"
	sentence = "the quick brown fox jumps over the lazy dog"
	print("Our string is: Ziquiday")
	print(reverse(zqd))
	print("Our triangle has sides of length 2 each")
	print(whichTriangle(2,2,2))
	print("We value the word: Ziquiday")
	print(scrabble(zqd))
	print(acronym(TLA))
	print(getPrimeFactors(910))
	print("Our number is 153")
	print(armstrong(number))
	print("Our sentence is 'the quick brown fox jumped over the lazy dog'")
	print(pangram(sentence))
	print("Our list is (1,2,3,4,5,6,7,8,9,0)")
	print(sort(x))
	print(rot(5, 'hello'))
	print(rot(26, 'hello'))
	evenAndOdds()
	print("Files made / appended")


'''
1. Reverse a String. Example: reverse("example"); -> "elpmaxe"

Rules:
- Do NOT use built-in tools
- Reverse it your own way

param: str
return: str
'''
def reverse(string):
	str=""
	for ch in string:
		str=ch+str
	return str
'''
2. Convert a phrase to its acronym. Techies love their TLA (Three Letter
Acronyms)! Help generate some jargon by writing a program that converts a
long name like Portable Network Graphics to its acronym (PNG).

param: str
return: str
'''
def acronym(phrase):
	
    phrase = phrase.replace("-", " ")

    phraseList = phrase.split()

    print (phraseList)

    returnString = ""

    for i in phraseList:

        substring = i[0:1]

        returnString += substring

    

    returnString = returnString.upper()

    print(returnString)

    return returnString

'''
3. Determine if a triangle is equilateral, isosceles, or scalene. An
equilateral triangle has all three sides the same length. An isosceles
triangle has at least two sides the same length. (It is sometimes specified
as having exactly two sides the same length, but for the purposes of this
exercise we'll say at least two.) A scalene triangle has all sides of
different lengths.

param: float, float, float
return: str -> 'equilateral', 'isoceles', 'scalene'
'''
def whichTriangle(sideOne, sideTwo, sideThree):
       equalSides = 0
       if sideOne == sideTwo:
               equalSides += 1
       if sideTwo == sideThree:
               equalSides += 1
       if sideOne == sideThree:
               equalSides += 1
       if equalSides == 3:
               return "Equilateral"
       elif equalSides == 1 or equalSides == 2:
               return "Isoceles"
       else:
               return "Scalene"

'''
4. Given a word, compute the scrabble score for that word.

--Letter Values-- Letter Value A, E, I, O, U, L, N, R, S, T = 1; D, G = 2; B,
C, M, P = 3; F, H, V, W, Y = 4; K = 5; J, X = 8; Q, Z = 10; Examples
"cabbage" should be scored as worth 14 points:

3 points for C, 1 point for A, twice 3 points for B, twice 2 points for G, 1
point for E And to total:

3 + 2*1 + 2*3 + 2 + 1 = 3 + 2 + 6 + 3 = 5 + 9 = 14

param: str
return: int
'''
def scrabble(word):
       point1 = "AEIOULNRST"
       point2 = "DG"
       point3 = "BCMP"
       point4 = "FHVWY"
       point5 = "K"
       point8 = "JX"
       point10 = "QZ"
       score = 0
       word = word.upper()
       for i in word:
               if i in point1:
                       score += 1
               elif i in point2:
                       score += 2
               elif i in point3:
                       score += 3
               elif i in point4:
                       score += 4
               elif i in point5:
                       score += 5
               elif i in point8:
                       score += 8
               elif i in point10:
                       score += 10
       print(score)
       return (score)
'''
5. An Armstrong number is a number that is the sum of its own digits each
raised to the power of the number of digits.

For example:

9 is an Armstrong number, because 9 = 9^1 = 9 10 is not an Armstrong number,
because 10 != 1^2 + 0^2 = 2 153 is an Armstrong number, because: 153 = 1^3 +
5^3 + 3^3 = 1 + 125 + 27 = 153 154 is not an Armstrong number, because: 154
!= 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190 Write some code to determine whether
a number is an Armstrong number.

param: int
return: bool
'''
def armstrong(number):
		#convert number to string
        #get number of digits by finding length of 
		#the string
        digits = len(str(number))
        sum = 0
		
		#iterate through string
        for n in str(number):
                sum += int(n) ** digits
        return sum == number
'''
6. Compute the prime factors of a given natural number.

A prime number is only evenly divisible by itself and 1.
 
Note that 1 is not a prime number.

param: int
return: list
'''
def getPrimeFactors(number):
	primeFactors = []
	for n in range(2,number):
		if number % n == 0:
			prime = True
	for fact in range(2, n):
		if n % fact == 0:
			prime = False
	if prime:
		primeFactors.append(n)  #check out list.append(entry) !
	return primeFactors

'''
7. Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan
gramma, "every letter") is a sentence using every letter of the alphabet at
least once. The best known English pangram is:

The quick brown fox jumps over the lazy dog.
 
The alphabet used consists of ASCII letters a to z, inclusive, and is case
insensitive. Input will not contain non-ASCII symbols.
 
param: str
return: bool
'''

def pangram(sentence):
       found = False
       sentence = sentence.lower()
       for n in range(ord('a'), ord('z') + 1):
               for m in sentence:
                       if ord(m) == n:
                               found = True
               if found:
                       found = False
               else:
                       return False
       return True

'''
8. Sort list of integers.
f([2,4,5,1,3,1]) = [1,1,2,3,4,5]

Rules:
- Do NOT sort it with .sort() or sorted(list) or any built-in tools.
- Sort it your own way

param: list
return: list
'''

def sort(value):
	result = []
	return sorting(value, result)

def sorting(value, result):
	if(len(value) == 0):
		return result
	low = min(value)
	value.pop(value.index(low))
	result.append(low)
	return sorting(value, result)
'''
9. Create an implementation of the rotational cipher, also sometimes called
the Caesar cipher.

The Caesar cipher is a simple shift cipher that relies on transposing all the
letters in the alphabet using an integer key between 0 and 26. Using a key of
0 or 26 will always yield the same output due to modular arithmetic. The
letter is shifted for as many values as the value of the key.

The general notation for rotational ciphers is ROT + <key>. The most commonly
used rotational cipher is ROT13.

A ROT13 on the Latin alphabet would be as follows:

Plain: abcdefghijklmnopqrstuvwxyz Cipher: nopqrstuvwxyzabcdefghijklm It is
stronger than the Atbash cipher because it has 27 possible keys, and 25
usable keys.

Ciphertext is written out in the same formatting as the input including
spaces and punctuation.

Examples: ROT5 omg gives trl ROT0 c gives c ROT26 Cool gives Cool ROT13 The
quick brown fox jumps over the lazy dog. gives Gur dhvpx oebja sbk whzcf bire
gur ynml qbt. ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. gives The
quick brown fox jumps over the lazy dog.

param: int, str
return: str
'''
def rot(shift, string):
	returnStringN = ''
	alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for n in range(0, len(string)):
		if alpha.index(string[n]) + shift > 25:
			shift -= 26
	returnStringN += alpha[alpha.index(string[n]) + shift]
	return returnStringN

'''
10. Take 10 numbers as input from the user and store all the even numbers in a file called even.txt and
the odd numbers in a file called odd.txt.

param: none, from the keyboard
return: nothing
'''
def evenAndOdds():
       increase = 0
       while( increase  < 10) :
               innum = input("Insert a number: ")
               if increase != 0:
                       numbers.insert(increase,int(innum))
                       increase += 1
               else:
                       numbers = [int(innum)]
                       increase += 1
       outfile1 = open("Even.txt",'a')
       outfile2 = open("Odd.txt",'a')
       for num in numbers:
               if num%2 == 0:
                       outfile1.write(str(num)+"\n")
               else:
                       outfile2.write(str(num)+"\n")
       outfile1.close()
       outfile2.close() 



if __name__ == '__main__':
	main()


