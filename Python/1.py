
names="john:doe;jack:nickolson;name:surname"
for x in names.upper().split(';'):
    print(x)

#string format
stringToFormat = "first {} second {}, third {}"
formattedString=stringToFormat.format("abc","def","ghi")


#string format with parameter name
stringToFormat = "I am  {name} and i am {age} years old"
formattedString=stringToFormat.format(name="John",age="25")
print(formattedString)


# <string {placeholder}>.format(<argument for placeholder>)
ageNamePair=[]
ageNamePair.append((21,"name1"))
ageNamePair.append((22,"name2"))
ageNamePair.append((23,"name3"))
ageNamePair.append((24,"name4"))
for part in ("{0}, {1} ".format(*(x[0],x[1])) for x in ageNamePair):
    print(part)
# usage of * in format is, that the row is in loop and multiple times


#we have a string containing of names and ages. 
stringNamesAges="Name1:20;Name2:18;Name3:17;Name4:19"
#the task is to rebuild the string
#The names must be in uppercase
#elements must be ordered by ages (ascending)
# formatt to achieve: (age1, name1)(age2, name2)(age3, name3)

def meeting(s):
    return ''.join(sorted('({1}, {0})'.format(*(x.split(':'))) for x in s.upper().split(';')))


#Lambda espressions
ages=[1,2,3,4,5,6]
lambdaExpression= lambda x: [print(element) for element in x] 
lambdaExpression(ages)

list1=[1,2,3]
list2=[4,5,6]
print(list1+list2) #concatenation [1,2,3,4,5,6]


def squareMe(x):
    return x*x
listToSquare=[1,2,3,4,5,6]
listSquared=list(map(squareMe,listToSquare))
print(listSquared)

#add elements of two lists in pairs
list1=[1,2,3,4]
list2=[4,5,6]
listSum=list(map(lambda x,y: x+y,list1,list2)) #[5, 7, 9]  without 4

list1 = [1,2,3,4,5]
list1=map(lambda x:x*x,list1)
print(list1)



#zip in Python
questions = ["What is your name","What is your age","What do you study"]
answers = ["my name is Robert","I am twenty years old","I study informatics"]

questionAnswerTuples = zip(questions,answers)
#print(list(questionAnswerTuples)) 

for question,answer in questionAnswerTuples:
    print("Question is: {0}, and answer on this question is {1} ".format(question,answer))

#let explain zip mathmetically: 
# zip([a1,a2,a3,a4],[b1,b2,b3,b4]) = (a1,b1),(a2,b2),(a3,b3),(a4,b4)