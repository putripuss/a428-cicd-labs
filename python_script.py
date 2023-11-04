import random
import os

game = True
skor = 0

while game == True:
    bilangan1 = random.randrange(1,20)
    bilangan2 = random.randrange(1,20)
    print(f'\nBerapakah hasil perkalian berikut ini')
    jawab = os.getenv('JAWABAN')  # Mengambil nilai dari variabel lingkungan JAWABAN
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