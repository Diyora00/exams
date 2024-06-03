#Baxtiyorova Diyora  Varinat"A"


#1-misol
p1={'name':input("Enter name:"),'age':input ("Enter age:")}
p2={'name':input("Enter name:"),'age':input ("Enter age:")}
if p1['age'] > p2['age']:
    print("Yoshi kattasi:",p1['name'])
elif p1['age'] == p2['age']:
    print("Yoshlari bir xil.")
else:
    print("Yoshi kattasi:",p2['name'])



#2-misol
my_db={"name":input('Enter name:'),"age":int(input('Enter age:'))}
print(my_db['name'],my_db['age']+10)



#3-misol
def useer_info(name=input("Enter name:"),age=input("Enter age:"),email=input("Enter email:")):
    print('Name:',name,'Age:',age,'Email:',email)
useer_info()



#4-misol
list=[]
print("Input word:")
word=input("...")
list.append(word)
while word !=' ':
 word=input("...")
 if word=='':
     break
 if word not in list:
  list.append(word)

print(list)


#5-misol
dic={}
n=int(input("Input n:"))
for i in range(1,n+1):
    dic[i]=i**2
print(dic)
