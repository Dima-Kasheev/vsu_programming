x = float(input('x: '))
y = float(input('y: '))

if x > 0 and y > 0:
    print('I Chetvert`')
elif x < 0 and y > 0:
    print('II Chetvert`')
elif x < 0 and y < 0:
    print('III Chetvert`')
elif x > 0 and y < 0:
    print('IV Chetvert`')
else:
    print('Lezhat na odnoi osi')
