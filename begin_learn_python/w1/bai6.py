s = input("Enter string : \n ")
w = int (input("Enter width : \n "))
k = 0
while k < len(s):
    print (s[k:(w+k)])
    k +=w
