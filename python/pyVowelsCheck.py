### Checking if the character is vowels;
vowels = ['a', 'e', 'i', 'o', 'u']
sample = input("Kindly write your String: ")
length = len(sample)
if(length > 1):
    for x in range(0, length):
        char = sample[x:x+1]
        # result = print(f"Character {char} is a Vowel") if char in vowels else print("Character %s is not a Vowel", char)
        result = print("Character %s is a Vowel" %(char)) if char in vowels else print("Character %s is not a vowels" %(char)) 
        # if char != " " print("Character %d is NA" %(char)) else print("Character is NA")
else:
    if sample in vowels: print("Character %s is a Vowel" %(sample))
    else: print("Character %s is not a Vowel" %(sample))
### End;