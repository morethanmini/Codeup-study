inp = list(input().split())
inp_count = inp.count('1')

if inp_count == 1:
    print('도')
elif inp_count == 2:
    print('개')
elif inp_count == 3:
    print('걸')
elif inp_count == 4:
    print('윷')
else:
    print('모')