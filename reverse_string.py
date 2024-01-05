string = input("give me a word to reverse: ")

cut = [i for i in string]

length = len(cut)

reversed_string = []

for letter in range(length):
    n =1
    m = n + letter
    jack = reversed_string.append(cut[length-m])
print(reversed_string)

#the easy way
#txt = "Hello World"[::-1]
#print(txt) 
