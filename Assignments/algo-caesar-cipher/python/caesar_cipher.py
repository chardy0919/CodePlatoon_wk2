
def caesar_cipher(string, shift_amount):
    alph = "abcdefghijklmnopqrstuvwxyz"
    big_alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = ""
    for letter in string:
        if letter in alph:
            letter = alph[(alph.index(letter) + shift_amount) % 26]
            answer += letter
        elif letter in big_alph:
            letter = big_alph[(big_alph.index(letter) + shift_amount) % 26]
            answer += letter
        else:
            answer += letter
    return answer

print(caesar_cipher("Boy! What a string!", -5))
print(caesar_cipher("Hello zach168! Yes here.", 5))
print(caesar_cipher("Hello Zach168! Yes here.", -5))

