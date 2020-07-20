def count_str():
    str1 = 'Hello World'
    l1 = [12,2,3,4,5,6,6,7,7,7]
    ans = str1.count('o')
    ans1 = l1.count(7);
    return "String ",ans," Integer ",ans1

print(count_str())

#counting each word
str1="Hello World"
for i in str1:
    a1 = str1.count(i)
    #print(a1)
