inital =0
inital1=1

fibonacci=[inital,inital1]

number = int(input())

for i in range(2,number):
    temp = inital1+inital
    inital=inital1
    inital1=temp
    fibonacci.append(temp)
print(' '.join(map(str,fibonacci)))