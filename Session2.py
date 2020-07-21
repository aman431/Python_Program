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


c = Even_Odd()
c.accept()
c.check()
c.display()
