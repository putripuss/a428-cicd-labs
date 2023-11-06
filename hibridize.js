const banyak = 2543998;

const sifat1 = ['BB', 'Bb', 'bB', 'bb'];
const sifat2 = ['KK', 'Kk', 'kK', 'kk'];

let bulat_kuning = 0;
let bulat_hijau = 0;
let kisut_kuning = 0;
let kisut_hijau = 0;

for (let i = 0; i < banyak; i++) {
    const gen1 = sifat1[Math.floor(Math.random() * sifat1.length)];
    const gen2 = sifat2[Math.floor(Math.random() * sifat2.length)];

    const fen1 = gen1 === 'bb' ? 'kisut' : 'bulat';
    const fen2 = gen2 === 'kk' ? 'hijau' : 'kuning';

    const fenotipe = `${fen1}_${fen2}`;

    switch (fenotipe) {
        case 'bulat_kuning':
            bulat_kuning++;
            break;
        case 'bulat_hijau':
            bulat_hijau++;
            break;
        case 'kisut_kuning':
            kisut_kuning++;
            break;
        default:
            kisut_hijau++;
    }
}

console.log(`Bulat Kuning = ${bulat_kuning} => ${Math.round((bulat_kuning/banyak)*100)} => ${Math.round(((bulat_kuning/banyak)*100)/25)}`);
console.log(`Bulat Hijau = ${bulat_hijau} => ${Math.round((bulat_hijau/banyak)*100)} => ${Math.round(((bulat_hijau/banyak)*100)/25)}`);
console.log(`Kisut Kuning = ${kisut_kuning} => ${Math.round((kisut_kuning/banyak)*100)} => ${Math.round(((kisut_kuning/banyak)*100)/25)}`);
console.log(`Kisut Hijau = ${kisut_hijau} => ${Math.round((kisut_hijau/banyak)*100)} => ${Math.round(((kisut_hijau/banyak)*100)/25)}`);
