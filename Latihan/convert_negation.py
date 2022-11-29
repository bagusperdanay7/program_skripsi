s1 = "hello python world , i'm a beginner"
s2 = "world"

print(s1[s1.index(s2) + len(s2):])

kalimat = ["tidak", "enak", "makanannya", "jangan", "dibeli", "teman-teman"]
kata_negasi = ['tidak', 'bukan', 'jangan', 'belum']

list_baru = []
for word in kalimat:
    if word in kata_negasi:
        print(word)
        list_baru.append(word)
print(list_baru)

if any((match := substring) in kalimat for substring in kata_negasi):
    # 👇️ this runs
    print(match)  # 👉️ 'two'
else:
    print('The string does NOT contain any of the elements in the list')

if any(ext in kalimat for ext in kata_negasi):
    print(kalimat)

sentence = ['this ', 'is ', 'are ', 'a ', 'sentence']
string = ''.join([i for i in sentence if i != 'are '])
print(string)

# for kata in kata_negasi:
#     kata = kata.replace("Tidak bisa", "gagal")
#     kata = kata.replace("Belum bisa", "gagal")
#     kata = kata.replace("jangan dipake", "yang lain")
#     kata = kata.replace("tidak murah", "mahal")
#     kata_negasi_baru.append(kata)

# print(kata_negasi_baru)

list_word = ['Ini', 'sudah', 'tidak', 'bisa', 'dibiarkan']

baru = list_word[2] + list_word[3]
print(baru)

for word in list_word:
    if word == "tidak":
        anu = word.join(map(str, word))
        print(anu)
    # print(word)

text = "tidak direkomendasiin nih bukan favorit lagi intinya mah bye bye belum puas kalau gini caranya"


def convert_negation(teks):
    convert_tidak = teks.replace("tidak ", "tidak_")
    convert_belum = convert_tidak.replace("belum ", "belum_")
    last_convert = convert_belum.replace("bukan ", "bukan_")

    return last_convert


print(convert_negation(text))
