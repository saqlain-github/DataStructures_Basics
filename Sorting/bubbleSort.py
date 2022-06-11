a = [20,10,30,60,50]

for i in range(len(a),0,-1):
    for j in range(i-1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

'''
for i in range(len(a)):
    for j in range(0,len(a)-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
'''

#both codes are working
print(a)