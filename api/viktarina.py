from rest_framework.views import APIView
from rest_framework.response import Response
import random

class Viktoriya(APIView):
    def get(self, request):
 


        quiz_1 = [
            {
                "question": "Dunyoning eng katta tog‘ tizmalari?",
                "answer": "Gimolay",
                "variant": ["Gimolay", "And", "Alp", "Tyan-Shan"]
            },
            {
                "question": "Rassiyaning poytaxti qaysi?",
                "answer": "Maskva",
                "variant": ["Maskva", "Sankt-Peterburg", "Leningrad", " Astrahan"]
            },
            {
                "question": "Yerning sun’iy yo‘ldoshi qaysi?",
                "answer": "Oy",
                "variant": ["Oy", "Quyosh", "Mars", "Sirius"]
            },
            {
                "question": "Dunyodagi eng katta okean?",
                "answer": "Tinch okeani",
                "variant": ["Tinch okeani", "Atlantika okeani", "Hind okeani", "Shimoliy muz okeani"]
            },
            {
                "question": "O‘zbekiston bayrog‘ida nechta rang bor?",
                "answer": "4",
                "variant": ["3", "4", "2", "5"]
            },
            {
                "question": "Inson tanasida nechta yurak mavjud?",
                "answer": "1",
                "variant": ["1", "2", "3", "4"]
            },
            {
                "question": "Yer yuzidagi eng katta qit’a?",
                "answer": "Osiyo",
                "variant": ["Osiyo", "Afrika", "Yevropa", "Amerika"]
            },
            {
                "question": "Futbol o‘yinida maydonda bir jamoada nechta o‘yinchi bo‘ladi?",
                "answer": "11",
                "variant": ["11", "10", "9", "12"]
            },
            {
                "question": "Atom raqami 1 bo‘lgan kimyoviy element?",
                "answer": "Vodorod",
                "variant": ["Vodorod", "Kislorod", "Azot", "Heliy"]
            },
            {
                "question": "‘Alpomish’ dostoni muallifi kim?",
                "answer": "O'zbek xalq dostoni",
                "variant": ["O'zbek xalq dostoni", "Erkin Vohidov", "Said Ahmad", "Hamza Hakimzoda"]
            },
            {
                "question": "Eng uzun daryo?",
                "answer": "Nil",
                "variant": ["Nil", "Amazonka", "Amudaryo", "Sirdaryo"]
            },
            {
                "question": "Inson tanasidagi eng katta suyak?",
                "answer": "Son suyagi",
                "variant": ["Son suyagi", "Bilak suyagi", "Umurtqa", "To‘piq suyagi"]
            },
            {
                "question": "Kompyuterning asosiy qurilmasi?",
                "answer": "Protsessor",
                "variant": ["Protsessor", "Monitor", "Klaviatura", "Sichqoncha"]
            },
            {
                "question": "O‘zbekiston mustaqillikka qachon erishgan?",
                "answer": "1991",
                "variant": ["1991", "1990", "1992", "1989"]
            },
            {
                "question": "Poytaxti Parij bo‘lgan davlat?",
                "answer": "Fransiya",
                "variant": ["Fransiya", "Germaniya", "Italiya", "Ispaniya"]
            },
            {
                "question": "Yer yuzidagi eng baland tog‘?",
                "answer": "Everest",
                "variant": ["Everest", "Kilimanjaro", "Tyan-Shan", "Pomir"]
            },
            {
                "question": "Quyosh tizimidagi eng katta sayyora?",
                "answer": "Yupiter",
                "variant": ["Yupiter", "Saturn", "Yer", "Mars"]
            },
            {
                "question": "‘Layli va Majnun’ asarining muallifi?",
                "answer": "Navoiy",
                "variant": ["Navoiy", "Bobur", "Pushkin", "Shakespeare"]
            },
            {
                "question": "Amerika qit’asini kim kashf qilgan?",
                "answer": "Xristofor Kolumb",
                "variant": ["Xristofor Kolumb", "Magellan", "Vasko da Gama", "Marko Polo"]
            },
            {
                "question": "Shaxmat o‘yinida nechta dona mavjud?",
                "answer": "32",
                "variant": ["32", "36", "40", "28"]
            },
            {
                "question": "Yengil atletikada marafon masofasi nechchi km?",
                "answer": "42",
                "variant": ["42", "40", "36", "50"]
            },
            {
                "question": "Qozogiston milliy valyutasi?",
                "answer": "Tenge",
                "variant": ["Tenge", "Rubl", "Dollar", "so'm"]
            },
            {
                "question": "Qadimgi Misr ehromlari qaysi shaharda joylashgan?",
                "answer": "Qohira yaqinida",
                "variant": ["Qohira yaqinida", "Aleksandriya", "Luksor", "Asuan"]
            },
            {
                "question": "Dunyodagi eng sovuq qit’a?",
                "answer": "Antarktida",
                "variant": ["Antarktida", "Osiyo", "Shimoliy Amerika", "Yevropa"]
            },
            {
                "question": "Quyosh chiqadigan yo‘nalish?",
                "answer": "Sharq",
                "variant": ["Sharq", "G‘arb", "Shimol", "Janub"]
            },
            {
                "question": "Kompyuterdagi ‘Ctrl+C’ amalini bajaradi?",
                "answer": "Nusxa olish",
                "variant": ["Nusxa olish", "Kesish", "Joylashtirish", "O‘chirish"]
            },
            {
                "question": "Dunyodagi eng katta orol?",
                "answer": "Grenlandiya",
                "variant": ["Grenlandiya", "Madagaskar", "Borneo", "Sumatra"]
            },
            {
                "question": "Inson tanasida qancha juft qovurg‘a bor?",
                "answer": "12 juft",
                "variant": ["12 juft", "10 juft", "14 juft", "11 juft"]
            },
            {
                "question": "Samolyotni kim ixtiro qilgan?",
                "answer": "Rayt aka-ukalari",
                "variant": ["Rayt aka-ukalari", "Edison", "Tesla", "Fulton"]
            },
            {
                "question": "Ertak qahramoni Zumradning singlisi kim edi?",
                "answer": "Qimmat",
                "variant": ["Qimmat", "Oysuluv", "Malika", "Shirin"]
            },
            {
                "question": "Mingbaytli she’r qanday ataladi?",
                "answer": "Doston",
                "variant": ["Doston", "Ruboi", "G‘azal", "Qit’a"]
            },
            {
                "question": "Poytaxti Tokio bo‘lgan davlat?",
                "answer": "Yaponiya",
                "variant": ["Yaponiya", "Xitoy", "Janubiy Koreya", "Tayvan"]
            },
            {
                "question": "O‘zbekistonda nechta viloyat bor?",
                "answer": "12",
                "variant": ["12", "13", "14", "10"]
            },
            {
                "question": "Navoiy qaysi asari bilan mashhur?",
                "answer": "Xamsa",
                "variant": ["Xamsa", "Boburnoma", "Qutadg‘u bilig", "Shohnoma"]
            },
            {
                "question": "Kompyuterdagi ‘Ctrl+V’ nima qiladi?",
                "answer": "Joylashtirish",
                "variant": ["Joylashtirish", "O‘chirish", "Nusxa olish", "Qidirish"]
            },
            {
                "question": "Hujayraning markazi nima?",
                "answer": "Yadro",
                "variant": ["Yadro", "Sitoplazma", "Ribosoma", "Membrana"]
            },
            {
                "question": "Amerika bayrog‘ida nechta yulduz bor?",
                "answer": "50",
                "variant": ["50", "52", "48", "45"]
            },
            {
                "question": "Shaharlarda odamlar ko‘p to‘plangan maydon?",
                "answer": "Maidon",
                "variant": ["Maidon", "Bog‘", "Ko‘cha", "Bozor"]
            },
            {
                "question": "‘Alibaba va qirq qaroqchi’ ertagida nechta qaroqchi bo‘lgan?",
                "answer": "40",
                "variant": ["40", "30", "50", "25"]
            },
            {
                "question": "Poytaxti Moskva bo‘lgan davlat?",
                "answer": "Rossiya",
                "variant": ["Rossiya", "Belarus", "Ukraina", "Latviya"]
            },
            {
                "question": "Basketbol o‘yinida to‘pni savatchaga tashlash nechta ochko?",
                "answer": "2 yoki 3",
                "variant": ["2 yoki 3", "1 yoki 2", "3 yoki 4", "5"]
            },
            {
                "question": "‘Qizil qalpoqcha’ ertagida qizil qalpoqcha kim bilan yashagan?",
                "answer": "Onasi bilan",
                "variant": ["Onasi bilan", "Bobosi bilan", "Opasi bilan", "Buvasi bilan"]
            },
            {
                "question": "Eng yirik quruqlik hayvoni?",
                "answer": "Fil",
                "variant": ["Fil", "Ot", "Sigir", "Yo‘lbars"]
            },
            {
                "question": "Qur’onda nechta sura bor?",
                "answer": "114",
                "variant": ["114", "112", "120", "110"]
            },
            {
                "question": "Musiqa notalari nechta?",
                "answer": "7",
                "variant": ["7", "6", "8", "5"]
            },
            {
                "question": "O‘zbekistonning eng katta viloyati?",
                "answer": "Navoiy",
                "variant": ["Navoiy", "Buxoro", "Toshkent", "Farg‘ona"]
            },
            {
                "question": "Inson tanasida nechta barmoq bor?",
                "answer": "20",
                "variant": ["20", "18", "22", "19"]
            },
            {
                "question": "Amerikaning ramziy hayvoni?",
                "answer": "Burgut",
                "variant": ["Burgut", "Sher", "Fil", "Qoplon"]
            },
            {
                "question": "Yerning qaysi qatlami eng tashqi?",
                "answer": "Qobiq",
                "variant": ["Qobiq", "Mantiya", "Yadro", "Atmosfera"]
            },
            {
                "question": "O‘zbek milliy taomi?",
                "answer": "Palov",
                "variant": ["Palov", "Lag‘mon", "Somsa", "Shashlik"]
            },
            {
                "question": "Yer sharining necha qit’asi mavjud?",
                "answer": "6",
                "variant": ["6", "5", "7", "4"]
            },
            {
                "question": "O‘zbekistonda eng ko‘p aholiga ega viloyat?",
                "answer": "Farg‘ona",
                "variant": ["Farg‘ona", "Andijon", "Samarqand", "Toshkent viloyati"]
            },
            {
                "question": "O‘zbekistonning ramziy me’moriy inshooti Registon qayerda joylashgan?",
                "answer": "Samarqand",
                "variant": ["Samarqand", "Buxoro", "Xiva", "Shahrisabz"]
            },
            {
                "question": "Elektr toki kuchi birligi?",
                "answer": "Amper",
                "variant": ["Amper", "Volt", "Vatt", "Om"]
            },
            {
                "question": "O‘zbekistonda oltin qazib olish markazi bo‘lgan shaharcha?",
                "answer": "Muruntov",
                "variant": ["Muruntov", "Zarafshon", "Angren", "Olmaliq"]
            },
            {
                "question": "Dunyodagi eng baland sharshara?",
                "answer": "Anxel",
                "variant": ["Anxel", "Niagara", "Victoria", "Iguasu"]
            },
            {
                "question": "Qanday metall 'qora oltin' deb ataladi?",
                "answer": "Neft",
                "variant": ["Neft", "Ko‘mir", "Gaz", "Temir"]
            },
            {
                "question": "Inson tanasida eng katta ichki organ?",
                "answer": "Jigar",
                "variant": ["Jigar", "Oshqozon", "Yurak", "Buyrak"]
            },
            {
                "question": "Yevropadagi eng katta davlat maydon jihatdan?",
                "answer": "Rossiya",
                "variant": ["Rossiya", "Ukraina", "Fransiya", "Ispaniya"]
            },
            {
                "question": "Dunyodagi eng yirik qush?",
                "answer": "Tuyoqqush (Strus)",
                "variant": ["Tuyoqqush (Strus)", "Burgut", "Pingvin", "Tovus"]
            },
            {
                "question": "O‘zbekistonning birinchi Prezidenti kim edi?",
                "answer": "Islom Karimov",
                "variant": ["Islom Karimov", "Shavkat Mirziyoyev", "Abduqosimov", "Abdulla Oripov"]
            },
            {
                "question": "Shahzoda qahramoni bo‘lgan mashhur ingliz yozuvchisi?",
                "answer": "Shakespeare",
                "variant": ["Shakespeare", "Dante", "Balzak", "Pushkin"]
            },
            {
                "question": "O‘zbekiston hududi asosan qaysi iqlim zonasida joylashgan?",
                "answer": "Quruq va kontinental",
                "variant": ["Quruq va kontinental", "Ekvatorial", "Subtropik", "Nam tropik"]
            },
            {
                "question": "Dunyodagi eng katta cho‘l?",
                "answer": "Sahroi Kabir",
                "variant": ["Sahroi Kabir", "Karakum", "Kizilqum", "Gobi"]
            },
            {
                "question": "Qaysi hayvon 'o‘rmon shohi' deb ataladi?",
                "answer": "Sher",
                "variant": ["Sher", "Yo‘lbars", "Burgut", "Bo‘ri"]
            },
            {
                "question": "Mingbuloq, Arnasoy, Dengizko‘l — bular nima?",
                "answer": "Ko‘llar",
                "variant": ["Ko‘llar", "Tog‘lar", "Shaharlar", "Daryolar"]
            },
            {
                "question": "‘Yulduzli tunlar’ romanining muallifi kim?",
                "answer": "Pirimqul Qodirov",
                "variant": ["Pirimqul Qodirov", "O‘tkir Hoshimov", "Cho‘lpon", "Abdulla Qahhor"]
            },
            {
                "question": "Dunyodagi eng uzun devor?",
                "answer": "Xitoy devori",
                "variant": ["Xitoy devori", "Berlin devori", "Hadrianning devori", "Bobil devori"]
            },
            {
                "question": "O‘zbekiston Konstitutsiyasi qachon qabul qilingan?",
                "answer": "1992 yil 8 dekabr",
                "variant": ["1992 yil 8 dekabr", "1991 yil 1 sentyabr", "1993 yil 1 yanvar", "1995 yil 9 may"]
            },
            {
                "question": "O‘zbekistondagi eng uzun daryo?",
                "answer": "Amudaryo",
                "variant": ["Amudaryo", "Sirdaryo", "Zarafshon", "Chirchiq"]
            },
            {
                "question": "Quyoshdan keyingi eng yaqin yulduz?",
                "answer": "Proksima Kentavra",
                "variant": ["Proksima Kentavra", "Sirius", "Vega", "Betelgeyze"]
            },
            {
                "question": "Elektr toki kuchlanishi birligi?",
                "answer": "Volt",
                "variant": ["Volt", "Amper", "Vatt", "Om"]
            },
            {
                "question": "Musiqada 4/4 o‘lchov nimani anglatadi?",
                "answer": "Oddiy marsh ritmi",
                "variant": ["Oddiy marsh ritmi", "Vals", "Polka", "Rap"]
            },
            {
                "question": "O‘zbekiston bayrog‘ida nechta yulduz bor?",
                "answer": "12",
                "variant": ["12", "13", "11", "10"]
            },
            {
                "question": "Dunyodagi eng baland hayvon?",
                "answer": "Jirafa",
                "variant": ["Jirafa", "Fil", "Sher", "Ot"]
            },
            {
                "question": "O‘zbekiston gerbida tasvirlangan qush?",
                "answer": "Xumo",
                "variant": ["Xumo", "Burgut", "Qarg‘a", "Qaldirg‘och"]
            },
            {
                "question": "Futbolning vatani hisoblangan davlat?",
                "answer": "Angliya",
                "variant": ["Angliya", "Braziliya", "Italiya", "Ispaniya"]
            },
            {
                "question": "Dunyodagi eng yirik sutemizuvchi hayvon?",
                "answer": "Ko‘k kit",
                "variant": ["Ko‘k kit", "Fil", "Tulki", "Ayiq"]
            },
            {
                "question": "Dunyodagi eng kichik mamlakat?",
                "answer": "Vatikan",
                "variant": ["Vatikan", "Monako", "Andorra", "Lixtenshteyn"]
            },
            {
                "question": "O‘zbekistonning eng katta ko‘li?",
                "answer": "Aral dengizi",
                "variant": ["Aral dengizi", "Aydarko‘l", "Tuzkon", "Qorako‘l"]
            },
            {
                "question": "Kislorodning kimyoviy belgisi?",
                "answer": "O",
                "variant": ["O", "K", "N", "H"]
            },
            {
                "question": "Dunyodagi eng mashhur minoralardan biri – Eyfel minorasi qaysi shaharda?",
                "answer": "Parij",
                "variant": ["Parij", "London", "Rim", "Berlin"]
            },
            {
                "question": "Qaysi sport turi 'oq sport' deb ataladi?",
                "answer": "Tennis",
                "variant": ["Tennis", "Shaxmat", "Boks", "Basketbol"]
            },
            {
                "question": "Inson tanasida qancha tish bo‘ladi (katta yoshda)?",
                "answer": "32",
                "variant": ["32", "28", "36", "30"]
            },
            {
                "question": "Qadimgi yunonlarning bosh xudosi kim?",
                "answer": "Zevs",
                "variant": ["Zevs", "Afina", "Apollon", "Germes"]
            },
            {
                "question": "Kompyuter sichqonchasini ixtiro qilgan olim?",
                "answer": "Duqlas Engelbart",
                "variant": ["Duqlas Engelbart", "Geyts", "Jobs", "Cerf"]
            },
            {
                "question": "Shaxmatdagi eng kuchli figura?",
                "answer": "Ferz",
                "variant": ["Ferz", "Ot", "Shah", "Piyoda"]
            },
            {
                "question": "Armaniston poytaxti?",
                "answer": "Yerevan",
                "variant": ["Yerevan", "Tbilisi", "Boku", "Minsk"]
            },
            {
                "question": "‘Bahor’ faslidan keyin qaysi fasl keladi?",
                "answer": "Yoz",
                "variant": ["Yoz", "Kuz", "Qish", "Bahor yana"]
            },
            {
                "question": "Dunyodagi eng baland daraxt turi?",
                "answer": "Sekvoyya",
                "variant": ["Sekvoyya", "Eman", "Qayrag‘och", "Tol"]
            },
            {
                "question": "Sho‘ro davrida qurilgan kosmik stansiya?",
                "answer": "Mir",
                "variant": ["Mir", "Soyuz", "Saluyt", "Sputnik"]
            },
            {
                "question": "Avesto kitobi qaysi xalq merosi?",
                "answer": "Zardushtiylar",
                "variant": ["Zardushtiylar", "Yunon", "Arab", "Hind"]
            },
            {
                "question": "O‘zbekistonning eng baland nuqtasi?",
                "answer": "Hazrati Sulton cho‘qqisi",
                "variant": ["Hazrati Sulton cho‘qqisi", "Chimgan", "Bobotog‘", "Ayritom"]
            },
            {
                "question": "Osiyodagi eng uzun daryo?",
                "answer": "Yanszi",
                "variant": ["Yanszi", "Sirdaryo", "Ind", "Amur"]
            },
            {
                "question": "O‘zbekiston milliy teatrining nomi?",
                "answer": "Navoi nomidagi teatr",
                "variant": ["Navoi nomidagi teatr", "Yosh tomoshabinlar teatri", "O‘zbek filarmoniyasi", "Ilhom teatri"]
            },
            {
                "question": "Qaysi sayyora 'Qizil sayyora' deb ataladi?",
                "answer": "Mars",
                "variant": ["Mars", "Yupiter", "Venera", "Merkuriy"]
            },
            {
                "question": "Dunyodagi eng katta yarimorol?",
                "answer": "Arabiston yarimoroli",
                "variant": ["Arabiston yarimoroli", "Hindiston yarimoroli", "Iberiya yarimoroli", "Skandinaviya yarimoroli"]
            },
            {
                "question": "O‘zbekistonning eng ko‘p aholiga ega shahri?",
                "answer": "Toshkent",
                "variant": ["Toshkent", "Samarqand", "Andijon", "Namangan"]
            },
            {
                "question": "Amerika bayrog‘idagi qizil rang nimani bildiradi?",
                "answer": "Jasorat",
                "variant": ["Jasorat", "Ozodlik", "Adolat", "Birlik"]
            },
            {
                "question": "Qaysi davlatda eng ko‘p orollar bor?",
                "answer": "Shvetsiya",
                "variant": ["Shvetsiya", "Indoneziya", "Filippin", "Yaponiya"]
            }
        ]

        quiz_2 = [
            {
                "question": "Quyosh tizimidagi eng kichik sayyora?",
                "answer": "Merkuriy",
                "variant": ["Merkuriy", "Mars", "Pluton", "Venera"]
            },
            {
                "question": "Birinchi avtomobilni kim yasagan?",
                "answer": "Karl Bens",
                "variant": ["Karl Bens", "Genri Ford", "Nikola Tesla", "Tomas Edison"]
            },
            {
                "question": "Qaysi davlat 'Quyosh chiqish mamlakati' deb ataladi?",
                "answer": "Yaponiya",
                "variant": ["Yaponiya", "Xitoy", "Koreya", "Hindiston"]
            },
            {
                "question": "Alisher Navoiy qaysi tilning asoschisi hisoblanadi?",
                "answer": "O‘zbek adabiy tili",
                "variant": ["O‘zbek adabiy tili", "Fors tili", "Arab tili", "Turk tili"]
            },
            {
                "question": "Qaysi hayvon tuxum qo‘yadi?",
                "answer": "To‘tiqush",
                "variant": ["To‘tiqush", "Mushuk", "Ot", "Fil"]
            },
            {
                "question": "Afrikadagi eng baland tog‘?",
                "answer": "Kilimanjaro",
                "variant": ["Kilimanjaro", "Atlas", "Drakensberg", "Kenya"]
            },
            {
                "question": "O‘zbek xalqining milliy cholg‘usi?",
                "answer": "Doira",
                "variant": ["Doira", "Gitara", "Fortepiano", "Skripka"]
            },
            {
                "question": "Yevropadagi eng katta shahar?",
                "answer": "Moskva",
                "variant": ["Moskva", "London", "Parij", "Berlin"]
            },
            {
                "question": "Suvning kimyoviy formulasi?",
                "answer": "H2O",
                "variant": ["H2O", "CO2", "O2", "NaCl"]
            },
            {
                "question": "Qaysi sport turi 'shohlar o‘yini' deb ataladi?",
                "answer": "Shaxmat",
                "variant": ["Shaxmat", "Futbol", "Basketbol", "Boks"]
            },
            {
                "question": "Qadimgi Rim imperiyasining poytaxti?",
                "answer": "Rim",
                "variant": ["Rim", "Afina", "Istanbul", "Neapol"]
            },
            {
                "question": "O‘zbekistonning milliy valyutasi 1994 yilda qaysi pul o‘rniga kiritilgan?",
                "answer": "So‘m-kupon",
                "variant": ["So‘m-kupon", "Rubl", "Tanga", "Dollar"]
            },
            {
                "question": "Afrika qit’asida joylashgan eng katta davlat?",
                "answer": "Jazoir",
                "variant": ["Jazoir", "Misr", "Nigeriya", "Kongo"]
            },
            {
                "question": "O‘zbekistondagi eng qadimiy shahar?",
                "answer": "Buxoro",
                "variant": ["Buxoro", "Samarqand", "Xiva", "Termiz"]
            },
            {
                "question": "Dunyodagi eng mashhur klassik bastakor?",
                "answer": "Betxoven",
                "variant": ["Betxoven", "Motsart", "Bax", "Sho‘stopovich"]
            },
            {
                "question": "Avstraliya qit’asida uchraydigan mashhur hayvon?",
                "answer": "Kanguru",
                "variant": ["Kanguru", "Fil", "Sher", "Bo‘ri"]
            },
            {
                "question": "O‘zbekistondagi eng katta kon?",
                "answer": "Qizilqum oltin koni",
                "variant": ["Qizilqum oltin koni", "Angren ko‘mir koni", "Olmaliq mis koni", "Sharg‘un ko‘mir koni"]
            },
            {
                "question": "Yevropadagi eng uzun daryo?",
                "answer": "Volga",
                "variant": ["Volga", "Dunay", "Rhin", "Loira"]
            },
            {
                "question": "Dunyodagi eng yirik sport musobaqasi?",
                "answer": "Olimpiya o‘yinlari",
                "variant": ["Olimpiya o‘yinlari", "Jahon chempionati", "UEFA Chempionlar ligasi", "Davis kubogi"]
            },
            {
                "question": "O‘zbekistonning milliy taomi tandirda pishiriladigan non?",
                "answer": "Tandir non",
                "variant": ["Tandir non", "Somsa", "Chuchvara", "Lag‘mon"]
            },
            {
                "question": "Yer yuzidagi eng issiq harorat qayd etilgan cho‘l?",
                "answer": "Lut cho‘li",
                "variant": ["Lut cho‘li", "Sahroi Kabir", "Karakum", "Kizilqum"]
            },
            {
                "question": "Qaysi davlatda 'Taj Mahal' joylashgan?",
                "answer": "Hindiston",
                "variant": ["Hindiston", "Pokiston", "Bangladesh", "Nepal"]
            },
            {
                "question": "O‘zbekistonda qaysi viloyat 'paxtachilik markazi' sifatida tanilgan?",
                "answer": "Farg‘ona",
                "variant": ["Farg‘ona", "Samarqand", "Buxoro", "Navoiy"]
            },
            {
                "question": "Eng mashhur rus yozuvchilaridan biri?",
                "answer": "Tolstoy",
                "variant": ["Tolstoy", "Pushkin", "Dostoevskiy", "Chexov"]
            },
            {
                "question": "Qaysi sport turi muz ustida o‘ynaladi?",
                "answer": "Xokkey",
                "variant": ["Xokkey", "Basketbol", "Futbol", "Voleybol"]
            },
            {
                "question": "Qaysi shahar 'sharq durdonasi' deb ataladi?",
                "answer": "Samarqand",
                "variant": ["Samarqand", "Buxoro", "Xiva", "Termiz"]
            },
            {
                "question": "Bir soatda nechta daqiqa bor?",
                "answer": "60",
                "variant": ["60", "100", "30", "90"]
            },
            {
                "question": "Qaysi davlatda eng ko‘p aholiga ega shahar — Mexiko joylashgan?",
                "answer": "Meksika",
                "variant": ["Meksika", "Braziliya", "Argentina", "Ispaniya"]
            },
            {
                "question": "Qaysi hayvon 'sahro kemasi' deb ataladi?",
                "answer": "Tuyа",
                "variant": ["Tuyа", "Ot", "Sigir", "Fil"]
            },
            {
                "question": "O‘zbekiston qaysi materikda joylashgan?",
                "answer": "Osiyo",
                "variant": ["Osiyo", "Yevropa", "Afrika", "Amerika"]
            },
            {
                "question": "Eng mashhur italyan rassomi?",
                "answer": "Leonardo da Vinchi",
                "variant": ["Leonardo da Vinchi", "Mikelanjelo", "Rafael", "Donatello"]
            },
            {
                "question": "Yer sharidagi eng katta okean qirg‘og‘iga ega davlat?",
                "answer": "Kanada",
                "variant": ["Kanada", "Rossiya", "AQSh", "Avstraliya"]
            },
            {
                "question": "O‘zbekistonda eng katta suv ombori?",
                "answer": "To‘dako‘l",
                "variant": ["To‘dako‘l", "Chorvoq", "Qoratepa", "Bo‘zsuv"]
            },
            {
                "question": "Qaysi hayvon eng tez yuguradi?",
                "answer": "Gepard",
                "variant": ["Gepard", "Ot", "Bo‘ri", "Sher"]
            },
            {
                "question": "Qaysi shahar 'abadiy shahar' deb ataladi?",
                "answer": "Rim",
                "variant": ["Rim", "Afina", "Istanbul", "Parij"]
            },
            {
                "question": "Dunyodagi eng ko‘p aholiga ega davlat?",
                "answer": "Xitoy",
                "variant": ["Xitoy", "Hindiston", "AQSh", "Indoneziya"]
            },
            {
                "question": "O‘zbek milliy libosidagi eng asosiy bosh kiyim?",
                "answer": "Do‘ppi",
                "variant": ["Do‘ppi", "Telpak", "Salla", "Kepka"]
            },
            {
                "question": "Qaysi davlat 'pasta' va 'pitsa' vatani?",
                "answer": "Italiya",
                "variant": ["Italiya", "Fransiya", "Ispaniya", "Gretsiya"]
            },
            {
                "question": "Qaysi davlatning poytaxti Berlin?",
                "answer": "Germaniya",
                "variant": ["Germaniya", "Fransiya", "Polsha", "Avstriya"]
            },
            {
                "question": "Yerning o‘rtacha radiusi taxminan nechaga teng?",
                "answer": "6371 km",
                "variant": ["6371 km", "7000 km", "5500 km", "6000 km"]
            },
            {
                "question": "O‘zbekiston hududidan oqib o‘tadigan eng yirik daryo?",
                "answer": "Amudaryo",
                "variant": ["Sirdaryo", "Amudaryo", "Zarafshon", "Qashqadaryo"]
            },
            {
                "question": "Qaysi davlatda eng ko‘p ko‘llar bor?",
                "answer": "Kanada",
                "variant": ["Kanada", "Rossiya", "Braziliya", "AQSh"]
            },
            {
                "question": "Dunyodagi eng katta tog‘ tizmasi?",
                "answer": "Gimolay",
                "variant": ["Gimolay", "And", "Tyan-Shan", "Alp"]
            },
            {
                "question": "O‘zbekistonning eng baland shahri?",
                "answer": "Chorvoq",
                "variant": ["Chorvoq", "Termiz", "Buxoro", "Urganch"]
            },
            {
                "question": "Afrikadagi eng ko‘p aholiga ega davlat?",
                "answer": "Nigeriya",
                "variant": ["Nigeriya", "Misr", "Efiopiya", "Jazoir"]
            },
            {
                "question": "Dunyodagi eng katta ormon?",
                "answer": "Amazonka",
                "variant": ["Amazonka", "Taiga", "Kongo", "Yevropa o‘rmonlari"]
            },
            {
                "question": "Qaysi shahar Buyuk Britaniya poytaxti?",
                "answer": "London",
                "variant": ["London", "Parij", "Madrid", "Berlin"]
            },
            {
                "question": "Shveytsariya qaysi narsalari bilan mashhur?",
                "answer": "Soatlar",
                "variant": ["Soatlar", "Mashinalar", "Telefonlar", "Raketalar"]
            },
            {
                "question": "O‘zbekistonda eng ko‘p yetishtiriladigan meva?",
                "answer": "Uzum",
                "variant": ["Uzum", "Olma", "Anor", "O‘rik"]
            },
            {
                "question": "Qaysi shahar O‘zbekistonning qadimiy poytaxti bo‘lgan?",
                "answer": "Samarqand",
                "variant": ["Samarqand", "Buxoro", "Xiva", "Toshkent"]
            },
            {
                "question": "Amerikada joylashgan eng mashhur sharshara?",
                "answer": "Niagara",
                "variant": ["Niagara", "Iguasu", "Victoria", "Anxel"]
            },
            {
                "question": "Mashhur futbolchi Lionel Messining vatani?",
                "answer": "Argentina",
                "variant": ["Argentina", "Ispaniya", "Braziliya", "Portugaliya"]
            },
            {
                "question": "Hindistondagi eng mashhur kino sanoati nomi?",
                "answer": "Bollivud",
                "variant": ["Bollivud", "Gollivud", "Tolivud", "Kolivud"]
            },
            {
                "question": "Dunyodagi eng katta ko‘rfaz?",
                "answer": "Bengal ko‘rfazi",
                "variant": ["Bengal ko‘rfazi", "Meksika ko‘rfazi", "Aden ko‘rfazi", "Pers ko‘rfazi"]
            },
            {
                "question": "Elektr toki qarshiligi birligi?",
                "answer": "Om",
                "variant": ["Om", "Amper", "Volt", "Vatt"]
            },
            {
                "question": "Yaponiyaning milliy sporti?",
                "answer": "Sumo",
                "variant": ["Sumo", "Karate", "Judo", "Kendo"]
            },
            {
                "question": "O‘zbekiston Respublikasi Davlat madhiyasining matn muallifi kim?",
                "answer": "Abdulla Oripov",
                "variant": ["Abdulla Oripov", "Erkin Vohidov", "Cho‘lpon", "O‘tkir Hoshimov"]
            },
            {
                "question": "Qaysi davlat 'piramidalar mamlakati' deb ataladi?",
                "answer": "Misr",
                "variant": ["Misr", "Meksika", "Xitoy", "Hindiston"]
            },
            {
                "question": "Dunyodagi eng katta metall ishlab chiqaruvchi davlat?",
                "answer": "Xitoy",
                "variant": ["Xitoy", "AQSh", "Rossiya", "Hindiston"]
            },
            {
                "question": "Yer yuzidagi eng chuqur ko‘l?",
                "answer": "Baykal",
                "variant": ["Baykal", "Tanganika", "Viktoriya", "Aral"]
            },
            {
                "question": "Dunyodagi eng baland minora?",
                "answer": "Burj Xalifa",
                "variant": ["Burj Xalifa", "Eyfel minorasi", "CN Tower", "Empire State Building"]
            },
            {
                "question": "Kimyo fanida O belgisi qaysi elementga tegishli?",
                "answer": "Kislorod",
                "variant": ["Kislorod", "Vodorod", "Azot", "Heliy"]
            },
            {
                "question": "Yozuv mashinasini kim ixtiro qilgan?",
                "answer": "Sholes",
                "variant": ["Sholes", "Bell", "Edison", "Tesla"]
            },
            {
                "question": "Qaysi shahar 'Osmon minoralari shahri' deb ataladi?",
                "answer": "Dubay",
                "variant": ["Dubay", "Nyu-York", "Parij", "Seul"]
            },
            {
                "question": "Dunyodagi eng ko‘p aholiga ega shahar?",
                "answer": "Tokio",
                "variant": ["Tokio", "Dehli", "Shanxay", "Meksiko"]
            },
            {
                "question": "Sharqning mashhur olimi Ibn Sino qaysi sohada mashhur?",
                "answer": "Tibbiyot",
                "variant": ["Tibbiyot", "Matematika", "Astronomiya", "Adabiyot"]
            },
            {
                "question": "Yashil rangdagi sabzavotlardan biri?",
                "answer": "Bodring",
                "variant": ["Bodring", "Sabzi", "Karam", "Piyoz"]
            },
            {
                "question": "Dunyodagi eng katta dengiz?",
                "answer": "Qora dengiz",
                "variant": ["Qora dengiz", "O‘lik dengiz", "Kaspiy dengizi", "Oq dengiz"]
            },
            {
                "question": "Kompyuter klaviaturasidagi 'Space' tugmasi nima vazifani bajaradi?",
                "answer": "Bo‘sh joy qo‘yish",
                "variant": ["Bo‘sh joy qo‘yish", "O‘chirish", "Nusxa olish", "Kiritish"]
            },
            {
                "question": "O‘zbekistonning eng katta cho‘li?",
                "answer": "Qizilqum",
                "variant": ["Qizilqum", "Karakum", "Sahroi Kabir", "Gobi"]
            },
            {
                "question": "Qaysi davlatda eng ko‘p vulqonlar mavjud?",
                "answer": "Indoneziya",
                "variant": ["Indoneziya", "Yaponiya", "Italiya", "Rossiya"]
            },
            {
                "question": "O‘zbek milliy ertak qahramonlaridan biri?",
                "answer": "Zumrad va Qimmat",
                "variant": ["Zumrad va Qimmat", "Shrek", "Aladin", "Cinderella"]
            },
            {
                "question": "Shaharlarda odam tashuvchi asosiy transport vositasi?",
                "answer": "Avtobus",
                "variant": ["Avtobus", "Samolyot", "Poyezd", "Tramvay"]
            },
            {
                "question": "Qaysi davlatning poytaxti Vashington?",
                "answer": "AQSh",
                "variant": ["AQSh", "Kanada", "Meksika", "Braziliya"]
            },
            {
                "question": "Kompyuter monitorida tasvir hosil qiluvchi nuqta nima deb ataladi?",
                "answer": "Piksel",
                "variant": ["Piksel", "Bayt", "Kadr", "Bit"]
            },
            {
                "question": "Mashhur bastakor Motsart qaysi davlatda tug‘ilgan?",
                "answer": "Avstriya",
                "variant": ["Avstriya", "Germaniya", "Fransiya", "Italiya"]
            },
            {
                "question": "Dunyodagi eng baland binolardan biri - 'Taipei 101' qayerda joylashgan?",
                "answer": "Tayvan",
                "variant": ["Tayvan", "Xitoy", "Singapur", "Malayziya"]
            },
            {
                "question": "Afrikaning eng uzun daryosi?",
                "answer": "Nil",
                "variant": ["Nil", "Niger", "Kongo", "Zambezi"]
            },
            {
                "question": "Dunyodagi eng sovuq shahar?",
                "answer": "Oymyakon",
                "variant": ["Oymyakon", "Moskva", "Oslo", "Reykyavik"]
            },
            {
                "question": "Insoniyat tarixidagi birinchi yozuv qaysi?",
                "answer": "Mixxat",
                "variant": ["Mixxat", "Lotin alifbosi", "Kirill alifbosi", "Arab yozuvi"]
            },
            {
                "question": "Dunyodagi eng katta metall ishlab chiqaruvchi kompaniya?",
                "answer": "ArcelorMittal",
                "variant": ["ArcelorMittal", "General Motors", "Samsung", "Apple"]
            },
            {
                "question": "Mashhur multfilm qahramoni Mickey Mouse qaysi studiyaga tegishli?",
                "answer": "Disney",
                "variant": ["Disney", "Pixar", "Marvel", "DreamWorks"]
            },
            {
                "question": "Dunyodagi eng baland daraxt qayerda o‘sadi?",
                "answer": "Kaliforniya",
                "variant": ["Kaliforniya", "Amazonka", "Kanada", "Avstraliya"]
            },
            {
                "question": "O‘zbekistonda qaysi sport turi juda mashhur?",
                "answer": "Kurash",
                "variant": ["Kurash", "Boks", "Shaxmat", "Futbol"]
            },
            {
                "question": "Yer yuzida eng ko‘p tarqalgan tilda so‘zlashuvchilar?",
                "answer": "Xitoy tili",
                "variant": ["Xitoy tili", "Ingliz tili", "Ispan tili", "Hind tili"]
            },
            {
                "question": "Insoniyat tarixidagi birinchi yozma kitob?",
                "answer": "Avesto",
                "variant": ["Avesto", "Injil", "Qur’on", "Torah"]
            },
            {
                "question": "O‘zbekistonning eng issiq shahri?",
                "answer": "Termiz",
                "variant": ["Termiz", "Nukus", "Xiva", "Urganch"]
            },
            {
                "question": "Mashhur futbolchi Ronaldoning vatani?",
                "answer": "Portugaliya",
                "variant": ["Portugaliya", "Braziliya", "Ispaniya", "Argentina"]
            },
            {
                "question": "Eng mashhur yunon matematigi?",
                "answer": "Pifagor",
                "variant": ["Pifagor", "Evklid", "Arximed", "Tales"]
            },
            {
                "question": "O‘zbek milliy kuylaridan biri?",
                "answer": "Tanovar",
                "variant": ["Tanovar", "Segoh", "Munojot", "Rast"]
            },
            {
                "question": "Yer kurrasidagi eng katta yarim shar qaysi?",
                "answer": "Shimoliy yarim shar",
                "variant": ["Shimoliy yarim shar", "Janubiy yarim shar", "Sharqiy yarim shar", "G‘arbiy yarim shar"]
            },
            {
                "question": "Qaysi shaharni 'Shamollar shahri' deb atashadi?",
                "answer": "Chicago",
                "variant": ["Chicago", "Nyu-York", "London", "Tokio"]
            },
            {
                "question": "Qaysi hayvon sut beruvchi hayvon emas?",
                "answer": "To‘tiqush",
                "variant": ["To‘tiqush", "Sigir", "Ot", "Qo‘y"]
            },
            {
                "question": "Qaysi davlatda 'Kreml' joylashgan?",
                "answer": "Rossiya",
                "variant": ["Rossiya", "Xitoy", "Fransiya", "Germaniya"]
            },
            {
                "question": "O‘zbekistonda eng mashhur milliy o‘yinlardan biri?",
                "answer": "Ko‘pkari",
                "variant": ["Ko‘pkari", "Shaxmat", "Tennis", "Futbol"]
            },
            {
                "question": "O‘zbekistonning milliy sport turi qaysi?",
                "answer": "Kurash",
                "variant": ["Kurash", "Boks", "Futbol", "Basketbol"]
            },
            {
                "question": "Qaysi hayvon uchib yuradi?",
                "answer": "Qush",
                "variant": ["Qush", "Ot", "Sigir", "Ilon"]
            },
            {
                "question": "Yer sharida nechta qutb bor?",
                "answer": "2",
                "variant": ["2", "3", "4", "1"]
            },
            {
                "question": "O‘zbekistonning milliy musiqiy cholg‘ularidan biri?",
                "answer": "Doira",
                "variant": ["Gitara", "Doira", "Pianino", "Skripka"]
            },
            {
                "question": "Yerning sun’iy yo‘ldoshi nima deb ataladi?",
                "answer": "Sun’iy yo‘ldosh",
                "variant": ["Oy", "Sun’iy yo‘ldosh", "Quyosh", "Sayyora"]
            }
        ]

        quiz_3 = [
            {
                "question": "Toshkent metrosi nechanchi yilda ochilgan?",
                "answer": "1977",
                "variant": ["1980", "1977", "1991", "1965"]
            },
            {
                "question": "Dunyoning eng katta qushi?",
                "answer": "Tuyoqqush",
                "variant": ["Qaldirg‘och", "Tuyoqqush", "Lochin", "Kabutar"]
            },
            {
                "question": "O‘zbekistonda qaysi shahar 'Go‘zal Buxoro' deb ataladi?",
                "answer": "Buxoro",
                "variant": ["Buxoro", "Xiva", "Samarqand", "Toshkent"]
            },
            {
                "question": "Eng mashhur futbolchilar o‘yinini o‘tkazadigan maydon?",
                "answer": "Stadion",
                "variant": ["Teatr", "Stadion", "Ko‘cha", "Zal"]
            },
            {
                "question": "Yer sharidagi eng katta hayvon?",
                "answer": "Ko‘k kit",
                "variant": ["Ko‘k kit", "Fil", "Akula", "Ot"]
            },
            {
                "question": "O‘zbekistonda qaysi shahar 'ko‘hna shahar' deb ataladi?",
                "answer": "Samarqand",
                "variant": ["Andijon", "Samarqand", "Qo‘qon", "Namangan"]
            },
            {
                "question": "Dunyodagi eng mashhur minoralardan biri — Big Ben qayerda joylashgan?",
                "answer": "London",
                "variant": ["Parij", "Berlin", "London", "Nyu-York"]
            },
            {
                "question": "O‘zbekistonning milliy raqsi?",
                "answer": "Lazgi",
                "variant": ["Vals", "Lazgi", "Sirtaki", "Samba"]
            },
            {
                "question": "Qaysi davlatda eng ko‘p kangurular yashaydi?",
                "answer": "Avstraliya",
                "variant": ["Avstraliya", "Afrika", "Hindiston", "Braziliya"]
            },
            {
                "question": "O‘zbekistonda qaysi viloyat 'paxtasi' bilan mashhur?",
                "answer": "Farg‘ona",
                "variant": ["Surxondaryo", "Farg‘ona", "Xorazm", "Jizzax"]
            },
            {
                "question": "O‘zbekistonning eng mashhur tarixiy obidalaridan biri — Minorai Kalon qayerda?",
                "answer": "Buxoro",
                "variant": ["Xiva", "Buxoro", "Samarqand", "Shahrisabz"]
            },
            {
                "question": "Kompyuterni boshqarish uchun ishlatiladigan qurilma?",
                "answer": "Sichqoncha",
                "variant": ["Mikrofon", "Sichqoncha", "Printer", "Kamera"]
            },
            {
                "question": "O‘zbekistonning milliy gullaridan biri?",
                "answer": "Lola",
                "variant": ["Atirgul", "Lola", "Chinnigul", "Nargis"]
            },
            {
                "question": "Telefonni kim ixtiro qilgan?",
                "answer": "Aleksandr Bell",
                "variant": ["Tomas Edison", "Aleksandr Bell", "Nyuton", "Einshteyn"]
            },
            {
                "question": "O‘zbekistonda qaysi shahar 'me’morlar shahri' deb ataladi?",
                "answer": "Shahrisabz",
                "variant": ["Shahrisabz", "Samarqand", "Buxoro", "Toshkent"]
            },
            {
                "question": "Dunyoning eng chuqur ko‘li?",
                "answer": "Baykal",
                "variant": ["Baykal", "Kaspiy", "Viktoriya", "Aydarko‘l"]
            },
            {
                "question": "O‘zbekiston milliy valyutasi qachon muomalaga kiritilgan?",
                "answer": "1994-yil",
                "variant": ["1991-yil", "1992-yil", "1994-yil", "1996-yil"]
            },
            {
                "question": "Samolyot uchuvchi joyi nima deb ataladi?",
                "answer": "Kabina",
                "variant": ["Kabina", "Salon", "Bagaj joyi", "Kokpit"]
            },
            {
                "question": "O‘zbekiston hududidagi eng katta cho‘l?",
                "answer": "Qizilqum",
                "variant": ["Qizilqum", "Karakum", "Gobi", "Sahroi Kabir"]
            },
            {
                "question": "Dunyoda eng ko‘p gaplashiladigan til?",
                "answer": "Xitoy tili",
                "variant": ["Ingliz tili", "Rus tili", "Xitoy tili", "Ispan tili"]
            },
            {
                "question": "O‘zbekistonda mashhur nonushta taomi?",
                "answer": "Somsa",
                "variant": ["Somsa", "Pizza", "Burger", "Norin"]
            },
            {
                "question": "Dunyodagi eng uzun daryo?",
                "answer": "Nil",
                "variant": ["Nil", "Amazonka", "Volga", "Ganga"]
            },
            {
                "question": "Dunyodagi eng mashhur muzlik qaysi qit’ada joylashgan?",
                "answer": "Antarktida",
                "variant": ["Antarktida", "Osiyo", "Shimoliy Amerika", "Afrika"]
            },
            {
                "question": "O‘zbekiston davlat madhiyasi qachon qabul qilingan?",
                "answer": "1992-yil",
                "variant": ["1991-yil", "1992-yil", "1993-yil", "1994-yil"]
            },
            {
                "question": "Qaysi sport turida sariq to‘p ishlatiladi?",
                "answer": "Tennis",
                "variant": ["Tennis", "Futbol", "Basketbol", "Bilyard"]
            },
            {
                "question": "O‘zbekistonning eng katta tog‘ tizmalari?",
                "answer": "Tyan-Shan",
                "variant": ["Tyan-Shan", "Pamir", "Altay", "Kavkaz"]
            },
            {
                "question": "Dunyodagi eng mashhur devor?",
                "answer": "Xitoy devori",
                "variant": ["Xitoy devori", "Berlin devori", "Hadrian devori", "Bobil devori"]
            },
            {
                "question": "O‘zbekistonda qadimiy qal’alar ko‘p bo‘lgan hudud?",
                "answer": "Ellikqal’a",
                "variant": ["Ellikqal’a", "Farg‘ona", "Samarqand", "Andijon"]
            },
            {
                "question": "Dunyodagi eng katta kitobxona qayerda joylashgan?",
                "answer": "AQSh",
                "variant": ["Rossiya", "Angliya", "AQSh", "Fransiya"]
            },
            {
                "question": "O‘zbekistonda qaysi viloyat 'mevasi' bilan mashhur?",
                "answer": "Farg‘ona",
                "variant": ["Farg‘ona", "Navoiy", "Jizzax", "Xorazm"]
            },
            {
                "question": "Dunyoning eng baland tog‘i?",
                "answer": "Everest",
                "variant": ["Everest", "Elbrus", "Kilimanjaro", "Montblan"]
            },
            {
                "question": "O‘zbekistonning eng mashhur xalq ertak qahramonlaridan biri?",
                "answer": "Afandi",
                "variant": ["Afandi", "Alpomish", "Rustam", "Qorako‘z"]
            },
            {
                "question": "Dunyodagi eng yirik davlat maydon bo‘yicha?",
                "answer": "Rossiya",
                "variant": ["Rossiya", "Xitoy", "AQSh", "Kanada"]
            },
            {
                "question": "O‘zbekistonning eng baland cho‘qqisi?",
                "answer": "Hazrati Sulton",
                "variant": ["Hazrati Sulton", "Chimyon", "Somoni cho‘qqisi", "Bobotog‘"]
            },
            {
                "question": "Dunyodagi eng mashhur minoralardan biri — Pisa minorasi qayerda?",
                "answer": "Italiya",
                "variant": ["Italiya", "Ispaniya", "Gretsiya", "Fransiya"]
            },
            {
                "question": "O‘zbekistonning milliy ichimliklaridan biri?",
                "answer": "Choy",
                "variant": ["Sharbat", "Choy", "Qahva", "Sut"]
            },
            {
                "question": "Dunyodagi eng tez yuguradigan hayvon?",
                "answer": "Gepard",
                "variant": ["Gepard", "Ot", "Arslon", "Tulki"]
            },
            {
                "question": "O‘zbekistonning eng mashhur shaharlaridan biri — Xiva qayerda joylashgan?",
                "answer": "Xorazm",
                "variant": ["Buxoro", "Xorazm", "Samarqand", "Qashqadaryo"]
            },
            {
                "question": "Dunyoning eng katta okeani?",
                "answer": "Tinch okeani",
                "variant": ["Tinch okeani", "Atlantika", "Hind okeani", "Shimoliy muz okeani"]
            },
            {
                "question": "O‘zbekiston milliy kiyimlaridan biri?",
                "answer": "Chopon",
                "variant": ["Chopon", "Futbolka", "Palto", "Jinsi"]
            },
            {
                "question": "Dunyodagi eng ko‘p ishlatiladigan transport vositasi?",
                "answer": "Avtomobil",
                "variant": ["Avtomobil", "Samolyot", "Kema", "Velosiped"]
            },
            {
                "question": "O‘zbekistonning mashhur shoirlaridan biri?",
                "answer": "Erkin Vohidov",
                "variant": ["Erkin Vohidov", "Pushkin", "Gyote", "Navoiy"]
            },
            {
                "question": "O‘zbekistonning eng yirik suv ombori?",
                "answer": "Chorvoq",
                "variant": ["Chorvoq", "Tuyamo‘yin", "Qoratepa", "Andijon"]
            },
            {
                "question": "Dunyodagi eng mashhur hayvonlardan biri — Panda qaysi davlatda yashaydi?",
                "answer": "Xitoy",
                "variant": ["Hindiston", "Xitoy", "Nepal", "Mongoliya"]
            },
            {
                "question": "O‘zbekistonda mashhur hunarmandchilik markazi bo‘lgan shahar?",
                "answer": "Rishton",
                "variant": ["Shahrisabz", "Rishton", "Qo‘qon", "Buxoro"]
            },
            {
                "question": "Dunyodagi eng baland daraxtlar qaysi turga mansub?",
                "answer": "Sekvoyalar",
                "variant": ["Sekvoyalar", "Yong‘oq", "Qayrag‘och", "Tol"]
            },
            {
                "question": "O‘zbekistonning janubiy qo‘shni davlati?",
                "answer": "Afg‘oniston",
                "variant": ["Tojikiston", "Afg‘oniston", "Turkmaniston", "Eron"]
            },
            {
                "question": "Dunyodagi eng mashhur hayvon — Mickey Mouse qaysi kompaniya qahramoni?",
                "answer": "Disney",
                "variant": ["Marvel", "Disney", "Pixar", "DreamWorks"]
            },
            {
                "question": "O‘zbekistonda mashhur bozor — Chorsu qayerda joylashgan?",
                "answer": "Toshkent",
                "variant": ["Toshkent", "Andijon", "Samarqand", "Xiva"]
            },
            {
                "question": "Dunyodagi eng mashhur sport musobaqasi?",
                "answer": "Olimpiada",
                "variant": ["Olimpiada", "Futbol jahon chempionati", "Regbi kubogi", "Tennis US Open"]
            },
            {
                "question": "O‘zbekistonning eng mashhur qadimiy obidalaridan biri — Ark qayerda?",
                "answer": "Buxoro",
                "variant": ["Xiva", "Buxoro", "Samarqand", "Termiz"]
            },
            {
                "question": "Dunyodagi eng mashhur avtomobil kompaniyalaridan biri?",
                "answer": "Toyota",
                "variant": ["Toyota", "Mercedes", "Tesla", "BMW"]
            },
            {
                "question": "O‘zbekistonda mashhur milliy shirinliklardan biri?",
                "answer": "Halva",
                "variant": ["Halva", "Shokolad", "Tort", "Keks"]
            },
            {
                "question": "Dunyodagi eng mashhur sportchilaridan biri — Lionel Messi qaysi sport turida mashhur?",
                "answer": "Futbol",
                "variant": ["Futbol", "Basketbol", "Boks", "Tennis"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Amir Temur qaysi shaharda tug‘ilgan?",
                "answer": "Shahrisabz",
                "variant": ["Shahrisabz", "Samarqand", "Buxoro", "Xiva"]
            },
            {
                "question": "Dunyodagi eng mashhur ichimliklardan biri?",
                "answer": "Choy",
                "variant": ["Choy", "Qahva", "Sharbat", "Sut"]
            },
            {
                "question": "O‘zbekistonning mashhur olimlaridan biri?",
                "answer": "Al-Farg‘oniy",
                "variant": ["Al-Farg‘oniy", "Beruniy", "Ibn Sino", "Xorazmiy"]
            },
            {
                "question": "Dunyodagi eng mashhur qasrlardan biri — Versal qayerda?",
                "answer": "Fransiya",
                "variant": ["Fransiya", "Germaniya", "Italiya", "Ispaniya"]
            },
            {
                "question": "O‘zbekistonda mashhur milliy liboslardan biri?",
                "answer": "Atlas",
                "variant": ["Atlas", "Kimono", "Kurtka", "Palto"]
            },
            {
                "question": "Dunyodagi eng mashhur fastfud taomi?",
                "answer": "Burger",
                "variant": ["Burger", "Somsa", "Pizza", "Hot-dog"]
            },
            {
                "question": "O‘zbekistonda mashhur ko‘llardan biri?",
                "answer": "Aydarko‘l",
                "variant": ["Aydarko‘l", "Qorako‘l", "Sarezko‘l", "Tuzko‘l"]
            },
            {
                "question": "Dunyodagi eng mashhur telefon markalaridan biri?",
                "answer": "Apple",
                "variant": ["Apple", "Samsung", "Nokia", "Huawei"]
            },
            {
                "question": "O‘zbekiston hududida qadimiy qal’alardan biri — Topraqqal’a qayerda?",
                "answer": "Qoraqalpog‘iston",
                "variant": ["Qoraqalpog‘iston", "Buxoro", "Samarqand", "Surxondaryo"]
            },
            {
                "question": "Dunyodagi eng mashhur futbol klublaridan biri?",
                "answer": "Real Madrid",
                "variant": ["Real Madrid", "Barcelona", "Milan", "Manchester United"]
            },
            {
                "question": "O‘zbekistonning mashhur milliy ashulachisi?",
                "answer": "Yulduz Usmonova",
                "variant": ["Yulduz Usmonova", "Sevara Nazarkhan", "Ozodbek Nazarbekov", "Botir Zokirov"]
            },
            {
                "question": "Dunyodagi eng mashhur tog‘?",
                "answer": "Everest",
                "variant": ["Kilimanjaro", "Everest", "Elbrus", "Montblan"]
            },
            {
                "question": "O‘zbekistonning mashhur milliy taomlaridan biri?",
                "answer": "Norin",
                "variant": ["Norin", "Palov", "Somsa", "Lag‘mon"]
            },
            {
                "question": "Dunyodagi eng mashhur kinoteatrlardan biri — Hollywood qayerda?",
                "answer": "AQSh",
                "variant": ["AQSh", "Angliya", "Fransiya", "Italiya"]
            },
            {
                "question": "O‘zbekistonda mashhur milliy o‘yinlardan biri?",
                "answer": "Ko‘pkari",
                "variant": ["Ko‘pkari", "Shaxmat", "Basketbol", "futbol"]
            },
            {
                "question": "Dunyodagi eng mashhur ko‘rfaz?",
                "answer": "Bengal",
                "variant": ["Meksika", "Bengal", "Pers", "Aden"]
            },
            {
                "question": "O‘zbekistonning mashhur shaharlaridan biri — Qo‘qon qaysi viloyatda?",
                "answer": "Farg‘ona",
                "variant": ["Farg‘ona", "Andijon", "Namangan", "Toshkent"]
            },
            {
                "question": "Dunyodagi eng mashhur qasrlardan biri — Kreml qayerda?",
                "answer": "Moskva",
                "variant": ["Berlin", "Moskva", "Parij", "Pekin"]
            },
            {
                "question": "O‘zbekistonning mashhur milliy cholg‘u asbobi?",
                "answer": "G‘ijjak",
                "variant": ["G‘ijjak", "Skripka", "Pianino", "Gitara"]
            },
            {
                "question": "Dunyodagi eng mashhur muzliklardan biri?",
                "answer": "Grenlandiya",
                "variant": ["Grenlandiya", "Antarktida", "Alp", "And"]
            },
            {
                "question": "Dunyodagi eng mashhur teatrlaridan biri — Bolshoy teatri qayerda?",
                "answer": "Moskva",
                "variant": ["Moskva", "London", "Parij", "Berlin"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri?",
                "answer": "Abdulla Qahhor",
                "variant": ["Abdulla Qahhor", "Cho‘lpon", "Oybek", "Pirimqul Qodirov"]
            },
            {
                "question": "Dunyodagi eng mashhur muzeylardan biri — Luvr qayerda?",
                "answer": "Parij",
                "variant": ["London", "Parij", "Berlin", "Madrid"]
            },
            {
                "question": "O‘zbekistonning mashhur qo‘shiqchilaridan biri?",
                "answer": "Ozodbek Nazarbekov",
                "variant": ["Ozodbek Nazarbekov", "Yulduz Usmonova", "Botir Zokirov", "Munojot Yo‘lchiyeva"]
            },
            {
                "question": "Dunyodagi eng mashhur poyga musobaqasi?",
                "answer": "Formula 1",
                "variant": ["Formula 1", "Moto GP", "Rally Dakar", "IndyCar"]
            },
            {
                "question": "O‘zbekistonning mashhur milliy kiyimlaridan biri?",
                "answer": "Do‘ppi",
                "variant": ["Do‘ppi", "Kimono", "Sharf", "Jinsi"]
            },
            {
                "question": "Dunyodagi eng mashhur stadionlardan biri — Kamp Nou qayerda?",
                "answer": "Barselona",
                "variant": ["Barselona", "Madrid", "London", "Rim"]
            },
            {
                "question": "O‘zbekistonning mashhur milliy raqslaridan biri?",
                "answer": "Tanovar",
                "variant": ["Tanovar", "Vals", "Sirtaki", "Rumba"]
            },
            {
                "question": "Dunyodagi eng mashhur futbolchilaridan biri — Cristiano Ronaldo qaysi davlatdan?",
                "answer": "Portugaliya",
                "variant": ["Portugaliya", "Ispaniya", "Braziliya", "Italiya"]
            },
            {
                "question": "Dunyodagi eng mashhur minoralardan biri — CN Tower qayerda?",
                "answer": "Kanada",
                "variant": ["AQSh", "Kanada", "Fransiya", "Angliya"]
            },
            {
                "question": "Qarshi shahar qaysi viloyat markazi?",
                "answer": "Qashqadaryo",
                "variant": ["Qashqadaryo", "Buxoro", "Jizzax", "Namangan"]
            },
            {
                "question": "Dunyodagi eng mashhur muzlatilgan qahva nomi?",
                "answer": "Frappe",
                "variant": ["Frappe", "Latte", "Amerikano", "Espresso"]
            },
            {
                "question": "O‘zbekistonning shimoliy viloyatlaridan biri?",
                "answer": "Qoraqalpog‘iston",
                "variant": ["Qoraqalpog‘iston", "Samarqand", "Buxoro", "Andijon"]
            },
            {
                "question": "Dunyodagi eng mashhur telefon ixtirochisi kim?",
                "answer": "Aleksandr Bell",
                "variant": ["Nikola Tesla", "Tomas Edison", "Aleksandr Bell", "Nyuton"]
            },
            {
                "question": "O‘zbekiston milliy sport turi?",
                "answer": "Kurash",
                "variant": ["Kurash", "Futbol", "Basketbol", "Shaxmat"]
            },
            {
                "question": "Dunyodagi eng mashhur minoralardan biri — Eiffel minorasi qaysi shaharda?",
                "answer": "Parij",
                "variant": ["London", "Berlin", "Parij", "Rim"]
            },
            {
                "question": "O‘zbekiston milliy libosida bosh kiyim qanday ataladi?",
                "answer": "Do‘ppi",
                "variant": ["Sharf", "Do‘ppi", "Kalpak", "Shlyapa"]
            },
            {
                "question": "Dunyoning eng mashhur futbol musobaqasi?",
                "answer": "Jahon chempionati",
                "variant": ["Jahon chempionati", "Olimpiada", "Yevropa Ligasi", "Osiyo Kubogi"]
            },
            {
                "question": "O‘zbekiston hududidagi eng mashhur suv omborlaridan biri — Chorvoq qaysi viloyatda joylashgan?",
                "answer": "Toshkent viloyati",
                "variant": ["Toshkent viloyati", "Namangan viloyati", "Andijon viloyati", "Samarqand viloyati"]
            },
            {
                "question": "Dunyoning eng katta yarim oroli?",
                "answer": "Arabiston yarim oroli",
                "variant": ["Arabiston yarim oroli", "Iberiya", "Skandinaviya", "Hindiston yarim oroli"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan qadimiy madrasalardan biri — Ko‘kaldosh qayerda joylashgan?",
                "answer": "Toshkent",
                "variant": ["Toshkent", "Buxoro", "Xiva", "Samarqand"]
            },
            {
                "question": "Dunyoning eng uzun qirg‘oq chizig‘iga ega davlat?",
                "answer": "Kanada",
                "variant": ["Kanada", "Rossiya", "Avstraliya", "AQSh"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaharlaridan biri — Shahrisabz qaysi vohada joylashgan?",
                "answer": "Qashqadaryo vohasi",
                "variant": ["Qashqadaryo vohasi", "Surxondaryo vohasi", "Zarafshon vohasi", "Farg‘ona vohasi"]
            },
            {
                "question": "Dunyoning eng katta muzliklari qaysi hududda joylashgan?",
                "answer": "Antarktida",
                "variant": ["Antarktida", "Grenlandiya", "Shimoliy qutb", "Islandiya"]
            },
            {
                "question": "Buyuk astronom Galiley qanday ixtirosi bilan mashhur?",
                "answer": "Teleskopni takomillashtirish",
                "variant": ["Teleskopni takomillashtirish", "Kompasni ixtiro qilish", "Bug‘ mashinasi", "Telefon"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Pirimqul Qodirov mashhur asari?",
                "answer": "Avlodlar dovoni",
                "variant": ["Avlodlar dovoni", "Yulduzli tunlar", "Sarob", "O‘tkan kunlar"]
            }
        ]

        quiz_4 = [
            {
                "question": "O‘zbekiston hududidagi mashhur maqbaralardan biri — Ismoil Somoniy maqbarasi qayerda?",
                "answer": "Buxoro",
                "variant": ["Buxoro", "Samarqand", "Xiva", "Andijon"]
            },
            {
                "question": "Buyuk yozuvchi Abdulla Qodiriy mashhur asarlaridan biri?",
                "answer": "O‘tkan kunlar",
                "variant": ["O‘tkan kunlar", "Mehrobdan chayon", "Sarob", "Yulduzli tunlar"]
            },
            {
                "question": "Yevropadagi eng mashhur futbol klublaridan biri — Real Madrid qaysi davlatda?",
                "answer": "Ispaniya",
                "variant": ["Ispaniya", "Italiya", "Fransiya", "Angliya"]
            },
            {
                "question": "O‘zbekiston hududidagi eng katta ko‘l?",
                "answer": "Aral dengizi",
                "variant": ["Aral dengizi", "Aydarko‘l", "Sarezko‘l", "Tuzko‘l"]
            },
            {
                "question": "Dunyoning eng baland hayvonlaridan biri?",
                "answer": "Jirafa",
                "variant": ["Jirafa", "Fil", "Gepard", "Arslon"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Jaloliddin Manguberdi qaysi asrda yashagan?",
                "answer": "XIII asr",
                "variant": ["XIII asr", "XI asr", "XIV asr", "XV asr"]
            },
            {
                "question": "Dunyoning eng katta arxipelaglari qayerda joylashgan?",
                "answer": "Janubi-Sharqiy Osiyo",
                "variant": ["Janubi-Sharqiy Osiyo", "Shimoliy Amerika", "Afrika", "Yevropa"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan mashhur yodgorlik — Guri Amir maqbarasi kimga bag‘ishlangan?",
                "answer": "Amir Temur",
                "variant": ["Amir Temur", "Ulug‘bek", "Alisher Navoiy", "Ibn Sino"]
            },
            {
                "question": "Dunyodagi eng chuqur okean?",
                "answer": "Tinch okeani",
                "variant": ["Tinch okeani", "Atlantika okeani", "Hind okeani", "Shimoliy muz okeani"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Abdulla Qodiriy qaysi davr adibi?",
                "answer": "XX asr boshlarida",
                "variant": ["XX asr boshlarida", "XV asrda", "XVIII asrda", "XIX asrda"]
            },
            {
                "question": "Eng qadimgi yozuvlardan biri — mixxat qayerda paydo bo‘lgan?",
                "answer": "Shumer",
                "variant": ["Shumer", "Misr", "Xitoy", "Hindiston"]
            },
            {
                "question": "O‘zbekistonning milliy o‘yinlaridan biri?",
                "answer": "Ko‘pkari",
                "variant": ["Ko‘pkari", "Futbol", "Shaxmat", "Basketbol"]
            },
            {
                "question": "Dunyoning eng mashhur san’at muzeylaridan biri — Prado qayerda joylashgan?",
                "answer": "Madrid",
                "variant": ["Madrid", "Parij", "Berlin", "Rim"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur tarixiy obidalaridan biri — Minorai Jam qayerda joylashgan?",
                "answer": "Afg‘oniston bilan chegarada",
                "variant": ["Afg‘oniston bilan chegarada", "Buxoro", "Samarqand", "Xorazm"]
            },
            {
                "question": "Dunyoning eng baland tog‘ dovonlaridan biri?",
                "answer": "Torong-La",
                "variant": ["Torong-La", "Elbrus", "Altay", "Ural"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Alisher Navoiy qaysi asrda yashagan?",
                "answer": "XV asr",
                "variant": ["XV asr", "XVI asr", "XIV asr", "XIII asr"]
            },
            {
                "question": "Dunyoning eng katta ichki daryosiz hududi qayerda joylashgan?",
                "answer": "Mongoliya",
                "variant": ["Mongoliya", "Liviya", "Avstraliya", "Kanada"]
            },
            {
                "question": "Quyoshdan eng uzoq joylashgan sayyora qaysi?",
                "answer": "Neptun",
                "variant": ["Yupiter", "Uran", "Neptun", "Saturn"]
            },
            {
                "question": "Buyuk Britaniyaning rasmiy valyutasi?",
                "answer": "Funt sterling",
                "variant": ["Funt sterling", "Yevro", "Dollar", "Frank"]
            },
            {
                "question": "O‘zbekistonda eng yirik gaz koni?",
                "answer": "Sho‘rtan",
                "variant": ["Sho‘rtan", "Muborak", "Qandim", "Gazli"]
            },
            {
                "question": "AQShning eng katta shtati maydon jihatdan?",
                "answer": "Alyaska",
                "variant": ["Texas", "Kaliforniya", "Alyaska", "Nevada"]
            },
            {
                "question": "Yerning qaysi qatlamida magma mavjud?",
                "answer": "Mantiya",
                "variant": ["Mantiya", "Qobiq", "Yadro", "Atmosfera"]
            },
            {
                "question": "Qaysi davlatni 'Tuliplar mamlakati' deb atashadi?",
                "answer": "Niderlandiya",
                "variant": ["Belgiya", "Niderlandiya", "Daniya", "Avstriya"]
            },
            {
                "question": "O‘zbekiston Konstitutsiyasi nechta bobdan iborat?",
                "answer": "6",
                "variant": ["6", "7", "5", "8"]
            },
            {
                "question": "O‘zbekistonda eng yirik issiqlik elektr stansiyasi?",
                "answer": "Talimarjon IES",
                "variant": ["Talimarjon IES", "Sirdaryo IES", "Novoangren IES", "Navoiy IES"]
            },
            {
                "question": "Qaysi olim 'harakatning uchinchi qonuni'ni kashf qilgan?",
                "answer": "Nyuton",
                "variant": ["Nyuton", "Galiley", "Arximed", "Paskal"]
            },
            {
                "question": "O‘zbekistonda eng yirik toshko‘mir koni?",
                "answer": "Sharg‘un",
                "variant": ["Sharg‘un", "Angren", "Boysun", "Baysun"]
            },
            {
                "question": "Dunyoning eng chuqur okean joyi?",
                "answer": "Mariana chuqurligi",
                "variant": ["Mariana chuqurligi", "Filippin chuqurligi", "Tonga chuqurligi", "Puerto-Riko chuqurligi"]
            },
            {
                "question": "Yer yuzida eng ko‘p maydonni egallagan davlat?",
                "answer": "Rossiya",
                "variant": ["Kanada", "AQSh", "Rossiya", "Xitoy"]
            },
            {
                "question": "O‘zbekistondagi eng uzun kanal?",
                "answer": "Amu-Buxoro",
                "variant": ["Amu-Buxoro", "Amu-Qorako‘l", "Amu-Zang", "Qizilqum kanali"]
            },
            {
                "question": "Qaysi yulduz 'qutb yulduzi' deb ataladi?",
                "answer": "Polaris",
                "variant": ["Sirius", "Polaris", "Vega", "Antares"]
            },
            {
                "question": "Qaysi metall 'eng yengil metall' hisoblanadi?",
                "answer": "Litiy",
                "variant": ["Litiy", "Natriy", "Alyuminiy", "Berilliy"]
            },
            {
                "question": "O‘zbekistonda eng ko‘p koni mavjud bo‘lgan foydali qazilma?",
                "answer": "Oltin",
                "variant": ["Oltin", "Gaz", "Ko‘mir", "Mis"]
            },
            {
                "question": "Qadimgi Bobil minorasi qayerda joylashgan edi?",
                "answer": "Mesopotamiya",
                "variant": ["Misr", "Mesopotamiya", "Gretsiya", "Hindiston"]
            },
            {
                "question": "Yer yuzida eng katta yarim orol?",
                "answer": "Arabiston",
                "variant": ["Arabiston", "Skandinaviya", "Iberiya", "Hindiston"]
            },
            {
                "question": "Qaysi davlatning poytaxti Ottava?",
                "answer": "Kanada",
                "variant": ["Kanada", "Avstraliya", "AQSh", "Meksika"]
            },
            {
                "question": "O‘zbekiston mustaqillik ramzi sifatida nechta yulduz bayroqda tasvirlangan?",
                "answer": "12",
                "variant": ["12", "14", "10", "16"]
            },
            {
                "question": "Buyuk geografik kashfiyotlar davrida Hindistonga dengiz yo‘lini kim topgan?",
                "answer": "Vasko da Gama",
                "variant": ["Magellan", "Kolumb", "Vasko da Gama", "Diaz"]
            },
            {
                "question": "Quyosh tizimidagi eng issiq sayyora?",
                "answer": "Venera",
                "variant": ["Venera", "Mars", "Yupiter", "Merkuriy"]
            },
            {
                "question": "O‘zbekistonda eng katta daryo havzasi?",
                "answer": "Amudaryo",
                "variant": ["Sirdaryo", "Amudaryo", "Zarafshon", "Chirchiq"]
            },
            {
                "question": "AQShning birinchi Prezidenti kim?",
                "answer": "Jorj Vashington",
                "variant": ["Jorj Vashington", "Avraam Linkoln", "Tomas Jefferson", "Jeyms Madison"]
            },
            {
                "question": "Yerning eng yaqin yulduz qo‘shnisi?",
                "answer": "Proksima Kentavra",
                "variant": ["Sirius", "Proksima Kentavra", "Vega", "Betelgeyze"]
            },
            {
                "question": "Qaysi yozuvchi 'Urush va tinchlik' romanini yozgan?",
                "answer": "Lev Tolstoy",
                "variant": ["Lev Tolstoy", "Dostoyevskiy", "Pushkin", "Lermontov"]
            },
            {
                "question": "Qaysi dengiz eng sho‘r suvli hisoblanadi?",
                "answer": "O‘lik dengiz",
                "variant": ["O‘lik dengiz", "Qora dengiz", "Kaspiy dengizi", "Adriatika dengizi"]
            },
            {
                "question": "Yer yuzida eng katta ko‘rfaz?",
                "answer": "Bengal ko‘rfazi",
                "variant": ["Bengal ko‘rfazi", "Meksika ko‘rfazi", "Pers ko‘rfazi", "Aden ko‘rfazi"]
            },
            {
                "question": "O‘zbekiston hududidagi eng qadimiy universitet?",
                "answer": "Mirzo Ulug‘bek madrasasi",
                "variant": ["Mirzo Ulug‘bek madrasasi", "Registon madrasasi", "Ko‘kaldosh madrasasi", "Sherdor madrasasi"]
            },
            {
                "question": "Qaysi davlat 'osmon mamlakati' deb ataladi?",
                "answer": "Qirg‘iziston",
                "variant": ["Qirg‘iziston", "Mongoliya", "Nepal", "Tibet"]
            },
            {
                "question": "Qaysi hayvon tuxum qo‘yib, sut bilan boqadi?",
                "answer": "Utka (platypus)",
                "variant": ["Utka (platypus)", "Kenguru", "Tovuq", "Qush"]
            },
            {
                "question": "Qaysi olim nisbiylik nazariyasini yaratgan?",
                "answer": "Albert Eynshteyn",
                "variant": ["Albert Eynshteyn", "Nyuton", "Galiley", "Planck"]
            },
            {
                "question": "O‘zbekiston hududidan o‘tadigan eng yirik tog‘ tizmasi?",
                "answer": "Tyan-Shan",
                "variant": ["Tyan-Shan", "Gimolay", "Alp", "And"]
            },
            {
                "question": "Qaysi davlatda eng ko‘p vaqt mintaqalari mavjud?",
                "answer": "Rossiya",
                "variant": ["Rossiya", "Kanada", "AQSh", "Avstraliya"]
            },
            {
                "question": "Qaysi davlat poytaxti Anqara?",
                "answer": "Turkiya",
                "variant": ["Turkiya", "Eron", "Suriya", "Gretsiya"]
            },
            {
                "question": "Yer sharining eng chuqur ko‘li?",
                "answer": "Baykal",
                "variant": ["Baykal", "Tanganika", "Viktoriya", "Aral"]
            },
            {
                "question": "Sharq mutafakkiri Beruniy qaysi sohada mashhur?",
                "answer": "Astronomiya",
                "variant": ["Astronomiya", "Matematika", "Tibbiyot", "Adabiyot"]
            },
            {
                "question": "Qaysi davlat 'g‘o‘za mamlakati' deb ataladi?",
                "answer": "O‘zbekiston",
                "variant": ["O‘zbekiston", "AQSh", "Hindiston", "Braziliya"]
            },
            {
                "question": "Qaysi yevropa davlatida eng ko‘p orollar bor?",
                "answer": "Shvetsiya",
                "variant": ["Shvetsiya", "Norvegiya", "Gretsiya", "Italiya"]
            },
            {
                "question": "Quyoshdan keyin eng yorqin yulduz?",
                "answer": "Sirius",
                "variant": ["Sirius", "Vega", "Antares", "Proksima Kentavra"]
            },
            {
                "question": "Buyuk ipak yo‘li Yevropani qaysi qit’a bilan bog‘lagan?",
                "answer": "Osiyo",
                "variant": ["Osiyo", "Afrika", "Amerika", "Avstraliya"]
            },
            {
                "question": "Qaysi mamlakatda eng baland bino joylashgan?",
                "answer": "Birlashgan Arab Amirliklari",
                "variant": ["Birlashgan Arab Amirliklari", "AQSh", "Xitoy", "Saudiya Arabistoni"]
            },
            {
                "question": "O‘zbekiston qaysi davlat bilan eng uzun chegaraga ega?",
                "answer": "Qozog‘iston",
                "variant": ["Qozog‘iston", "Tojikiston", "Qirg‘iziston", "Turkmaniston"]
            },
            {
                "question": "Qaysi olim 'Tabiatshunoslik otasi' deb ataladi?",
                "answer": "Aristotel",
                "variant": ["Aristotel", "Platon", "Sokrat", "Pifagor"]
            },
            {
                "question": "Yerning eng issiq joyi qaysi cho‘l?",
                "answer": "Lut cho‘li",
                "variant": ["Lut cho‘li", "Sahroi Kabir", "Karakum", "Gobi"]
            },
            {
                "question": "Qaysi davlatning poytaxti Braziliya shahri?",
                "answer": "Braziliya",
                "variant": ["Argentina", "Braziliya", "Meksika", "Kolumbiya"]
            },
            {
                "question": "Dunyodagi eng katta arxipelag qaysi?",
                "answer": "Indoneziya",
                "variant": ["Filippin", "Indoneziya", "Maldiv", "Shvetsiya"]
            },
            {
                "question": "Markaziy Osiyoda eng katta maydonga ega davlat?",
                "answer": "Qozog‘iston",
                "variant": ["Qozog‘iston", "O‘zbekiston", "Turkmaniston", "Tojikiston"]
            },
            {
                "question": "Qaysi olimning qonunlari suyuqliklar mexanikasini tushuntiradi?",
                "answer": "Arximed",
                "variant": ["Nyuton", "Arximed", "Pascal", "Ohm"]
            },
            {
                "question": "O‘zbekiston Respublikasi davlat gerbida qaysi tog‘ tasvirlangan?",
                "answer": "Humo tog‘i emas, Hazrati Sulton",
                "variant": ["Hazrati Sulton", "Tyan-Shan", "Bobotog‘", "Chimyon"]
            },
            {
                "question": "Shimoliy Afrikadagi eng katta shahar?",
                "answer": "Qohira",
                "variant": ["Qohira", "Aljir", "Kasablanka", "Tunis"]
            },
            {
                "question": "Yevropa Ittifoqiga a’zo davlatlar soni?",
                "answer": "27",
                "variant": ["25", "27", "30", "28"]
            },
            {
                "question": "O‘zbekistonda eng ko‘p oltin qazib olinadigan joy?",
                "answer": "Muruntov",
                "variant": ["Muruntov", "Olmaliq", "Zarafshon", "Qizilqum"]
            },
            {
                "question": "Buyuk geografik kashfiyotlar davrida dunyoni birinchi bo‘lib aylanib chiqqan dengizchi?",
                "answer": "Magellan",
                "variant": ["Magellan", "Kolumb", "Vasko da Gama", "Hudson"]
            },
            {
                "question": "Yer kurrasida eng katta tekislik?",
                "answer": "Amazon tekisligi",
                "variant": ["Amazon tekisligi", "Sibir tekisligi", "Afrika tekisligi", "O‘zbekiston tekisligi"]
            },
            {
                "question": "Qaysi davlat 'Shamol tegirmonlari mamlakati' deb ataladi?",
                "answer": "Niderlandiya",
                "variant": ["Niderlandiya", "Daniya", "Norvegiya", "Belgiya"]
            },
            {
                "question": "Buyuk Ipak yo‘li O‘zbekistonning qaysi viloyati orqali Xitoyga chiqadi?",
                "answer": "Farg‘ona vodiysi",
                "variant": ["Farg‘ona vodiysi", "Qashqadaryo", "Xorazm", "Navoiy"]
            },
            {
                "question": "Dunyodagi eng uzun temir yo‘l magistrali?",
                "answer": "Transsibir magistrali",
                "variant": ["Transsibir magistrali", "Transamerika", "Transafrika", "Yevropa-Osiyo"]
            },
            {
                "question": "Buyuk rus shoiri Pushkin qaysi asar bilan mashhur?",
                "answer": "Yevgeniy Onegin",
                "variant": ["Yevgeniy Onegin", "Urush va tinchlik", "Qizil qalpoqcha", "Otello"]
            },
            {
                "question": "O‘zbekistonning eng yirik metallurgiya kombinati?",
                "answer": "Olmaliq KMK",
                "variant": ["Olmaliq KMK", "Navoiy KMK", "Angren KMK", "Talimarjon KMK"]
            },
            {
                "question": "Buyuk fransuz inqilobi qachon boshlangan?",
                "answer": "1789",
                "variant": ["1789", "1776", "1812", "1848"]
            },
            {
                "question": "Qaysi davlat 'Kengurular mamlakati' deb ataladi?",
                "answer": "Avstraliya",
                "variant": ["Avstraliya", "Yangi Zelandiya", "Janubiy Afrika", "Kanada"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan qadimiy astronomik rasadxonani kim qurgan?",
                "answer": "Mirzo Ulug‘bek",
                "variant": ["Mirzo Ulug‘bek", "Ibn Sino", "Beruniy", "Al-Xorazmiy"]
            },
            {
                "question": "Qaysi davlatning poytaxti Dushanbe?",
                "answer": "Tojikiston",
                "variant": ["Tojikiston", "Qirg‘iziston", "Afg‘oniston", "Turkmaniston"]
            },
            {
                "question": "Osiyo qit’asining janubi-g‘arbiy qismi qaysi nom bilan ataladi?",
                "answer": "Yaqin Sharq",
                "variant": ["Yaqin Sharq", "Markaziy Osiyo", "Uzoq Sharq", "Kavkaz"]
            },
            {
                "question": "Qaysi davlatda eng ko‘p musulmon aholi yashaydi?",
                "answer": "Indoneziya",
                "variant": ["Indoneziya", "Turkiya", "Hindiston", "Pokiston"]
            },
            {
                "question": "O‘zbekiston hududidagi eng katta suv ombori?",
                "answer": "Tuyamo‘yin",
                "variant": ["Tuyamo‘yin", "Chorvoq", "Qoratepa", "To‘dako‘l"]
            },
            {
                "question": "Qaysi davlatni 'Qadimiy sivilizatsiyalar vatani' deb atashadi?",
                "answer": "Misr",
                "variant": ["Misr", "Xitoy", "Hindiston", "Bobil"]
            },
            {
                "question": "Yer kurrasidagi eng baland plato?",
                "answer": "Tibet",
                "variant": ["Tibet", "Pamir", "And", "Altay"]
            },
            {
                "question": "Buyuk Aleksandr qaysi mamlakat hukmdori edi?",
                "answer": "Makedoniya",
                "variant": ["Makedoniya", "Rim", "Sparta", "Bobil"]
            },
            {
                "question": "O‘zbekistonda eng katta yog‘och ishlovchi kombinat qayerda joylashgan?",
                "answer": "Qo‘qon",
                "variant": ["Qo‘qon", "Andijon", "Namangan", "Buxoro"]
            },
            {
                "question": "Qaysi davlatning poytaxti Nayrobi?",
                "answer": "Keniya",
                "variant": ["Keniya", "Efiopiya", "Uganda", "Tanzaniya"]
            },
            {
                "question": "Shimoliy qutbni birinchi bo‘lib kim kashf qilgan?",
                "answer": "Robert Piri",
                "variant": ["Robert Piri", "Magellan", "Amundsen", "Kolumb"]
            },
            {
                "question": "Qaysi davlat 'Alp tog‘lari mamlakati' deb ataladi?",
                "answer": "Shveytsariya",
                "variant": ["Shveytsariya", "Avstriya", "Fransiya", "Italiya"]
            },
            {
                "question": "O‘zbekiston Respublikasida Prezident lavozimi nechchi yil muddatga saylanadi?",
                "answer": "7 yil",
                "variant": ["5 yil", "7 yil", "6 yil", "4 yil"]
            },
            {
                "question": "Qaysi davlatda Sahara cho‘li joylashgan?",
                "answer": "Jazoir",
                "variant": ["Jazoir", "Misr", "Sudan", "Liviya"]
            },
            {
                "question": "Buyuk astronom Galiley qanday asbobni takomillashtirgan?",
                "answer": "Teleskop",
                "variant": ["Teleskop", "Kompas", "Soat", "Termometr"]
            },
            {
                "question": "Qaysi davlatning rasmiy tili ispan tili emas?",
                "answer": "Braziliya",
                "variant": ["Braziliya", "Argentina", "Kolumbiya", "Meksika"]
            },
            {
                "question": "O‘zbekistonning eng katta tabiiy gaz eksportchisi bo‘lgan davri?",
                "answer": "Sovet davri",
                "variant": ["Sovet davri", "1991-yil", "2000-yillar", "2010-yillar"]
            },
            {
                "question": "Yer yuzida eng baland vodiy?",
                "answer": "Pamir",
                "variant": ["Pamir", "Tibet", "And", "Himalay"]
            },
            {
                "question": "O‘zbekistonning qadimiy shaharlari ichida qaysi biri 'Oqshahr' deb ataladi?",
                "answer": "Shahrisabz",
                "variant": ["Shahrisabz", "Buxoro", "Xiva", "Urganch"]
            },
            {
                "question": "Qaysi davlatning poytaxti Karakas?",
                "answer": "Venesuela",
                "variant": ["Venesuela", "Kolumbiya", "Ekvador", "Peru"]
            },
            {
                "question": "O‘zbekiston Respublikasida mustaqillik e’lon qilingan joy?",
                "answer": "Oliy Kengash",
                "variant": ["Oliy Kengash", "Senat", "Prezident qarorgohi", "Adliya vazirligi"]
            }
        ]
    
        quiz_5 = [
            {
                "question": "Dunyoning eng mashhur muzeylaridan biri — Britaniya muzeyi qayerda?",
                "answer": "London",
                "variant": ["London", "Berlin", "Parij", "Madrid"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Alisher Navoiy nechanchi asrda yashagan?",
                "answer": "15-asr",
                "variant": ["15-asr", "14-asr", "16-asr", "17-asr"]
            },
            {
                "question": "Dunyoning eng mashhur teatrlaridan biri — Bolshoy teatri qayerda?",
                "answer": "Moskva",
                "variant": ["Moskva", "London", "Parij", "Berlin"]
            },
            {
                "question": "Dunyoning eng mashhur tog‘laridan biri — Montblan qayerda joylashgan?",
                "answer": "Fransiya va Italiya",
                "variant": ["Fransiya va Italiya", "Shveytsariya", "Avstriya", "Germaniya"]
            },
            {
                "question": "Dunyoning eng mashhur sharsharalaridan biri — Iguasu qayerda joylashgan?",
                "answer": "Braziliya va Argentina",
                "variant": ["Braziliya va Argentina", "Peru va Boliviya", "Kolumbiya va Venesuela", "Meksika va AQSh"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Abdulla Qodiriy mashhur asari?",
                "answer": "O‘tkan kunlar",
                "variant": ["O‘tkan kunlar", "Mehrobdan chayon", "Sarob", "Yulduzli tunlar"]
            },
            {
                "question": "Dunyoning eng mashhur orollaridan biri — Sumatra qayerda joylashgan?",
                "answer": "Indoneziya",
                "variant": ["Indoneziya", "Filippin", "Malayziya", "Singapur"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Ibn Sino qaysi sohada mashhur?",
                "answer": "Tibbiyot",
                "variant": ["Tibbiyot", "Matematika", "Adabiyot", "Kimyo"]
            },
            {
                "question": "Dunyoning eng mashhur daryolaridan biri — Yanszi qaysi davlatdan oqib o‘tadi?",
                "answer": "Xitoy",
                "variant": ["Xitoy", "Hindiston", "Rossiya", "Mongoliya"]
            },
            {
                "question": "O‘zbekistonning mashhur shoirlaridan biri — Cho‘lpon mashhur romani?",
                "answer": "Kecha va kunduz",
                "variant": ["Kecha va kunduz", "O‘tkan kunlar", "Sarob", "Shaytanat"]
            },
            {
                "question": "Dunyoning eng mashhur teatrlaridan biri — Metropolitan Opera qayerda joylashgan?",
                "answer": "Nyu-York",
                "variant": ["Nyu-York", "London", "Moskva", "Parij"]
            },
            {
                "question": "YUNESKO tomonidan jahon merosi ro‘yxatiga kiritilgan O‘zbekiston shaharlari qaysilar?",
                "answer": "Samarqand, Buxoro, Xiva, Shahrisabz",
                "variant": ["Samarqand, Buxoro, Xiva, Shahrisabz", "Toshkent, Andijon, Namangan", "Qo‘qon, Jizzax, Guliston", "Termiz, Qarshi, Nukus"]
            },
            {
                "question": "Dunyoning eng katta vodiylaridan biri — Grand Kanyon qayerda joylashgan?",
                "answer": "AQSh",
                "variant": ["AQSh", "Kanada", "Meksika", "Braziliya"]
            },
            {
                "question": "Yevropa va Osiyoni bog‘lab turuvchi mashhur ko‘prik qayerda joylashgan?",
                "answer": "Turkiya",
                "variant": ["Turkiya", "Rossiya", "Fransiya", "Angliya"]
            },
            {
                "question": "O‘zbekistonning milliy bog‘laridan biri — Zomin milliy bog‘i qaysi viloyatda joylashgan?",
                "answer": "Jizzax",
                "variant": ["Jizzax", "Namangan", "Farg‘ona", "Surxondaryo"]
            },
            {
                "question": "Dunyoning eng mashhur futbol jamoalaridan biri — 'Bavariya' qaysi shaharda joylashgan?",
                "answer": "Myunxen",
                "variant": ["Myunxen", "Berlin", "Dortmund", "Hamburg"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy yodgorliklaridan biri — Qizil minor masjidi qayerda?",
                "answer": "Xiva",
                "variant": ["Xiva", "Buxoro", "Toshkent", "Samarqand"]
            },
            {
                "question": "Dunyodagi eng katta arxipelag davlat?",
                "answer": "Indoneziya",
                "variant": ["Indoneziya", "Filippin", "Shvetsiya", "Malayziya"]
            },
            {
                "question": "Buyuk olim Muhammad al-Xorazmiy qaysi fan asoschisi?",
                "answer": "Algebra",
                "variant": ["Algebra", "Geometriya", "Astronomiya", "Kimyo"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan qadimiy Budda ibodatxonasi?",
                "answer": "Fayoztepa",
                "variant": ["Fayoztepa", "Shohi Zinda", "Registon", "Qoratepa"]
            },
            {
                "question": "Dunyoning eng baland sharsharasi Anxel qaysi mamlakatda joylashgan?",
                "answer": "Venesuela",
                "variant": ["Venesuela", "Braziliya", "Argentina", "Kolumbiya"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan eng baland tog‘ cho‘qqisi?",
                "answer": "Hazrati Sulton",
                "variant": ["Hazrati Sulton", "Chimyon", "Bobotog‘", "Somoni cho‘qqisi"]
            },
            {
                "question": "Yevropadagi eng katta ko‘l?",
                "answer": "Ladoga",
                "variant": ["Ladoga", "Onega", "Viktoriya", "Kaspiy"]
            },
            {
                "question": "O‘zbekiston hududidagi qadimiy madaniy markazlardan biri — Termiz qaysi daryo bo‘yida joylashgan?",
                "answer": "Amudaryo",
                "variant": ["Amudaryo", "Sirdaryo", "Zarafshon", "Chirchiq"]
            },
            {
                "question": "Dunyodagi eng ko‘p orolga ega davlat?",
                "answer": "Shvetsiya",
                "variant": ["Shvetsiya", "Norvegiya", "Indoneziya", "Yaponiya"]
            },
            {
                "question": "O‘zbekiston hududidagi qadimiy qal’alardan biri — Qo‘yqirilgan qal’a qayerda joylashgan?",
                "answer": "Qoraqalpog‘iston",
                "variant": ["Qoraqalpog‘iston", "Buxoro", "Xorazm", "Samarqand"]
            },
            {
                "question": "Dunyodagi eng mashhur rasm galereyalaridan biri — Prado muzeyi qayerda joylashgan?",
                "answer": "Ispaniya",
                "variant": ["Ispaniya", "Italiya", "Fransiya", "Angliya"]
            },
            {
                "question": "O‘zbekistonning milliy musiqiy asboblaridan biri?",
                "answer": "Doira",
                "variant": ["Doira", "G‘ijjak", "Pianino", "Gitara"]
            },
            {
                "question": "Afrikadagi eng uzun daryo?",
                "answer": "Nil",
                "variant": ["Nil", "Kongo", "Niger", "Zambezi"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur arxeologik yodgorliklardan biri?",
                "answer": "Topraqqal’a",
                "variant": ["Topraqqal’a", "Ayazqal’a", "Qo‘yqirilgan qal’a", "Mug‘ qal’a"]
            },
            {
                "question": "Dunyodagi eng mashhur teatrlaridan biri — La Skala qaysi shaharda joylashgan?",
                "answer": "Milan",
                "variant": ["Milan", "Parij", "London", "Vena"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Abdulla Qahhorning mashhur asari?",
                "answer": "Sarob",
                "variant": ["Sarob", "Anor", "Sinchalak", "O‘tkan kunlar"]
            },
            {
                "question": "Shimoliy Amerikadagi eng uzun daryo?",
                "answer": "Missisipi",
                "variant": ["Missisipi", "Amazonka", "Orinoko", "Parana"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur tarixiy me’moriy majmualardan biri — Registon?",
                "answer": "Samarqand",
                "variant": ["Samarqand", "Buxoro", "Xiva", "Toshkent"]
            },
            {
                "question": "Dunyodagi eng baland tog‘ tizmasi?",
                "answer": "Gimolay",
                "variant": ["Gimolay", "Alp", "And", "Tyan-Shan"]
            },
            {
                "question": "O‘zbekistonning mashhur shoirlaridan biri — Cho‘lponning mashhur asari?",
                "answer": "Kecha va kunduz",
                "variant": ["Kecha va kunduz", "Yulduzli tunlar", "O‘tkan kunlar", "Sarob"]
            },
            {
                "question": "Dunyodagi eng mashhur sharsharalardan biri — Viktoriya qayerda joylashgan?",
                "answer": "Zambiya va Zimbabve",
                "variant": ["Zambiya va Zimbabve", "Braziliya va Argentina", "Venesuela", "Kanada va AQSh"]
            },
            {
                "question": "O‘zbekiston hududidagi qadimiy shaharlaridan biri?",
                "answer": "Buxoro",
                "variant": ["Buxoro", "Samarqand", "Xiva", "Shahrisabz"]
            },
            {
                "question": "Dunyodagi eng mashhur universitetlardan biri — Garvard qaysi davlatda joylashgan?",
                "answer": "AQSh",
                "variant": ["AQSh", "Angliya", "Kanada", "Avstraliya"]
            },
            {
                "question": "Dunyoning eng katta ichki dengizi?",
                "answer": "Kaspiy",
                "variant": ["Kaspiy", "Aral", "Qora dengiz", "Oq dengiz"]
            },
            {
                "question": "Afrikadagi eng katta ko‘l?",
                "answer": "Viktoriya",
                "variant": ["Viktoriya", "Tanganika", "Malavi", "Chad"]
            },
            {
                "question": "O‘zbekistonning mashhur shoirlaridan biri — Erkin Vohidov mashhur she’riy turkumi?",
                "answer": "Tong nafasi",
                "variant": ["Tong nafasi", "Ruhlar isyoni", "O‘zbekiston", "Sarob"]
            },
            {
                "question": "Dunyoning eng mashhur orollardan biri — Madagaskar qayerda joylashgan?",
                "answer": "Hind okeani",
                "variant": ["Hind okeani", "Tinch okeani", "Atlantika okeani", "Shimoliy muz okeani"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Tohir Malik mashhur romani?",
                "answer": "Shaytanat",
                "variant": ["Shaytanat", "Dunyoning ishlari", "Yulduzli tunlar", "Sarob"]
            },
            {
                "question": "Dunyoning eng mashhur teatrlaridan biri — Katta teatr qaysi shaharda joylashgan?",
                "answer": "Moskva",
                "variant": ["Moskva", "London", "Parij", "Rim"]
            },
            {
                "question": "Dunyoning eng mashhur sharsharalaridan biri — Niagara qaysi ikki davlat chegarasida?",
                "answer": "AQSh va Kanada",
                "variant": ["AQSh va Kanada", "Braziliya va Argentina", "Venesuela", "Zambiya va Zimbabve"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Abdulla Qodiriy mashhur romani?",
                "answer": "Mehrobdan chayon",
                "variant": ["Mehrobdan chayon", "O‘tkan kunlar", "Sarob", "Kecha va kunduz"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Ibn Sino qaysi asarda tibbiy bilimlarni jamlagan?",
                "answer": "Tib qonunlari",
                "variant": ["Tib qonunlari", "Shohnoma", "Xamsa", "Qutadg‘u bilig"]
            },
            {
                "question": "Yer kurrasidagi eng baland plato qaysi?",
                "answer": "Tibet platosi",
                "variant": ["Tibet platosi", "Pamir", "Altay", "And"]
            },
            {
                "question": "Dunyoning eng yirik metall ishlab chiqaruvchilaridan biri?",
                "answer": "Xitoy",
                "variant": ["Xitoy", "AQSh", "Rossiya", "Hindiston"]
            },
            {
                "question": "O‘zbekiston hududidagi qadimiy qal’alardan biri — Ayazqal’a qaysi hududda joylashgan?",
                "answer": "Qoraqalpog‘iston",
                "variant": ["Qoraqalpog‘iston", "Buxoro", "Samarqand", "Namangan"]
            },
            {
                "question": "Buyuk astronom Kopernik qanday nazariyasi bilan mashhur?",
                "answer": "Geliosentrik nazariya",
                "variant": ["Geliosentrik nazariya", "Geosentrik nazariya", "Atom nazariyasi", "Evolyutsiya nazariyasi"]
            },
            {
                "question": "O‘zbekistonning mashhur shaharlaridan biri — Nukus qaysi hudud markazi?",
                "answer": "Qoraqalpog‘iston",
                "variant": ["Qoraqalpog‘iston", "Buxoro", "Qashqadaryo", "Xorazm"]
            },
            {
                "question": "Afrikadagi eng baland tog‘ cho‘qqisi?",
                "answer": "Kilimanjaro",
                "variant": ["Kilimanjaro", "Elbrus", "Atlas", "Drakensberg"]
            },
            {
                "question": "Shimoliy Amerikadagi eng katta ko‘l?",
                "answer": "Yuqori ko‘l",
                "variant": ["Yuqori ko‘l", "Michigan", "Ontario", "Eri"]
            },
            {
                "question": "Buyuk yozuvchi Abdulla Oripov mashhur asarlaridan biri?",
                "answer": "Jannatga yo‘l",
                "variant": ["Jannatga yo‘l", "Tong nafasi", "Sarob", "Kecha va kunduz"]
            },
            {
                "question": "Dunyoning eng mashhur sharsharalaridan biri — Iguasu qaysi davlatlarda joylashgan?",
                "answer": "Braziliya va Argentina",
                "variant": ["Braziliya va Argentina", "Venesuela", "Kanada va AQSh", "Kolumbiya va Peru"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaharlaridan biri — Qarshi qaysi davrda tashkil topgan?",
                "answer": "Miloddan avvalgi davrda",
                "variant": ["Miloddan avvalgi davrda", "IX asrda", "XIV asrda", "XVIII asrda"]
            },
            {
                "question": "Osiyodagi eng baland tog‘ cho‘qqisi?",
                "answer": "Everest",
                "variant": ["Everest", "K2", "Kangchenjunga", "Makalu"]
            },
            {
                "question": "Dunyodagi eng mashhur teatr binosi — Sidney Opera House qayerda joylashgan?",
                "answer": "Avstraliya",
                "variant": ["Avstraliya", "Yangi Zelandiya", "Kanada", "AQSh"]
            },
            {
                "question": "O‘zbekistonning eng katta gaz konlaridan biri?",
                "answer": "Sho‘rtan",
                "variant": ["Sho‘rtan", "Qandim", "Muborak", "Olmaliq"]
            },
            {
                "question": "Dunyoning eng mashhur universitetlaridan biri — Kembridj qaysi davlatda joylashgan?",
                "answer": "Angliya",
                "variant": ["Angliya", "AQSh", "Kanada", "Avstraliya"]
            },
            {
                "question": "Afrikadagi eng katta daryo havzasi?",
                "answer": "Kongo",
                "variant": ["Kongo", "Nil", "Niger", "Zambezi"]
            },
            {
                "question": "Buyuk yozuvchi Erkin Vohidov mashhur asarlaridan biri?",
                "answer": "Ruhlar isyoni",
                "variant": ["Ruhlar isyoni", "O'zbegim", "O‘zbekiston", "Sarob"]
            },
            {
                "question": "Dunyoning eng katta ichki ko‘li?",
                "answer": "Kaspiy",
                "variant": ["Kaspiy", "Baykal", "Viktoriya", "Aral"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Beruniy qaysi sohalarda mashhur?",
                "answer": "Matematika va astronomiya",
                "variant": ["Matematika va astronomiya", "Kimyo va tibbiyot", "Adabiyot va san’at", "Geografiya va tarix"]
            },
            {
                "question": "Janubiy Amerikadagi eng katta mamlakat?",
                "answer": "Braziliya",
                "variant": ["Braziliya", "Argentina", "Kolumbiya", "Peru"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur shoirlardan biri — Bobur qayerda tug‘ilgan?",
                "answer": "Andijon",
                "variant": ["Andijon", "Samarqand", "Toshkent", "Xiva"]
            },
            {
                "question": "Dunyoning eng mashhur sport musobaqalaridan biri — Olimpiada dastlab qayerda boshlangan?",
                "answer": "Yunoniston",
                "variant": ["Yunoniston", "Italiya", "Fransiya", "Misr"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — O‘tkir Hoshimovning mashhur asari?",
                "answer": "Ikki eshik orasi",
                "variant": ["Ikki eshik orasi", "Dunyoning ishlari", "Sarob", "Anor"]
            },
            {
                "question": "Osiyodagi eng katta orol?",
                "answer": "Borneo",
                "variant": ["Borneo", "Sumatra", "Yava", "Saxalin"]
            },
            {
                "question": "Dunyoning eng mashhur qal’alaridan biri — Alhambra qayerda joylashgan?",
                "answer": "Ispaniya",
                "variant": ["Ispaniya", "Italiya", "Fransiya", "Portugaliya"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur yodgorliklardan biri — Ismoil Somoniy maqbarasi qayerda joylashgan?",
                "answer": "Buxoro",
                "variant": ["Buxoro", "Samarqand", "Xiva", "Shahrisabz"]
            },
            {
                "question": "Shimoliy Amerikadagi eng baland tog‘?",
                "answer": "Denali",
                "variant": ["Denali", "Logan", "Orizaba", "Rainier"]
            },
            {
                "question": "Dunyoning eng mashhur universitetlaridan biri — Sorbonna qayerda joylashgan?",
                "answer": "Parij",
                "variant": ["Parij", "London", "Berlin", "Madrid"]
            },
            {
                "question": "Dunyoning eng mashhur sharsharalaridan biri — Dettifoss qayerda joylashgan?",
                "answer": "Islandiya",
                "variant": ["Islandiya", "Norvegiya", "Kanada", "AQSh"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur san’at maktablaridan biri?",
                "answer": "Bekzod san’at maktabi",
                "variant": ["Bekzod san’at maktabi", "Ilhom san’at maktabi", "Usto", "Kamolot"]
            },
            {
                "question": "Janubiy Amerikadagi eng mashhur tog‘ tizmasi?",
                "answer": "And",
                "variant": ["And", "Syerra-Madre", "Patagoniya", "Altiplano"]
            },
            {
                "question": "Dunyoning eng mashhur cho‘llaridan biri — Atakama qayerda joylashgan?",
                "answer": "Chili",
                "variant": ["Chili", "Argentina", "Peru", "Boliviya"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Cho‘lponning mashhur she’riy to‘plamlaridan biri?",
                "answer": "Buloqlar",
                "variant": ["Buloqlar", "Tong nafasi", "O‘zbekiston", "Sarob"]
            },
            {
                "question": "Afrikadagi eng mashhur sharsharalardan biri — Tugela qayerda joylashgan?",
                "answer": "Janubiy Afrika",
                "variant": ["Janubiy Afrika", "Namibiya", "Kongo", "Zimbabve"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur shahar — Andijon qaysi vohada joylashgan?",
                "answer": "Farg‘ona vodiysi",
                "variant": ["Farg‘ona vodiysi", "Qashqadaryo", "Surxondaryo", "Zarafshon"]
            },
            {
                "question": "Dunyoning eng mashhur sportchilaridan biri — Muhammad Ali qaysi sport turi bo‘yicha mashhur?",
                "answer": "Boks",
                "variant": ["Boks", "Futbol", "Basketbol", "Tennis"]
            },
            {
                "question": "Dunyodagi eng uzun daryo qaysi ikki davlat hududidan oqib o‘tadi?",
                "answer": "Misr va Sudan",
                "variant": ["Misr va Sudan", "Braziliya va Peru", "Xitoy va Hindiston", "Rossiya va Qozog‘iston"]
            },
            {
                "question": "Dunyoning eng katta ko‘llaridan biri — Baykal qayerda joylashgan?",
                "answer": "Rossiya",
                "variant": ["Rossiya", "Mongoliya", "Qozog‘iston", "Xitoy"]
            },
            {
                "question": "Buyuk geografik kashfiyotlar davrida Hindistonga dengiz yo‘lini topgan kim?",
                "answer": "Vasko da Gama",
                "variant": ["Vasko da Gama", "Kolumb", "Magellan", "Hudson"]
            },
            {
                "question": "O‘zbekiston hududidagi qadimiy buddaviy yodgorliklardan biri — Zurmala stupasi qayerda?",
                "answer": "Termez",
                "variant": ["Termez", "Samarqand", "Xiva", "Toshkent"]
            },
            {
                "question": "Dunyoning eng katta orollaridan biri — Madagaskar qaysi okeanda joylashgan?",
                "answer": "Hind okeani",
                "variant": ["Hind okeani", "Tinch okeani", "Atlantika okeani", "Shimoliy muz okeani"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Utkir Hoshimov mashhur hikoyasi?",
                "answer": "Dunyoning ishlari",
                "variant": ["Dunyoning ishlari", "Bahor qaytmaydi", "Ikki eshik orasi", "Shum bola"]
            },
            {
                "question": "Dunyoning eng katta aholi yashaydigan oroli?",
                "answer": "Yava",
                "variant": ["Yava", "Sumatra", "Bali", "Filippin oroli"]
            },
            {
                "question": "O‘zbekiston hududidagi qadimiy qal’alardan biri — Devxona qayerda joylashgan?",
                "answer": "Surxondaryo",
                "variant": ["Surxondaryo", "Buxoro", "Qashqadaryo", "Xorazm"]
            },
            {
                "question": "Dunyoning eng baland shahri?",
                "answer": "La-Pas",
                "variant": ["La-Pas", "Katmandu", "Quito", "Bogota"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Al-Farg‘oniy asosan qaysi fan bilan shug‘ullangan?",
                "answer": "Astronomiya",
                "variant": ["Astronomiya", "Matematika", "Kimyo", "Fizika"]
            },
            {
                "question": "Dunyoning eng uzun yerosti daryosi?",
                "answer": "Perto Princeso",
                "variant": ["Perto Princeso", "Nil", "Amazonka", "Yanszi"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur tarixiy obidalaridan biri — Ko‘hna Ark qayerda joylashgan?",
                "answer": "Xiva",
                "variant": ["Xiva", "Buxoro", "Samarqand", "Shahrisabz"]
            },
            {
                "question": "Dunyoning eng mashhur san’at muzeylaridan biri — Uffizi galereyasi qayerda joylashgan?",
                "answer": "Florensiya",
                "variant": ["Florensiya", "Rim", "Venetsiya", "Milan"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Erkin Vohidovning mashhur dostoni?",
                "answer": "Sadoqat",
                "variant": ["Sadoqat", "Ruhlar isyoni", "Tong nafasi", "O‘zbekiston"]
            },
            {
                "question": "Dunyoning eng katta cho‘llaridan biri — Kalahari qaysi qit’ada joylashgan?",
                "answer": "Afrika",
                "variant": ["Afrika", "Osiyo", "Janubiy Amerika", "Avstraliya"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan qadimiy shahar qal’alaridan biri — Qo‘yqirilgan qal’a qaysi vohada joylashgan?",
                "answer": "Ellikqal’a",
                "variant": ["Ellikqal’a", "Buxoro vohasi", "Zarafshon vohasi", "Farg‘ona vodiysi"]
            },
            {
                "question": "Dunyoning eng mashhur orollaridan biri — Shpitsbergen qaysi davlat hududida joylashgan?",
                "answer": "Norvegiya",
                "variant": ["Norvegiya", "Daniya", "Islandiya", "Shvetsiya"]
            }
        ]
            
        quiz_6 = [
            {
                "question": "Kompyuter klaviaturasida 'Esc' tugmasi odatda qaysi burchakda joylashgan?",
                "answer": "Yuqori chap burchak",
                "variant": ["Yuqori chap burchak", "Yuqori o‘ng burchak", "Pastki chap burchak", "Pastki o‘ng burchak"]
            },
            {
                "question": "Rubik kubigini kim ixtiro qilgan?",
                "answer": "Ernő Rubik",
                "variant": ["Ernő Rubik", "Nikola Tesla", "Tim Berners-Lee", "Alan Turing"]
            },
            {
                "question": "HTML tilida gipermurojaat yaratish uchun qaysi teg ishlatiladi?",
                "answer": "<a>",
                "variant": ["<a>", "<link>", "<href>", "<url>"]
            },
            {
                "question": "Toshkent metropoliteni qaysi yilda ishga tushirilgan?",
                "answer": "1977",
                "variant": ["1977", "1984", "1969", "1991"]
            },
            {
                "question": "O‘zbekistonda 'Alpomish' dostoni qaysi og‘zaki ijod turiga mansub?",
                "answer": "Epos",
                "variant": ["Epos", "Lyirika", "Doston drama", "Novella"]
            },
            {
                "question": "Qaysi gaz Yer atmosferasida eng ko‘p uchraydi?",
                "answer": "Azot",
                "variant": ["Azot", "Kislorod", "Argon", "Karbonat angidrid"]
            },
            {
                "question": "SI tizimida elektr tok kuchining birliksi?",
                "answer": "Amper",
                "variant": ["Amper", "Volt", "Om", "Vatt"]
            },
            {
                "question": "Chopar (courier) xizmatlarida 'ETA' qisqartmasi odatda nimani anglatadi?",
                "answer": "Taxminiy yetib kelish vaqti",
                "variant": ["Taxminiy yetib kelish vaqti", "Eng tez adres", "Elektron tranzit ariza", "Yuk turi"]
            },
            {
                "question": "Qaysi musiqiy asbob torli cholg‘u hisoblanadi?",
                "answer": "Skripka",
                "variant": ["Skripka", "Fleyta", "Klarnet", "Baraban"]
            },
            {
                "question": "Qog‘ozning A4 formatida uzun tomoni taxminan nechaga teng?",
                "answer": "297 mm",
                "variant": ["297 mm", "210 mm", "300 mm", "250 mm"]
            },
            {
                "question": "Dunyoning eng kichik qit’asi qaysi?",
                "answer": "Avstraliya",
                "variant": ["Avstraliya", "Yevropa", "Antarktida", "Afrika"]
            },
            {
                "question": "DNS qisqartmasi kompyuter tarmoqlarida nimani anglatadi?",
                "answer": "Domain Name System",
                "variant": ["Domain Name System", "Data Network Service", "Digital Node Server", "Dynamic Name Source"]
            },
            {
                "question": "Fizikada 'harorat'ni o‘lchash uchun xalqaro birlik tizimidagi asosiy birlik qaysi?",
                "answer": "Kelvin",
                "variant": ["Kelvin", "Selsiy", "Farengeyt", "Rankin"]
            },
            {
                "question": "Qaysi shaxs zamonaviy 'Vikipediya' loyihasining hammuassisi sifatida tanilgan?",
                "answer": "Jimmi Uels",
                "variant": ["Jimmi Uels", "Mark Sukerberg", "Sergey Brin", "Lerri Peyj"]
            },
            {
                "question": "O‘zbek tilida 'q' va 'k' tovushlari farqlanishi fonetik jihatdan nimaga bog‘liq?",
                "answer": "Til orqa va til oldi artikulyatsiyasiga",
                "variant": ["Til orqa va til oldi artikulyatsiyasiga", "Lab-lab artikulyatsiyasiga", "Burun rezonansiga", "Tanglay yumshoqligiga"]
            },
            {
                "question": "Fotosintez jarayonida o‘simliklar asosan qaysi gazni yutadi?",
                "answer": "Karbonat angidrid",
                "variant": ["Karbonat angidrid", "Kislorod", "Azot", "Vodorod"]
            },
            {
                "question": "O‘zbekistonda milliy valyuta — so‘m qaysi yilda joriy qilingan?",
                "answer": "1994",
                "variant": ["1994", "1991", "1992", "1996"]
            },
            {
                "question": "Qaysi futbol qoidasi 'o‘yindan tashqari holat'ni belgilaydi?",
                "answer": "Ofsayd",
                "variant": ["Ofsayd", "Penalti", "Aut", "Korner"]
            },
            {
                "question": "Matnda yangi satrga o‘tish belgisi qanday yoziladi (ko‘p dasturlash tillarida)?",
                "answer": "\\n",
                "variant": ["\\n", "\\t", "\\r", "\\b"]
            },
            {
                "question": "Qaysi ko‘paytirish natijasi to‘g‘ri: 9 × 7 = ?",
                "answer": "63",
                "variant": ["63", "56", "72", "64"]
            },
            {
                "question": "Toshkentdagi Mustaqillik maydonida qaysi ramziy obida joylashgan?",
                "answer": "Baxtiyor ona va bolakay haykali",
                "variant": ["Baxtiyor ona va bolakay haykali", "Temuriylar haykali", "Qaldirg‘och haykali", "Amir Temur haykali"]
            },
            {
                "question": "Qaysi yirik adabiy janr voqeaband nasriy asar hisoblanadi?",
                "answer": "Roman",
                "variant": ["Roman", "G‘azal", "She’r", "Doston"]
            },
            {
                "question": "Kimyo darsida H2O formulasi qaysi moddagi ifodalaydi?",
                "answer": "Suv",
                "variant": ["Suv", "Vodorod peroksid", "Metan", "Oksigen"]
            },
            {
                "question": "Qaysi so‘z imlo jihatidan to‘g‘ri yozilgan?",
                "answer": "Muammo",
                "variant": ["Muammo", "Muammoh", "Muaamo", "Muama"]
            },
            {
                "question": "Qaysi shahar 'shamollar shahri' laqabiga ega?",
                "answer": "Chicago",
                "variant": ["Chicago", "Seul", "Berlin", "Madrid"]
            },
            {
                "question": "Algoritm nima?",
                "answer": "Muammoni yechish uchun aniq qadamlar ketma-ketligi",
                "variant": ["Muammoni yechish uchun aniq qadamlar ketma-ketligi", "Kompyuter qurilmasi", "Ma’lumotlar bazasi", "Dasturiy interfeys"]
            },
            {
                "question": "Quyosh tizimidagi eng katta sayyora qaysi?",
                "answer": "Yupiter",
                "variant": ["Yupiter", "Saturn", "Yer", "Uran"]
            },
            {
                "question": "Qaysi davlat 'qahva vatani' hisoblanadi?",
                "answer": "Efiopiya",
                "variant": ["Efiopiya", "Braziliya", "Kolumbiya", "Vyetnam"]
            },
            {
                "question": "Buyuk ipak yo‘lining asosiy markazlaridan biri bo‘lgan shahar?",
                "answer": "Buxoro",
                "variant": ["Buxoro", "Samarqand", "Xiva", "Urganch"]
            },
            {
                "question": "Qaysi davlatning poytaxti Ulan-Bator?",
                "answer": "Mongoliya",
                "variant": ["Mongoliya", "Qozog‘iston", "Qirg‘iziston", "Rossiya"]
            },
            {
                "question": "Sharq mutafakkiri Al-Xorazmiy qaysi fan asoschisi?",
                "answer": "Algebra",
                "variant": ["Algebra", "Geometriya", "Astronomiya", "Kimyo"]
            },
            {
                "question": "Qaysi davlatda 'Machu-Pikchu' yodgorligi joylashgan?",
                "answer": "Peru",
                "variant": ["Peru", "Meksika", "Boliviya", "Argentina"]
            },
            {
                "question": "Yer kurrasidagi eng katta chuchuk suv ko‘li qaysi?",
                "answer": "Baykal",
                "variant": ["Baykal", "Viktoriya", "Tanganika", "Kaspiy"]
            },
            {
                "question": "Buyuk Britaniyaning milliy valyutasi nima?",
                "answer": "Funt sterling",
                "variant": ["Funt sterling", "Yevro", "Dollar", "Frank"]
            },
            {
                "question": "O‘zbekistonning eng shimoliy viloyati qaysi?",
                "answer": "Qoraqalpog‘iston",
                "variant": ["Qoraqalpog‘iston", "Surxondaryo", "Andijon", "Jizzax"]
            },
            {
                "question": "Qaysi sport turida 'Ace' atamasi ishlatiladi?",
                "answer": "Tennis",
                "variant": ["Tennis", "Futbol", "Basketbol", "Boks"]
            },
            {
                "question": "Dunyodagi eng baland tog‘ cho‘qqisi qaysi ikki davlat chegarasida joylashgan?",
                "answer": "Nepal va Xitoy",
                "variant": ["Nepal va Xitoy", "Hindiston va Pokiston", "Rossiya va Gruziya", "Eron va Turkiya"]
            },
            {
                "question": "Kim ilk bo‘lib Oyga qadam qo‘ygan?",
                "answer": "Nil Armstrong",
                "variant": ["Nil Armstrong", "Yuriy Gagarin", "Buz Oldrin", "Germanning Titov"]
            },
            {
                "question": "Yer yuzidagi eng baland poytaxt shahar?",
                "answer": "La-Pas",
                "variant": ["La-Pas", "Katmandu", "Quito", "Bogota"]
            },
            {
                "question": "Qaysi davlatda eng ko‘p orollar mavjud?",
                "answer": "Shvetsiya",
                "variant": ["Shvetsiya", "Indoneziya", "Filippin", "Yaponiya"]
            },
            {
                "question": "Buyuk Ipak yo‘li asosan qaysi ikki qit’ani bog‘lagan?",
                "answer": "Osiyo va Yevropa",
                "variant": ["Osiyo va Yevropa", "Osiyo va Afrika", "Yevropa va Amerika", "Osiyo va Janubiy Amerika"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan eng baland suv ombori?",
                "answer": "Tuyamo‘yin",
                "variant": ["Tuyamo‘yin", "Chorvoq", "Andijon", "To‘dako‘l"]
            },
            {
                "question": "Parijdagi mashhur muzey nomi?",
                "answer": "Luvr",
                "variant": ["Luvr", "Eremitaj", "Britaniya muzeyi", "Metropoliten muzeyi"]
            },
            {
                "question": "Yer yuzidagi eng katta arxipelag?",
                "answer": "Indoneziya",
                "variant": ["Indoneziya", "Filippin", "Malayziya", "Gretsiya"]
            },
            {
                "question": "O‘zbekistonning milliy bog‘i nomi?",
                "answer": "Navro‘z bog‘i",
                "variant": ["Navro‘z bog‘i", "Zafar bog‘i", "Amir Temur bog‘i", "Mustaqillik bog‘i"]
            },
            {
                "question": "Dunyodagi eng uzun tog‘ tizmasi?",
                "answer": "And tog‘lari",
                "variant": ["And tog‘lari", "Alp", "Gimolay", "Ural"]
            },
            {
                "question": "Qaysi sport turida 'Knockout' atamasi ishlatiladi?",
                "answer": "Boks",
                "variant": ["Boks", "Regbi", "Futbol", "Basketbol"]
            },
            {
                "question": "O‘zbekiston hududidagi eng qadimiy yozuv topilgan joy?",
                "answer": "Mug‘ tog‘i",
                "variant": ["Mug‘ tog‘i", "Termiz", "Samarqand", "Xorazm"]
            },
            {
                "question": "Qaysi shahar 'shamollar shahri' deb ataladi?",
                "answer": "Chicago",
                "variant": ["Chicago", "London", "Parij", "Berlin"]
            },
            {
                "question": "Eng mashhur yunon faylasufi?",
                "answer": "Platon",
                "variant": ["Platon", "Aristotel", "Sokrat", "Pifagor"]
            },
            {
                "question": "Dunyodagi eng katta cho‘l qaysi qit’ada joylashgan?",
                "answer": "Afrika",
                "variant": ["Afrika", "Osiyo", "Janubiy Amerika", "Avstraliya"]
            },
            {
                "question": "Qaysi davlatning poytaxti Seul?",
                "answer": "Janubiy Koreya",
                "variant": ["Janubiy Koreya", "Xitoy", "Yaponiya", "Tayvan"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy qal’alaridan biri?",
                "answer": "Ayazqal’a",
                "variant": ["Ayazqal’a", "Ark", "Qo‘yqirilgan qal’a", "Topraqqal’a"]
            },
            {
                "question": "Qaysi futbol jamoasi 'qizil iblislar' laqabi bilan mashhur?",
                "answer": "Manchester United",
                "variant": ["Manchester United", "Liverpool", "Chelsea", "Arsenal"]
            },
            {
                "question": "O‘zbekistonda ishlab chiqariladigan mashhur avtomobil markasi?",
                "answer": "Chevrolet",
                "variant": ["Chevrolet", "Hyundai", "Lada", "Toyota"]
            },
            {
                "question": "Yer sharidagi eng uzun daryo Janubiy Amerikada joylashgan. Bu qaysi?",
                "answer": "Amazonka",
                "variant": ["Amazonka", "Nil", "Orinoko", "Parana"]
            },
            {
                "question": "O‘zbekistonning mashhur bog‘laridan biri — Amir Temur xiyoboni qayerda joylashgan?",
                "answer": "Toshkent",
                "variant": ["Toshkent", "Samarqand", "Buxoro", "Namangan"]
            },
            {
                "question": "Dunyodagi eng katta hayvon qaysi turga mansub?",
                "answer": "Kit",
                "variant": ["Kit", "Fil", "Akula", "Jirafa"]
            },
            {
                "question": "Qaysi davlatning milliy bayrog‘ida zarang bargi tasvirlangan?",
                "answer": "Kanada",
                "variant": ["Kanada", "Avstraliya", "Shvetsiya", "Norvegiya"]
            },
            {
                "question": "Dunyodagi eng katta yarim orol?",
                "answer": "Arabiston yarim oroli",
                "variant": ["Arabiston yarim oroli", "Iberiya", "Skandinaviya", "Hindiston"]
            },
            {
                "question": "O‘zbekistonning mashhur san’atkorlaridan biri?",
                "answer": "Ozodbek Nazarbekov",
                "variant": ["Ozodbek Nazarbekov", "Yulduz Usmonova", "Munojot Yo‘lchiyeva", "Sevara Nazarkhan"]
            },
            {
                "question": "Qaysi shahar 'sehrli shahar' nomi bilan mashhur?",
                "answer": "Venetsiya",
                "variant": ["Venetsiya", "Parij", "Rim", "Madrid"]
            },
            {
                "question": "Dunyodagi eng katta davlat maydon bo‘yicha?",
                "answer": "Rossiya",
                "variant": ["Rossiya", "AQSh", "Xitoy", "Kanada"]
            },
            {
                "question": "O‘zbekistonning eng katta viloyati maydon bo‘yicha?",
                "answer": "Navoiy",
                "variant": ["Navoiy", "Buxoro", "Qashqadaryo", "Surxondaryo"]
            },
            {
                "question": "Yer yuzida eng katta yarim yopiq dengiz?",
                "answer": "Qora dengiz",
                "variant": ["Qora dengiz", "Oq dengiz", "O‘lik dengiz", "Aral dengizi"]
            },
            {
                "question": "Buyuk olim Pifagor qaysi fanda mashhur?",
                "answer": "Matematika",
                "variant": ["Matematika", "Astronomiya", "Fizika", "Kimyo"]
            },
            {
                "question": "O‘zbekistonning eng mashhur teatrlaridan biri?",
                "answer": "Navoi opera va balet teatri",
                "variant": ["Navoi opera va balet teatri", "Ilhom teatri", "Yosh tomoshabinlar teatri", "Qo‘qon teatri"]
            },
            {
                "question": "Qaysi davlatda 'Machu-Pikchu' joylashgan?",
                "answer": "Peru",
                "variant": ["Peru", "Meksika", "Boliviya", "Ekvador"]
            },
            {
                "question": "Dunyodagi eng katta ichki dengiz?",
                "answer": "Kaspiy",
                "variant": ["Kaspiy", "Oq dengiz", "Qora dengiz", "Aral dengizi"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Jaloliddin Manguberdi qaysi shahar yaqinida tug‘ilgan?",
                "answer": "Urgench",
                "variant": ["Urgench", "Buxoro", "Andijon", "Termiz"]
            },
            {
                "question": "Dunyodagi eng katta orol?",
                "answer": "Grenlandiya",
                "variant": ["Grenlandiya", "Yangi Gvineya", "Sumatra", "Madagaskar"]
            },
            {
                "question": "Yer sharidagi eng katta okean oqimi?",
                "answer": "Golfstrim",
                "variant": ["Golfstrim", "Kuro-Sio", "Labrador", "Antarktika oqimi"]
            },
            {
                "question": "Buyuk olim Arximed qaysi shahar fuqarosi bo‘lgan?",
                "answer": "Sirakuza",
                "variant": ["Afina", "Rim", "Sirakuza", "Sparta"]
            },
            {
                "question": "O‘zbekiston hududidagi eng qadimiy me’moriy majmualardan biri?",
                "answer": "Shohi Zinda",
                "variant": ["Shohi Zinda", "Registon", "Gur Amir", "Minorai Kalon"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Pirimqul Qodirovning mashhur romani?",
                "answer": "Yulduzli tunlar",
                "variant": ["Yulduzli tunlar", "Avlodlar dovoni", "Sarob", "Qiyomat"]
            },
            {
                "question": "Dunyodagi eng mashhur minoralardan biri — Pisa minorasi qaysi mamlakatda joylashgan?",
                "answer": "Italiya",
                "variant": ["Italiya", "Ispaniya", "Fransiya", "Gretsiya"]
            },
            {
                "question": "Yer sharida eng ko‘p aholiga ega davlat?",
                "answer": "Xitoy",
                "variant": ["Xitoy", "Hindiston", "AQSh", "Indoneziya"]
            },
            {
                "question": "O‘zbekistonning mashhur me’moriy yodgorliklaridan biri — Gur Amir maqbarasi qayerda?",
                "answer": "Samarqand",
                "variant": ["Samarqand", "Buxoro", "Toshkent", "Shahrisabz"]
            },
            {
                "question": "Dunyodagi eng katta orol?",
                "answer": "Grenlandiya",
                "variant": ["Skandinaviya", "Iberiya", "Arabiston", "Grenlandiya"]
            },
            {
                "question": "Qaysi olim tortishish qonunini yaratgan?",
                "answer": "Isaak Nyuton",
                "variant": ["Isaak Nyuton", "Galiley", "Kopernik", "Paskal"]
            },
            {
                "question": "O‘zbekistonning eng mashhur tarixiy obidalaridan biri — Registon maydoni qayerda?",
                "answer": "Samarqand",
                "variant": ["Samarqand", "Buxoro", "Xiva", "Toshkent"]
            },
            {
                "question": "Dunyoning eng kichik qit’asi?",
                "answer": "Avstraliya",
                "variant": ["Avstraliya", "Yevropa", "Antarktida", "Janubiy Amerika"]
            },
            {
                "question": "O‘zbekistonning milliy teatrlaridan biri?",
                "answer": "Ilhom teatri",
                "variant": ["Ilhom teatri", "Bolshoy teatr", "Yosh tomoshabinlar teatri", "Qo‘qon teatri"]
            },
            {
                "question": "Dunyodagi eng baland vulqon?",
                "answer": "Ojos del Salado",
                "variant": ["Ojos del Salado", "Etna", "Fudziyama", "Kilimanjaro"]
            },
            {
                "question": "Qaysi shoir 'O‘zbekiston — Vatanim manim' she’rini yozgan?",
                "answer": "Abdulla Oripov",
                "variant": ["Abdulla Oripov", "Erkin Vohidov", "Cho‘lpon", "Pirimqul Qodirov"]
            },
            {
                "question": "Yer sharidagi eng uzun tog‘ tizmalari qaysi qit’ada?",
                "answer": "Janubiy Amerika",
                "variant": ["Janubiy Amerika", "Osiyo", "Afrika", "Shimoliy Amerika"]
            },
            {
                "question": "O‘zbekistonning mashhur me’moriy yodgorliklaridan biri — Ichan qal’a qayerda?",
                "answer": "Xiva",
                "variant": ["Xiva", "Buxoro", "Samarqand", "Toshkent"]
            },
            {
                "question": "Dunyodagi eng mashhur opera teatrlardan biri — La Skala qayerda?",
                "answer": "Milan",
                "variant": ["Milan", "Parij", "London", "Vena"]
            },
            {
                "question": "O‘zbekistonning mashhur qo‘lyozma kitoblaridan biri?",
                "answer": "Devonu lug‘otit turk",
                "variant": ["Devonu lug‘otit turk", "Shohnoma", "Qutadg‘u bilig", "Al-Jome’ as-sahih"]
            },
            {
                "question": "Dunyodagi eng uzun devorlardan biri?",
                "answer": "Xitoy devori",
                "variant": ["Xitoy devori", "Berlin devori", "Hadrian devori", "Bobil devori"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Jaloliddin Manguberdi qaysi daryodan kechib o‘tgan?",
                "answer": "Indus",
                "variant": ["Indus", "Amudaryo", "Sirdaryo", "Zarafshon"]
            },
            {
                "question": "Dunyodagi eng katta futbol stadionlaridan biri — Marakana qayerda joylashgan?",
                "answer": "Braziliya",
                "variant": ["Braziliya", "Argentina", "Meksika", "Ispaniya"]
            },
            {
                "question": "Yer sharidagi eng katta yarim yopiq ko‘rfaz?",
                "answer": "Bengal ko‘rfazi",
                "variant": ["Bengal ko‘rfazi", "Meksika ko‘rfazi", "Pers ko‘rfazi", "Aden ko‘rfazi"]
            },
            {
                "question": "Dunyoning eng mashhur arxitekturalaridan biri — Kolizey qayerda?",
                "answer": "Rim",
                "variant": ["Rim", "Parij", "Afina", "Madrid"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Amir Temur qabrini qayerda topish mumkin?",
                "answer": "Samarqand",
                "variant": ["Samarqand", "Shahrisabz", "Toshkent", "Xiva"]
            },
            {
                "question": "Dunyodagi eng mashhur futbol klublaridan biri — Barcelona qaysi mamlakatda?",
                "answer": "Ispaniya",
                "variant": ["Ispaniya", "Italiya", "Fransiya", "Angliya"]
            },
            {
                "question": "Dunyodagi eng mashhur universitetlardan biri — Oksford qayerda joylashgan?",
                "answer": "Angliya",
                "variant": ["Angliya", "AQSh", "Kanada", "Avstraliya"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Al-Farg‘oniy qaysi fan sohasida mashhur?",
                "answer": "Astronomiya",
                "variant": ["Astronomiya", "Matematika", "Kimyo", "Tibbiyot"]
            },
            {
                "question": "Yer sharidagi eng mashhur tog‘ dovonlaridan biri?",
                "answer": "Torong-La",
                "variant": ["Torong-La", "Altay", "Pamir", "And"]
            },
            {
                "question": "O‘zbekistonning mashhur me’moriy obidalaridan biri — Minorai Kalon qayerda joylashgan?",
                "answer": "Buxoro",
                "variant": ["Buxoro", "Samarqand", "Xiva", "Shahrisabz"]
            }
        ]

        quiz_7 = [
            {
                "question": "Yer yuzida eng baland tog‘ tizmasi qaysi?",
                "answer": "Gimolay",
                "variant": ["Alp", "And", "Gimolay", "Kavkaz"]
            },
            {
                "question": "Buyuk Ipak yo‘li O‘zbekistondan qaysi davlatga chiqib ketgan?",
                "answer": "Xitoy",
                "variant": ["Turkiya", "Rossiya", "Xitoy", "Eron"]
            },
            {
                "question": "Qaysi sport turi O‘zbekistonning milliy sporti hisoblanadi?",
                "answer": "Kurash",
                "variant": ["Kurash", "Boks", "Futbol", "Tennis"]
            },
            {
                "question": "Dunyodagi eng katta qit’a?",
                "answer": "Osiyo",
                "variant": ["Osiyo", "Afrika", "Yevropa", "Amerika"]
            },
            {
                "question": "O‘zbekiston davlat madhiyasi muallifi kim?",
                "answer": "Abdulla Oripov",
                "variant": ["Erkin Vohidov", "Cho‘lpon", "Abdulla Oripov", "Oybek"]
            },
            {
                "question": "O‘zbekiston poytaxti qaysi shaharda joylashgan?",
                "answer": "Toshkent",
                "variant": ["Toshkent", "Samarqand", "Buxoro", "Andijon"]
            },
            {
                "question": "Yer yuzidagi eng uzun daryo?",
                "answer": "Nil",
                "variant": ["Nil", "Amazonka", "Yanszi", "Missisipi"]
            },
            {
                "question": "Buyuk yozuvchi Alisher Navoiy nechta tilni bilgan?",
                "answer": "3 dan ortiq",
                "variant": ["2", "3 dan ortiq", "1", "4"]
            },
            {
                "question": "O‘zbekiston Respublikasi davlat bayrog‘ida nechta yulduz bor?",
                "answer": "12",
                "variant": ["12", "10", "11", "14"]
            },
            {
                "question": "Yer yuzida eng katta cho‘l?",
                "answer": "Sahroi Kabir",
                "variant": ["Sahroi Kabir", "Atakama", "Gobi", "Karakum"]
            },
            {
                "question": "Shaxmat o‘yinida eng kuchli dona qaysi?",
                "answer": "Ferz",
                "variant": ["Shah", "Ferz", "Ot", "Ladya"]
            },
            {
                "question": "O‘zbekiston Respublikasi mustaqillik kuni qachon?",
                "answer": "1-sentyabr",
                "variant": ["8-dekabr", "1-sentyabr", "21-mart", "9-may"]
            },
            {
                "question": "Yer sharidagi eng katta okean?",
                "answer": "Tinch okeani",
                "variant": ["Tinch okeani", "Atlantika okeani", "Hind okeani", "Shimoliy Muz okeani"]
            },
            {
                "question": "Buyuk yozuvchi Abdulla Qodiriy mashhur asari?",
                "answer": "O‘tkan kunlar",
                "variant": ["O‘tkan kunlar", "Kecha va kunduz", "Dunyoning ishlari", "Qiyomat"]
            },
            {
                "question": "Qaysi sport turida Jahon chempionati eng ko‘p tomoshabin yig‘adi?",
                "answer": "Futbol",
                "variant": ["Futbol", "Basketbol", "Shaxmat", "Boks"]
            },
            {
                "question": "Yer yuzidagi eng baland cho‘qqi?",
                "answer": "Everest",
                "variant": ["Everest", "Elbrus", "K2", "Montblan"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat tili?",
                "answer": "O‘zbek tili",
                "variant": ["Rus tili", "O‘zbek tili", "Qoraqalpoq tili", "Ingliz tili"]
            },
            {
                "question": "Qaysi sport turida Ronaldo mashhur bo‘lgan?",
                "answer": "Futbol",
                "variant": ["Futbol", "Basketbol", "Regbi", "Boks"]
            },
            {
                "question": "Buyuk yozuvchi Chingiz Aytmatovning asari?",
                "answer": "Qiyomat",
                "variant": ["Qiyomat", "Shohnoma", "Kecha va kunduz", "Urush va tinchlik"]
            },
            {
                "question": "Yer sharida eng katta orol?",
                "answer": "Grenlandiya",
                "variant": ["Grenlandiya", "Madagaskar", "Sumatra", "Yangi Gvineya"]
            },
            {
                "question": "O‘zbekiston davlat gerbida qanotini yozgan qush qaysi?",
                "answer": "Humo qushi",
                "variant": ["Humo qushi", "Lochin", "Qaldirg‘och", "Burgut"]
            },
            {
                "question": "Buyuk yozuvchi O‘tkir Hoshimov mashhur asari?",
                "answer": "Dunyoning ishlari",
                "variant": ["Dunyoning ishlari", "Yulduzli tunlar", "Qiyomat", "Kecha va kunduz"]
            },
            {
                "question": "Yer sharida eng katta yarim orol?",
                "answer": "Arabiston yarim oroli",
                "variant": ["Arabiston yarim oroli", "Skandinaviya", "Iberiya", "Hindiston yarim oroli"]
            },
            {
                "question": "Buyuk yozuvchi Firdavsiyning mashhur asari?",
                "answer": "Shohnoma",
                "variant": ["Shohnoma", "Xamsa", "Devonu lug‘otit turk", "Qutadg‘u bilig"]
            },
            {
                "question": "O‘zbekistonning eng katta shahri?",
                "answer": "Toshkent",
                "variant": ["Samarqand", "Andijon", "Toshkent", "Namangan"]
            },
            {
                "question": "Yer sharida eng baland sharshara?",
                "answer": "Anxel",
                "variant": ["Niagara", "Victoria", "Iguasu", "Anxel"]
            },
            {
                "question": "Buyuk yozuvchi Pirimqul Qodirov mashhur asari?",
                "answer": "Yulduzli tunlar",
                "variant": ["Yulduzli tunlar", "Kecha va kunduz", "Shohnoma", "Qiyomat"]
            },
            {
                "question": "O‘zbekiston hududida nechta viloyat bor?",
                "answer": "12 + Qoraqalpog‘iston",
                "variant": ["11", "12 + Qoraqalpog‘iston", "13", "14"]
            },
            {
                "question": "Yer sharida eng baland tog‘ cho‘qqisi?",
                "answer": "Everest",
                "variant": ["Everest", "Elbrus", "Montblan", "Hazrati Sulton"]
            },
            {
                "question": "Buyuk yozuvchi Tohir Malik mashhur asari?",
                "answer": "Shaytanat",
                "variant": ["Shaytanat", "Qiyomat", "Dunyoning ishlari", "O‘tkan kunlar"]
            },
            {
                "question": "O‘zbekiston Respublikasining Konstitutsiya kuni qachon?",
                "answer": "8-dekabr",
                "variant": ["8-dekabr", "1-sentyabr", "21-mart", "9-may"]
            },
            {
                "question": "Yer sharida eng katta qit’a?",
                "answer": "Osiyo",
                "variant": ["Afrika", "Yevropa", "Osiyo", "Amerika"]
            },
            {
                "question": "Buyuk yozuvchi Erkin Vohidov mashhur asari?",
                "answer": "Ruhlar isyoni",
                "variant": ["Ruhlar isyoni", "Shohnoma", "O‘tkan kunlar", "Qutadg‘u bilig"]
            },
            {
                "question": "Buyuk yozuvchi Cho‘lpon mashhur asari?",
                "answer": "Kecha va kunduz",
                "variant": ["Kecha va kunduz", "Shohnoma", "Xamsa", "Yulduzli tunlar"]
            },
            {
                "question": "O‘zbekiston davlat madhiyasi musiqasini kim bastalagan?",
                "answer": "Mutal Burhonov",
                "variant": ["Mutal Burhonov", "Mansur Toshmatov", "Ortiq Otajonov", "Botir Zokirov"]
            },
            {
                "question": "Yer sharidagi eng katta ichki suv havzasi?",
                "answer": "Kaspiy dengizi",
                "variant": ["Oq dengiz", "Qora dengiz", "Kaspiy dengizi", "Aral dengizi"]
            },
            {
                "question": "Buyuk yozuvchi O‘tkir Hoshimovning yana bir mashhur asari?",
                "answer": "Ikki eshik orasi",
                "variant": ["Ikki eshik orasi", "Dunyoning ishlari", "Shaytanat", "Qiyomat"]
            },
            {
                "question": "O‘zbekiston davlat gerbidagi bug‘doy nimani bildiradi?",
                "answer": "Hosildorlik va farovonlik",
                "variant": ["Hosildorlik va farovonlik", "Barqarorlik", "Ona tabiat", "Adolat"]
            },
            {
                "question": "Yer sharidagi eng sovuq qit’a?",
                "answer": "Antarktida",
                "variant": ["Antarktida", "Osiyo", "Yevropa", "Afrika"]
            },
            {
                "question": "Buyuk yozuvchi Abdulla Qahhor mashhur asari?",
                "answer": "Sarob",
                "variant": ["Sarob", "Shohnoma", "O‘tkan kunlar", "Kecha va kunduz"]
            },
            {
                "question": "Yer sharidagi eng katta orollar arxipelagi?",
                "answer": "Indoneziya",
                "variant": ["Indoneziya", "Filippin", "Maldiv", "Shvetsiya"]
            },
            {
                "question": "Yer sharidagi eng chuqur ko‘l?",
                "answer": "Baykal",
                "variant": ["Baykal", "Tanganika", "Viktoriya", "Kaspiy"]
            },
            {
                "question": "Buyuk yozuvchi Lev Tolstoy qaysi asarni yozgan?",
                "answer": "Anna Karenina",
                "variant": ["Urush va tinchlik", "Anna Karenina", "Jinoyat va jazo", "Qariya va dengiz"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan eng qadimiy shahar?",
                "answer": "Samarqand",
                "variant": ["Samarqand", "Buxoro", "Xiva", "Termiz"]
            },
            {
                "question": "Buyuk yozuvchi Dostoyevskiyning mashhur asari?",
                "answer": "Aka-uka Karamazovlar",
                "variant": ["Aka-uka Karamazovlar", "O‘tkan kunlar", "Shohnoma", "Yulduzli tunlar"]
            },
            {
                "question": "O‘zbekistonning eng katta shaharlardan keyingi ikkinchi shahri?",
                "answer": "Samarqand",
                "variant": ["Samarqand", "Andijon", "Buxoro", "Namangan"]
            },
            {
                "question": "Yer sharidagi eng baland tog‘ cho‘qqisi qaysi davlatda joylashgan?",
                "answer": "Nepal",
                "variant": ["Nepal", "Hindiston", "Xitoy", "Butan"]
            },
            {
                "question": "Buyuk yozuvchi Cho‘lponning ismi aslida qanday bo‘lgan?",
                "answer": "Abdulhamid Sulaymon o‘g‘li",
                "variant": ["Abdulhamid Sulaymon o‘g‘li", "Abdulla Qodiriy", "Erkin Vohidov", "O‘tkir Hoshimov"]
            },
            {
                "question": "O‘zbekiston hududidagi eng baland tog‘ tizmasi?",
                "answer": "Tyan-Shan",
                "variant": ["Tyan-Shan", "Pamir", "Altay", "Ural"]
            },
            {
                "question": "Yer sharidagi eng mashhur orollardan biri — Madagaskar qaysi okeanda joylashgan?",
                "answer": "Hind okeani",
                "variant": ["Hind okeani", "Tinch okeani", "Atlantika okeani", "Shimoliy muz okeani"]
            },
            {
                "question": "Buyuk yozuvchi Abdulla Qodiriyning asl ismi?",
                "answer": "Abdulla Qodiriy Yoqub o‘g‘li",
                "variant": ["Abdulla Qodiriy Yoqub o‘g‘li", "Abdulla Qahhor", "Cho‘lpon", "Abdulla Oripov"]
            },
            {
                "question": "O‘zbekistonning eng katta tog‘ konlaridan biri?",
                "answer": "Olmaliq",
                "variant": ["Olmaliq", "Muruntov", "Sho‘rtan", "Qandim"]
            },
            {
                "question": "Yer sharida eng katta yarim yopiq dengiz?",
                "answer": "Qora dengiz",
                "variant": ["Qora dengiz", "Oq dengiz", "O‘lik dengiz", "Kaspiy"]
            },
            {
                "question": "Buyuk yozuvchi Pushkinning mashhur asari?",
                "answer": "Yevgeniy Onegin",
                "variant": ["Yevgeniy Onegin", "Shohnoma", "Kecha va kunduz", "Urush va tinchlik"]
            },
            {
                "question": "Yer sharidagi eng uzun devor?",
                "answer": "Xitoy devori",
                "variant": ["Xitoy devori", "Berlin devori", "Hadrian devori", "Bobil devori"]
            },
            {
                "question": "Buyuk yozuvchi Ernest Xeminguey mashhur asari?",
                "answer": "Qariya va dengiz",
                "variant": ["Qariya va dengiz", "Jarayon", "Sariq devni minib", "Shohnoma"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat tili qaysi?",
                "answer": "O‘zbek tili",
                "variant": ["O‘zbek tili", "Rus tili", "Ingliz tili", "Qoraqalpoq tili"]
            },
            {
                "question": "Buyuk yozuvchi Navoiy tug‘ilgan yil?",
                "answer": "1441",
                "variant": ["1441", "1451", "1430", "1420"]
            },
            {
                "question": "O‘zbekiston Respublikasining pul birligi?",
                "answer": "So‘m",
                "variant": ["So‘m", "Rubl", "Tiyin", "Dollar"]
            },
            {
                "question": "Buyuk yozuvchi Pirimqul Qodirov qaysi asarni yozgan?",
                "answer": "Avlodlar dovoni",
                "variant": ["Avlodlar dovoni", "Yulduzli tunlar", "Sarob", "Shaytanat"]
            },
            {
                "question": "Yer sharidagi eng uzun daryo Osiyoda joylashgan. U qaysi?",
                "answer": "Yanszi",
                "variant": ["Yanszi", "Amudaryo", "Ganga", "Sirdaryo"]
            },
            {
                "question": "Buyuk yozuvchi Firdavsiy qaysi asar muallifi?",
                "answer": "Shohnoma",
                "variant": ["Shohnoma", "Devonu lug‘otit turk", "Xamsa", "O‘tkan kunlar"]
            },
            {
                "question": "O‘zbekiston Respublikasi ramzlaridan biri?",
                "answer": "Davlat bayrog‘i",
                "variant": ["Davlat bayrog‘i", "Qur’on", "Shohnoma", "Davlat kutubxonasi"]
            },
            {
                "question": "Buyuk yozuvchi Shakespeare mashhur asari?",
                "answer": "Otello",
                "variant": ["Otello", "Hamlet", "Shohnoma", "Urush va tinchlik"]
            },
            {
                "question": "O‘zbekiston Respublikasida mustaqillik kuni qachon nishonlanadi?",
                "answer": "1-sentyabr",
                "variant": ["8-dekabr", "9-may", "1-sentyabr", "21-mart"]
            },
            {
                "question": "Yer sharidagi eng katta ichki ko‘l?",
                "answer": "Kaspiy",
                "variant": ["Kaspiy", "Baykal", "Viktoriya", "Tanganika"]
            },
            {
                "question": "Buyuk yozuvchi Erkin Vohidovning mashhur she’riy turkumi?",
                "answer": "Tong nafasi",
                "variant": ["Tong nafasi", "Oltin vodiydan", "Sarob", "Shohnoma"]
            },
            {
                "question": "O‘zbekiston hududidagi eng yirik daryo?",
                "answer": "Amudaryo",
                "variant": ["Amudaryo", "Sirdaryo", "Zarafshon", "Chirchiq"]
            },
            {
                "question": "Buyuk yozuvchi Abdulla Qahhor mashhur hikoyasi?",
                "answer": "Anor",
                "variant": ["Anor", "Sarob", "Shohnoma", "Dunyoning ishlari"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat madhiyasi muallifi?",
                "answer": "Abdulla Oripov",
                "variant": ["Mutal Burhonov", "Cho‘lpon", "Abdulla Oripov", "Erkin Vohidov"]
            },
            {
                "question": "Yer sharida eng baland tog‘ qaysi davlatlarda joylashgan?",
                "answer": "Nepal va Xitoy",
                "variant": ["Hindiston", "Butan", "Nepal va Xitoy", "Pokiston"]
            },
            {
                "question": "Buyuk yozuvchi Navoiy mashhur asarlari turkumi?",
                "answer": "Xamsa",
                "variant": ["Xamsa", "Shohnoma", "Qutadg‘u bilig", "Devonu lug‘otit turk"]
            },
            {
                "question": "O‘zbekiston Respublikasining milliy valyutasi?",
                "answer": "So‘m",
                "variant": ["So‘m", "Tiyin", "Rubl", "Dollar"]
            },
            {
                "question": "Yer sharidagi eng katta sharshara?",
                "answer": "Anxel",
                "variant": ["Viktoriya", "Niagara", "Anxel", "Angel"]
            },
            {
                "question": "O‘zbekiston Respublikasining milliy sporti?",
                "answer": "Kurash",
                "variant": ["Kurash", "Futbol", "Boks", "Shaxmat"]
            },
            {
                "question": "Yer sharidagi eng qadimiy yozuv turi?",
                "answer": "Mixxat",
                "variant": ["Mixxat", "Lotin", "Arab yozuvi", "Sanskrit"]
            },
            {
                "question": "Buyuk yozuvchi Cho‘lpon mashhur she’riy turkumi?",
                "answer": "Buloqlar",
                "variant": ["Buloqlar", "Sarob", "Tong nafasi", "Shohnoma"]
            },
            {
                "question": "O‘zbekiston Respublikasi davlat gerbida nechta yulduz aks etgan?",
                "answer": "12",
                "variant": ["10", "11", "12", "14"]
            },
            {
                "question": "Yer sharidagi eng baland platosi?",
                "answer": "Tibet",
                "variant": ["Pamir", "And", "Altay", "Tibet"]
            },
            {
                "question": "O‘zbekiston Respublikasining milliy ramzlaridan biri?",
                "answer": "Gerb",
                "variant": ["Gerb", "Qur’on", "Shohnoma", "Bayt"]
            },
            {
                "question": "O‘zbekiston Respublikasining milliy valyutasi joriy etilgan yil?",
                "answer": "1994-yil",
                "variant": ["1994-yil", "1991-yil", "1992-yil", "1993-yil"]
            },
            {
                "question": "Yer sharidagi eng katta ichki dengiz?",
                "answer": "Qora dengiz",
                "variant": ["Qora dengiz", "Adriatika", "Oq dengiz", "O‘lik dengiz"]
            },
            {
                "question": "Buyuk yozuvchi Erkin Vohidov tug‘ilgan yili?",
                "answer": "1936-yil",
                "variant": ["1936-yil", "1940-yil", "1930-yil", "1945-yil"]
            },
            {
                "question": "O‘zbekistonning milliy taomlaridan biri?",
                "answer": "Palov",
                "variant": ["Palov", "Somsa", "Lag‘mon", "Norin"]
            },
            {
                "question": "Yer sharidagi eng baland binolardan biri?",
                "answer": "Burj Xalifa",
                "variant": ["Burj Xalifa", "Eiffel minorasi", "CN Tower", "Big Ben"]
            },
            {
                "question": "Buyuk yozuvchi Abdulla Oripov mashhur she’riy asari?",
                "answer": "O‘zbekiston — Vatanim manim",
                "variant": ["O‘zbekiston — Vatanim manim", "Tong nafasi", "Shohnoma", "Sarob"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat madhiyasi qachon qabul qilingan?",
                "answer": "1992-yil",
                "variant": ["1992-yil", "1991-yil", "1993-yil", "1994-yil"]
            },
            {
                "question": "Buyuk yozuvchi Abdulla Qahhor mashhur qissasi?",
                "answer": "O‘g‘ri",
                "variant": ["O‘g‘ri", "Sarob", "Anor", "Shohnoma"]
            },
            {
                "question": "O‘zbekistonning eng yirik oltin koni?",
                "answer": "Muruntov",
                "variant": ["Muruntov", "Olmaliq", "Zarafshon", "Qizilqum"]
            },
            {
                "question": "Yer sharidagi eng mashhur sharsharalardan biri?",
                "answer": "Niagara",
                "variant": ["Niagara", "Anxel", "Victoria", "Iguasu"]
            },
            {
                "question": "Buyuk yozuvchi O‘tkir Hoshimovning mashhur qissasi?",
                "answer": "Ikki eshik orasi",
                "variant": ["Ikki eshik orasi", "Dunyoning ishlari", "Shohnoma", "Kecha va kunduz"]
            },
            {
                "question": "O‘zbekiston Respublikasining Konstitutsiyasi nechta bo‘limdan iborat?",
                "answer": "6",
                "variant": ["6", "5", "7", "8"]
            },
            {
                "question": "Yer sharida eng baland tog‘ dovoni?",
                "answer": "Thorong La",
                "variant": ["Thorong La", "And", "Altay", "Tyan-Shan"]
            },
            {
                "question": "O‘zbekiston hududidan oqib o‘tuvchi eng yirik daryo?",
                "answer": "Amudaryo",
                "variant": ["Amudaryo", "Sirdaryo", "Zarafshon", "Chirchiq"]
            },
            {
                "question": "Yer sharidagi eng katta orollar davlati?",
                "answer": "Indoneziya",
                "variant": ["Indoneziya", "Filippin", "Yaponiya", "Madagaskar"]
            },
            {
                "question": "Buyuk yozuvchi Alisher Navoiy qaysi shaharda tug‘ilgan?",
                "answer": "Xirot",
                "variant": ["Xirot", "Buxoro", "Samarqand", "Toshkent"]
            },
            {
                "question": "O‘zbekiston davlat gerbidagi Humo qushi nimani bildiradi?",
                "answer": "Erkinlik",
                "variant": ["Erkinlik", "Adolat", "Hosildorlik", "Ona tabiat"]
            },
            {
                "question": "Yer sharidagi eng uzun daryo Afrikada joylashgan. Bu qaysi?",
                "answer": "Nil",
                "variant": ["Nil", "Amazonka", "Yanszi", "Ganga"]
            },
            {
                "question": "Buyuk yozuvchi Pirimqul Qodirov mashhur romani?",
                "answer": "Avlodlar dovoni",
                "variant": ["Avlodlar dovoni", "Yulduzli tunlar", "Sarob", "Shohnoma"]
            },
            {
                "question": "O‘zbekiston Respublikasida Konstitutsiya kuni qachon?",
                "answer": "8-dekabr",
                "variant": ["8-dekabr", "1-sentyabr", "21-mart", "9-may"]
            }
        ]
    
        quiz_8 = [
            {
                "question": "O‘zbekiston Respublikasining Konstitutsiyasi qachon qabul qilingan?",
                "answer": "1992-yil 8-dekabr",
                "variant": ["1992-yil 8-dekabr", "1991-yil 1-sentyabr", "1993-yil 31-avgust", "1994-yil 20-iyun"]
            },
            {
                "question": "Yer sharidagi eng mashhur cho‘llardan biri?",
                "answer": "Sahroi Kabir",
                "variant": ["Gobi", "Atakama", "Lut cho‘li", "Sahroi Kabir"]
            },
            {
                "question": "Buyuk yozuvchi Abdulla Qahhor mashhur hikoyalaridan biri?",
                "answer": "O‘g‘ri",
                "variant": ["O‘g‘ri", "Anor", "Sarob", "Shohnoma"]
            },
            {
                "question": "O‘zbekiston Respublikasining birinchi Prezidenti kim?",
                "answer": "Islom Karimov",
                "variant": ["Islom Karimov", "Shavkat Mirziyoyev", "Abdulla Qodiriy", "Cho‘lpon"]
            },
            {
                "question": "O‘zbekiston davlat gerbidagi bug‘doy va paxta ramzi nimani bildiradi?",
                "answer": "Farovonlik va hosildorlik",
                "variant": ["Farovonlik va hosildorlik", "Adolat", "Erkinlik", "Barqarorlik"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat ramzlaridan biri?",
                "answer": "Bayroq",
                "variant": ["Bayroq", "Gerb", "Madhiy", "Konstitutsiya"]
            },
            {
                "question": "Yer sharida eng katta tog‘ tizmalari qaysi qit’ada joylashgan?",
                "answer": "Osiyo",
                "variant": ["Osiyo", "Afrika", "Yevropa", "Amerika"]
            },
            {
                "question": "Buyuk yozuvchi Firdavsiy mashhur eposi?",
                "answer": "Shohnoma",
                "variant": ["Shohnoma", "Devonu lug‘otit turk", "Xamsa", "Sarob"]
            },
            {
                "question": "O‘zbekiston Respublikasining milliy sport turi?",
                "answer": "Kurash",
                "variant": ["Kurash", "Futbol", "Boks", "Tennis"]
            },
            {
                "question": "Buyuk yozuvchi Cho‘lpon mashhur dramasi?",
                "answer": "Yorqinoy",
                "variant": ["Yorqinoy", "Kecha va kunduz", "Shohnoma", "Tong nafasi"]
            },
            {
                "question": "O‘zbekiston Respublikasining Konstitutsiyasi nechta moddadan iborat?",
                "answer": "128",
                "variant": ["128", "121", "130", "100"]
            },
            {
                "question": "O‘zbekiston Respublikasida qabul qilingan birinchi Konstitutsiya qachon e’lon qilingan?",
                "answer": "1992-yil",
                "variant": ["1992-yil", "1991-yil", "1993-yil", "1994-yil"]
            },
            {
                "question": "Yer sharidagi eng mashhur tog‘ cho‘qqilaridan biri?",
                "answer": "Elbrus",
                "variant": ["Elbrus", "Everest", "Kilimanjaro", "Montblan"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat madhiyasi musiqasini kim bastalagan?",
                "answer": "Mutal Burhonov",
                "variant": ["Mutal Burhonov", "Abdulla Oripov", "Botir Zokirov", "Erkin Vohidov"]
            },
            {
                "question": "Yer sharidagi eng katta tog‘ tizmasi qaysi?",
                "answer": "And tog‘lari",
                "variant": ["And tog‘lari", "Alp", "Gimolay", "Tyan-Shan"]
            },
            {
                "question": "Buyuk yozuvchi Abdulla Qodiriy mashhur romani?",
                "answer": "O‘tkan kunlar",
                "variant": ["O‘tkan kunlar", "Mehrobdan chayon", "Sarob", "Qiyomat"]
            },
            {
                "question": "O‘zbekistonning eng katta viloyati hududi bo‘yicha?",
                "answer": "Qashqadaryo",
                "variant": ["Qashqadaryo", "Buxoro", "Surxondaryo", "Navoiy"]
            },
            {
                "question": "Buyuk yozuvchi Cho‘lpon mashhur she’rlaridan biri?",
                "answer": "Ona tilim",
                "variant": ["Ona tilim", "Sarob", "Tong nafasi", "Shohnoma"]
            },
            {
                "question": "O‘zbekiston davlat bayrog‘idagi yashil rang nimani anglatadi?",
                "answer": "Tabiat va yangilanish",
                "variant": ["Tabiat va yangilanish", "Hosildorlik", "Adolat", "Farovonlik"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan eng mashhur me’moriy obidalaridan biri?",
                "answer": "Registon",
                "variant": ["Registon", "Ark", "Ko‘kaldosh", "Hazrati Imam"]
            },
            {
                "question": "Yer sharidagi eng mashhur muz saroyi qaysi davlatda?",
                "answer": "Rossiya",
                "variant": ["Rossiya", "Kanada", "Norvegiya", "Shvetsiya"]
            },
            {
                "question": "Buyuk yozuvchi O‘tkir Hoshimov mashhur qissalaridan biri?",
                "answer": "Ikki eshik orasi",
                "variant": ["Ikki eshik orasi", "Dunyoning ishlari", "Yulduzli tunlar", "Shohnoma"]
            },
            {
                "question": "O‘zbekiston davlat gerbidagi paxta nimani bildiradi?",
                "answer": "Boylik va farovonlik",
                "variant": ["Boylik va farovonlik", "Hosildorlik", "Adolat", "Ona tabiat"]
            },
            {
                "question": "Buyuk yozuvchi Pirimqul Qodirov mashhur asarlaridan biri?",
                "answer": "Yulduzli tunlar",
                "variant": ["Yulduzli tunlar", "Avlodlar dovoni", "Sarob", "Shohnoma"]
            },
            {
                "question": "O‘zbekiston Respublikasining eng katta shaharlaridan biri?",
                "answer": "Namangan",
                "variant": ["Namangan", "Andijon", "Buxoro", "Samarqand"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat bayrog‘idagi oq rang nimani anglatadi?",
                "answer": "Poklik va tinchlik",
                "variant": ["Poklik va tinchlik", "Adolat", "Hosildorlik", "Barqarorlik"]
            },
            {
                "question": "Yer sharida eng sovuq dengiz?",
                "answer": "Sibir",
                "variant": ["O‘lik dengiz", "Qora dengiz", "Kaspiy", "Sibir"]
            },
            {
                "question": "Buyuk yozuvchi Navoiy mashhur dostonlaridan biri?",
                "answer": "Layli va Majnun",
                "variant": ["Layli va Majnun", "Shohnoma", "Farhod va Shirin", "Sarob"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat bayrog‘ida nechta rang mavjud?",
                "answer": "4",
                "variant": ["3", "4", "5", "2"]
            },
            {
                "question": "O‘zbekiston Respublikasining Konstitutsiyasi nechta bobdan iborat?",
                "answer": "26",
                "variant": ["26", "25", "30", "22"]
            },
            {
                "question": "Buyuk yozuvchi Cho‘lpon mashhur she’riy turkumlaridan biri?",
                "answer": "Buloqlar",
                "variant": ["Buloqlar", "Tong nafasi", "Shohnoma", "Sarob"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat gerbidagi quyosh nimani bildiradi?",
                "answer": "Kelajak va baxt",
                "variant": ["Kelajak va baxt", "Adolat", "Farovonlik", "Tabiat"]
            },
            {
                "question": "Buyuk yozuvchi O‘tkir Hoshimov mashhur romani?",
                "answer": "Dunyoning ishlari",
                "variant": ["Dunyoning ishlari", "Ikki eshik orasi", "Shohnoma", "Sarob"]
            },
            {
                "question": "O‘zbekiston Respublikasining Konstitutsiyasi nechta modda o‘z ichiga olgan?",
                "answer": "128",
                "variant": ["128", "130", "121", "115"]
            },
            {
                "question": "O‘zbekiston Respublikasining mustaqilligi qachon e’lon qilingan?",
                "answer": "1991-yil 1-sentyabr",
                "variant": ["1991-yil 1-sentyabr", "1992-yil 8-dekabr", "1990-yil 20-iyun", "1994-yil 21-mart"]
            },
            {
                "question": "O‘zbekiston Respublikasining Konstitutsiyasi nechta qismdan iborat?",
                "answer": "6",
                "variant": ["6", "5", "7", "8"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat bayrog‘idagi ko‘k rang nimani bildiradi?",
                "answer": "Osmon va tinchlik",
                "variant": ["Osmon va tinchlik", "Adolat", "Hosildorlik", "Ona tabiat"]
            },
            {
                "question": "Buyuk yozuvchi Cho‘lpon mashhur romani?",
                "answer": "Kecha va kunduz",
                "variant": ["Kecha va kunduz", "Shohnoma", "Sarob", "Oltin vodiydan"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat madhiyasi so‘zlarini kim yozgan?",
                "answer": "Abdulla Oripov",
                "variant": ["Abdulla Oripov", "Erkin Vohidov", "Cho‘lpon", "O‘tkir Hoshimov"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat gerbidagi Humo qushi nimani bildiradi?",
                "answer": "Baxt va erkinlik",
                "variant": ["Baxt va erkinlik", "Adolat", "Tabiat", "Hosildorlik"]
            },
            {
                "question": "Yer sharida eng katta arxipelag qaysi?",
                "answer": "Indoneziya",
                "variant": ["Indoneziya", "Filippin", "Maldiv", "Yaponiya"]
            },
            {
                "question": "O‘zbekiston Respublikasining Konstitutsiya mualliflaridan biri kim?",
                "answer": "Islom Karimov",
                "variant": ["Islom Karimov", "Shavkat Mirziyoyev", "Abdulla Qodiriy", "Cho‘lpon"]
            },
            {
                "question": "Yer sharida eng uzun metro tarmog‘i qaysi shaharda?",
                "answer": "Pekin",
                "variant": ["Pekin", "London", "Moskva", "Nyu-York"]
            },
            {
                "question": "O‘zbekiston Respublikasi bayrog‘idagi 12 yulduz nimani bildiradi?",
                "answer": "Viloyatlar va Qoraqalpog‘istonni",
                "variant": ["Viloyatlar va Qoraqalpog‘istonni", "12 oy", "12 xalq", "12 ramz"]
            },
            {
                "question": "Eng qadimiy shaharlaridan biri — Ur qaysi davlat hududida joylashgan?",
                "answer": "Iroq",
                "variant": ["Iroq", "Eron", "Suriya", "Misr"]
            },
            {
                "question": "O‘zbek adabiyotining “Cho‘lpon” taxallusi ma’nosi nima?",
                "answer": "Tong yulduzi",
                "variant": ["Tong yulduzi", "Oy", "Yorug‘lik", "Quyosh"]
            },
            {
                "question": "Yer sharidagi eng baland mustaqil minora?",
                "answer": "Tokio minorasi",
                "variant": ["Tokio minorasi", "Eiffel minorasi", "CN Tower", "Burj Xalifa"]
            },
            {
                "question": "O‘zbekistonning eng yirik shaharlaridan biri Farg‘ona qaysi viloyat markazi?",
                "answer": "Farg‘ona viloyati",
                "variant": ["Farg‘ona viloyati", "Andijon viloyati", "Namangan viloyati", "Toshkent viloyati"]
            },
            {
                "question": "Yer sharidagi eng chuqur joy — Mariana chuqurligi qaysi okeanda?",
                "answer": "Tinch okeani",
                "variant": ["Tinch okeani", "Hind okeani", "Atlantika okeani", "Shimoliy muz okeani"]
            },
            {
                "question": "O‘zbekiston Respublikasining asosiy qonuni nima?",
                "answer": "Konstitutsiya",
                "variant": ["Konstitutsiya", "Madhiy", "Gerb", "Bayroq"]
            },
            {
                "question": "Dunyoning eng mashhur sharsharalaridan biri — Viktoriya qayerda joylashgan?",
                "answer": "Zambiya va Zimbabve",
                "variant": ["Zambiya va Zimbabve", "Braziliya va Argentina", "Venesuela", "AQSh va Kanada"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur tarixiy shahar — Samarqand qachon asos solingan?",
                "answer": "2700 yil avval",
                "variant": ["2700 yil avval", "2000 yil avval", "1500 yil avval", "1000 yil avval"]
            },
            {
                "question": "Dunyoning eng mashhur universitetlaridan biri — Tokio universiteti qayerda joylashgan?",
                "answer": "Yaponiya",
                "variant": ["Yaponiya", "Xitoy", "Janubiy Koreya", "Singapur"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Cho‘lpon mashhur asari?",
                "answer": "Yorqinoy",
                "variant": ["Yorqinoy", "Kecha va kunduz", "Buloqlar", "Tong nafasi"]
            },
            {
                "question": "Dunyoning eng mashhur san’at muzeylaridan biri — Luvr qayerda joylashgan?",
                "answer": "Parij",
                "variant": ["Parij", "London", "Madrid", "Berlin"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaharlaridan biri — Urganch qaysi vohada joylashgan?",
                "answer": "Xorazm vohasi",
                "variant": ["Xorazm vohasi", "Farg‘ona vohasi", "Surxondaryo vohasi", "Qashqadaryo vohasi"]
            },
            {
                "question": "Dunyoning eng mashhur tog‘ cho‘qqilaridan biri — Montblan qayerda joylashgan?",
                "answer": "Fransiya va Italiya",
                "variant": ["Fransiya va Italiya", "Shveytsariya", "Avstriya", "Ispaniya"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Tohir Malik mashhur kitobi?",
                "answer": "Shaytanat",
                "variant": ["Shaytanat", "O‘tkan kunlar", "Yulduzli tunlar", "Sarob"]
            },
            {
                "question": "Osiyodagi eng mashhur daryolardan biri?",
                "answer": "Ganga",
                "variant": ["Ganga", "Yanszi", "Amur", "Mekong"]
            },
            {
                "question": "Dunyoning eng mashhur sportchilaridan biri — Usayn Bolt qaysi sport turi bo‘yicha mashhur?",
                "answer": "Yugurish",
                "variant": ["Yugurish", "Futbol", "Tennis", "Suzish"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur qadimiy qal’alardan biri — Topraqqal’a qaysi davrga oid?",
                "answer": "Kushon davriga",
                "variant": ["Kushon davriga", "Temuriylar davriga", "Arab xalifaligi davriga", "Sovet davriga"]
            },
            {
                "question": "Dunyoning eng mashhur minoralaridan biri — Burj Xalifa qayerda joylashgan?",
                "answer": "BAA",
                "variant": ["BAA", "Saudiya Arabistoni", "Katar", "Kuvayt"]
            },
            {
                "question": "O‘zbekistonning mashhur shoirlaridan biri — G‘afur G‘ulom mashhur asari?",
                "answer": "Shum bola",
                "variant": ["Shum bola", "Sarob", "Anor", "O‘tkan kunlar"]
            },
            {
                "question": "Shimoliy Amerikadagi eng katta ko‘rfaz?",
                "answer": "Meksika ko‘rfazi",
                "variant": ["Meksika ko‘rfazi", "Bengal ko‘rfazi", "Pers ko‘rfazi", "Aden ko‘rfazi"]
            },
            {
                "question": "Dunyoning eng baland vulqon?",
                "answer": "Etna",
                "variant": ["Ojos del Salado", "Etna", "Fudziyama", "Vezuviy"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Oybek mashhur romani?",
                "answer": "Navoiy",
                "variant": ["Navoiy", "Sarob", "Kecha va kunduz", "Yulduzli tunlar"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur tarixiy yodgorliklardan biri — Minorai Kalon qayerda?",
                "answer": "Buxoro",
                "variant": ["Buxoro", "Samarqand", "Xiva", "Toshkent"]
            },
            {
                "question": "Dunyoning eng mashhur orollardan biri — Bali qaysi davlatda joylashgan?",
                "answer": "Indoneziya",
                "variant": ["Indoneziya", "Filippin", "Malayziya", "Tailand"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur maqbaralardan biri — Shohizinda majmuasi qayerda joylashgan?",
                "answer": "Samarqand",
                "variant": ["Samarqand", "Buxoro", "Xiva", "Shahrisabz"]
            },
            {
                "question": "Dunyoning eng mashhur futbol jamoalaridan biri — Juventus qayerda joylashgan?",
                "answer": "Italiya",
                "variant": ["Italiya", "Ispaniya", "Fransiya", "Angliya"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Mirzo Ulug‘bek qaysi sohaga ko‘proq hissa qo‘shgan?",
                "answer": "Astronomiya",
                "variant": ["Astronomiya", "Matematika", "Tibbiyot", "Kimyo"]
            },
            {
                "question": "Osiyodagi eng katta ko‘rfaz?",
                "answer": "Bengal ko‘rfazi",
                "variant": ["Bengal ko‘rfazi", "Pers ko‘rfazi", "Meksika ko‘rfazi", "Aden ko‘rfazi"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — O‘tkir Hoshimov mashhur qissasi?",
                "answer": "Bahor qaytmaydi",
                "variant": ["Bahor qaytmaydi", "Ikki eshik orasi", "Dunyoning ishlari", "Sarob"]
            },
            {
                "question": "Dunyoning eng mashhur tog‘ tizmalardan biri — Alp qaysi qit’ada joylashgan?",
                "answer": "Yevropa",
                "variant": ["Yevropa", "Osiyo", "Janubiy Amerika", "Afrika"]
            },
            {
                "question": "O‘zbekistonning mashhur shoirlaridan biri — Erkin Vohidov mashhur dramasi?",
                "answer": "Oltin devor",
                "variant": ["Oltin devor", "Sarob", "Shohnoma", "Yulduzli tunlar"]
            },
            {
                "question": "Dunyoning eng mashhur sharsharalaridan biri — Seljalandsfoss qayerda joylashgan?",
                "answer": "Islandiya",
                "variant": ["Islandiya", "Norvegiya", "Shvetsiya", "Finlyandiya"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur tarixiy majmualardan biri — Ichan qal’a qayerda joylashgan?",
                "answer": "Xiva",
                "variant": ["Xiva", "Buxoro", "Samarqand", "Andijon"]
            },
            {
                "question": "Dunyoning eng mashhur futbol jamoalaridan biri — PSG qayerda joylashgan?",
                "answer": "Parij",
                "variant": ["Parij", "Madrid", "Milan", "Manchester"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Cho‘lpon mashhur she’ri?",
                "answer": "Ona tilim",
                "variant": ["Ona tilim", "Tong nafasi", "Sarob", "Ruhlar isyoni"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur tarixiy obidalardan biri — Ark qal’asi qayerda joylashgan?",
                "answer": "Buxoro",
                "variant": ["Buxoro", "Samarqand", "Toshkent", "Shahrisabz"]
            },
            {
                "question": "Dunyoning eng mashhur minoralaridan biri — Big Ben qayerda joylashgan?",
                "answer": "London",
                "variant": ["London", "Parij", "Berlin", "Madrid"]
            },
            {
                "question": "O‘zbekistonning mashhur shoirlaridan biri — Abdulla Oripov mashhur dostoni?",
                "answer": "Sohibqiron",
                "variant": ["Sohibqiron", "Sarob", "Jannatga yo‘l", "O‘zbekiston"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Pirimqul Qodirov mashhur kitobi?",
                "answer": "Qora ko‘zlar",
                "variant": ["Qora ko‘zlar", "Avlodlar dovoni", "Yulduzli tunlar", "Sarob"]
            },
            {
                "question": "Dunyoning eng mashhur muzliklaridan biri — Vatnajokull qayerda joylashgan?",
                "answer": "Islandiya",
                "variant": ["Islandiya", "Norvegiya", "Kanada", "Grenlandiya"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy obidalaridan biri — Bibi Xonim masjidi qayerda joylashgan?",
                "answer": "Samarqand",
                "variant": ["Samarqand", "Buxoro", "Xiva", "Toshkent"]
            },
            {
                "question": "Dunyoning eng mashhur futbol jamoalaridan biri — Milan qayerda joylashgan?",
                "answer": "Italiya",
                "variant": ["Italiya", "Ispaniya", "Fransiya", "Angliya"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Abdulla Qahhor mashhur qissasi?",
                "answer": "Oltin yulduz",
                "variant": ["Oltin yulduz", "Sarob", "Anor", "Sinchalak"]
            },
            {
                "question": "Osiyodagi eng usun tog‘ tizmasi?",
                "answer": "Himolay",
                "variant": ["Tyan-Shan", "Pamir", "Altay", "Himolay"]
            },
            {
                "question": "O‘zbekistonning mashhur shoirlaridan biri — Erkin Vohidov mashhur she’ri?",
                "answer": "Nido",
                "variant": ["Nido", "Ruhlar isyoni", "Tong nafasi", "O‘zbekiston"]
            },
            {
                "question": "Dunyoning eng mashhur sharsharalaridan biri — Plitvice qayerda joylashgan?",
                "answer": "Xorvatiya",
                "variant": ["Xorvatiya", "Sloveniya", "Chexiya", "Serbiya"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur tarixiy qal’alardan biri — Ayazqal’a qayerda joylashgan?",
                "answer": "Qoraqalpog‘iston",
                "variant": ["Qoraqalpog‘iston", "Buxoro", "Xorazm", "Samarqand"]
            },
            {
                "question": "Dunyoning eng mashhur sportchilardan biri — Diego Maradona qaysi davlat fuqarosi edi?",
                "answer": "Argentina",
                "variant": ["Argentina", "Braziliya", "Ispaniya", "Urugvay"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Tohir Malik mashhur hikoyasi?",
                "answer": "So‘nggi o‘q",
                "variant": ["So‘nggi o‘q", "Shaytanat", "Sarob", "Bahor qaytmaydi"]
            },
            {
                "question": "Dunyoning eng mashhur orollardan biri — Yangi Gvineya qaysi okeanda joylashgan?",
                "answer": "Tinch okeani",
                "variant": ["Tinch okeani", "Hind okeani", "Atlantika okeani", "Shimoliy muz okeani"]
            },
            {
                "question": "O‘zbekistonning mashhur shoirlaridan biri — G‘afur G‘ulom mashhur she’ri?",
                "answer": "Sen yetim emassan",
                "variant": ["Sen yetim emassan", "Shum bola", "Sarob", "Yulduzli tunlar"]
            },
            {
                "question": "Dunyoning eng mashhur minoralaridan biri — Ostankino minorasi qayerda joylashgan?",
                "answer": "Moskva",
                "variant": ["Moskva", "Sankt-Peterburg", "Novosibirsk", "Minsk"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Cho‘lpon mashhur hikoyasi?",
                "answer": "Sevgi va hayot",
                "variant": ["Sevgi va hayot", "Yorqinoy", "Kecha va kunduz", "Buloqlar"]
            },
            {
                "question": "Dunyoning eng mashhur teatrlaridan biri — Bolshoy teatri qaysi shaharda joylashgan?",
                "answer": "Moskva",
                "variant": ["Moskva", "Parij", "London", "Berlin"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaharlaridan biri — Jizzax qaysi yo‘lda muhim nuqta bo‘lgan?",
                "answer": "Buyuk Ipak yo‘li",
                "variant": ["Buyuk Ipak yo‘li", "Arab savdo yo‘li", "Buyuk ipak dengiz yo‘li", "Yevropa savdo yo‘li"]
            },
            {
                "question": "Buyuk geografik kashfiyotlar davrida Amerikani ochgan kishi kim?",
                "answer": "Xristofor Kolumb",
                "variant": ["Xristofor Kolumb", "Vasko da Gama", "Magellan", "Amerigo Vespucci"]
            }
        ]
    
        quiz_9 = [
            {
                "question": "Qaysi davlatning poytaxti Addis-Abeba?",
                "answer": "Efiopiya",
                "variant": ["Efiopiya", "Sudan", "Nigeriya", "Uganda"]
            },
            {
                "question": "O‘zbekiston hududidagi eng qadimiy buddaviylik yodgorligi?",
                "answer": "Fayoztepa",
                "variant": ["Topraq-qal’a", "Qiziltepa", "Fayoztepa", "Qal’aliqir"]
            },
            {
                "question": "Dunyodagi eng ko‘p rasmiy tilga ega mamlakat?",
                "answer": "Janubiy Afrika",
                "variant": ["Kanada", "Shveytsariya", "Janubiy Afrika", "Belgiya"]
            },
            {
                "question": "Yer yuzidagi eng baland faol vulqon?",
                "answer": "Kilimanjaro",
                "variant": ["Fudziyama", "Kilimanjaro", "Etna", "Vezuviy"]
            },
            {
                "question": "O‘zbekistonda 'Qatag‘on qurbonlari xotirasi kuni' qachon?",
                "answer": "31-avgust",
                "variant": ["9-may", "8-dekabr", "31-avgust", "1-sentyabr"]
            },
            {
                "question": "Dunyodagi eng katta yarim yopiq dengiz?",
                "answer": "Kaspiy dengizi",
                "variant": ["O‘lik dengiz", "Qora dengiz", "Adriatika dengizi", "Kaspiy dengizi"]
            },
            {
                "question": "'1984' romanining muallifi kim?",
                "answer": "Jorj Oruell",
                "variant": ["F. Kafka", "Jorj Oruell", "E. Xeminguey", "Ch. Dikkens"]
            },
            {
                "question": "Yaponiyaning milliy pul birligi?",
                "answer": "Yen",
                "variant": ["Won", "Peso", "Dollar", "Yen"]
            },
            {
                "question": "Markaziy Osiyodagi eng chuqur ko‘l?",
                "answer": "Issiqko‘l",
                "variant": ["Sarezko‘l", "Issiqko‘l", "Qorako‘l", "Aydarko‘l"]
            },
            {
                "question": "Ibn Sinoning mashhur asari?",
                "answer": "Tib qonunlari",
                "variant": ["Xamsa", "Avesto", "Tib qonunlari", "Donishnoma"]
            },
            {
                "question": "Qaysi davlat 'Tinch okeani orollari federatsiyasi' deb ataladi?",
                "answer": "Mikroneziya",
                "variant": ["Mikroneziya", "Fiji", "Tonga", "Kiribati"]
            },
            {
                "question": "Eng uzoq yashovchi daraxt turi?",
                "answer": "Sekvoyya",
                "variant": ["Tol", "Sekvoyya", "Eman", "Qayin"]
            },
            {
                "question": "Yevropada 'Qora o‘lim' deb atalgan ofat nima edi?",
                "answer": "Vabo",
                "variant": ["Gripp", "Tif", "Chechak", "Vabo"]
            },
            {
                "question": "Al-Xorazmiy mashhur asari?",
                "answer": "Al-jabr va al-muqobala",
                "variant": ["Bayt ul-hikma", "Al-jabr va al-muqobala", "Tib qonunlari", "Qutadg‘u bilig"]
            },
            {
                "question": "Osiyodagi eng kichik davlat?",
                "answer": "Maldiv orollari",
                "variant": ["Butan", "Bruney", "Maldiv orollari", "Nepal"]
            },
            {
                "question": "Dunyoning eng baland platosi?",
                "answer": "Tibet platosi",
                "variant": ["Altay", "And", "Tibet platosi", "Pamir"]
            },
            {
                "question": "Qadimgi Mesopotamiya qaysi hududda joylashgan edi?",
                "answer": "Ikki daryo oralig‘i",
                "variant": ["Arabiston", "Ikki daryo oralig‘i", "Eron", "Misr"]
            },
            {
                "question": "'Jarayon' romanining muallifi kim?",
                "answer": "Frans Kafka",
                "variant": ["Frans Kafka", "Balzak", "Alber Kamyu", "Sartre"]
            },
            {
                "question": "Ulug‘bek rasadxonasi qaysi shaharda joylashgan?",
                "answer": "Samarqand",
                "variant": ["Xiva", "Samarqand", "Buxoro", "Toshkent"]
            },
            {
                "question": "Qaysi davlatning poytaxti Naypyido?",
                "answer": "Myanma",
                "variant": ["Kambodja", "Laos", "Myanma", "Malayziya"]
            },
            {
                "question": "Yevropadagi eng baland tog‘?",
                "answer": "Elbrus",
                "variant": ["Montblan", "Elbrus", "Alp", "Kavkaz"]
            },
            {
                "question": "O‘zbekiston hududidagi eng qadimiy shahar?",
                "answer": "Termiz",
                "variant": ["Buxoro", "Xiva", "Samarqand", "Termiz"]
            },
            {
                "question": "Yer sharining eng yirik ko‘rfazi?",
                "answer": "Bengal ko‘rfazi",
                "variant": ["Aden ko‘rfazi", "Meksika ko‘rfazi", "Pers ko‘rfazi", "Bengal ko‘rfazi"]
            },
            {
                "question": "Qaysi davlatda Machu-Pikchu joylashgan?",
                "answer": "Peru",
                "variant": ["Boliviya", "Peru", "Argentina", "Meksika"]
            },
            {
                "question": "Buyuk astronom Ptolemey qaysi shaharda yashagan?",
                "answer": "Iskandariya",
                "variant": ["Iskandariya", "Afina", "Rim", "Qohira"]
            },
            {
                "question": "Yer yuzidagi eng baland sharshara?",
                "answer": "Anxel",
                "variant": ["Niagara", "Victoria", "Anxel", "Iguasu"]
            },
            {
                "question": "Markaziy Osiyodagi eng baland cho‘qqi?",
                "answer": "Somoni cho‘qqisi",
                "variant": ["Bobotog‘", "Somoni cho‘qqisi", "Hazrati Sulton", "Tyan-Shan"]
            },
            {
                "question": "O‘zbekiston hududidan o‘tgan qadimiy daryo?",
                "answer": "Oks (Amudaryo)",
                "variant": ["Sirdaryo", "Oks (Amudaryo)", "Zarafshon", "Chirchiq"]
            },
            {
                "question": "Yer sharidagi eng sovuq aholi punkti?",
                "answer": "Oymyakon",
                "variant": ["Yakutsk", "Oymyakon", "Norilsk", "Reykyavik"]
            },
            {
                "question": "Qaysi yozuvchi 'Sarguzashtlar oroli' asarini yozgan?",
                "answer": "Robert Luis Stivenson",
                "variant": ["Daniel Defo", "Robert Luis Stivenson", "Jek London", "Mark Tven"]
            },
            {
                "question": "Buyuk Ipak yo‘li orqali O‘zbekistonga kelgan mashhur sayyoh?",
                "answer": "Marko Polo",
                "variant": ["Ibn Battuta", "Marko Polo", "Kolumb", "Hudson"]
            },
            {
                "question": "Yer kurrasidagi eng katta tekislik?",
                "answer": "Amazon tekisligi",
                "variant": ["Afrika tekisligi", "Amazon tekisligi", "Sibir tekisligi", "Kanada tekisligi"]
            },
            {
                "question": "Qaysi davlatda Viktoriya sharsharasi joylashgan?",
                "answer": "Zambiya va Zimbabve",
                "variant": ["Tanzaniya", "Zambiya va Zimbabve", "Uganda", "Mozambik"]
            },
            {
                "question": "Qaysi yozuvchi 'Qariya va dengiz' asarini yozgan?",
                "answer": "Ernest Xeminguey",
                "variant": ["Ernest Xeminguey", "Dreiser", "Balzak", "London"]
            },
            {
                "question": "Dunyodagi eng katta ko‘prik qaysi davlatda?",
                "answer": "Xitoy",
                "variant": ["AQSh", "Xitoy", "Fransiya", "Kanada"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan eng katta qo‘rg‘on?",
                "answer": "Toproq qal’a",
                "variant": ["Toproq qal’a", "Ayazqal’a", "Ark", "Xiva qal’asi"]
            },
            {
                "question": "Qaysi davlatning milliy sporti kriket?",
                "answer": "Hindiston",
                "variant": ["Hindiston", "Avstraliya", "Angliya", "Pokiston"]
            },
            {
                "question": "Yer yuzidagi eng uzun devor?",
                "answer": "Xitoy devori",
                "variant": ["Xitoy devori", "Hadrian devori", "Berlin devori", "Bobil devori"]
            },
            {
                "question": "Dunyodagi eng katta orollardan biri — Yangi Gvineya qaysi okeanda joylashgan?",
                "answer": "Tinch okeani",
                "variant": ["Hind okeani", "Tinch okeani", "Atlantika okeani", "Shimoliy muz okeani"]
            },
            {
                "question": "O‘zbekiston hududidagi eng mashhur maqbara?",
                "answer": "Shohi Zinda",
                "variant": ["Shohi Zinda", "Ismoil Somoniy maqbarasi", "Gur Amir", "Hazrati Imam"]
            },
            {
                "question": "Qaysi yozuvchi 'Xamsa'ni yaratgan?",
                "answer": "Alisher Navoiy",
                "variant": ["Bobur", "Cho‘lpon", "Alisher Navoiy", "Shakespeare"]
            },
            {
                "question": "Qaysi davlatni 'Ko‘l mamlakati' deb atashadi?",
                "answer": "Finlyandiya",
                "variant": ["Shvetsiya", "Norvegiya", "Finlyandiya", "Islandiya"]
            },
            {
                "question": "Yer yuzidagi eng chuqur okean joyi?",
                "answer": "Mariana chuqurligi",
                "variant": ["Puerto-Riko chuqurligi", "Tonga chuqurligi", "Filippin chuqurligi", "Mariana chuqurligi"]
            },
            {
                "question": "Qaysi yozuvchi 'Faust' asarini yozgan?",
                "answer": "Gyote",
                "variant": ["Gyote", "Shiller", "Balzak", "Hamsun"]
            },
            {
                "question": "Dunyoning eng katta daryosi suv hajmi bo‘yicha?",
                "answer": "Amazonka",
                "variant": ["Amazonka", "Nil", "Yanszi", "Missisipi"]
            },
            {
                "question": "Qaysi davlat poytaxti Karakas?",
                "answer": "Venesuela",
                "variant": ["Kolumbiya", "Venesuela", "Ekvador", "Peru"]
            },
            {
                "question": "Yer sharidagi eng ko‘p muzliklar qaysi qit’ada?",
                "answer": "Antarktida",
                "variant": ["Antarktida", "Shimoliy Amerika", "Osiyo", "Yevropa"]
            },
            {
                "question": "Qaysi yozuvchi 'Otello' tragediyasini yozgan?",
                "answer": "Shakespeare",
                "variant": ["Shakespeare", "Tolstoy", "Chexov", "Dante"]
            },
            {
                "question": "Buyuk Britaniya qaysi qit’ada joylashgan?",
                "answer": "Yevropa",
                "variant": ["Avstraliya", "Osiyo", "Yevropa", "Afrika"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan qadimiy qal’alar majmuasi?",
                "answer": "Ellikqal’a",
                "variant": ["Ellikqal’a", "Ark", "Ko‘kaldosh", "Ayazqal’a"]
            },
            {
                "question": "Qaysi yozuvchi 'Don Kixot' asarini yozgan?",
                "answer": "Servantes",
                "variant": ["Servantes", "Shakespeare", "Balzak", "Gyote"]
            },
            {
                "question": "Yer kurrasida eng ko‘p aholiga ega shahar?",
                "answer": "Tokio",
                "variant": ["Shanxay", "Tokio", "Mumbay", "Meksiko"]
            },
            {
                "question": "Qaysi davlatda Amazonka daryosi oqib o‘tadi?",
                "answer": "Braziliya",
                "variant": ["Braziliya", "Argentina", "Peru", "Kolumbiya"]
            },
            {
                "question": "O‘zbekiston hududidagi eng qadimiy maqbara?",
                "answer": "Ismoil Somoniy maqbarasi",
                "variant": ["Shohi Zinda", "Ismoil Somoniy maqbarasi", "Gur Amir", "Hazrati Imam"]
            },
            {
                "question": "Qaysi yozuvchi 'Qiyomat' romanini yozgan?",
                "answer": "Chingiz Aytmatov",
                "variant": ["Chingiz Aytmatov", "Oybek", "Cho‘lpon", "Erkin Vohidov"]
            },
            {
                "question": "Dunyodagi eng katta okean oqimi?",
                "answer": "Gulfstrim",
                "variant": ["Gulfstrim", "Oyashio", "Peru oqimi", "Bengal oqimi"]
            },
            {
                "question": "Afrikaning eng katta davlati maydon jihatdan?",
                "answer": "Jazoir",
                "variant": ["Misr", "Efiopiya", "Jazoir", "Nigeriya"]
            },
            {
                "question": "Qaysi davlatning poytaxti Islombul (Istanbul emas, tarixda)?",
                "answer": "Vizantiya imperiyasi",
                "variant": ["Vizantiya imperiyasi", "Usmoniylar davlati", "Rim", "Sparta"]
            },
            {
                "question": "Buyuk olim Beruniy qaysi shaharda tug‘ilgan?",
                "answer": "Xorazm",
                "variant": ["Xorazm", "Buxoro", "Samarqand", "Nishopur"]
            },
            {
                "question": "Yer sharidagi eng katta orol davlati?",
                "answer": "Avstraliya",
                "variant": ["Avstraliya", "Madagaskar", "Grenlandiya", "Yangi Zelandiya"]
            },
            {
                "question": "Qaysi yozuvchi 'Anna Karenina' asarini yozgan?",
                "answer": "Lev Tolstoy",
                "variant": ["Lev Tolstoy", "Dostoyevskiy", "Pushkin", "Chexov"]
            },
            {
                "question": "Buyuk olim Arximed qayerda tug‘ilgan?",
                "answer": "Sirakuza",
                "variant": ["Afina", "Sirakuza", "Rim", "Iskandariya"]
            },
            {
                "question": "O‘zbekiston hududidagi eng baland tog‘ cho‘qqisi?",
                "answer": "Hazrati Sulton",
                "variant": ["Hazrati Sulton", "Somoni cho‘qqisi", "Bobotog‘", "Chimyon"]
            },
            {
                "question": "Yer kurrasida eng issiq joy qaysi cho‘l?",
                "answer": "Lut cho‘li",
                "variant": ["Lut cho‘li", "Sahroi Kabir", "Gobi", "Karakum"]
            },
            {
                "question": "Qaysi yozuvchi 'Qizil va qora' romanini yozgan?",
                "answer": "Stendal",
                "variant": ["Stendal", "Balzak", "Flaubert", "Gyote"]
            },
            {
                "question": "Dunyodagi eng chuqur ko‘l?",
                "answer": "Baykal",
                "variant": ["Baykal", "Tanganika", "Viktoriya", "Chad"]
            },
            {
                "question": "O‘zbek xalq dostonlaridan biri?",
                "answer": "Alpomish",
                "variant": ["Alpomish", "Manas", "Shohnoma", "Qutadg‘u bilig"]
            },
            {
                "question": "Qaysi davlatning poytaxti Buenos-Ayres?",
                "answer": "Argentina",
                "variant": ["Argentina", "Braziliya", "Urugvay", "Paragvay"]
            },
            {
                "question": "Buyuk Ipak yo‘lining asosiy markazlaridan biri?",
                "answer": "Samarqand",
                "variant": ["Samarqand", "Buxoro", "Xiva", "Urganch"]
            },
            {
                "question": "Qaysi yozuvchi 'Jinoyat va jazo' romanini yozgan?",
                "answer": "Dostoyevskiy",
                "variant": ["Dostoyevskiy", "Tolstoy", "Pushkin", "Gogol"]
            },
            {
                "question": "Yer kurrasida eng baland tog‘ tizmasi?",
                "answer": "Gimolay",
                "variant": ["Gimolay", "And", "Alp", "Kavkaz"]
            },
            {
                "question": "Buyuk yozuvchi Gyote qaysi asari bilan mashhur?",
                "answer": "Faust",
                "variant": ["Faust", "Otello", "Anna Karenina", "Qariya va dengiz"]
            },
            {
                "question": "Qaysi davlat 'Ko‘llar mamlakati' deb ataladi?",
                "answer": "Finlyandiya",
                "variant": ["Shvetsiya", "Finlyandiya", "Norvegiya", "Islandiya"]
            },
            {
                "question": "Dunyodagi eng uzun daryo?",
                "answer": "Nil",
                "variant": ["Nil", "Amazonka", "Yanszi", "Missisipi"]
            },
            {
                "question": "Qaysi yozuvchi 'Sariq devni minib' asarini yozgan?",
                "answer": "Xudoyberdi To‘xtaboyev",
                "variant": ["Xudoyberdi To‘xtaboyev", "Erkin Vohidov", "O‘tkir Hoshimov", "Abdulla Qahhor"]
            },
            {
                "question": "Yer sharida eng katta muzliklar massivi?",
                "answer": "Antarktida",
                "variant": ["Antarktida", "Grenlandiya", "Arktika", "Kanada"]
            },
            {
                "question": "Buyuk mutafakkir Platon qaysi shaharda tug‘ilgan?",
                "answer": "Afina",
                "variant": ["Rim", "Afina", "Sparta", "Delphi"]
            },
            {
                "question": "Qaysi davlatda Kilimanjaro tog‘i joylashgan?",
                "answer": "Tanzaniya",
                "variant": ["Keniya", "Uganda", "Efiopiya", "Tanzaniya"]
            },
            {
                "question": "O‘zbekistonning eng katta suv omborlaridan biri?",
                "answer": "Chorvoq",
                "variant": ["Tuyamo‘yin", "Chorvoq", "To‘dako‘l", "Qoratepa"]
            },
            {
                "question": "Qaysi yozuvchi 'Urush va tinchlik' asarini yozgan?",
                "answer": "Lev Tolstoy",
                "variant": ["Lev Tolstoy", "Pushkin", "Chexov", "Dostoyevskiy"]
            },
            {
                "question": "Dunyoning eng sovuq qit’asi?",
                "answer": "Antarktida",
                "variant": ["Antarktida", "Osiyo", "Shimoliy Amerika", "Yevropa"]
            },
            {
                "question": "Buyuk astronom Kopernik qanday nazariya yaratgan?",
                "answer": "Geotsentrik emas, geliosentrik",
                "variant": ["Geliosentrik", "Atom", "Kvark", "Nisbiylik"]
            },
            {
                "question": "Qaysi davlatda Burj Xalifa minorasi joylashgan?",
                "answer": "BAA",
                "variant": ["BAA", "Saudiya Arabistoni", "Qatar", "Kuvayt"]
            },
            {
                "question": "O‘zbekiston hududidagi eng qadimiy teatr?",
                "answer": "Navoi nomidagi teatr",
                "variant": ["Navoi nomidagi teatr", "Yosh tomoshabinlar teatri", "Ilhom teatri", "Qo‘qon teatri"]
            },
            {
                "question": "Qaysi yozuvchi 'Qutadg‘u bilig' asarini yozgan?",
                "answer": "Yusuf Xos Hojib",
                "variant": ["Yusuf Xos Hojib", "Mahmud Qoshg‘ariy", "Navoiy", "Beruniy"]
            },
            {
                "question": "Yer yuzidagi eng katta orol?",
                "answer": "Grenlandiya",
                "variant": ["Grenlandiya", "Madagaskar", "Yangi Gvineya", "Sumatra"]
            },
            {
                "question": "Qaysi davlatda Viktoriya ko‘li joylashgan?",
                "answer": "Afrika (Keniya, Tanzaniya, Uganda)",
                "variant": ["Afrika (Keniya, Tanzaniya, Uganda)", "Zambiya", "Efiopiya", "Mozambik"]
            },
            {
                "question": "Buyuk olim Nyuton qaysi qonunlari bilan mashhur?",
                "answer": "Harakat qonunlari",
                "variant": ["Gravitatsiya qonuni", "Harakat qonunlari", "Issiqlik qonuni", "Suyuqlik qonunlari"]
            },
            {
                "question": "Qaysi yozuvchi 'Shohnoma'ni yozgan?",
                "answer": "Firdavsiy",
                "variant": ["Firdavsiy", "Navoiy", "Bobur", "Beruniy"]
            },
            {
                "question": "Yer kurrasida eng katta tog‘ tizmasi qaysi qit’ada?",
                "answer": "Janubiy Amerika (And)",
                "variant": ["Janubiy Amerika (And)", "Osiyo (Gimolay)", "Yevropa (Alp)", "Afrika (Atlas)"]
            },
            {
                "question": "Qaysi yozuvchi 'Shaytonatlar' romanini yozgan?",
                "answer": "Tohir Malik",
                "variant": ["Tohir Malik", "Pirimqul Qodirov", "O‘tkir Hoshimov", "Abdulla Qahhor"]
            },
            {
                "question": "Qaysi davlatda Petra shahri joylashgan?",
                "answer": "Iordaniya",
                "variant": ["Iordaniya", "Suriya", "Livan", "Misr"]
            },
            {
                "question": "Dunyodagi eng katta yarim orollardan biri — Iberiya yarim oroli qaysi davlatlarga tegishli?",
                "answer": "Ispaniya va Portugaliya",
                "variant": ["Fransiya va Italiya", "Ispaniya va Portugaliya", "Turkiya va Gretsiya", "Angliya va Irlandiya"]
            },
            {
                "question": "Dunyoning eng mashhur tog‘ cho‘qqilaridan biri — K2 qayerda joylashgan?",
                "answer": "Pokiston va Xitoy",
                "variant": ["Pokiston va Xitoy", "Nepal va Xitoy", "Hindiston va Tibet", "Butan va Hindiston"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — O‘tkir Hoshimov mashhur asari?",
                "answer": "Ikki eshik orasi",
                "variant": ["Ikki eshik orasi", "Dunyoning ishlari", "Sarob", "Shaytanat"]
            },
            {
                "question": "Afrikadagi eng katta davlat maydon bo‘yicha?",
                "answer": "Jazoir",
                "variant": ["Jazoir", "Misr", "Sudan", "Efiopiya"]
            },
            {
                "question": "O‘zbekiston hududidagi qadimiy yodgorliklardan biri — Shohi Zinda majmuasi qayerda?",
                "answer": "Samarqand",
                "variant": ["Samarqand", "Buxoro", "Xiva", "Toshkent"]
            },
            {
                "question": "Dunyoning eng mashhur minoralaridan biri — CN Tower qayerda joylashgan?",
                "answer": "Kanada",
                "variant": ["Kanada", "AQSh", "Fransiya", "Germaniya"]
            },
            {
                "question": "Buyuk olim Arximedning mashhur iborasi?",
                "answer": "Menga tayanch nuqta bering, men Yer sharini ko‘taraman",
                "variant": ["Menga tayanch nuqta bering, men Yer sharini ko‘taraman", "Bilim kuchdir", "Men o‘ylayman, demak men borman", "Hammasi oqimda"]
            },
            {
                "question": "O‘zbekistonning mashhur shaharlaridan biri — Qo‘qon qaysi tarixiy davrda xonlik markazi bo‘lgan?",
                "answer": "XVIII-XIX asr",
                "variant": ["XVIII-XIX asr", "XVI asr", "XIV-XV asr", "XX asr"]
            }
        ]
   
        quiz_10 = [
            {
                "question": "Buyuk ipak yo‘li nechta qit’ani bog‘lagan?",
                "answer": "2 qit’a – Osiyo va Yevropa",
                "variant": ["Afrika va Osiyo", "2 qit’a – Osiyo va Yevropa", "Amerika va Osiyo", "Yevropa va Afrika"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan eng baland cho‘qqi nechchi metr?",
                "answer": "4643 metr",
                "variant": ["4643 metr", "5120 metr", "4300 metr", "4790 metr"]
            },
            {
                "question": "Dunyodagi eng qadimiy yozuv tizimlaridan biri?",
                "answer": "Mixxat",
                "variant": ["Lotin yozuvi", "Mixxat", "Arab yozuvi", "Sanskrit"]
            },
            {
                "question": "Qaysi davlat 'Inkalar imperiyasi'ning vatani?",
                "answer": "Peru",
                "variant": ["Peru", "Meksika", "Boliviya", "Ekvador"]
            },
            {
                "question": "Qaysi yozuvchi 'Ilahi komediya' asarini yozgan?",
                "answer": "Dante Aligyeriy",
                "variant": ["Gyote", "Balzak", "Dante Aligyeriy", "Shiller"]
            },
            {
                "question": "O‘zbekistonda eng katta tabiiy gaz konlaridan biri?",
                "answer": "Qandim",
                "variant": ["Sho‘rtan", "Muborak", "Qandim", "Gazli"]
            },
            {
                "question": "Yer sharining eng quruq cho‘li?",
                "answer": "Atakama",
                "variant": ["Gobi", "Atakama", "Lut cho‘li", "Sahroi Kabir"]
            },
            {
                "question": "Qaysi davlat 'Suvoqlar mamlakati' sifatida mashhur?",
                "answer": "Misr",
                "variant": ["Misr", "Yaponiya", "Xitoy", "Gretsiya"]
            },
            {
                "question": "Sharq mutafakkiri Forobiy qaysi sohada mashhur?",
                "answer": "Falsafa",
                "variant": ["Matematika", "Falsafa", "Tibbiyot", "Astronomiya"]
            },
            {
                "question": "Buyuk fransuz yozuvchisi Viktor Gyugoning mashhur asari?",
                "answer": "Notre-Dame qozoni (Quasimodo)",
                "variant": ["Urush va tinchlik", "Notre-Dame qozoni (Quasimodo)", "Otello", "Don Kixot"]
            },
            {
                "question": "Qaysi davlatning milliy sporti 'Gaelik futboli'?",
                "answer": "Irlandiya",
                "variant": ["Irlandiya", "Shotlandiya", "Angliya", "Vels"]
            },
            {
                "question": "Yer sharidagi eng sovuq okean?",
                "answer": "Shimoliy Muz okeani",
                "variant": ["Atlantika", "Tinch okeani", "Shimoliy Muz okeani", "Hind okeani"]
            },
            {
                "question": "Buyuk Aleksandrning ustozlaridan biri kim edi?",
                "answer": "Aristotel",
                "variant": ["Aristotel", "Platon", "Sokrat", "Pifagor"]
            },
            {
                "question": "O‘zbekistonda eng katta suv omborlaridan biri?",
                "answer": "Tuyamo‘yin",
                "variant": ["Chorvoq", "To‘dako‘l", "Tuyamo‘yin", "Bo‘zsuv"]
            },
            {
                "question": "Qaysi yozuvchi 'Madam Bovari' romanini yozgan?",
                "answer": "Gustav Flaubert",
                "variant": ["Balzak", "Stendal", "Gustav Flaubert", "Tolstoy"]
            },
            {
                "question": "Qaysi davlat poytaxti Suva?",
                "answer": "Fiji",
                "variant": ["Fiji", "Kiribati", "Tonga", "Mikroneziya"]
            },
            {
                "question": "Dunyoning eng baland tog‘ dovoni?",
                "answer": "Thorong La (Nepal)",
                "variant": ["Thorong La (Nepal)", "Tyan-Shan", "And", "Altay"]
            },
            {
                "question": "Qaysi yozuvchi 'Odyssey' asarini yozgan?",
                "answer": "Gomer",
                "variant": ["Gomer", "Vergiliy", "Sofokl", "Aristotel"]
            },
            {
                "question": "Qaysi davlat poytaxti Tashkent?",
                "answer": "O‘zbekiston",
                "variant": ["Tojikiston", "O‘zbekiston", "Qozog‘iston", "Turkmaniston"]
            },
            {
                "question": "Yer yuzidagi eng katta tog‘ tizmasi qaysi?",
                "answer": "And tog‘lari",
                "variant": ["And tog‘lari", "Gimolay", "Alp", "Kavkaz"]
            },
            {
                "question": "Qaysi yozuvchi 'Qonli uy' dramasini yozgan?",
                "answer": "Garcia Lorka",
                "variant": ["Garcia Lorka", "Kafka", "Dikkens", "Pushkin"]
            },
            {
                "question": "Dunyoning eng qadimiy shaharlardan biri – Quddus qaysi hududda?",
                "answer": "Falastin",
                "variant": ["Misr", "Falastin", "Livan", "Suriya"]
            },
            {
                "question": "Sharq mutafakkiri Mahmud Qoshg‘ariy mashhur asari?",
                "answer": "Devonu lug‘otit turk",
                "variant": ["Qutadg‘u bilig", "Devonu lug‘otit turk", "Xamsa", "Shohnoma"]
            },
            {
                "question": "Qaysi davlatda Angkor-Vat ibodatxonasi joylashgan?",
                "answer": "Kambodja",
                "variant": ["Kambodja", "Hindiston", "Indoneziya", "Vyetnam"]
            },
            {
                "question": "Yer sharining eng baland poytaxt shahri?",
                "answer": "La-Pas (Boliviya)",
                "variant": ["La-Pas (Boliviya)", "Quito", "Katmandu", "Karakas"]
            },
            {
                "question": "Qaysi yozuvchi 'Shifo ilmi' asarini yozgan?",
                "answer": "Ibn Sino",
                "variant": ["Ibn Sino", "Beruniy", "Navoiy", "Qoshg‘ariy"]
            },
            {
                "question": "Dunyodagi eng katta ko‘ldan ham kattaroq yopiq suv havzasi?",
                "answer": "Kaspiy dengizi",
                "variant": ["O‘lik dengiz", "Kaspiy dengizi", "Qora dengiz", "Aral dengizi"]
            },
            {
                "question": "Qaysi davlat poytaxti Katmandu?",
                "answer": "Nepal",
                "variant": ["Butan", "Nepal", "Hindiston", "Pokiston"]
            },
            {
                "question": "Buyuk yunon dramaturgi Sofokl mashhur asari?",
                "answer": "Shoh Edip",
                "variant": ["Shoh Edip", "Odyssey", "Iliada", "Qizil va qora"]
            },
            {
                "question": "Yer kurrasida eng ko‘p vulqonlar joylashgan davlat?",
                "answer": "Indoneziya",
                "variant": ["Indoneziya", "Yaponiya", "Italiya", "Meksika"]
            },
            {
                "question": "O‘zbek xalqining eng mashhur eposlaridan biri?",
                "answer": "Alpomish",
                "variant": ["Alpomish", "Shohnoma", "Manas", "Qutadg‘u bilig"]
            },
            {
                "question": "Dunyoning eng yirik arxipelagi?",
                "answer": "Indoneziya",
                "variant": ["Filippin", "Indoneziya", "Yaponiya", "Maldiv"]
            },
            {
                "question": "Buyuk yunon faylasufi Sokrat nima bilan mashhur?",
                "answer": "Dialogik usul",
                "variant": ["Dialogik usul", "Astronomiya", "Tibbiyot", "Adabiyot"]
            },
            {
                "question": "Qaysi davlat poytaxti Ulan-Bator?",
                "answer": "Mongoliya",
                "variant": ["Mongoliya", "Rossiya", "Qozog‘iston", "Tojikiston"]
            },
            {
                "question": "Yer yuzidagi eng sho‘r suvli dengiz?",
                "answer": "O‘lik dengiz",
                "variant": ["O‘lik dengiz", "Kaspiy", "Qora dengiz", "Adriatika"]
            },
            {
                "question": "Qaysi yozuvchi 'Gulliverning sayohatlari' asarini yozgan?",
                "answer": "Jonatan Svift",
                "variant": ["Mark Tven", "Jonatan Svift", "Defo", "Balzak"]
            },
            {
                "question": "Buyuk alloma Beruniy mashhur asari?",
                "answer": "Qadimgi xalqlardan qolgan yodgorliklar",
                "variant": ["Qadimgi xalqlardan qolgan yodgorliklar", "Shohnoma", "Xamsa", "Devonu lug‘otit turk"]
            },
            {
                "question": "Dunyoning eng katta sharsharasi suv hajmi bo‘yicha?",
                "answer": "Inga sharsharasi",
                "variant": ["Niagara", "Victoria", "Inga sharsharasi", "Iguasu"]
            },
            {
                "question": "Qaysi davlat 'ko‘plab orollar mamlakati' deb ataladi?",
                "answer": "Filippin",
                "variant": ["Filippin", "Yaponiya", "Norvegiya", "Indoneziya"]
            },
            {
                "question": "Yer kurrasidagi eng baland minoralardan biri – CN Tower qayerda joylashgan?",
                "answer": "Kanada",
                "variant": ["Kanada", "AQSh", "Xitoy", "BAA"]
            },
            {
                "question": "Qaysi yozuvchi 'Yuz yil yolg‘izlik' asarini yozgan?",
                "answer": "Gabriel Garsia Markes",
                "variant": ["Gabriel Garsia Markes", "Borges", "Isabel Allende", "Mario Vargas Losa"]
            },
            {
                "question": "Sharq mutafakkiri Yusuf Xos Hojib asari?",
                "answer": "Qutadg‘u bilig",
                "variant": ["Qutadg‘u bilig", "Devonu lug‘otit turk", "Shohnoma", "Xamsa"]
            },
            {
                "question": "Yer kurrasidagi eng katta yarim orol?",
                "answer": "Arabiston yarim oroli",
                "variant": ["Arabiston yarim oroli", "Iberiya", "Skandinaviya", "Hindiston yarim oroli"]
            },
            {
                "question": "Qaysi yozuvchi 'Forslar' tragediyasini yozgan?",
                "answer": "Aysxil",
                "variant": ["Sofokl", "Evripid", "Aysxil", "Aristofan"]
            },
            {
                "question": "Yer yuzidagi eng baland ko‘prik — Millau Viaduct qaysi davlatda?",
                "answer": "Fransiya",
                "variant": ["AQSh", "Fransiya", "Xitoy", "Italiya"]
            },
            {
                "question": "O‘zbekiston hududida necha xil iqlim tipi mavjud?",
                "answer": "3",
                "variant": ["2", "3", "4", "5"]
            },
            {
                "question": "Qaysi davlatning rasmiy poytaxti va hukumat poytaxti turlicha shaharlarda joylashgan?",
                "answer": "Janubiy Afrika",
                "variant": ["Janubiy Afrika", "Braziliya", "Avstraliya", "Kanada"]
            },
            {
                "question": "Qaysi yozuvchi 'Choliqushi' romanini yozgan?",
                "answer": "Reshod Nuri Guntekin",
                "variant": ["Reshod Nuri Guntekin", "Orxon Pamuk", "Nazim Hikmat", "Tolstoy"]
            },
            {
                "question": "Yer yuzida eng baland daryo sharsharasi qaysi?",
                "answer": "Anxel",
                "variant": ["Niagara", "Victoria", "Anxel", "Iguasu"]
            },
            {
                "question": "Qaysi davlatda eng qadimiy parlament — Alting mavjud?",
                "answer": "Islandiya",
                "variant": ["Islandiya", "Norvegiya", "Angliya", "Shvetsiya"]
            },
            {
                "question": "Buyuk yozuvchi Alber Kamyu mashhur asari?",
                "answer": "Begona",
                "variant": ["Begona", "Jarayon", "Sariq devni minib", "Shohnoma"]
            },
            {
                "question": "Sharq mutafakkiri Umar Xayyom nima bilan mashhur?",
                "answer": "Ruboiatlar",
                "variant": ["Ruboiatlar", "Shohnoma", "Xamsa", "Qutadg‘u bilig"]
            },
            {
                "question": "Qaysi davlatning poytaxti Valetta?",
                "answer": "Malta",
                "variant": ["Malta", "Kipr", "Andorra", "San-Marino"]
            },
            {
                "question": "Yer sharida eng uzun orol zanjiri?",
                "answer": "Kuril orollari",
                "variant": ["Kuril orollari", "Aleut orollari", "Filippin orollari", "Malay arxipelagi"]
            },
            {
                "question": "Qaysi yozuvchi 'Karamazov aka-ukalari' asarini yozgan?",
                "answer": "Dostoyevskiy",
                "variant": ["Dostoyevskiy", "Tolstoy", "Gogol", "Chexov"]
            },
            {
                "question": "Qaysi davlatda Mo‘g‘ul imperiyasi paydo bo‘lgan?",
                "answer": "Mongoliya",
                "variant": ["Mongoliya", "Xitoy", "Rossiya", "Qozog‘iston"]
            },
            {
                "question": "Buyuk yunon olimi Pifagor mashhur asari?",
                "answer": "Pifagor teoremasi",
                "variant": ["Pifagor teoremasi", "Arximed qonuni", "Nyuton qonuni", "Eynshteyn nazariyasi"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan eng qadimiy karvonsaroy qoldiqlari?",
                "answer": "Raboti Malik",
                "variant": ["Raboti Malik", "Ko‘hna Urganch", "Ark", "Ellikqal’a"]
            },
            {
                "question": "Yer sharidagi eng katta ichki cho‘l?",
                "answer": "Gobi",
                "variant": ["Gobi", "Karakum", "Kizilqum", "Sahroi Kabir"]
            },
            {
                "question": "Qaysi yozuvchi 'Falsafiy maktublar' asarini yozgan?",
                "answer": "Volter",
                "variant": ["Volter", "Russo", "Gyote", "Makiavelli"]
            },
            {
                "question": "Qaysi davlatning milliy sporti regbi?",
                "answer": "Yangi Zelandiya",
                "variant": ["Yangi Zelandiya", "Janubiy Afrika", "Avstraliya", "Angliya"]
            },
            {
                "question": "Buyuk mutafakkir Alisher Navoiyning tug‘ilgan yili?",
                "answer": "1441",
                "variant": ["1441", "1501", "1397", "1456"]
            },
            {
                "question": "Yer sharidagi eng katta sho‘r ko‘l?",
                "answer": "Qaspiy dengizi",
                "variant": ["Qaspiy dengizi", "O‘lik dengiz", "Tuzko‘l", "Qora dengiz"]
            },
            {
                "question": "Qaysi yozuvchi 'Chol va dengiz' asarini yozgan?",
                "answer": "Ernest Xeminguey",
                "variant": ["Ernest Xeminguey", "Jek London", "Mark Tven", "Balzak"]
            },
            {
                "question": "O‘zbekiston hududidagi eng yirik mis koni?",
                "answer": "Olmaliq",
                "variant": ["Olmaliq", "Angren", "Qizilqum", "Zarafshon"]
            },
            {
                "question": "Dunyodagi eng qadimiy shahar sifatida tanilgan?",
                "answer": "Jerixo",
                "variant": ["Quddus", "Jerixo", "Afina", "Damashq"]
            },
            {
                "question": "Qaysi yozuvchi 'Qizil chiroqlar' asarini yozgan?",
                "answer": "Abdulla Qahhor",
                "variant": ["Abdulla Qahhor", "Cho‘lpon", "Oybek", "Erkin Vohidov"]
            },
            {
                "question": "Yer sharidagi eng chuqur vodiy?",
                "answer": "Kolorado Kanyoni",
                "variant": ["Kolorado Kanyoni", "Yarlung", "Pamir", "Hindukush"]
            },
            {
                "question": "Buyuk faylasuf Platon mashhur asari?",
                "answer": "Davlat",
                "variant": ["Davlat", "Etika", "Dialoglar", "Metafizika"]
            },
            {
                "question": "Qaysi davlatning poytaxti Ashxobod?",
                "answer": "Turkmaniston",
                "variant": ["Turkmaniston", "Tojikiston", "O‘zbekiston", "Qozog‘iston"]
            },
            {
                "question": "Sharq mutafakkiri Ibn Xaldun nima bilan mashhur?",
                "answer": "Tarixshunoslik asoschisi",
                "variant": ["Tarixshunoslik asoschisi", "Astronomiya", "Tibbiyot", "Matematika"]
            },
            {
                "question": "Qaysi yozuvchi 'Sho‘rodan qolgan odamlar' asarini yozgan?",
                "answer": "Pirimqul Qodirov",
                "variant": ["Pirimqul Qodirov", "O‘tkir Hoshimov", "Tahir Malik", "Navoiy"]
            },
            {
                "question": "Yer sharidagi eng qadimiy teatr binolaridan biri?",
                "answer": "Afina Dionis teatri",
                "variant": ["Afina Dionis teatri", "Rim Kolizey", "Bolshoy teatr", "London Globe"]
            },
            {
                "question": "Qaysi davlatning milliy sporti hurling?",
                "answer": "Irlandiya",
                "variant": ["Irlandiya", "Angliya", "Shotlandiya", "Kanada"]
            },
            {
                "question": "Yer sharida eng katta ko‘rfaz?",
                "answer": "Bengal ko‘rfazi",
                "variant": ["Bengal ko‘rfazi", "Meksika ko‘rfazi", "Aden ko‘rfazi", "Pers ko‘rfazi"]
            },
            {
                "question": "Qaysi davlatda 'Terrakota askarlari' topilgan?",
                "answer": "Xitoy",
                "variant": ["Xitoy", "Yaponiya", "Koreya", "Hindiston"]
            },
            {
                "question": "Buyuk yozuvchi Balzak mashhur asari?",
                "answer": "Inson komediyasi",
                "variant": ["Inson komediyasi", "Anna Karenina", "Jarayon", "Urush va tinchlik"]
            },
            {
                "question": "Qaysi davlatning poytaxti Vena?",
                "answer": "Avstriya",
                "variant": ["Avstriya", "Shveytsariya", "Germaniya", "Chexiya"]
            },
            {
                "question": "Yer sharidagi eng katta cho‘l qaysi?",
                "answer": "Antarktida cho‘li",
                "variant": ["Antarktida cho‘li", "Sahroi Kabir", "Gobi", "Atakama"]
            },
            {
                "question": "Qaysi yozuvchi 'Manas' eposi bilan mashhur?",
                "answer": "Qirg‘iz xalqi",
                "variant": ["Qirg‘iz xalqi", "O‘zbek xalqi", "Qozoq xalqi", "Turkman xalqi"]
            },
            {
                "question": "Buyuk yunon faylasufi Aristotel mashhur asari?",
                "answer": "Metafizika",
                "variant": ["Metafizika", "Dialoglar", "Davlat", "Etika"]
            },
            {
                "question": "Qaysi davlatning poytaxti Bogota?",
                "answer": "Kolumbiya",
                "variant": ["Kolumbiya", "Venesuela", "Ekvador", "Peru"]
            },
            {
                "question": "Sharq mutafakkiri Al-Kindiy nima bilan mashhur?",
                "answer": "Islom falsafasi asoschisi",
                "variant": ["Islom falsafasi asoschisi", "Astronom", "Tibbiyotchi", "Matematik"]
            },
            {
                "question": "Qaysi yozuvchi 'O‘tkan kunlar' romanini yozgan?",
                "answer": "Abdulla Qodiriy",
                "variant": ["Abdulla Qodiriy", "Cho‘lpon", "Oybek", "Tahir Malik"]
            },
            {
                "question": "Yer sharidagi eng yirik plato?",
                "answer": "Tibet platosi",
                "variant": ["Tibet platosi", "Pamir", "And", "Altay"]
            },
            {
                "question": "Qaysi davlat 'Ko‘hna Rim davlati'ning markazi edi?",
                "answer": "Italiya",
                "variant": ["Italiya", "Gretsiya", "Fransiya", "Ispaniya"]
            },
            {
                "question": "Buyuk mutafakkir Erkin Vohidov mashhur asari?",
                "answer": "Ruhlar isyoni",
                "variant": ["Ruhlar isyoni", "O‘tkan kunlar", "Shohnoma", "Qiyomat"]
            },
            {
                "question": "Buyuk yunon tarixchisi Gerodot qaysi asari bilan mashhur?",
                "answer": "Tarix",
                "variant": ["Tarix", "Davlat", "Dialoglar", "Shohnoma"]
            },
            {
                "question": "Yer sharidagi eng baland vodiy qaysi davlat hududida joylashgan?",
                "answer": "Nepal",
                "variant": ["Nepal", "Tibet", "Butan", "Hindiston"]
            },
            {
                "question": "Qaysi yozuvchi 'Otamdan qolgan dalalar' asarini yozgan?",
                "answer": "O‘tkir Hoshimov",
                "variant": ["O‘tkir Hoshimov", "Pirimqul Qodirov", "Tahir Malik", "Cho‘lpon"]
            },
            {
                "question": "Dunyoning eng katta okean oroli qaysi?",
                "answer": "Yangi Gvineya",
                "variant": ["Yangi Gvineya", "Sumatra", "Borneo", "Madagaskar"]
            },
            {
                "question": "Sharq mutafakkiri Ibn Rushd nima bilan mashhur?",
                "answer": "Aristotel falsafasini sharhlash",
                "variant": ["Aristotel falsafasini sharhlash", "Astronomiya", "Tibbiyot", "Adabiyot"]
            },
            {
                "question": "Qaysi davlatda Teotiuakan shahri joylashgan?",
                "answer": "Meksika",
                "variant": ["Meksi  ka", "Peru", "Boliviya", "Ekvador"]
            },
            {
                "question": "Dunyoning eng mashhur sharsharalaridan biri — Tugela qaysi davlatda joylashgan?",
                "answer": "Janubiy Afrika",
                "variant": ["Janubiy Afrika", "Namibiya", "Keniya", "Zimbabve"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan qadimiy shaharlaridan biri — Termiz qaysi viloyatda?",
                "answer": "Surxondaryo",
                "variant": ["Surxondaryo", "Buxoro", "Samarqand", "Xorazm"]
            },
            {
                "question": "Dunyoning eng katta ko‘rfazlaridan biri?",
                "answer": "Bengal ko‘rfazi",
                "variant": ["Bengal ko‘rfazi", "Meksika ko‘rfazi", "Pers ko‘rfazi", "Aden ko‘rfazi"]
            },
            {
                "question": "Buyuk yozuvchi Abdulla Qahhor mashhur asarlaridan biri?",
                "answer": "Anor",
                "variant": ["Anor", "Sarob", "O‘tkan kunlar", "Sinchalak"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur masjidlardan biri — Hazrati Imom majmuasi qayerda joylashgan?",
                "answer": "Toshkent",
                "variant": ["Toshkent", "Samarqand", "Buxoro", "Andijon"]
            },
            {
                "question": "Dunyoning eng mashhur muzeylaridan biri — Eremitaj qayerda joylashgan?",
                "answer": "Sankt-Peterburg",
                "variant": ["Sankt-Peterburg", "Moskva", "Parij", "Berlin"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur qal’alardan biri — Ark qaysi shaharda?",
                "answer": "Buxoro",
                "variant": ["Buxoro", "Samarqand", "Xiva", "Shahrisabz"]
            }
        ]
               

        lvl_1 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4)
        lvl_2 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4)
        lvl_3 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4)
        lvl_4 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4)
        lvl_5 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4)
        lvl_6 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5)
        lvl_7 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5)
        lvl_8 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5)
        lvl_9 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5)
        lvl_10 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5)
        lvl_11 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6)
        lvl_12 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6)
        lvl_13 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6)
        lvl_14 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6)
        lvl_15 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6)
        lvl_16 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6)
        lvl_17 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6)
        lvl_18 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6)
        lvl_19 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6)
        lvl_20 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6)
        lvl_21 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7)
        lvl_22 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7)
        lvl_23 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7)
        lvl_24 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7)
        lvl_25 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7)
        lvl_26 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7)
        lvl_27 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7)
        lvl_28 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7)
        lvl_29 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7)
        lvl_30 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7)
        lvl_31 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7)
        lvl_32 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7)
        lvl_33 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7)
        lvl_34 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7)
        lvl_35 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7)
        lvl_36 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7)
        lvl_37 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7)
        lvl_38 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7)
        lvl_39 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7)
        lvl_40 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7)
        lvl_41 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8)
        lvl_42 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8)
        lvl_43 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8)
        lvl_44 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8)
        lvl_45 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8)
        lvl_46 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8)
        lvl_47 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8)
        lvl_48 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8)
        lvl_49 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8)
        lvl_50 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8)
        lvl_51 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8)
        lvl_52 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8)
        lvl_53 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8)
        lvl_54 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8)
        lvl_55 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8)
        lvl_56 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8)
        lvl_57 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8)
        lvl_58 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8)
        lvl_59 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8)
        lvl_60 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8)
        lvl_61 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9)
        lvl_62 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9)
        lvl_63 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9)
        lvl_64 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9)
        lvl_65 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9)
        lvl_66 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9)
        lvl_67 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9)
        lvl_68 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9)
        lvl_69 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9)
        lvl_70 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9)
        lvl_71 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9)
        lvl_72 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9)
        lvl_73 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9)
        lvl_74 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9)
        lvl_75 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9)
        lvl_76 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9)
        lvl_77 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9)
        lvl_78 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9)
        lvl_79 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9)
        lvl_80 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9)
        lvl_81 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10)
        lvl_82 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10)
        lvl_83 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10)
        lvl_84 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10)
        lvl_85 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10)
        lvl_86 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10)
        lvl_87 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10)
        lvl_88 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10)
        lvl_89 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10)
        lvl_90 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10)
        lvl_91 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10)
        lvl_92 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10)
        lvl_93 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10)
        lvl_94 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10)
        lvl_95 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10)
        lvl_96 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10)
        lvl_97 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10)
        lvl_98 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10)
        lvl_99 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10)
        lvl_100 = random.choice(quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10)



        
        return Response(name) 
