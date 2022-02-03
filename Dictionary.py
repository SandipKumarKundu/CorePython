# presence of Vaowel in any word
def isVowelPresent(word):
    vowel = ["a", "e", "i", "o", "u"]
    occurrence = {}
    for j in word:
        if j in vowel:
            if j in occurrence:
                occurrence[j] = occurrence[j] + 1
            else:
                # print(j)
                occurrence[j] = 1
                # print(occurrence[j])
    for k,v in occurrence.items():
        print(k,v)

isVowelPresent("sampadh")
