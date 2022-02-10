x=input('Enter Hours: ')
y=input('Enter Rate: ')

try:
    a=float(x)
    b=float(y)
except:
    print("Error,please enter numeric input")
    quit()

if a>40:
    print("Overtime")
    reg=a*b
    otp=(a-40.0)*(b*0.5)
    print(reg,otp)
    c=reg+otp
else:
    print("Regular")
    c=a*b
print("Pay:",c)    

