try:
    print 5 / 0
except:
    print "It is not correct!"

print "Give me two numbers, and I'll divide them."
print "Enter 'q' to quit."

while True:
    first = raw_input('Input the first number:')
    if first == 'q':
        break
    second = raw_input('Input the second number:')
    try:
        answer = int(first) / int(second)
    except:
        print 'This is not valid.'
    else:
        print 'The answer is: ' + str(answer)
