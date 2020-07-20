#count single character using count method
def count_str():
    str1 = 'Hello World'
    l1 = [12,2,3,4,5,6,6,7,7,7]
    ans = str1.count('o')
    ans1 = l1.count(7);
    return "String ",ans," Integer ",ans1

#print(count_str())


#counting each word by using loop
str1="Hello World"
for i in str1:
    a1 = str1.count(i)
    #print(a1)

#count all character and store in Object with a Name of a Character
str1 = "Hello World"
Obj = {}
for i in str1:
    if i in Obj:
        Obj[i] += 1
    else:
        Obj[i] = 1
print(Obj)

#Sum of digit 
def sum_of_num(n):
    sum=0
    while n!=0:
        rem=n%10
        sum = sum+rem
        n=n/10
    return int(sum)

#n=int(input("Enter the number"))
#print(sum_of_num(n))



#class program to calculate a factor
class factor:
   #def __init__(self,number):
        #self.number = number

    def accept(self,number):
        self.number = number

    def display(self):
        fact = 1 
        for i in range(1,n):
            fact = fact*i
            print(fact)

n = int(input("Enter the number"))
f1 = factor()
f1.accept(n)
f1.display()
