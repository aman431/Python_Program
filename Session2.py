#check a number is Even or Odd

class Even_Odd:
    def accept(self):
        self.n=int(input("Enter the Number"))

    def check(self):
        self.l1 = []
        i=2
        num = 10
        while i <= self.n:
            if self.n%i == 0:
                self.l1.append(i)
            i=i+1
        #print(self.l1)

    def display(self):
        print("The list of ", self.l1)
'''
c = Even_Odd()
c.accept()
c.check()
c.display()
'''

#Store the String in array which is in the position of even Number
class Count_String:
    def accept(self):
        self.str1 = input("Enter the String")

    def check(self):

        self.str2 = ''
        for i in range(len(self.str1)):
            if(i%2==0):
                self.str2 = self.str2+ self.str1[i]

    def display(self):
        print(self.str1)
        print(self.str2)


c = Count_String()
c.accept()
c.check()
c.display()
