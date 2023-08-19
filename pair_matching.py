word=input("Enter the string: ")
letters={}
count=0
for letter in word:
    if letter in letters:
        letters[letter]+=1
    else:
        letters[letter]=1
for c in letters.values():
    count+=(c//2)
print(count)