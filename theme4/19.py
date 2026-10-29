x = int(input('Input number in [0..30]: '))

if 0 <= x < 10:
    print('[0, 10)')
elif 10 <= x < 20:
    print('[10, 20)')
elif 20 <= x <= 30:
    print('[20, 30]')
else:
    print('Out of range')
