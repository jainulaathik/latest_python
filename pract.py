print("hello world")
print("this is the first program")

#arithmetic opoerators
x=10;y=25
#addition
print(x+y)
#subtraction
print(x-y)
#multiply
print(x*y)
#division
print(x/y)
#module
print(x%y)
#floor
print(x//y)
#exponent
print(x**y)

#comparison operator or regional operator
a,b=25,10
#check a is less than b
print(a<b)
#check a is greater than b
print(a>b)
#check a is equal to b
print(a==b)
#check a is not equal to b
print(a!=b)
#check a is greater than or equal to b
print(a>=b)
#check a is less than or equal to b
print(a<=b)

#logical operator or boolean operator
a,b = True,False
#print a and b
print(a&b)
#print a or b
print(a|b)
#print a not b
print( a != b )

#bitwise operator
a,b = 10 ,5
#bitwise and
print(a&b)
#bitwise or
print(a|b)
#bitwise not
print(~b)
#bitwise rightshift
print(a>>b)
#bitwise leftshift
print(a<<b)

num1 = 2
print(type(num1))
print(bin(num1))

num2 = 10
print(bin(num1),bin(num2))
print(num1&num2)

#assignment opeartor
a = 10

#add and
a+=10
print(a)
#subtraction
a-=10
print(a)
#multiply
a*=10
print(a)
#division
a/=10
print(a)
#module
a%=10
print(a)
#floor
a//=10
print(a)
#exponent
a**=10
print(a)

#special operator
a=5
b=4
print(a is not b)

ak=[1,2,3]
bk=[1,2,3]
print(ak is bk)

at="aathik"
bt="aathik"
print(at is bt)
print(at is not bt)

#membership operator - in and in not
aathik = [1,2,3,4]
print(5 not in aathik)

#in dictionary
d = {1:"a",2:"b"}
print(1 in d)

#if  statement
a = 20
if a>10:
    print("a is greter than value")
print("intha elavu eppayum irukum waste one")

#if else statement
a = 20
if a>10:
    print("positive")
else:
    print("negative")

#if elif statement
a = 8
if a>10:
    print("positive")
elif a==10:
    print("equal")
else:
    print("negative")

#nested if
a = 8
if a>= 10:
    if a==10:
        print("equal")
    else:
        print("positive")
else:
    print("negative")

#to find which number is biggest
a=25
b=35
c=45
if (a>=b)and(a>=c):
    largest=a
elif(b>=a)and(b>=c):
    largest = b
else:
    largest = c
print("the largest value is : {}".format(largest))


#while loop
list = [10,20,30,40,50]
product=1
index=0
while index < len(list):
    product *= list[index]
    index += 1
print("product is :{}".format(product))

#while else loop
numbers = [1,2,3]
index = 0
while index<len(numbers):
    print(numbers[index])
    index+=1
else:
    print("vera madri")

#to check given number is prime or not
#num =int(input("enter a number : "))
#isDivisible = False
#i=2;
#while i < num:
#    if num % i == 0:
#        isDivisible = True;
#        print("{} is divisible by {}".format(num,i) )
#    i+=1;
#if isDivisible :
#    print("{} is not prime number".format(num))
#else:
#    print("{} is a prime number".format(num))

#for loop
list = [10,20,30,40,50]
product = 1
for element in list:
    product *= element
print("the product of {}".format(product))

#range function in for loop
for i in range(10):
    print(i)

#range function in for loop
for i in range(10,100,5):
    print(i)

#range function in list example 1
name = ["aathik","naveen","karthick","srini","vimal"]
for element in name:
    print(element)
#range function in list example 2
name = ["aathik","naveen","karthick","srini","vimal"]
for index in range(len(name)):
    print(name[index])

#for loop with else
number = [1,2,3,4,5]
for engal in number:
    print(engal)
else:
    print("ithuku mela number illapa")
#combination of all in for loop
number = [10,20,33,40,50]
for engal in number:
    print(engal)
    if engal % 2 == 0:
        print("{}this are module of 2".format(engal))
    else:
        print("{}this are not module of 2".format(engal))
else:
    print("ithuku mela number illapa")
#for loop with break
number = [1,2,3,4,5]
for varum in number:
    print(varum)
    if varum % 2 == 0:
        break
else:
    print("ithuku mela number illapa")

#display all primary number with interval
index1=0
index2=1000
print("prime numbers between {} and {} are : ".format(index1,index2))

for num in range(index1,index2+1):
    if num > 0:
         isDivisible = False;
         for index in range(2,num):
             if num % index == 0:
               isDivisible = True;
         if not isDivisible:
             print(num);

#printing patter in python
for i in range(4):
    for j in range(4):
        print(" # ",end="")
    print()

#break statement in for loop
numbers = [1,2,3,4,5,6]
for num in numbers:
    if num == 6:
        break
    print(num)
else:
    print("in the else blocl")
print("outside the llop")


#used to check prime  number or not using break
#num = int(input("enter a value"))
#isDivisible = False
#i = 2;
#while i < num:
#    if num % i == 0:
#        isDivisible = True;
#        print("{} is divisible by {}".format(num,i))
#        break;
#    i+=1;
#if isDivisible:
#    print("{} is not prime number".format(num))
#else:
#    print("{} is a prime number".format(num))

#continue statement in loop
number = [1,2,3,4,5,6]
for num in number:
    if num % 2 == 0:
        continue
    print(num)
else:
    print("else block")

#list creation
#list of strings
list1 = ['aathik','vimal','karthick','naveen']
#length
print(list1)
print(len(list1))

#list of integer
list2 = [1,2,3,4,5,6,7,8,9]
print(list2)
print(len(list2))

#list of lists
list3 = [[1,25],[55,70]]
print(list3)
print(len(list3))

#list of different datatypes
list4 = [5,'venam da',55,2.5,25/2]
print(list4)
print(len(list4))

#list append
list1 = ['aathik','vimal','karthick','naveen']
#length
print(len(list1))
#list append
list1.append('shiva')
print(list1)

#list insert
#list of integer
list2 = [1,2,3,5,6]
list2.insert(3,4)
print(list2)

#list remove
list = ['one','two','three','four','two']
list.remove('two')
list.remove('four')
print(list)

#list append and extend
#append - it will append list at the end of the list
list = ['one','two','three','four']
list1 = ['aathik','rusaif']
list.append(list1)
print(list)

#extend -  it will add as the element in the list
list = ['one','two','three','four']
list1 = [5,6]
list.extend(list1)
print(list)

#list delete
#del to remove based on index position
list = ['one','two','three','four']
del list[1]
print(list)

#pop method pop up at the item mentioned in index
aathik = list.pop(1)
print(aathik)
print(list)

#delete particular thing
list = ['one','two','three','four','two']
list.remove('three')
print(list)

#list related keywords in python in and not in
#in function
list = ['one','two','three','four']
if 'two' in list:
    print("irukan da")
#not in function
if 'six' not in list:
    print("illada")

#list reverese
list = ['one','two','three','four']
list.reverse()
print(list)

#list sort
numbers = [10,30,20,50,40,60]
sorted_list = sorted(numbers)
#sorted list
print("the sorted list are ",sorted_list)
#original list
print("the original list are ",numbers)
#reverese sorted
print("the reverse sorted list are ",sorted(numbers, reverse = True))

list = ['one','four','two','five','three']
print("the sorted list are ",sorted(list))
print("the original list are ",list)
print("the reverse sorting in descending :",sorted(list,reverse=True))

#sort
numbers = [1,50,4.5,11.33,33.2]
numbers.sort()
print(numbers)
#mixing of elements we cant compare string with numerical we cant sort it out
#mix = [1,50,4.5,'a',11.33,'bc',33.2]
#mix.sort()
#print(mix)

#string split to a splirt
a = "aathik,venam,poda,venna"
split_string = a.split(',')
print(split_string)

#space()
a = "money heist is good series"
split_string = a.split()
print(split_string)

#indexing
numbers = [1,50,4.5,11.33,33.2]
number = numbers[2]
print(number)
#print lst element using index by (_-1_
numbers = [1,50,4.5,11.33,33.2]
print(numbers[-1])

#list slicing
numbers = [1,50,25,11,43,33,22,77]
print(numbers[:])
print(numbers[0:4])
print(numbers[::2])
print(numbers[2::2])

#alternative slicing
numbers = [10,20,30,40,50,60,70]
print(numbers[::2])
print(numbers[2::2])

#list extendinng using + symbol
list1 = [1,2,3,4,5,6]
list2 =['aathik','venam','da','venna']
new_list = list1 + list2
print(new_list)

#extend function
list1 = [5,6,7,8,9,10]
list2 =['aathik','venam','da','venna']
list1.extend(list2)
print(list1)

#list count - to check count of the given number in the list
numbers = [1,2,5,6,7,8,5,9,2,1,3,3,4,5,6,7,8]
print(numbers.count(5))

#list looping
list = ['one' ,'three','four','five']
for ele in list:
    print(ele)

#list comprehension
#without list comprehension
square =[]
for i in range(10):
    square.append(i**2)
print(square)

#using list comprehension
squares = [i**3 for i in range(10)]
print(squares)

#pudusu kanna
squares = []
list2 = [1,2,3,4,5,6,7,8]
squares.append(list2)
print(squares)

#example
list = [-10,-20,-30,10,20,30,40]
#create list with value doubles
double_value = [i*2 for i in list]
print(double_value)
#filter negative number
negative_number = [i for i in list if i>=0]
print(negative_number)
#create tuple in list
tuple =[(i,i**2)for i in list]
print(tuple)

#nested list
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
transposed = []
for i in range(4):
    list=[]
    for row in matrix:
        list.append(row[i])
    transposed.append(list)
print(transposed)

#matrix with lsit comprehension
transposed = [[row[i] for row in matrix]for i in range(4)]
print(transposed)

#tuple
#with integer
t =(1,2,3,4,5,6)
print(t)

#with mixed datatypes
t=(1,'aathik',2,'mark')
print(t)

#nested tuple
t=(1,(2,3,4),[1,'aathik',2,'mark'])
print(t)

#only paranthesis is not define tuple it shou;d end with comma
#paranthesisd
a = ('aathik')
print(type(a))

#with paranthesis and comma
a = ('aathik',)
print(type(a))
#in tuples paranthesis is optional but comma must
t = 'aathik',
print(type(t))
print(t)

#accessing element in tuple
tuple = ('one' ,'three','four','five')
print(tuple[1])

#negative index
tuple = ('one' ,'three','four','five')
print(tuple[-1])

#nested tuple
tuple = ('ithu venum',('one' ,'three','four','five'))
print(tuple[1])
print(tuple[1][2])

#slicing of tuple
t = (1,5,2,3,4,5,6)
print(t[0:3])
print(t[1::2])
print(t[::2])
print(t[:])

#print element from starting to 2nd last element
print(t[:-2])

#changes in tuples we cannot change in tuples because its in immutable but we can change list inside the tuples
t = (1,5,6,7,8,[5,6,7,8,9])
t[5][2] = 'aathik'
print(t)

#concanating in tuple
t = (1,2,3,4,5,6)
p = (7,8,9,10,11,12,13)
print(t + p)

#repeating of element
t = ((25,'aathik')* 5)
print(t)

#delete in tuple we cants delete or edit in tuple only it deleted entirely
t =(1,2,3,4,5,6,78,9)
del t

#count in tuple is same like as list it usd to check frequency of element repeating
p =(1,2,3,4,5,4,3,2,1)
print(p.count(5))

#tuple index - check elemnt which is present in which index
t =(1,2,3,1,3,3,4,1)
print(t.index(2))

#tuple memebership in fuction
t = (1,2,3,4,54,6,7,8,9)
print(4 in t)
print(55 in t)

#tuple lengtg
t = (1,2,3,4,5,6,7,8,9)
print(len(t))

#tuple sort we can edit directly by adding new variable we cam edit
t = (9,7,5,6,0,4,2,1,3)
new_dorted_tuple = sorted(t)
print(new_dorted_tuple)

#largest,amallest and sum of element in tuples
t = (9,7,5,6,0,4,2,1,3)
print(max(t))
print(min(t))
print(sum(t))


#set
#set creation
s ={1,3,4,5,2,1}
#it will show error set dont have index thing
#print(s[1])
print(s)

#make set from list using set function
s = set([1,2,3,4,5,6,4,1,2,3])
print(s)

#add element is the set
a = {1,3}
a.add(2)
print(a)

#add multiple elem,ent
a.update([4,5,6,7,8,9])
print(a)

#add list and set in same
a.update([10,11],{11,12,13,14,15})
print(a)

#deleteion in set we have different type of process
aa ={1,2,3,4,5,6,7,8,9}
#discard function
aa.discard(8)
print(aa)
#remove function
aa.remove(6)
print(aa)
#difference in discard and remove
aa.discard(11)
print(aa)
#remove will show error
#aa.remove(11)
#print(aa)

#pop function in set - it removes randomlyn in set
aa.pop()
print(aa)

#clear function to remove all item in the set
aa.clear()
print(aa)

#set operator
#union |
a = {1,2,3,4,5}
b= {3,4,5,6,7,8}
print(a | b)
print(a.union(b))

#intersection
print(a&b)
print(a.intersection(b))


##differnce
print(a-b)
print(a.difference(b))

#symmentric difference
print(a^b)
print(a.symmetric_difference(b))

#issubset peresent or not
print("set a in subset of b ?",a.issubset(b))
print("set b in subset of a ?",b.issubset(a))

#frozen set is similar to like set
#frozen set is immutable and hasable so we cant change things here its can be used as dictionary key
#it dont support addition,index,remove
set1 = frozenset([1,2,3,4,5,6,7])
set2 =frozenset([5,6,7,8,9,10,11])

#union
print(set1 | set2)
print(set1.union(set2))

#intersection
print(set1&set2)
print(set1.intersection(set2))


##differnce
print(set1-set2)
print(set1.difference(set2))

#symmentric difference
print(set1^set2)
print(set1.symmetric_difference(set2))

#issubset peresent or not
print("set a in subset of b ?",set1.issubset(set2))
print("set b in subset of a ?",set2.issubset(set1))

#dictionary - {}
#empty dictionary
my_dict = {}
#dictionary with integer
my_dict = {1:'aathik',2:'varuran'}
print(my_dict)
#dictionary with mixed key
my_dict = {'name':'aathik',2:['nan','varuran']}
print(my_dict)
#using dict() function
my_dict=dict()
my_dict = dict([(1,'abc'),(2,'xyz')])
print(my_dict)

#dict access only with key
my_dict ={'name':'satish','age':27,'address':'tamilnadu'}
print(my_dict['name'])
#it will show error print(my_dict['degree'])


#other way of accessing dictionary .get function
print(my_dict.get('name'))
print(my_dict.get('degree'))

#add or modify elemenet
my_dict['name'] = 'aathik'
print(my_dict)
my_dict['age'] = '25'
print(my_dict)

#adding new key to the dictionary
my_dict['degree'] ='MBA'
print(my_dict)
my_dict['phone number'] = 9047952960
print(my_dict)

#dictionary delete or remove element using pop function
print(my_dict.pop('age'))
print(my_dict)

#pop item - it removes randomly
print(my_dict.popitem())

#delete particular key del function
sq = {2:3,4:5,6:7,8:9,10:12}
del sq[4]
print(sq)

#to remove complete dictionary put del directly
#del sq
#print(sq)

#various dictionary method
#copy function
sq = {2:3,4:5,6:7,8:9,10:12}
copy_in_a = sq.copy()
print(copy_in_a)

#fromkeys
subject = {}.fromkeys(['math','english','tamil'],2)
print(subject)

#items - tuples in the list
subject = {2:4,3:5,4:5,6:4,7:3}
print(subject.items())

#keys &values
subject = {2:4,3:5,4:5,6:4,7:3}
print(subject.keys())
print(subject.values())

#display all available method and dictionary
d ={}
print(dir(d))

#dict ccomprehnesion
d = {'a':1,'b':2,'c':3}
for pair in d.items():
    print(pair)

#creating new dictionary only where value is higher than 2
d = {'a':1,'b':2,'c':3,'d':4,'e':5}
new_dict ={k:v for k,v in d.items() if v>2}
print(new_dict)

#perform on key value pairs
d = {'a':1,'b':2,'c':3,'d':4,'e':5}
dc = {k+'aathik':v**2 for k,v in d.items() if v>2}
print(dc)

#characteristics into strings
my_string = 'hello'
print(my_string)
print(my_string[0])
print(my_string[-1])
print(my_string[1::3])

#decimal number in index of string it will give error
a ='aathik'
print(a[2])

#change on delete on string we cannot do this because its immutable
#we can have option only to delete complete string using del function
a = 'hello'
#del a
#print(a)

s1 = ' hello '
s2 = ' world '
s3 = ' eppudi irukinga'
s4=s1+s2+s3
print(s4)

#iterating through string
count =0
for l in 'hello world':
    if l=='l':
        count+=1
print(count,"letters found")

#string memebership test to check whether its in string
print('l' in 'hello world')
print('o' in 'hello world')

#string method
aathik ='hello how are you how life going?'
print(aathik.upper())
print(aathik.lower())
print(aathik.split())

#join function
d =" "
print(d.join(['hello', 'how', 'are', 'you', 'how', 'life', 'going?']))

#find function
a = 'gppd morning'
print(a.find('g'))

#replace
a='good morning'
b=a.replace('good','bad')
print(b)

#check palindrome in string #check in scratch py
#string = 'MadaM'
#my_string=string.lower()
#revers_string =reversed(my_string)
#if list== (revers_string):
#    print("its in palindrome")
#else:
#    print("its not palindrome")


#sort & splitword in aplhabetical oreder
my ="python word to sort alphetical order"
words =my.split()
print(words)
words.sort()
for word in words:
    print(word)


#function introduction in python
def print_name(name):
    """
    this function is to print namwe
    """
    print('hello eppudi irfukinga' + str(name))

#functioncall we can call from anywhere
print_name(' aahik')

def print_nick_name(nick_name):
    """
    this function is used to print nick name
    """
    print("unnaku nick name neeya vachiko" + str(nick_name))

#Wcallfunctio
print_nick_name(" venna")

#return statement
def get_sum(list):
    """
    this function is used return the sum of all elements
    """
    _sum = 0
    for num22 in list:
        _sum += num22
    return _sum

print(get_sum([1,2,3,4,5,6,7,8,9]))


#to display doc string
print(print_name.__doc__)

#scope and lifetime variable
global_var ="this is global variable"
def test_life_time():
    """
    this function is life time variable
    """
    local_var ="this is local variable"
    print(global_var)

    print(local_var)
#calling the function for above
test_life_time()
print(global_var)
#print(local_var) it can display seperately because present inside function

# define a function
def compute_hcf(x, y):


# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

num1 = 85
num2 = 95
print("hcf of {} and {} is :{}".format(num1, num2, compute_hcf(num1, num2)))


#types of function
#built in function
#abs function
#to find the absolute number
num = -100
print(abs(num))

#all function
lst = [1,2,3,4,5,6,7,8,9]
print(all(lst))
lst1 = (1,2,3,4,5,6,7,8,9)
print(all(lst1))
lst2 = {1,2,3,4,5,6,7,8,9}
print(all(lst2))
lst3 = [0,1,2,3,4,5,6,7,8,9]
print(all(lst3))
lst4 = [False,1,2,3,4,5,6,7,8,9]
print(all(lst4))

#dir function
numbers = [2,3,4,5]
numbers1 = (2,3,4,5)
numbers2= {2,3,4,5}
print(dir(numbers2))
print(type(numbers1))

#divmod consiting of quotient and remainder
print(divmod(9,2))
#9 is quotient
#2 is remainder

#enumerate function
numbers = [1,2,3,4,5,6]
for index,num in enumerate(numbers):
    print("index {0} is value {1} ".format(index,num))


#modules
import math
print(math.pi)