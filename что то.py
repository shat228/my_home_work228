s="""
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
"""
print(s)
s1="hello world"
print(s1[0])
print(s1[::4])
##s1[-1]="a"
##priny(s1)
s2="hello world"
s2=s2[0:-1]+"a"
print(s2)
str.split( "hello world")
print(str.split( "hello world"))
s3=input("enter symbols:")
print(s3.split())
print("-".join(s3))
s4="red blue yellow green pink"
print(s4.find("green"))
print(s4.find("violet"))
y ="yellow"
r="red"
b="blue"
g="green"
print("yellow:{0}, red:{3}.".format(y,b,r,g))
s5=input("enter your symdols:")
num_up=0 
num_low=0
for i in s5:
    if i.islower():
        num_low+=1
    elif i.isupper():
        num_up+=1
if num_low<num_up:
    print("upper:"), s5.upper()
elif num_up<num_low:
    print("lower:"),s5.lower()
