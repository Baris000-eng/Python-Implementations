inputtedStr= input("Please enter a text: ")
print()
vowelsInInputtedStr= " "
consonantsInInputtedStr=" "
wordsInInputtedStr=[]
for i in inputtedStr:
  if (i in "AEIİOÖUÜ") or (i in "aeıioöuü"):
    vowelsInInputtedStr=vowelsInInputtedStr+i
  elif i != " " and i.isalpha():
    consonantsInInputtedStr=consonantsInInputtedStr+i
print("The vowels in the inputted string : "+vowelsInInputtedStr)
print("The consonants in the inputted string: "+consonantsInInputtedStr)
print()
countVowel= 0
countConsonant=0
countBlank=0

for i in vowelsInInputtedStr:
  if i!=" ":
   countVowel=countVowel+1

for j in consonantsInInputtedStr:
  if i!=" ":
   countConsonant=countConsonant+1

for k in inputtedStr:
  if k==" ":
    countBlank=countBlank+1

print("The words in the inputted string are: ")
wordCounter= 0
wordsInInputtedStr= inputtedStr.split(' ')
for i in range(0,len(wordsInInputtedStr)):
        print(wordsInInputtedStr[i])
        wordCounter=wordCounter+1

print()

print("The sentences in the inputted string are:")
sentenceCounter=0
sentencesInInputtedStr= inputtedStr.split('.')
for l in range(0,len(sentencesInInputtedStr)):
  sentenceCounter=sentenceCounter+1
  print(sentencesInInputtedStr[l])


print(sentencesInInputtedStr[1])




upperCaseCount=0
for x in inputtedStr:
  if x.isupper():
    print("The uppercase letter"+str(upperCaseCount)+" is: "+x)
    upperCaseCount=upperCaseCount+1

print()

lowerCaseCount=0
for y in inputtedStr:
  if y.islower():
    lowerCaseCount=lowerCaseCount+1
    print("The lowercase letter "+str(lowerCaseCount)+" is: "+y)

print()

digitCount=0
for k in inputtedStr:
  if k.isdigit():
    digitCount=digitCount+1
    print("The digit "+str(digitCount)+" in the inputted string is: "+k)



print()

print("The number of the vowels in the inputted string is: "+str(countVowel))
print("The number of the consonant in the inputted string is: "+str(countConsonant))
print("The number of the blanks in the inputted string is: "+str(countBlank))
print("The number of the words in the inputted string is: "+str(wordCounter))
print("The number of the sentences in the inputted string is: "+str(sentenceCounter))
print("The number of the uppercase letters in the inputted string is: "+str(upperCaseCount))
print("The number of the lowercase letters in the inputted string is: "+str(lowerCaseCount))
print("The number of the digits in the inputted string is: "+str(digitCount))



