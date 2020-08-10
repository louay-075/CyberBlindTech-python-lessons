import sys

def add(a, b):
    print "The result is :", a + b

def d(a, b):
    a = float(a)
    b = float(b)
    if b < a:
        print "The result is : ", a / b
    else:
        print "The result is : ", b / a

def m(a, b):
    print "The result is :", a * b

def s(a,b):
    if a < b:
        print "The result is : ", b - a
    else:
        print "The result is : ", a - b

def main():
    print "Welcome !!!"
    num = int(raw_input('Enter a number : '))
    o = raw_input('Operation : ')
    num2 = int(raw_input('Enter a second number :'))
    
    if '+' in o:
        add(num, num2)
        main()
    elif '/' in o:
        d(num, num2)
        main()
    elif '*' in o:
        m(num, num2)
        main()
    elif '-' in o:
        s(num, num2)
        main()
    elif 'x' in o or 'exit' in o:
        sys.exit()
    else:
        print "Please enter a valid operation!"
        main()
    

main()