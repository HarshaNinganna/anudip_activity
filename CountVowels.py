def count_vowels():
    text ="Anudip Foundation"
    vowels = "aeiouAEIOU"
    count=0
    for char in text:
        if char in vowels:
            count += 1
    print("Number of vowels:", count)
count_vowels()
        
