import sys

game = True
skor = 0

while game == True:
    bilangan1 = int(sys.argv[1])  # Mengambil bilangan pertama dari argumen
    bilangan2 = int(sys.argv[2])  # Mengambil bilangan kedua dari argumen
    print(f'\nBerapakah hasil perkalian berikut ini')
    jawab = input(str(bilangan1) + " x " + str(bilangan2) + " = ")
    jawaban_benar = bilangan1*bilangan2
    if jawab == str(jawaban_benar):
        skor += 10
        print(f'Jawaban Anda Benar, Skor Anda = {skor}')
    else:
        print(f'Jawaban anda salah, jawaban seharusnya adalah {jawaban_benar}')
    konfirmasi = input('\nApakah ingin melanjutkan game (Y/T)?')
    if konfirmasi == 'T':
        break
print('Akhiri Game\n')
