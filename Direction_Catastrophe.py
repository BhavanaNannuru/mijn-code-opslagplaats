opp={
    'north':'south',
    'south':'north',
    'east':'west',
    'west':'east'
}

n=int(input("Enter the number of instructions: "))
dir=[]
out=[]
for i in range(n):
    dir.append(input("Enter the direction: "))
for i in range(n):
    if out and dir[i] == opp[out[-1]]:
        out.pop()
        i+=1
    elif out and dir[i]==out[-1]:
        i+=1
    else:
        out.append(dir[i])
for i in out:
    print(i,end=' ')
