# def is_vowel(letter):
#     return letter in ['a', 'e', 'i', 'o', 'u', 'y']

# def score_words(words):
#     score = 0
#     for word in words:
#         num_vowels = 0
#         for letter in word:
#             if is_vowel(letter):
#                 num_vowels += 1
#         if num_vowels % 2 == 0:
#             score += 2
#         else:
#             ++score
#     return score
# n = int(input())
# words = input().split()
# print(score_words(words))

# x="hacker book"
# vowels=["a","e","i","o","u"]
# vowel=0
# consonants=0
# for i in x:
#     if i in vowels:
#         vowel=vowel+1
#     else:
#         consonants=consonants+1
# print(vowel)
# print(consonants)


def fun(x):
    vowels=["a","e","i","o","u"]
    vowel=0
    for i in x:
        if i in vowels:
            vowel=vowel+1
    print(vowel)
x="hacker book"
fun(x)

