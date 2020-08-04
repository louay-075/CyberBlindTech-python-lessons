def add(a, b):
    print "The result is :", a + b

def d(a, b):
    print "The result is : ", a / b

def m(a, b):
    print "The result is :", a * b

def s(a,b):
    print "The result is : ", a - b

def main():
    print "Welcome !!!"
    num = int(raw_input('Enter a number : '))
    o = raw_input('Operation : ')
    num2 = int(raw_input('Enter a second number :'))
    
    if o == '+':
        add(num, num2)
    elif o == '/':
        d(num, num2)
    elif o == '*':
        m(num, num2)
    elif o == '-':
        s(num, num2)
    else:
        print "Please enter a valid operation!"
    

main()