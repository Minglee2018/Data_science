b = input("Nhap va chuoi doi xung \n ")
c = b[:len(b)//2]
d = b[(len(b)//2 if len(b)%2==0 else len(b)//2+1):][::-1]
print ("YES") if c == d else print ("NO")
