
num = int(input("How many terms? "))
num1=0
num2=1
sum=0
if num<=0:
    print("enter valid limit")
elif num==1:
    print(num2)
else:
    print("fibonacci series form 0 to Num:")
    while sum<num:
        print(num1)
        new= num1+num2
        num1=num2
        num2=new
        sum+=1
    
    
    


