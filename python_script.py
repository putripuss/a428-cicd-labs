import sys
bilangan1 = int(sys.argv[1])
bilangan2 = int(sys.argv[2])

if len(sys.argv) < 3:
    print("Dua angka diperlukan sebagai argumen")
    sys.exit(1)

game = True
skor = 0

while game == True:
    bilangan1 = int(sys.argv[1])
    bilangan2 = int(sys.argv[2])
    print(f'\nBerapakah hasil perkalian berikut ini')
    jawab = input(str(bilangan1) + " x " + str(bilangan2) + " = ")
    jawaban_benar = bilangan1 * bilangan2
    if jawab == str(jawaban_benar):
        skor += 10
        print(f'Jawaban Anda Benar, Skor Anda = {skor}')
    else:
        print(f'Jawaban anda salah, jawaban seharusnya adalah {jawaban_benar}')
    konfirmasi = input('\nApakah ingin melanjutkan game (Y/T)?')
    if konfirmasi == 'T':
        break
print('Akhiri Game\n')
