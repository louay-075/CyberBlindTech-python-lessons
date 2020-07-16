num1 = int(raw_input('Enter first number :'))
o = raw_input('Choose the operation :')
num2 = int(raw_input('Enter the second number :'))

if o == '+':
  print 'The result is ', num1 + num2 
elif o == '/':
  print 'The result is ', num1 / num2
elif o == '*':
  print 'The result is ', num1 * num2
elif o == '-':
  print 'The result is ', num1 - num2
else:
  print 'ERROR , you need to choose + or / or * or -'