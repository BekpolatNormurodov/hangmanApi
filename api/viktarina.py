from rest_framework.views import APIView
from rest_framework.response import Response
import random

class Viktoriya(APIView):
    def get(self, request):
 
        # Savollar jami: 150ta (50ta Diniy + 100ta Fan)

        quiz_1 = [
            # Diniy savollar 50ta
            {
                "question": "Qur’onda nechta sura mavjud?",
                "answer": "114 ta",
                "options": ["114 ta", "110 ta", "120 ta", "100 ta"]
            },
            {
                "question": "Qur’onda nechta oyat mavjud?",
                "answer": "6236 ta",
                "options": ["6236 ta", "6000 ta", "7000 ta", "6500 ta"]
            },
            {
                "question": "Qur’onda eng uzun sura?",
                "answer": "Baqara",
                "options": ["Baqara", "Niso", "Yusuf", "Yunus"]
            },
            {
                "question": "Islom dinining asosiy kalimasi nima?",
                "answer": "La ilaha illalloh Muhammadur Rasululloh",
                "options": ["La ilaha illalloh Muhammadur Rasululloh", "Allohu akbar", "Bismillahir rohmanir rohiym", "Alhamdulillah"]
            },
            {
                "question": "Qur’on nechta qismga bo‘lingan?",
                "answer": "30 juz",
                "options": ["30 juz", "7 qism", "12 qism", "60 qism"]
            },
            {
                "question": "Qur’onning oxirgi surasi?",
                "answer": "Nas surasi",
                "options": ["Nas surasi", "Falaq surasi", "Ikhlos surasi", "Kavsar surasi"]
            },
            {
                "question": "Musulmonlarning birinchi qiblasi?",
                "answer": "Masjidul Aqso",
                "options": ["Masjidul Aqso", "Ka’ba", "Madina masjidi", "Tur tog‘i"]
            },
            {
                "question": "Ka’ba yonida joylashgan muqaddas quduq?",
                "answer": "Zam-zam",
                "options": ["Zam-zam", "Furot", "Nil", "Sirdaryo"]
            },
            {
                "question": "Islomda ro‘za tutiladigan oy?",
                "answer": "Ramazon",
                "options": ["Ramazon", "Muharram", "Zulhijja", "Sha’bon"]
            },
            {
                "question": "Payg‘ambarimizning otlari qaysi qabiladan edi?",
                "answer": "Quraysh",
                "options": ["Quraysh", "Banu Zuhra", "Banu Tamim", "Banu Umayya"]
            },
            {
                "question": "Payg‘ambarimizning onalari ismi?",
                "answer": "Omina",
                "options": ["Omina", "Xadicha", "Maryam", "Fotima"]
            },
            {
                "question": "Payg‘ambarimizning eng yaqin do‘stlari kim edi?",
                "answer": "Abu Bakr",
                "options": ["Abu Bakr", "Umar", "Usmon", "Ali"]
            },
            {
                "question": "Islomda taqiqlangan ichimlik?",
                "answer": "Spirtli ichimlik",
                "options": ["Spirtli ichimlik", "Suv", "Sut", "Asal"]
            },
            {
                "question": "Islomda halol qilinmagan go‘sht?",
                "answer": "Cho‘chqa go‘shti",
                "options": ["Cho‘chqa go‘shti", "Qo‘y go‘shti", "Mol go‘shti", "Tovuq go‘shti"]
            },
            {
                "question": "Payg‘ambarimizning birinchi xotinlari?",
                "answer": "Xadicha (r.a.)",
                "options": ["Xadicha", "Ayshe", "Sofiya", "Hafsa"]
            },
            {
                "question": "Payg‘ambarimizning oxirgi xotinlari kim?",
                "answer": "Ummu Salama",
                "options": ["Ummu Salama", "Ayshe", "Hafsa", "Maymuna"]
            },
            {
                "question": "Islomda zakot qanday ibodat?",
                "answer": "Mol-dunyodan beriladigan sadaqa",
                "options": ["Mol-dunyodan beriladigan sadaqa", "Sunnat namoz", "Haj safari", "Ro‘za"]
            },
            {
                "question": "Islomda namoz vaqtida qaysi tilda o‘qiladi?",
                "answer": "Arab tilida",
                "options": ["Arab tilida", "O‘zbek tilida", "Fors tilida", "Turk tilida"]
            },
            {
                "question": "Azonni kim aytadi?",
                "answer": "Muazzin",
                "options": ["Muazzin", "Imom", "Qori", "Faqih"]
            },
            {
                "question": "Musulmonlarning salomi?",
                "answer": "Assalomu alaykum",
                "options": ["Assalomu alaykum", "Salom", "Marhabo", "Hayr"]
            },
            {
                "question": "Salomga javob?",
                "answer": "Va alaykumussalom",
                "options": ["Va alaykumussalom", "Rahmat", "Yaxshi", "Hayr"]
            },
            {
                "question": "Payg‘ambarimizning tug‘ilgan shahri?",
                "answer": "Makka",
                "options": ["Makka", "Madina", "Quddus", "Damashq"]
            },
            {
                "question": "Payg‘ambarimizning hijrat qilgan shahri?",
                "answer": "Madina",
                "options": ["Madina", "Makka", "Quddus", "Toyĭf"]
            },
            {
                "question": "Payg‘ambarimizning amakilari ichidan musulmon bo‘lganlari?",
                "answer": "Hamza",
                "options": ["Hamza", "Abu Lahab", "Abbos", "Abu Tolib"]
            },
            {
                "question": "Ka’baning ustini yopib turadigan mato?",
                "answer": "Kisva",
                "options": ["Kisva", "Bayroq", "Libos", "Paranda"]
            },
            {
                "question": "Haj ibodatida Ka’bani aylanib yurish nima deyiladi?",
                "answer": "Tavof",
                "options": ["Tavof", "Sa’y", "Wuquf", "Tahallul"]
            },
            {
                "question": "Safa va Marva oralig‘ida yurish amali?",
                "answer": "Sa’y",
                "options": ["Sa’y", "Tavof", "Tahallul", "Wuquf"]
            },
            {
                "question": "Hajda Arafotda turish nima deyiladi?",
                "answer": "Wuquf",
                "options": ["Wuquf", "Tavof", "Sa’y", "Qasr"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ning amakivachchalari orasida mashhur xalifa?",
                "answer": "Ali ibn Abu Tolib",
                "options": ["Ali ibn Abu Tolib", "Umar ibn Xattob", "Usmon ibn Affon", "Abu Bakr"]
            },
            {
                "question": "Payg‘ambarimizning qizlaridan biri?",
                "answer": "Ruqayya",
                "options": ["Ruqayya", "Ayshe", "Maryam", "Ummu Salama"]
            },
            {
                "question": "Payg‘ambarimizning qizlaridan yana biri?",
                "answer": "Zaynab",
                "options": ["Zaynab", "Fotima", "Hafsa", "Sofiya"]
            },
            {
                "question": "Payg‘ambarimizning qizlaridan yana biri?",
                "answer": "Ummu Kulsum",
                "options": ["Ummu Kulsum", "Xadicha", "Oyshe", "Maryam"]
            },
            {
                "question": "Payg‘ambarimizning o‘g‘illari ichidan eng mashhuri?",
                "answer": "Ibrohim",
                "options": ["Ibrohim", "Qosim", "Abdulloh", "Ismoil"]
            },
            {
                "question": "Islomda Qur’onni yodlagan kishiga qanday nom beriladi?",
                "answer": "Hofiz",
                "options": ["Hofiz", "Qori", "Imom", "Faqih"]
            },
            {
                "question": "Qur’onni chiroyli o‘qiydigan kishi?",
                "answer": "Qori",
                "options": ["Qori", "Hofiz", "Imom", "Muazzin"]
            },
            {
                "question": "Namozni boshqaradigan kishi?",
                "answer": "Imom",
                "options": ["Imom", "Muazzin", "Faqih", "Qori"]
            },
            {
                "question": "Hadislarni o‘rgangan olimlar?",
                "answer": "Muhaddis",
                "options": ["Muhaddis", "Faqih", "Imom", "Qori"]
            },
            {
                "question": "Fiqh ilmini bilgan olim?",
                "answer": "Faqih",
                "options": ["Faqih", "Muhaddis", "Imom", "Qori"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) nabiralaridan biri?",
                "answer": "Hasan",
                "options": ["Hasan", "Husayn", "Ali", "Umar"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) nabiralaridan yana biri?",
                "answer": "Husayn",
                "options": ["Husayn", "Hasan", "Ali", "Usmon"]
            },
            {
                "question": "Ramazonda kechqurun o‘qiladigan namoz?",
                "answer": "Tarovih",
                "options": ["Tarovih", "Juma namozi", "Vitr", "Iyd namozi"]
            },
            {
                "question": "Namozdan oldin qaysi zikr aytiladi?",
                "answer": "Bismillahir rohmanir rohiym",
                "options": ["Bismillahir rohmanir rohiym", "Allohu akbar", "Subhanalloh", "Alhamdulillah"]
            },
            {
                "question": "Musulmonlar uchun juma kuni qanday kun hisoblanadi?",
                "answer": "Bayram kuni",
                "options": ["Bayram kuni", "Oddiy kun", "Ro‘za kuni", "Sokin kun"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) tug‘ilgan kuni qanday ataladi?",
                "answer": "Mavlud",
                "options": ["Mavlud", "Hijrat", "Laylatul-Qadr", "Navro‘z"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur daryo?",
                "answer": "Furot",
                "options": ["Furot", "Nil", "Dajla", "Zamzam"]
            },
            {
                "question": "Islomda eng qadimiy payg‘ambarlardan biri?",
                "answer": "Nuh (a.s.)",
                "options": ["Nuh", "Muso", "Iso", "Ya’qub"]
            },
            {
                "question": "Allohning eng yaqin farishtalaridan biri?",
                "answer": "Mikoil",
                "options": ["Mikoil", "Isrofil", "Jabroil", "Azroil"]
            },
            {
                "question": "Islomda o‘lim farishtasi kim?",
                "answer": "Azroil",
                "options": ["Azroil", "Jabroil", "Isrofil", "Mikoil"]
            },
            {
                "question": "Qur’onni nozil qilgan zot?",
                "answer": "Alloh taolo",
                "options": ["Alloh taolo", "Muhammad (s.a.v.)", "Jabroil", "Musulmonlar"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ning bolalik chog‘ida tarbiyalagan sut onasi?",
                "answer": "Halima Sa’diyya",
                "options": ["Halima Sa’diyya", "Omina", "Xadicha", "Maymuna"]
            },
            # Fanga oid savollar 100ta
            {
                "question": "Dunyoning eng katta tog‘ tizmalari?",
                "answer": "Gimolay",
                "options": ["Gimolay", "And", "Alp", "Tyan-Shan"]
            },
            {
                "question": "Rassiyaning poytaxti qaysi?",
                "answer": "Maskva",
                "options": ["Maskva", "Sankt-Peterburg", "Leningrad", " Astrahan"]
            },
            {
                "question": "Yerning sun’iy yo‘ldoshi qaysi?",
                "answer": "Oy",
                "options": ["Oy", "Quyosh", "Mars", "Sirius"]
            },
            {
                "question": "Dunyodagi eng katta okean?",
                "answer": "Tinch okeani",
                "options": ["Tinch okeani", "Atlantika okeani", "Hind okeani", "Shimoliy muz okeani"]
            },
            {
                "question": "O‘zbekiston bayrog‘ida nechta rang bor?",
                "answer": "4",
                "options": ["3", "4", "2", "5"]
            },
            {
                "question": "Inson tanasida nechta yurak mavjud?",
                "answer": "1",
                "options": ["1", "2", "3", "4"]
            },
            {
                "question": "Yer yuzidagi eng katta qit’a?",
                "answer": "Osiyo",
                "options": ["Osiyo", "Afrika", "Yevropa", "Amerika"]
            },
            {
                "question": "Futbol o‘yinida maydonda bir jamoada nechta o‘yinchi bo‘ladi?",
                "answer": "11",
                "options": ["11", "10", "9", "12"]
            },
            {
                "question": "Atom raqami 1 bo‘lgan kimyoviy element?",
                "answer": "Vodorod",
                "options": ["Vodorod", "Kislorod", "Azot", "Heliy"]
            },
            {
                "question": "‘Alpomish’ dostoni muallifi kim?",
                "answer": "O'zbek xalq dostoni",
                "options": ["O'zbek xalq dostoni", "Erkin Vohidov", "Said Ahmad", "Hamza Hakimzoda"]
            },
            {
                "question": "Eng uzun daryo?",
                "answer": "Nil",
                "options": ["Nil", "Amazonka", "Amudaryo", "Sirdaryo"]
            },
            {
                "question": "Inson tanasidagi eng katta suyak?",
                "answer": "Son suyagi",
                "options": ["Son suyagi", "Bilak suyagi", "Umurtqa", "To‘piq suyagi"]
            },
            {
                "question": "Kompyuterning asosiy qurilmasi?",
                "answer": "Protsessor",
                "options": ["Protsessor", "Monitor", "Klaviatura", "Sichqoncha"]
            },
            {
                "question": "O‘zbekiston mustaqillikka qachon erishgan?",
                "answer": "1991",
                "options": ["1991", "1990", "1992", "1989"]
            },
            {
                "question": "Poytaxti Parij bo‘lgan davlat?",
                "answer": "Fransiya",
                "options": ["Fransiya", "Germaniya", "Italiya", "Ispaniya"]
            },
            {
                "question": "Yer yuzidagi eng baland tog‘?",
                "answer": "Everest",
                "options": ["Everest", "Kilimanjaro", "Tyan-Shan", "Pomir"]
            },
            {
                "question": "Quyosh tizimidagi eng katta sayyora?",
                "answer": "Yupiter",
                "options": ["Yupiter", "Saturn", "Yer", "Mars"]
            },
            {
                "question": "‘Layli va Majnun’ asarining muallifi?",
                "answer": "Navoiy",
                "options": ["Navoiy", "Bobur", "Pushkin", "Shakespeare"]
            },
            {
                "question": "Amerika qit’asini kim kashf qilgan?",
                "answer": "Xristofor Kolumb",
                "options": ["Xristofor Kolumb", "Magellan", "Vasko da Gama", "Marko Polo"]
            },
            {
                "question": "Shaxmat o‘yinida nechta dona mavjud?",
                "answer": "32",
                "options": ["32", "36", "40", "28"]
            },
            {
                "question": "Yengil atletikada marafon masofasi nechchi km?",
                "answer": "42",
                "options": ["42", "40", "36", "50"]
            },
            {
                "question": "Qozogiston milliy valyutasi?",
                "answer": "Tenge",
                "options": ["Tenge", "Rubl", "Dollar", "so'm"]
            },
            {
                "question": "Qadimgi Misr ehromlari qaysi shaharda joylashgan?",
                "answer": "Qohira yaqinida",
                "options": ["Qohira yaqinida", "Aleksandriya", "Luksor", "Asuan"]
            },
            {
                "question": "Dunyodagi eng sovuq qit’a?",
                "answer": "Antarktida",
                "options": ["Antarktida", "Osiyo", "Shimoliy Amerika", "Yevropa"]
            },
            {
                "question": "Quyosh chiqadigan yo‘nalish?",
                "answer": "Sharq",
                "options": ["Sharq", "G‘arb", "Shimol", "Janub"]
            },
            {
                "question": "Kompyuterdagi ‘Ctrl+C’ amalini bajaradi?",
                "answer": "Nusxa olish",
                "options": ["Nusxa olish", "Kesish", "Joylashtirish", "O‘chirish"]
            },
            {
                "question": "Dunyodagi eng katta orol?",
                "answer": "Grenlandiya",
                "options": ["Grenlandiya", "Madagaskar", "Borneo", "Sumatra"]
            },
            {
                "question": "Inson tanasida qancha juft qovurg‘a bor?",
                "answer": "12 juft",
                "options": ["12 juft", "10 juft", "14 juft", "11 juft"]
            },
            {
                "question": "Samolyotni kim ixtiro qilgan?",
                "answer": "Rayt aka-ukalari",
                "options": ["Rayt aka-ukalari", "Edison", "Tesla", "Fulton"]
            },
            {
                "question": "Ertak qahramoni Zumradning singlisi kim edi?",
                "answer": "Qimmat",
                "options": ["Qimmat", "Oysuluv", "Malika", "Shirin"]
            },
            {
                "question": "Mingbaytli she’r qanday ataladi?",
                "answer": "Doston",
                "options": ["Doston", "Ruboi", "G‘azal", "Qit’a"]
            },
            {
                "question": "Poytaxti Tokio bo‘lgan davlat?",
                "answer": "Yaponiya",
                "options": ["Yaponiya", "Xitoy", "Janubiy Koreya", "Tayvan"]
            },
            {
                "question": "O‘zbekistonda nechta viloyat bor?",
                "answer": "12",
                "options": ["12", "13", "14", "10"]
            },
            {
                "question": "Navoiy qaysi asari bilan mashhur?",
                "answer": "Xamsa",
                "options": ["Xamsa", "Boburnoma", "Qutadg‘u bilig", "Shohnoma"]
            },
            {
                "question": "Kompyuterdagi ‘Ctrl+V’ nima qiladi?",
                "answer": "Joylashtirish",
                "options": ["Joylashtirish", "O‘chirish", "Nusxa olish", "Qidirish"]
            },
            {
                "question": "Hujayraning markazi nima?",
                "answer": "Yadro",
                "options": ["Yadro", "Sitoplazma", "Ribosoma", "Membrana"]
            },
            {
                "question": "Amerika bayrog‘ida nechta yulduz bor?",
                "answer": "50",
                "options": ["50", "52", "48", "45"]
            },
            {
                "question": "Shaharlarda odamlar ko‘p to‘plangan maydon?",
                "answer": "Maidon",
                "options": ["Maidon", "Bog‘", "Ko‘cha", "Bozor"]
            },
            {
                "question": "‘Alibaba va qirq qaroqchi’ ertagida nechta qaroqchi bo‘lgan?",
                "answer": "40",
                "options": ["40", "30", "50", "25"]
            },
            {
                "question": "Poytaxti Moskva bo‘lgan davlat?",
                "answer": "Rossiya",
                "options": ["Rossiya", "Belarus", "Ukraina", "Latviya"]
            },
            {
                "question": "Basketbol o‘yinida to‘pni savatchaga tashlash nechta ochko?",
                "answer": "2 yoki 3",
                "options": ["2 yoki 3", "1 yoki 2", "3 yoki 4", "5"]
            },
            {
                "question": "‘Qizil qalpoqcha’ ertagida qizil qalpoqcha kim bilan yashagan?",
                "answer": "Onasi bilan",
                "options": ["Onasi bilan", "Bobosi bilan", "Opasi bilan", "Buvasi bilan"]
            },
            {
                "question": "Eng yirik quruqlik hayvoni?",
                "answer": "Fil",
                "options": ["Fil", "Ot", "Sigir", "Yo‘lbars"]
            },
            {
                "question": "Qur’onda nechta sura bor?",
                "answer": "114",
                "options": ["114", "112", "120", "110"]
            },
            {
                "question": "Musiqa notalari nechta?",
                "answer": "7",
                "options": ["7", "6", "8", "5"]
            },
            {
                "question": "O‘zbekistonning eng katta viloyati?",
                "answer": "Navoiy",
                "options": ["Navoiy", "Buxoro", "Toshkent", "Farg‘ona"]
            },
            {
                "question": "Inson tanasida nechta barmoq bor?",
                "answer": "20",
                "options": ["20", "18", "22", "19"]
            },
            {
                "question": "Amerikaning ramziy hayvoni?",
                "answer": "Burgut",
                "options": ["Burgut", "Sher", "Fil", "Qoplon"]
            },
            {
                "question": "Yerning qaysi qatlami eng tashqi?",
                "answer": "Qobiq",
                "options": ["Qobiq", "Mantiya", "Yadro", "Atmosfera"]
            },
            {
                "question": "O‘zbek milliy taomi?",
                "answer": "Palov",
                "options": ["Palov", "Lag‘mon", "Somsa", "Shashlik"]
            },
            {
                "question": "Yer sharining necha qit’asi mavjud?",
                "answer": "6",
                "options": ["6", "5", "7", "4"]
            },
            {
                "question": "O‘zbekistonda eng ko‘p aholiga ega viloyat?",
                "answer": "Farg‘ona",
                "options": ["Farg‘ona", "Andijon", "Samarqand", "Toshkent viloyati"]
            },
            {
                "question": "O‘zbekistonning ramziy me’moriy inshooti Registon qayerda joylashgan?",
                "answer": "Samarqand",
                "options": ["Samarqand", "Buxoro", "Xiva", "Shahrisabz"]
            },
            {
                "question": "Elektr toki kuchi birligi?",
                "answer": "Amper",
                "options": ["Amper", "Volt", "Vatt", "Om"]
            },
            {
                "question": "O‘zbekistonda oltin qazib olish markazi bo‘lgan shaharcha?",
                "answer": "Muruntov",
                "options": ["Muruntov", "Zarafshon", "Angren", "Olmaliq"]
            },
            {
                "question": "Dunyodagi eng baland sharshara?",
                "answer": "Anxel",
                "options": ["Anxel", "Niagara", "Victoria", "Iguasu"]
            },
            {
                "question": "Qanday metall 'qora oltin' deb ataladi?",
                "answer": "Neft",
                "options": ["Neft", "Ko‘mir", "Gaz", "Temir"]
            },
            {
                "question": "Inson tanasida eng katta ichki organ?",
                "answer": "Jigar",
                "options": ["Jigar", "Oshqozon", "Yurak", "Buyrak"]
            },
            {
                "question": "Yevropadagi eng katta davlat maydon jihatdan?",
                "answer": "Rossiya",
                "options": ["Rossiya", "Ukraina", "Fransiya", "Ispaniya"]
            },
            {
                "question": "Dunyodagi eng yirik qush?",
                "answer": "Tuyoqqush (Strus)",
                "options": ["Tuyoqqush (Strus)", "Burgut", "Pingvin", "Tovus"]
            },
            {
                "question": "O‘zbekistonning birinchi Prezidenti kim edi?",
                "answer": "Islom Karimov",
                "options": ["Islom Karimov", "Shavkat Mirziyoyev", "Abduqosimov", "Abdulla Oripov"]
            },
            {
                "question": "Shahzoda qahramoni bo‘lgan mashhur ingliz yozuvchisi?",
                "answer": "Shakespeare",
                "options": ["Shakespeare", "Dante", "Balzak", "Pushkin"]
            },
            {
                "question": "O‘zbekiston hududi asosan qaysi iqlim zonasida joylashgan?",
                "answer": "Quruq va kontinental",
                "options": ["Quruq va kontinental", "Ekvatorial", "Subtropik", "Nam tropik"]
            },
            {
                "question": "Dunyodagi eng katta cho‘l?",
                "answer": "Sahroi Kabir",
                "options": ["Sahroi Kabir", "Karakum", "Kizilqum", "Gobi"]
            },
            {
                "question": "Qaysi hayvon 'o‘rmon shohi' deb ataladi?",
                "answer": "Sher",
                "options": ["Sher", "Yo‘lbars", "Burgut", "Bo‘ri"]
            },
            {
                "question": "Mingbuloq, Arnasoy, Dengizko‘l — bular nima?",
                "answer": "Ko‘llar",
                "options": ["Ko‘llar", "Tog‘lar", "Shaharlar", "Daryolar"]
            },
            {
                "question": "‘Yulduzli tunlar’ romanining muallifi kim?",
                "answer": "Pirimqul Qodirov",
                "options": ["Pirimqul Qodirov", "O‘tkir Hoshimov", "Cho‘lpon", "Abdulla Qahhor"]
            },
            {
                "question": "Dunyodagi eng uzun devor?",
                "answer": "Xitoy devori",
                "options": ["Xitoy devori", "Berlin devori", "Hadrianning devori", "Bobil devori"]
            },
            {
                "question": "O‘zbekiston Konstitutsiyasi qachon qabul qilingan?",
                "answer": "1992 yil 8 dekabr",
                "options": ["1992 yil 8 dekabr", "1991 yil 1 sentyabr", "1993 yil 1 yanvar", "1995 yil 9 may"]
            },
            {
                "question": "O‘zbekistondagi eng uzun daryo?",
                "answer": "Amudaryo",
                "options": ["Amudaryo", "Sirdaryo", "Zarafshon", "Chirchiq"]
            },
            {
                "question": "Quyoshdan keyingi eng yaqin yulduz?",
                "answer": "Proksima Kentavra",
                "options": ["Proksima Kentavra", "Sirius", "Vega", "Betelgeyze"]
            },
            {
                "question": "Elektr toki kuchlanishi birligi?",
                "answer": "Volt",
                "options": ["Volt", "Amper", "Vatt", "Om"]
            },
            {
                "question": "Musiqada 4/4 o‘lchov nimani anglatadi?",
                "answer": "Oddiy marsh ritmi",
                "options": ["Oddiy marsh ritmi", "Vals", "Polka", "Rap"]
            },
            {
                "question": "O‘zbekiston bayrog‘ida nechta yulduz bor?",
                "answer": "12",
                "options": ["12", "13", "11", "10"]
            },
            {
                "question": "Dunyodagi eng baland hayvon?",
                "answer": "Jirafa",
                "options": ["Jirafa", "Fil", "Sher", "Ot"]
            },
            {
                "question": "O‘zbekiston gerbida tasvirlangan qush?",
                "answer": "Xumo",
                "options": ["Xumo", "Burgut", "Qarg‘a", "Qaldirg‘och"]
            },
            {
                "question": "Futbolning vatani hisoblangan davlat?",
                "answer": "Angliya",
                "options": ["Angliya", "Braziliya", "Italiya", "Ispaniya"]
            },
            {
                "question": "Dunyodagi eng yirik sutemizuvchi hayvon?",
                "answer": "Ko‘k kit",
                "options": ["Ko‘k kit", "Fil", "Tulki", "Ayiq"]
            },
            {
                "question": "Dunyodagi eng kichik mamlakat?",
                "answer": "Vatikan",
                "options": ["Vatikan", "Monako", "Andorra", "Lixtenshteyn"]
            },
            {
                "question": "O‘zbekistonning eng katta ko‘li?",
                "answer": "Aral dengizi",
                "options": ["Aral dengizi", "Aydarko‘l", "Tuzkon", "Qorako‘l"]
            },
            {
                "question": "Kislorodning kimyoviy belgisi?",
                "answer": "O",
                "options": ["O", "K", "N", "H"]
            },
            {
                "question": "Dunyodagi eng mashhur minoralardan biri - Eyfel minorasi qaysi shaharda?",
                "answer": "Parij",
                "options": ["Parij", "London", "Rim", "Berlin"]
            },
            {
                "question": "Qaysi sport turi 'oq sport' deb ataladi?",
                "answer": "Tennis",
                "options": ["Tennis", "Shaxmat", "Boks", "Basketbol"]
            },
            {
                "question": "Inson tanasida qancha tish bo‘ladi (katta yoshda)?",
                "answer": "32",
                "options": ["32", "28", "36", "30"]
            },
            {
                "question": "Qadimgi yunonlarning bosh xudosi kim?",
                "answer": "Zevs",
                "options": ["Zevs", "Afina", "Apollon", "Germes"]
            },
            {
                "question": "Kompyuter sichqonchasini ixtiro qilgan olim?",
                "answer": "Duqlas Engelbart",
                "options": ["Duqlas Engelbart", "Geyts", "Jobs", "Cerf"]
            },
            {
                "question": "Shaxmatdagi eng kuchli figura?",
                "answer": "Ferz",
                "options": ["Ferz", "Ot", "Shah", "Piyoda"]
            },
            {
                "question": "Armaniston poytaxti?",
                "answer": "Yerevan",
                "options": ["Yerevan", "Tbilisi", "Boku", "Minsk"]
            },
            {
                "question": "‘Bahor’ faslidan keyin qaysi fasl keladi?",
                "answer": "Yoz",
                "options": ["Yoz", "Kuz", "Qish", "Bahor yana"]
            },
            {
                "question": "Dunyodagi eng baland daraxt turi?",
                "answer": "Sekvoyya",
                "options": ["Sekvoyya", "Eman", "Qayrag‘och", "Tol"]
            },
            {
                "question": "Sho‘ro davrida qurilgan kosmik stansiya?",
                "answer": "Mir",
                "options": ["Mir", "Soyuz", "Saluyt", "Sputnik"]
            },
            {
                "question": "Avesto kitobi qaysi xalq merosi?",
                "answer": "Zardushtiylar",
                "options": ["Zardushtiylar", "Yunon", "Arab", "Hind"]
            },
            {
                "question": "O‘zbekistonning eng baland nuqtasi?",
                "answer": "Hazrati Sulton cho‘qqisi",
                "options": ["Hazrati Sulton cho‘qqisi", "Chimgan", "Bobotog‘", "Ayritom"]
            },
            {
                "question": "Osiyodagi eng uzun daryo?",
                "answer": "Yanszi",
                "options": ["Yanszi", "Sirdaryo", "Ind", "Amur"]
            },
            {
                "question": "O‘zbekiston milliy teatrining nomi?",
                "answer": "Navoi nomidagi teatr",
                "options": ["Navoi nomidagi teatr", "Yosh tomoshabinlar teatri", "O‘zbek filarmoniyasi", "Ilhom teatri"]
            },
            {
                "question": "Qaysi sayyora 'Qizil sayyora' deb ataladi?",
                "answer": "Mars",
                "options": ["Mars", "Yupiter", "Venera", "Merkuriy"]
            },
            {
                "question": "Dunyodagi eng katta yarimorol?",
                "answer": "Arabiston yarimoroli",
                "options": ["Arabiston yarimoroli", "Hindiston yarimoroli", "Iberiya yarimoroli", "Skandinaviya yarimoroli"]
            },
            {
                "question": "O‘zbekistonning eng ko‘p aholiga ega shahri?",
                "answer": "Toshkent",
                "options": ["Toshkent", "Samarqand", "Andijon", "Namangan"]
            },
            {
                "question": "Amerika bayrog‘idagi qizil rang nimani bildiradi?",
                "answer": "Jasorat",
                "options": ["Jasorat", "Ozodlik", "Adolat", "Birlik"]
            },
            {
                "question": "Qaysi davlatda eng ko‘p orollar bor?",
                "answer": "Shvetsiya",
                "options": ["Shvetsiya", "Indoneziya", "Filippin", "Yaponiya"]
            }
        ]

        quiz_2 = [
            # Diniy savollar 50ta
            {
                "question": "Payg‘ambarimizning ismlari nima?",
                "answer": "Muhammad",
                "options": ["Muhammad", "Ismoil", "Ibrohim", "Yusuf"]
            },
            {
                "question": "Payg‘ambarimiz tug‘ilgan shahri?",
                "answer": "Makka",
                "options": ["Makka", "Madina", "Quddus", "Buxoro"]
            },
            {
                "question": "Payg‘ambarimiz ko‘chib o‘tgan shahri?",
                "answer": "Madina",
                "options": ["Madina", "Makka", "Quddus", "Toyĭf"]
            },
            {
                "question": "Qur’onni tushirgan Zot kim?",
                "answer": "Alloh",
                "options": ["Alloh", "Jabroil", "Muhammad (s.a.v.)", "Muso (a.s.)"]
            },
            {
                "question": "Qur’onni olib kelgan farishta kim?",
                "answer": "Jabroil (a.s.)",
                "options": ["Jabroil", "Mikoil", "Isrofil", "Azroil"]
            },
            {
                "question": "Musulmonlarning muqaddas kitobi?",
                "answer": "Qur’on",
                "options": ["Qur’on", "Injil", "Tavrot", "Zabur"]
            },
            {
                "question": "Qur’onning oyatlari nima deb ataladi?",
                "answer": "Oyat",
                "options": ["Oyat", "Sura", "Hadis", "Kalima"]
            },
            {
                "question": "Qur’on boblari nima deb ataladi?",
                "answer": "Sura",
                "options": ["Sura", "Oyat", "Hadis", "Kalima"]
            },
            {
                "question": "Payg‘ambarimizning onalari ismi?",
                "answer": "Omina",
                "options": ["Omina", "Xadicha", "Maryam", "Fotima"]
            },
            {
                "question": "Payg‘ambarimizning bobolari ismi?",
                "answer": "Abdulmuttalib",
                "options": ["Abdulmuttalib", "Abu Tolib", "Abu Lahab", "Hamza"]
            },
            {
                "question": "Payg‘ambarimizning otalari ismi?",
                "answer": "Abdulloh",
                "options": ["Abdulloh", "Abdulmuttalib", "Abu Tolib", "Hamza"]
            },
            {
                "question": "Payg‘ambarimizning mashhur laqabi?",
                "answer": "Al-Amin",
                "options": ["Al-Amin", "As-Siddiq", "Al-Faruq", "Zunnurayn"]
            },
            {
                "question": "Musulmonlar kuniga necha mahal namoz o‘qiydi?",
                "answer": "5",
                "options": ["5", "3", "4", "6"]
            },
            {
                "question": "Tongda o‘qiladigan namoz?",
                "answer": "Bomdod",
                "options": ["Bomdod", "Peshin", "Asr", "Shom"]
            },
            {
                "question": "Peshinda o‘qiladigan namoz?",
                "answer": "Peshin",
                "options": ["Peshin", "Asr", "Bomdod", "Shom"]
            },
            {
                "question": "Kechqurun o‘qiladigan namoz?",
                "answer": "Shom",
                "options": ["Shom", "Bomdod", "Asr", "Peshin"]
            },
            {
                "question": "Eng oxirgi o‘qiladigan namoz?",
                "answer": "Xufton",
                "options": ["Xufton", "Shom", "Asr", "Peshin"]
            },
            {
                "question": "Ro‘za qaysi oyda tutiladi?",
                "answer": "Ramazon",
                "options": ["Ramazon", "Sha’bon", "Muharram", "Zulhijja"]
            },
            {
                "question": "Qurbonlik qaysi bayramda qilinadi?",
                "answer": "Qurbon hayiti",
                "options": ["Qurbon hayiti", "Ro‘za hayiti", "Navro‘z", "Hijriy yilboshi"]
            },
            {
                "question": "Ro‘za tugagach nishonlanadigan bayram?",
                "answer": "Ro‘za hayiti",
                "options": ["Ro‘za hayiti", "Qurbon hayiti", "Navro‘z", "Mehnat bayrami"]
            },
            {
                "question": "Payg‘ambarimizning qizlaridan eng mashhuri?",
                "answer": "Fotima",
                "options": ["Fotima", "Ruqayya", "Zaynab", "Ummu Kulsum"]
            },
            {
                "question": "Payg‘ambarimizning nabiralari?",
                "answer": "Hasan va Husayn",
                "options": ["Hasan va Husayn", "Ali va Umar", "Abu Bakr va Usmon", "Yusuf va Ya’qub"]
            },
            {
                "question": "Payg‘ambarimizning birinchi xotinlari?",
                "answer": "Xadicha",
                "options": ["Xadicha", "Ayshe", "Hafsa", "Sofiya"]
            },
            {
                "question": "Musulmonlarning salomi?",
                "answer": "Assalomu alaykum",
                "options": ["Assalomu alaykum", "Salom", "Hayrli kun", "Marhabo"]
            },
            {
                "question": "Salomga javob?",
                "answer": "Va alaykumussalom",
                "options": ["Va alaykumussalom", "Rahmat", "Yaxshi", "Hayr"]
            },
            {
                "question": "Islomda halol so‘zining teskarisi?",
                "answer": "Harom",
                "options": ["Harom", "Halal", "Sunnat", "Muboh"]
            },
            {
                "question": "Payg‘ambarimizning sevimli mevasi?",
                "answer": "Xurmo",
                "options": ["Xurmo", "Uzum", "Anjir", "Anor"]
            },
            {
                "question": "Allohning sifatlaridan biri?",
                "answer": "Rahmon",
                "options": ["Rahmon", "Aziz", "Samad", "Nur"]
            },
            {
                "question": "Allohning sifatlaridan yana biri?",
                "answer": "Rahim",
                "options": ["Rahim", "Qahhor", "Hakim", "Latif"]
            },
            {
                "question": "Allohning sifatlaridan yana biri?",
                "answer": "G‘affor",
                "options": ["G‘affor", "Azim", "Alim", "Kabir"]
            },
            {
                "question": "Allohning sifatlaridan yana biri?",
                "answer": "Qahhor",
                "options": ["Qahhor", "Samad", "Nur", "Latif"]
            },
            {
                "question": "Payg‘ambarimizning sevimli ichimligi?",
                "answer": "Suv",
                "options": ["Suv", "Sut", "Asal", "Sharbat"]
            },
            {
                "question": "Payg‘ambarimizning sevimli libosi?",
                "answer": "Oq kiyim",
                "options": ["Oq kiyim", "Qora kiyim", "Yashil kiyim", "Qimmat libos"]
            },
            {
                "question": "Musulmonlarning eng muqaddas uyi?",
                "answer": "Ka’ba",
                "options": ["Ka’ba", "Masjidul Aqso", "Masjid Nabaviy", "Quba masjidi"]
            },
            {
                "question": "Musulmonlarning eng muhim shahri?",
                "answer": "Makka",
                "options": ["Makka", "Madina", "Quddus", "Bag‘dod"]
            },
            {
                "question": "Payg‘ambarimizning sevimli hayvonlaridan biri?",
                "answer": "Ot",
                "options": ["Ot", "Tuya", "Qoy", "Sigir"]
            },
            {
                "question": "Islomda taqiqlangan ichimlik?",
                "answer": "Sharob",
                "options": ["Sharob", "Suv", "Sut", "Asal"]
            },
            {
                "question": "Islomda taqiqlangan go‘sht?",
                "answer": "Cho‘chqa go‘shti",
                "options": ["Cho‘chqa go‘shti", "Mol go‘shti", "Qo‘y go‘shti", "Tovuq go‘shti"]
            },
            {
                "question": "Namozdan oldin nima qilish kerak?",
                "answer": "Tahorat",
                "options": ["Tahorat", "Duo", "Ro‘za", "Haj"]
            },
            {
                "question": "Qur’onning eng birinchi so‘zi?",
                "answer": "Iqro’",
                "options": ["Iqro’", "Bismillah", "Alhamdu", "Qul"]
            },
            {
                "question": "Qur’onning eng oxirgi surasi?",
                "answer": "Nas",
                "options": ["Nas", "Falaq", "Ikhlos", "Kavsar"]
            },
            {
                "question": "Payg‘ambarimizning qabr joyi qayerda?",
                "answer": "Madina",
                "options": ["Madina", "Makka", "Quddus", "Toyĭf"]
            },
            {
                "question": "Qur’onni o‘qiyotganda nima deyiladi?",
                "answer": "Tilovat",
                "options": ["Tilovat", "Tafsir", "Hifz", "Qiroat"]
            },
            {
                "question": "Qur’onni yoddan bilgan odam kim?",
                "answer": "Hofiz",
                "options": ["Hofiz", "Qori", "Imom", "Muazzin"]
            },
            {
                "question": "Qur’onni chiroyli o‘qiydigan odam kim?",
                "answer": "Qori",
                "options": ["Qori", "Hofiz", "Faqih", "Imom"]
            },
            {
                "question": "Namozni boshqaradigan odam kim?",
                "answer": "Imom",
                "options": ["Imom", "Qori", "Faqih", "Muazzin"]
            },
            {
                "question": "Azonni aytadigan odam kim?",
                "answer": "Muazzin",
                "options": ["Muazzin", "Imom", "Qori", "Faqih"]
            },
            {
                "question": "Hadislarni o‘rgangan olim kim?",
                "answer": "Muhaddis",
                "options": ["Muhaddis", "Faqih", "Imom", "Qori"]
            },
            {
                "question": "Fiqh ilmini bilgan olim kim?",
                "answer": "Faqih",
                "options": ["Faqih", "Muhaddis", "Imom", "Qori"]
            },
            {
                "question": "Musulmonlarning asosiy duosi qanday boshlanadi?",
                "answer": "Bismillahir rohmanir rohiym",
                "options": ["Bismillahir rohmanir rohiym", "Alhamdulillah", "La ilaha illalloh", "Subhanalloh"]
            },
            # Fanga oid savollar 100ta
            {
                "question": "Quyosh tizimidagi eng kichik sayyora?",
                "answer": "Merkuriy",
                "options": ["Merkuriy", "Mars", "Pluton", "Venera"]
            },
            {
                "question": "Birinchi avtomobilni kim yasagan?",
                "answer": "Karl Bens",
                "options": ["Karl Bens", "Genri Ford", "Nikola Tesla", "Tomas Edison"]
            },
            {
                "question": "Qaysi davlat 'Quyosh chiqish mamlakati' deb ataladi?",
                "answer": "Yaponiya",
                "options": ["Yaponiya", "Xitoy", "Koreya", "Hindiston"]
            },
            {
                "question": "Alisher Navoiy qaysi tilning asoschisi hisoblanadi?",
                "answer": "O‘zbek adabiy tili",
                "options": ["O‘zbek adabiy tili", "Fors tili", "Arab tili", "Turk tili"]
            },
            {
                "question": "Qaysi hayvon tuxum qo‘yadi?",
                "answer": "To‘tiqush",
                "options": ["To‘tiqush", "Mushuk", "Ot", "Fil"]
            },
            {
                "question": "Afrikadagi eng baland tog‘?",
                "answer": "Kilimanjaro",
                "options": ["Kilimanjaro", "Atlas", "Drakensberg", "Kenya"]
            },
            {
                "question": "O‘zbek xalqining milliy cholg‘usi?",
                "answer": "Doira",
                "options": ["Doira", "Gitara", "Fortepiano", "Skripka"]
            },
            {
                "question": "Yevropadagi eng katta shahar?",
                "answer": "Moskva",
                "options": ["Moskva", "London", "Parij", "Berlin"]
            },
            {
                "question": "Suvning kimyoviy formulasi?",
                "answer": "H2O",
                "options": ["H2O", "CO2", "O2", "NaCl"]
            },
            {
                "question": "Qaysi sport turi 'shohlar o‘yini' deb ataladi?",
                "answer": "Shaxmat",
                "options": ["Shaxmat", "Futbol", "Basketbol", "Boks"]
            },
            {
                "question": "Qadimgi Rim imperiyasining poytaxti?",
                "answer": "Rim",
                "options": ["Rim", "Afina", "Istanbul", "Neapol"]
            },
            {
                "question": "O‘zbekistonning milliy valyutasi 1994 yilda qaysi pul o‘rniga kiritilgan?",
                "answer": "So‘m-kupon",
                "options": ["So‘m-kupon", "Rubl", "Tanga", "Dollar"]
            },
            {
                "question": "Afrika qit’asida joylashgan eng katta davlat?",
                "answer": "Jazoir",
                "options": ["Jazoir", "Misr", "Nigeriya", "Kongo"]
            },
            {
                "question": "O‘zbekistondagi eng qadimiy shahar?",
                "answer": "Buxoro",
                "options": ["Buxoro", "Samarqand", "Xiva", "Termiz"]
            },
            {
                "question": "Dunyodagi eng mashhur klassik bastakor?",
                "answer": "Betxoven",
                "options": ["Betxoven", "Motsart", "Bax", "Sho‘stopovich"]
            },
            {
                "question": "Avstraliya qit’asida uchraydigan mashhur hayvon?",
                "answer": "Kanguru",
                "options": ["Kanguru", "Fil", "Sher", "Bo‘ri"]
            },
            {
                "question": "O‘zbekistondagi eng katta kon?",
                "answer": "Qizilqum oltin koni",
                "options": ["Qizilqum oltin koni", "Angren ko‘mir koni", "Olmaliq mis koni", "Sharg‘un ko‘mir koni"]
            },
            {
                "question": "Yevropadagi eng uzun daryo?",
                "answer": "Volga",
                "options": ["Volga", "Dunay", "Rhin", "Loira"]
            },
            {
                "question": "Dunyodagi eng yirik sport musobaqasi?",
                "answer": "Olimpiya o‘yinlari",
                "options": ["Olimpiya o‘yinlari", "Jahon chempionati", "UEFA Chempionlar ligasi", "Davis kubogi"]
            },
            {
                "question": "O‘zbekistonning milliy taomi tandirda pishiriladigan non?",
                "answer": "Tandir non",
                "options": ["Tandir non", "Somsa", "Chuchvara", "Lag‘mon"]
            },
            {
                "question": "Yer yuzidagi eng issiq harorat qayd etilgan cho‘l?",
                "answer": "Lut cho‘li",
                "options": ["Lut cho‘li", "Sahroi Kabir", "Karakum", "Kizilqum"]
            },
            {
                "question": "Qaysi davlatda 'Taj Mahal' joylashgan?",
                "answer": "Hindiston",
                "options": ["Hindiston", "Pokiston", "Bangladesh", "Nepal"]
            },
            {
                "question": "O‘zbekistonda qaysi viloyat 'paxtachilik markazi' sifatida tanilgan?",
                "answer": "Farg‘ona",
                "options": ["Farg‘ona", "Samarqand", "Buxoro", "Navoiy"]
            },
            {
                "question": "Eng mashhur rus yozuvchilaridan biri?",
                "answer": "Tolstoy",
                "options": ["Tolstoy", "Pushkin", "Dostoevskiy", "Chexov"]
            },
            {
                "question": "Qaysi sport turi muz ustida o‘ynaladi?",
                "answer": "Xokkey",
                "options": ["Xokkey", "Basketbol", "Futbol", "Voleybol"]
            },
            {
                "question": "Qaysi shahar 'sharq durdonasi' deb ataladi?",
                "answer": "Samarqand",
                "options": ["Samarqand", "Buxoro", "Xiva", "Termiz"]
            },
            {
                "question": "Bir soatda nechta daqiqa bor?",
                "answer": "60",
                "options": ["60", "100", "30", "90"]
            },
            {
                "question": "Qaysi davlatda eng ko‘p aholiga ega shahar — Mexiko joylashgan?",
                "answer": "Meksika",
                "options": ["Meksika", "Braziliya", "Argentina", "Ispaniya"]
            },
            {
                "question": "Qaysi hayvon 'sahro kemasi' deb ataladi?",
                "answer": "Tuyа",
                "options": ["Tuyа", "Ot", "Sigir", "Fil"]
            },
            {
                "question": "O‘zbekiston qaysi materikda joylashgan?",
                "answer": "Osiyo",
                "options": ["Osiyo", "Yevropa", "Afrika", "Amerika"]
            },
            {
                "question": "Eng mashhur italyan rassomi?",
                "answer": "Leonardo da Vinchi",
                "options": ["Leonardo da Vinchi", "Mikelanjelo", "Rafael", "Donatello"]
            },
            {
                "question": "Yer sharidagi eng katta okean qirg‘og‘iga ega davlat?",
                "answer": "Kanada",
                "options": ["Kanada", "Rossiya", "AQSh", "Avstraliya"]
            },
            {
                "question": "O‘zbekistonda eng katta suv ombori?",
                "answer": "To‘dako‘l",
                "options": ["To‘dako‘l", "Chorvoq", "Qoratepa", "Bo‘zsuv"]
            },
            {
                "question": "Qaysi hayvon eng tez yuguradi?",
                "answer": "Gepard",
                "options": ["Gepard", "Ot", "Bo‘ri", "Sher"]
            },
            {
                "question": "Qaysi shahar 'abadiy shahar' deb ataladi?",
                "answer": "Rim",
                "options": ["Rim", "Afina", "Istanbul", "Parij"]
            },
            {
                "question": "Dunyodagi eng ko‘p aholiga ega davlat?",
                "answer": "Xitoy",
                "options": ["Xitoy", "Hindiston", "AQSh", "Indoneziya"]
            },
            {
                "question": "O‘zbek milliy libosidagi eng asosiy bosh kiyim?",
                "answer": "Do‘ppi",
                "options": ["Do‘ppi", "Telpak", "Salla", "Kepka"]
            },
            {
                "question": "Qaysi davlat 'pasta' va 'pitsa' vatani?",
                "answer": "Italiya",
                "options": ["Italiya", "Fransiya", "Ispaniya", "Gretsiya"]
            },
            {
                "question": "Qaysi davlatning poytaxti Berlin?",
                "answer": "Germaniya",
                "options": ["Germaniya", "Fransiya", "Polsha", "Avstriya"]
            },
            {
                "question": "Yerning o‘rtacha radiusi taxminan nechaga teng?",
                "answer": "6371 km",
                "options": ["6371 km", "7000 km", "5500 km", "6000 km"]
            },
            {
                "question": "O‘zbekiston hududidan oqib o‘tadigan eng yirik daryo?",
                "answer": "Amudaryo",
                "options": ["Sirdaryo", "Amudaryo", "Zarafshon", "Qashqadaryo"]
            },
            {
                "question": "Qaysi davlatda eng ko‘p ko‘llar bor?",
                "answer": "Kanada",
                "options": ["Kanada", "Rossiya", "Braziliya", "AQSh"]
            },
            {
                "question": "Dunyodagi eng katta tog‘ tizmasi?",
                "answer": "Gimolay",
                "options": ["Gimolay", "And", "Tyan-Shan", "Alp"]
            },
            {
                "question": "O‘zbekistonning eng baland shahri?",
                "answer": "Chorvoq",
                "options": ["Chorvoq", "Termiz", "Buxoro", "Urganch"]
            },
            {
                "question": "Afrikadagi eng ko‘p aholiga ega davlat?",
                "answer": "Nigeriya",
                "options": ["Nigeriya", "Misr", "Efiopiya", "Jazoir"]
            },
            {
                "question": "Dunyodagi eng katta ormon?",
                "answer": "Amazonka",
                "options": ["Amazonka", "Taiga", "Kongo", "Yevropa o‘rmonlari"]
            },
            {
                "question": "Qaysi shahar Buyuk Britaniya poytaxti?",
                "answer": "London",
                "options": ["London", "Parij", "Madrid", "Berlin"]
            },
            {
                "question": "Shveytsariya qaysi narsalari bilan mashhur?",
                "answer": "Soatlar",
                "options": ["Soatlar", "Mashinalar", "Telefonlar", "Raketalar"]
            },
            {
                "question": "O‘zbekistonda eng ko‘p yetishtiriladigan meva?",
                "answer": "Uzum",
                "options": ["Uzum", "Olma", "Anor", "O‘rik"]
            },
            {
                "question": "Qaysi shahar O‘zbekistonning qadimiy poytaxti bo‘lgan?",
                "answer": "Samarqand",
                "options": ["Samarqand", "Buxoro", "Xiva", "Toshkent"]
            },
            {
                "question": "Amerikada joylashgan eng mashhur sharshara?",
                "answer": "Niagara",
                "options": ["Niagara", "Iguasu", "Victoria", "Anxel"]
            },
            {
                "question": "Mashhur futbolchi Lionel Messining vatani?",
                "answer": "Argentina",
                "options": ["Argentina", "Ispaniya", "Braziliya", "Portugaliya"]
            },
            {
                "question": "Hindistondagi eng mashhur kino sanoati nomi?",
                "answer": "Bollivud",
                "options": ["Bollivud", "Gollivud", "Tolivud", "Kolivud"]
            },
            {
                "question": "Dunyodagi eng katta ko‘rfaz?",
                "answer": "Bengal ko‘rfazi",
                "options": ["Bengal ko‘rfazi", "Meksika ko‘rfazi", "Aden ko‘rfazi", "Pers ko‘rfazi"]
            },
            {
                "question": "Elektr toki qarshiligi birligi?",
                "answer": "Om",
                "options": ["Om", "Amper", "Volt", "Vatt"]
            },
            {
                "question": "Yaponiyaning milliy sporti?",
                "answer": "Sumo",
                "options": ["Sumo", "Karate", "Judo", "Kendo"]
            },
            {
                "question": "O‘zbekiston Respublikasi Davlat madhiyasining matn muallifi kim?",
                "answer": "Abdulla Oripov",
                "options": ["Abdulla Oripov", "Erkin Vohidov", "Cho‘lpon", "O‘tkir Hoshimov"]
            },
            {
                "question": "Qaysi davlat 'piramidalar mamlakati' deb ataladi?",
                "answer": "Misr",
                "options": ["Misr", "Meksika", "Xitoy", "Hindiston"]
            },
            {
                "question": "Dunyodagi eng katta metall ishlab chiqaruvchi davlat?",
                "answer": "Xitoy",
                "options": ["Xitoy", "AQSh", "Rossiya", "Hindiston"]
            },
            {
                "question": "Yer yuzidagi eng chuqur ko‘l?",
                "answer": "Baykal",
                "options": ["Baykal", "Tanganika", "Viktoriya", "Aral"]
            },
            {
                "question": "Dunyodagi eng baland minora?",
                "answer": "Burj Xalifa",
                "options": ["Burj Xalifa", "Eyfel minorasi", "CN Tower", "Empire State Building"]
            },
            {
                "question": "Kimyo fanida O belgisi qaysi elementga tegishli?",
                "answer": "Kislorod",
                "options": ["Kislorod", "Vodorod", "Azot", "Heliy"]
            },
            {
                "question": "Yozuv mashinasini kim ixtiro qilgan?",
                "answer": "Sholes",
                "options": ["Sholes", "Bell", "Edison", "Tesla"]
            },
            {
                "question": "Qaysi shahar 'Osmon minoralari shahri' deb ataladi?",
                "answer": "Dubay",
                "options": ["Dubay", "Nyu-York", "Parij", "Seul"]
            },
            {
                "question": "Dunyodagi eng ko‘p aholiga ega shahar?",
                "answer": "Tokio",
                "options": ["Tokio", "Dehli", "Shanxay", "Meksiko"]
            },
            {
                "question": "Sharqning mashhur olimi Ibn Sino qaysi sohada mashhur?",
                "answer": "Tibbiyot",
                "options": ["Tibbiyot", "Matematika", "Astronomiya", "Adabiyot"]
            },
            {
                "question": "Yashil rangdagi sabzavotlardan biri?",
                "answer": "Bodring",
                "options": ["Bodring", "Sabzi", "Karam", "Piyoz"]
            },
            {
                "question": "Dunyodagi eng katta dengiz?",
                "answer": "Qora dengiz",
                "options": ["Qora dengiz", "O‘lik dengiz", "Kaspiy dengizi", "Oq dengiz"]
            },
            {
                "question": "Kompyuter klaviaturasidagi 'Space' tugmasi nima vazifani bajaradi?",
                "answer": "Bo‘sh joy qo‘yish",
                "options": ["Bo‘sh joy qo‘yish", "O‘chirish", "Nusxa olish", "Kiritish"]
            },
            {
                "question": "O‘zbekistonning eng katta cho‘li?",
                "answer": "Qizilqum",
                "options": ["Qizilqum", "Karakum", "Sahroi Kabir", "Gobi"]
            },
            {
                "question": "Qaysi davlatda eng ko‘p vulqonlar mavjud?",
                "answer": "Indoneziya",
                "options": ["Indoneziya", "Yaponiya", "Italiya", "Rossiya"]
            },
            {
                "question": "O‘zbek milliy ertak qahramonlaridan biri?",
                "answer": "Zumrad va Qimmat",
                "options": ["Zumrad va Qimmat", "Shrek", "Aladin", "Cinderella"]
            },
            {
                "question": "Shaharlarda odam tashuvchi asosiy transport vositasi?",
                "answer": "Avtobus",
                "options": ["Avtobus", "Samolyot", "Poyezd", "Tramvay"]
            },
            {
                "question": "Qaysi davlatning poytaxti Vashington?",
                "answer": "AQSh",
                "options": ["AQSh", "Kanada", "Meksika", "Braziliya"]
            },
            {
                "question": "Kompyuter monitorida tasvir hosil qiluvchi nuqta nima deb ataladi?",
                "answer": "Piksel",
                "options": ["Piksel", "Bayt", "Kadr", "Bit"]
            },
            {
                "question": "Mashhur bastakor Motsart qaysi davlatda tug‘ilgan?",
                "answer": "Avstriya",
                "options": ["Avstriya", "Germaniya", "Fransiya", "Italiya"]
            },
            {
                "question": "Dunyodagi eng baland binolardan biri - 'Taipei 101' qayerda joylashgan?",
                "answer": "Tayvan",
                "options": ["Tayvan", "Xitoy", "Singapur", "Malayziya"]
            },
            {
                "question": "Afrikaning eng uzun daryosi?",
                "answer": "Nil",
                "options": ["Nil", "Niger", "Kongo", "Zambezi"]
            },
            {
                "question": "Dunyodagi eng sovuq shahar?",
                "answer": "Oymyakon",
                "options": ["Oymyakon", "Moskva", "Oslo", "Reykyavik"]
            },
            {
                "question": "Insoniyat tarixidagi birinchi yozuv qaysi?",
                "answer": "Mixxat",
                "options": ["Mixxat", "Lotin alifbosi", "Kirill alifbosi", "Arab yozuvi"]
            },
            {
                "question": "Dunyodagi eng katta metall ishlab chiqaruvchi kompaniya?",
                "answer": "ArcelorMittal",
                "options": ["ArcelorMittal", "General Motors", "Samsung", "Apple"]
            },
            {
                "question": "Mashhur multfilm qahramoni Mickey Mouse qaysi studiyaga tegishli?",
                "answer": "Disney",
                "options": ["Disney", "Pixar", "Marvel", "DreamWorks"]
            },
            {
                "question": "Dunyodagi eng baland daraxt qayerda o‘sadi?",
                "answer": "Kaliforniya",
                "options": ["Kaliforniya", "Amazonka", "Kanada", "Avstraliya"]
            },
            {
                "question": "O‘zbekistonda qaysi sport turi juda mashhur?",
                "answer": "Kurash",
                "options": ["Kurash", "Boks", "Shaxmat", "Futbol"]
            },
            {
                "question": "Yer yuzida eng ko‘p tarqalgan tilda so‘zlashuvchilar?",
                "answer": "Xitoy tili",
                "options": ["Xitoy tili", "Ingliz tili", "Ispan tili", "Hind tili"]
            },
            {
                "question": "Insoniyat tarixidagi birinchi yozma kitob?",
                "answer": "Avesto",
                "options": ["Avesto", "Injil", "Qur’on", "Torah"]
            },
            {
                "question": "O‘zbekistonning eng issiq shahri?",
                "answer": "Termiz",
                "options": ["Termiz", "Nukus", "Xiva", "Urganch"]
            },
            {
                "question": "Mashhur futbolchi Ronaldoning vatani?",
                "answer": "Portugaliya",
                "options": ["Portugaliya", "Braziliya", "Ispaniya", "Argentina"]
            },
            {
                "question": "Eng mashhur yunon matematigi?",
                "answer": "Pifagor",
                "options": ["Pifagor", "Evklid", "Arximed", "Tales"]
            },
            {
                "question": "O‘zbek milliy kuylaridan biri?",
                "answer": "Tanovar",
                "options": ["Tanovar", "Segoh", "Munojot", "Rast"]
            },
            {
                "question": "Yer kurrasidagi eng katta yarim shar qaysi?",
                "answer": "Shimoliy yarim shar",
                "options": ["Shimoliy yarim shar", "Janubiy yarim shar", "Sharqiy yarim shar", "G‘arbiy yarim shar"]
            },
            {
                "question": "Qaysi shaharni 'Shamollar shahri' deb atashadi?",
                "answer": "Chicago",
                "options": ["Chicago", "Nyu-York", "London", "Tokio"]
            },
            {
                "question": "Qaysi hayvon sut beruvchi hayvon emas?",
                "answer": "To‘tiqush",
                "options": ["To‘tiqush", "Sigir", "Ot", "Qo‘y"]
            },
            {
                "question": "Qaysi davlatda 'Kreml' joylashgan?",
                "answer": "Rossiya",
                "options": ["Rossiya", "Xitoy", "Fransiya", "Germaniya"]
            },
            {
                "question": "O‘zbekistonda eng mashhur milliy o‘yinlardan biri?",
                "answer": "Ko‘pkari",
                "options": ["Ko‘pkari", "Shaxmat", "Tennis", "Futbol"]
            },
            {
                "question": "O‘zbekistonning milliy sport turi qaysi?",
                "answer": "Kurash",
                "options": ["Kurash", "Boks", "Futbol", "Basketbol"]
            },
            {
                "question": "Qaysi hayvon uchib yuradi?",
                "answer": "Qush",
                "options": ["Qush", "Ot", "Sigir", "Ilon"]
            },
            {
                "question": "Yer sharida nechta qutb bor?",
                "answer": "2",
                "options": ["2", "3", "4", "1"]
            },
            {
                "question": "O‘zbekistonning milliy musiqiy cholg‘ularidan biri?",
                "answer": "Doira",
                "options": ["Gitara", "Doira", "Pianino", "Skripka"]
            },
            {
                "question": "Yerning sun’iy yo‘ldoshi nima deb ataladi?",
                "answer": "Sun’iy yo‘ldosh",
                "options": ["Oy", "Sun’iy yo‘ldosh", "Quyosh", "Sayyora"]
            }
        ]

        quiz_3 = [
            # Diniy savollar 50ta
            {
                "question": "Qur’onda eng ko‘p ishlatilgan ism qaysi payg‘ambarnikidir?",
                "answer": "Muso (a.s.)",
                "options": ["Iso (a.s.)", "Ibrohim (a.s.)", "Muso (a.s.)", "Nuh (a.s.)"]
            },
            {
                "question": "Musulmonlarning muqaddas kitobi qaysi?",
                "answer": "Qur'on",
                "options": ["Injil", "Qur'on", "Tavrot", "Zabur"]
            },
            {
                "question": "Qibla qaysi shaharga qaratiladi?",
                "answer": "Makka",
                "options": ["Madina", "Quddus", "Makka", "Damashq"]
            },
            {
                "question": "Islomda eng asosiy kalima nima deb ataladi?",
                "answer": "Kalimai shahodat",
                "options": ["Kalimai shahodat", "Tasbih", "Takbir", "Tahlil"]
            },
            {
                "question": "Payg‘ambarimiz Muhammad (s.a.v.)ning tug‘ilgan shahri?",
                "answer": "Makka",
                "options": ["Makka", "Toyĭf", "Madina", "Badr"]
            },
            {
                "question": "Islomda kuniga necha mahal namoz farz?",
                "answer": "Besh mahal",
                "options": ["Uch mahal", "To‘rt mahal", "Besh mahal", "Olti mahal"]
            },
            {
                "question": "Ramazon oyida tutilgan ibodat qanday ataladi?",
                "answer": "Ro‘za",
                "options": ["Haj", "Ro‘za", "Zikr", "Sadaqa"]
            },
            {
                "question": "Qur’on oyatlarining tili qaysi?",
                "answer": "Arab tili",
                "options": ["Fors tili", "Arab tili", "Turk tili", "Ibroniy tili"]
            },
            {
                "question": "Islomning birinchi ustuni nima?",
                "answer": "Imon keltirish (kalima)",
                "options": ["Namoz", "Ro‘za", "Haj", "Imon keltirish (kalima)"]
            },
            {
                "question": "Azonni kim aytadi?",
                "answer": "Muazzin",
                "options": ["Imom", "Muazzin", "Qori", "Mudarris"]
            },
            {
                "question": "Qur’onda nechta sura bor?",
                "answer": "114",
                "options": ["99", "110", "114", "120"]
            },
            {
                "question": "Qur’onning eng uzun surasi qaysi?",
                "answer": "Al-Baqara",
                "options": ["Al-Fotiha", "Al-Baqara", "An-Nas", "Al-Ikhlos"]
            },
            {
                "question": "Qur’onning eng qisqa suralaridan biri qaysi?",
                "answer": "Al-Kavsar",
                "options": ["Al-Kavsar", "Yosin", "Ar-Rahmon", "Al-Mulk"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ga vahiy birinchi marta qaysi g‘orda nozil bo‘lgan?",
                "answer": "Hiro",
                "options": ["Saur", "Hiro", "Hira", "Safa"]
            },
            {
                "question": "Musulmonlarning jamoaviy ibodat joyi nima deb ataladi?",
                "answer": "Masjid",
                "options": ["Kalon", "Masjid", "Madrasa", "Honaqo"]
            },
            {
                "question": "Ramazon tugagach nishonlanadigan bayram nomi?",
                "answer": "Ramazon hayit",
                "options": ["Qurbon hayit", "Navro‘z", "Ramazon hayit", "Mehnat bayrami"]
            },
            {
                "question": "Qurbonlik qilinadigan bayram nomi?",
                "answer": "Qurbon hayit",
                "options": ["Qurbon hayit", "Ramazon hayit", "Navro‘z", "Ro‘za hayit"]
            },
            {
                "question": "Musulmonlarning salomi qaysi ibora?",
                "answer": "Assalomu alaykum",
                "options": ["Assalomu alaykum", "Marhabo", "Salom", "Xush kelibsiz"]
            },
            {
                "question": "“Assalomu alaykum” javobi qaysi?",
                "answer": "Vaalaykumussalom",
                "options": ["Vaalaykumussalom", "Rahmat", "Yaxshimisiz", "Hayr"]
            },
            {
                "question": "Namozdan oldin qilinadigan poklanish amali?",
                "answer": "Tahorat (vudu')",
                "options": ["G‘usl", "Tayammum", "Tahorat (vudu')", "Istinjo"]
            },
            {
                "question": "“Bismillahir rohmanir rohiym” qaysi ibora?",
                "answer": "Basmalah",
                "options": ["Kalima", "Basmalah", "Salavot", "Tasbih"]
            },
            {
                "question": "“Allohu akbar” iborasi nima deb ataladi?",
                "answer": "Takbir",
                "options": ["Takbir", "Tahmid", "Tahlil", "Tasbih"]
            },
            {
                "question": "“Alhamdulillah” qanday zikr?",
                "answer": "Tahmid",
                "options": ["Tahlil", "Tahmid", "Takbir", "Salavot"]
            },
            {
                "question": "“Subhanalloh” qanday zikr?",
                "answer": "Tasbih",
                "options": ["Tasbih", "Tahlil", "Tahmid", "Takbir"]
            },
            {
                "question": "“La ilaha illalloh” qanday zikr?",
                "answer": "Tahlil",
                "options": ["Takbir", "Tahmid", "Tahlil", "Tasbih"]
            },
            {
                "question": "Qur’onning birinchi surasi qaysi?",
                "answer": "Al-Fotiha",
                "options": ["Al-Fotiha", "Al-Baqara", "An-Naba", "Al-Ikhlos"]
            },
            {
                "question": "Islomda zakot nima?",
                "answer": "Mol-dunyodan beriladigan farz sadaqa",
                "options": ["Ro‘za tutish", "Mol-dunyodan beriladigan farz sadaqa", "Haj ibodati", "Sunnat namoz"]
            },
            {
                "question": "Haj ibodati qayerda ado etiladi?",
                "answer": "Makka atroflarida",
                "options": ["Quddus", "Makka atroflarida", "Madina", "Damashq"]
            },
            {
                "question": "Laylatul-Qadr qaysi oyda bo‘ladi?",
                "answer": "Ramazon",
                "options": ["Muharram", "Sha’bon", "Ramazon", "Zulhijja"]
            },
            {
                "question": "Ro‘za ochish vaqti nima deb ataladi?",
                "answer": "Iftor",
                "options": ["Imsok", "Iftor", "Tarovih", "Saharlik"]
            },
            {
                "question": "Ro‘zani boshlashdan oldingi tonggi taom?",
                "answer": "Saharlik",
                "options": ["Saharlik", "Iftor", "Nonushta", "Suhoor emas"]
            },
            {
                "question": "Tarovih namozi qachon o‘qiladi?",
                "answer": "Ramazon kechalarida",
                "options": ["Har kecha", "Jumada", "Ramazon kechalarida", "Bayram kunlari"]
            },
            {
                "question": "Islomda “halol” so‘zining ma’nosi?",
                "answer": "Ruxsat etilgan",
                "options": ["Man qilingan", "Ruxsat etilgan", "Shubhali", "Haromga yaqin"]
            },
            {
                "question": "“Harom” so‘zining ma’nosi?",
                "answer": "Ta’qiqlangan",
                "options": ["Go‘zal", "Muborak", "Ta’qiqlangan", "Mustahab"]
            },
            {
                "question": "Payg‘ambarimizga (s.a.v.) salom aytish qanday ibora bilan bo‘ladi?",
                "answer": "Salavot",
                "options": ["Salavot", "Takbir", "Tahlil", "Tahmid"]
            },
            {
                "question": "Masjidda namoz boshida qaysi takbir aytiladi?",
                "answer": "Takbiratul-ihram",
                "options": ["Takbiratul-ula", "Takbiratul-ihram", "Takbiratul-bayram", "Takbiratuz-zikr"]
            },
            {
                "question": "Qur’onni yod olgan kishiga beriladigan nom?",
                "answer": "Hofiz",
                "options": ["Qori", "Hofiz", "Imom", "Faqih"]
            },
            {
                "question": "Qur’onni chiroyli o‘qiydigan kishiga beriladigan nom?",
                "answer": "Qori",
                "options": ["Hofiz", "Qori", "Imom", "Muazzin"]
            },
            {
                "question": "Namoz yakunida o‘ng va chapga salom berish amali?",
                "answer": "Taslim",
                "options": ["Qiyom", "Ruku", "Sajda", "Taslim"]
            },
            {
                "question": "Tahoratda yuzni yuvishdan oldin nima qilinadi?",
                "answer": "Qo‘lni yuvish",
                "options": ["Qo‘lni yuvish", "Mas’h", "Oyog‘ni yuvish", "Sajda"]
            },
            {
                "question": "Juma kuni o‘qiladigan maxsus namoz?",
                "answer": "Juma namozi",
                "options": ["Tarovih", "Juma namozi", "Iyd namozi", "Vitr"]
            },
            {
                "question": "Makkadagi muqaddas uy qanday ataladi?",
                "answer": "Ka’ba",
                "options": ["Masjidun Nabaviy", "Al-Aqso", "Ka’ba", "Safa-Marva"]
            },
            {
                "question": "Namozdagi egilish amali nima?",
                "answer": "Ruku",
                "options": ["Ruku", "Sajda", "Qiyom", "Jalsa"]
            },
            {
                "question": "Namozdagi peshonani yerga qo‘yish amali nima?",
                "answer": "Sajda",
                "options": ["Jalsa", "Qiyom", "Sajda", "Ruku"]
            },
            {
                "question": "Musulmonlar uchun eng muqaddas ikki shahar qaysilar?",
                "answer": "Makka va Madina",
                "options": ["Makka va Madina", "Makka va Quddus", "Madina va Damashq", "Quddus va Bag‘dod"]
            },
            {
                "question": "Zakot berishning maqsadlaridan biri?",
                "answer": "Beva-bechoralarga yordam",
                "options": ["Molni ko‘paytirish uchun", "Beva-bechoralarga yordam", "Safarga ruxsat", "Bayram nishoni"]
            },
            {
                "question": "Islomda tozalikka oid umumiy tushuncha?",
                "answer": "Tahorat va poklik",
                "options": ["Husn", "Nafosat", "Tahorat va poklik", "Zuhd"]
            },
            {
                "question": "Qur’ondagi so‘nggi sura nomi?",
                "answer": "An-Nas",
                "options": ["Al-Falaq", "An-Nas", "Al-Ikhlos", "An-Naba"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.) hijrat qilgan shahar?",
                "answer": "Yasrib (Madina)",
                "options": ["Toyĭf", "Yasrib (Madina)", "Makka", "Hunayn"]
            },
            {
                "question": "Besh vaqt namozdan biri bo‘lmaganini toping.",
                "answer": "Tarovih",
                "options": ["Bomdod", "Peshin", "Asr", "Tarovih"]
            },
            # Fanga oid savollar 100ta
            {
                "question": "Toshkent metrosi nechanchi yilda ochilgan?",
                "answer": "1977",
                "options": ["1980", "1977", "1991", "1965"]
            },
            {
                "question": "Dunyoning eng katta qushi?",
                "answer": "Tuyoqqush",
                "options": ["Qaldirg‘och", "Tuyoqqush", "Lochin", "Kabutar"]
            },
            {
                "question": "O‘zbekistonda qaysi shahar 'Go‘zal Buxoro' deb ataladi?",
                "answer": "Buxoro",
                "options": ["Buxoro", "Xiva", "Samarqand", "Toshkent"]
            },
            {
                "question": "Eng mashhur futbolchilar o‘yinini o‘tkazadigan maydon?",
                "answer": "Stadion",
                "options": ["Teatr", "Stadion", "Ko‘cha", "Zal"]
            },
            {
                "question": "Yer sharidagi eng katta hayvon?",
                "answer": "Ko‘k kit",
                "options": ["Ko‘k kit", "Fil", "Akula", "Ot"]
            },
            {
                "question": "O‘zbekistonda qaysi shahar 'ko‘hna shahar' deb ataladi?",
                "answer": "Samarqand",
                "options": ["Andijon", "Samarqand", "Qo‘qon", "Namangan"]
            },
            {
                "question": "Dunyodagi eng mashhur minoralardan biri — Big Ben qayerda joylashgan?",
                "answer": "London",
                "options": ["Parij", "Berlin", "London", "Nyu-York"]
            },
            {
                "question": "O‘zbekistonning milliy raqsi?",
                "answer": "Lazgi",
                "options": ["Vals", "Lazgi", "Sirtaki", "Samba"]
            },
            {
                "question": "Qaysi davlatda eng ko‘p kangurular yashaydi?",
                "answer": "Avstraliya",
                "options": ["Avstraliya", "Afrika", "Hindiston", "Braziliya"]
            },
            {
                "question": "O‘zbekistonda qaysi viloyat 'paxtasi' bilan mashhur?",
                "answer": "Farg‘ona",
                "options": ["Surxondaryo", "Farg‘ona", "Xorazm", "Jizzax"]
            },
            {
                "question": "O‘zbekistonning eng mashhur tarixiy obidalaridan biri — Minorai Kalon qayerda?",
                "answer": "Buxoro",
                "options": ["Xiva", "Buxoro", "Samarqand", "Shahrisabz"]
            },
            {
                "question": "Kompyuterni boshqarish uchun ishlatiladigan qurilma?",
                "answer": "Sichqoncha",
                "options": ["Mikrofon", "Sichqoncha", "Printer", "Kamera"]
            },
            {
                "question": "O‘zbekistonning milliy gullaridan biri?",
                "answer": "Lola",
                "options": ["Atirgul", "Lola", "Chinnigul", "Nargis"]
            },
            {
                "question": "Telefonni kim ixtiro qilgan?",
                "answer": "Aleksandr Bell",
                "options": ["Tomas Edison", "Aleksandr Bell", "Nyuton", "Einshteyn"]
            },
            {
                "question": "O‘zbekistonda qaysi shahar 'me’morlar shahri' deb ataladi?",
                "answer": "Shahrisabz",
                "options": ["Shahrisabz", "Samarqand", "Buxoro", "Toshkent"]
            },
            {
                "question": "Dunyoning eng chuqur ko‘li?",
                "answer": "Baykal",
                "options": ["Baykal", "Kaspiy", "Viktoriya", "Aydarko‘l"]
            },
            {
                "question": "O‘zbekiston milliy valyutasi qachon muomalaga kiritilgan?",
                "answer": "1994-yil",
                "options": ["1991-yil", "1992-yil", "1994-yil", "1996-yil"]
            },
            {
                "question": "Samolyot uchuvchi joyi nima deb ataladi?",
                "answer": "Kabina",
                "options": ["Kabina", "Salon", "Bagaj joyi", "Kokpit"]
            },
            {
                "question": "O‘zbekiston hududidagi eng katta cho‘l?",
                "answer": "Qizilqum",
                "options": ["Qizilqum", "Karakum", "Gobi", "Sahroi Kabir"]
            },
            {
                "question": "Dunyoda eng ko‘p gaplashiladigan til?",
                "answer": "Xitoy tili",
                "options": ["Ingliz tili", "Rus tili", "Xitoy tili", "Ispan tili"]
            },
            {
                "question": "O‘zbekistonda mashhur nonushta taomi?",
                "answer": "Somsa",
                "options": ["Somsa", "Pizza", "Burger", "Norin"]
            },
            {
                "question": "Dunyodagi eng uzun daryo?",
                "answer": "Nil",
                "options": ["Nil", "Amazonka", "Volga", "Ganga"]
            },
            {
                "question": "Dunyodagi eng mashhur muzlik qaysi qit’ada joylashgan?",
                "answer": "Antarktida",
                "options": ["Antarktida", "Osiyo", "Shimoliy Amerika", "Afrika"]
            },
            {
                "question": "O‘zbekiston davlat madhiyasi qachon qabul qilingan?",
                "answer": "1992-yil",
                "options": ["1991-yil", "1992-yil", "1993-yil", "1994-yil"]
            },
            {
                "question": "Qaysi sport turida sariq to‘p ishlatiladi?",
                "answer": "Tennis",
                "options": ["Tennis", "Futbol", "Basketbol", "Bilyard"]
            },
            {
                "question": "O‘zbekistonning eng katta tog‘ tizmalari?",
                "answer": "Tyan-Shan",
                "options": ["Tyan-Shan", "Pamir", "Altay", "Kavkaz"]
            },
            {
                "question": "Dunyodagi eng mashhur devor?",
                "answer": "Xitoy devori",
                "options": ["Xitoy devori", "Berlin devori", "Hadrian devori", "Bobil devori"]
            },
            {
                "question": "O‘zbekistonda qadimiy qal’alar ko‘p bo‘lgan hudud?",
                "answer": "Ellikqal’a",
                "options": ["Ellikqal’a", "Farg‘ona", "Samarqand", "Andijon"]
            },
            {
                "question": "Dunyodagi eng katta kitobxona qayerda joylashgan?",
                "answer": "AQSh",
                "options": ["Rossiya", "Angliya", "AQSh", "Fransiya"]
            },
            {
                "question": "O‘zbekistonda qaysi viloyat 'mevasi' bilan mashhur?",
                "answer": "Farg‘ona",
                "options": ["Farg‘ona", "Navoiy", "Jizzax", "Xorazm"]
            },
            {
                "question": "Dunyoning eng baland tog‘i?",
                "answer": "Everest",
                "options": ["Everest", "Elbrus", "Kilimanjaro", "Montblan"]
            },
            {
                "question": "O‘zbekistonning eng mashhur xalq ertak qahramonlaridan biri?",
                "answer": "Afandi",
                "options": ["Afandi", "Alpomish", "Rustam", "Qorako‘z"]
            },
            {
                "question": "Dunyodagi eng yirik davlat maydon bo‘yicha?",
                "answer": "Rossiya",
                "options": ["Rossiya", "Xitoy", "AQSh", "Kanada"]
            },
            {
                "question": "O‘zbekistonning eng baland cho‘qqisi?",
                "answer": "Hazrati Sulton",
                "options": ["Hazrati Sulton", "Chimyon", "Somoni cho‘qqisi", "Bobotog‘"]
            },
            {
                "question": "Dunyodagi eng mashhur minoralardan biri — Pisa minorasi qayerda?",
                "answer": "Italiya",
                "options": ["Italiya", "Ispaniya", "Gretsiya", "Fransiya"]
            },
            {
                "question": "O‘zbekistonning milliy ichimliklaridan biri?",
                "answer": "Choy",
                "options": ["Sharbat", "Choy", "Qahva", "Sut"]
            },
            {
                "question": "Dunyodagi eng tez yuguradigan hayvon?",
                "answer": "Gepard",
                "options": ["Gepard", "Ot", "Arslon", "Tulki"]
            },
            {
                "question": "O‘zbekistonning eng mashhur shaharlaridan biri — Xiva qayerda joylashgan?",
                "answer": "Xorazm",
                "options": ["Buxoro", "Xorazm", "Samarqand", "Qashqadaryo"]
            },
            {
                "question": "Dunyoning eng katta okeani?",
                "answer": "Tinch okeani",
                "options": ["Tinch okeani", "Atlantika", "Hind okeani", "Shimoliy muz okeani"]
            },
            {
                "question": "O‘zbekiston milliy kiyimlaridan biri?",
                "answer": "Chopon",
                "options": ["Chopon", "Futbolka", "Palto", "Jinsi"]
            },
            {
                "question": "Dunyodagi eng ko‘p ishlatiladigan transport vositasi?",
                "answer": "Avtomobil",
                "options": ["Avtomobil", "Samolyot", "Kema", "Velosiped"]
            },
            {
                "question": "O‘zbekistonning mashhur shoirlaridan biri?",
                "answer": "Erkin Vohidov",
                "options": ["Erkin Vohidov", "Pushkin", "Gyote", "Navoiy"]
            },
            {
                "question": "O‘zbekistonning eng yirik suv ombori?",
                "answer": "Chorvoq",
                "options": ["Chorvoq", "Tuyamo‘yin", "Qoratepa", "Andijon"]
            },
            {
                "question": "Dunyodagi eng mashhur hayvonlardan biri — Panda qaysi davlatda yashaydi?",
                "answer": "Xitoy",
                "options": ["Hindiston", "Xitoy", "Nepal", "Mongoliya"]
            },
            {
                "question": "O‘zbekistonda mashhur hunarmandchilik markazi bo‘lgan shahar?",
                "answer": "Rishton",
                "options": ["Shahrisabz", "Rishton", "Qo‘qon", "Buxoro"]
            },
            {
                "question": "Dunyodagi eng baland daraxtlar qaysi turga mansub?",
                "answer": "Sekvoyalar",
                "options": ["Sekvoyalar", "Yong‘oq", "Qayrag‘och", "Tol"]
            },
            {
                "question": "O‘zbekistonning janubiy qo‘shni davlati?",
                "answer": "Afg‘oniston",
                "options": ["Tojikiston", "Afg‘oniston", "Turkmaniston", "Eron"]
            },
            {
                "question": "Dunyodagi eng mashhur hayvon — Mickey Mouse qaysi kompaniya qahramoni?",
                "answer": "Disney",
                "options": ["Marvel", "Disney", "Pixar", "DreamWorks"]
            },
            {
                "question": "O‘zbekistonda mashhur bozor — Chorsu qayerda joylashgan?",
                "answer": "Toshkent",
                "options": ["Toshkent", "Andijon", "Samarqand", "Xiva"]
            },
            {
                "question": "Dunyodagi eng mashhur sport musobaqasi?",
                "answer": "Olimpiada",
                "options": ["Olimpiada", "Futbol jahon chempionati", "Regbi kubogi", "Tennis US Open"]
            },
            {
                "question": "O‘zbekistonning eng mashhur qadimiy obidalaridan biri — Ark qayerda?",
                "answer": "Buxoro",
                "options": ["Xiva", "Buxoro", "Samarqand", "Termiz"]
            },
            {
                "question": "Dunyodagi eng mashhur avtomobil kompaniyalaridan biri?",
                "answer": "Toyota",
                "options": ["Toyota", "Mercedes", "Tesla", "BMW"]
            },
            {
                "question": "O‘zbekistonda mashhur milliy shirinliklardan biri?",
                "answer": "Halva",
                "options": ["Halva", "Shokolad", "Tort", "Keks"]
            },
            {
                "question": "Dunyodagi eng mashhur sportchilaridan biri — Lionel Messi qaysi sport turida mashhur?",
                "answer": "Futbol",
                "options": ["Futbol", "Basketbol", "Boks", "Tennis"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Amir Temur qaysi shaharda tug‘ilgan?",
                "answer": "Shahrisabz",
                "options": ["Shahrisabz", "Samarqand", "Buxoro", "Xiva"]
            },
            {
                "question": "Dunyodagi eng mashhur ichimliklardan biri?",
                "answer": "Choy",
                "options": ["Choy", "Qahva", "Sharbat", "Sut"]
            },
            {
                "question": "O‘zbekistonning mashhur olimlaridan biri?",
                "answer": "Al-Farg‘oniy",
                "options": ["Al-Farg‘oniy", "Beruniy", "Ibn Sino", "Xorazmiy"]
            },
            {
                "question": "Dunyodagi eng mashhur qasrlardan biri — Versal qayerda?",
                "answer": "Fransiya",
                "options": ["Fransiya", "Germaniya", "Italiya", "Ispaniya"]
            },
            {
                "question": "O‘zbekistonda mashhur milliy liboslardan biri?",
                "answer": "Atlas",
                "options": ["Atlas", "Kimono", "Kurtka", "Palto"]
            },
            {
                "question": "Dunyodagi eng mashhur fastfud taomi?",
                "answer": "Burger",
                "options": ["Burger", "Somsa", "Pizza", "Hot-dog"]
            },
            {
                "question": "O‘zbekistonda mashhur ko‘llardan biri?",
                "answer": "Aydarko‘l",
                "options": ["Aydarko‘l", "Qorako‘l", "Sarezko‘l", "Tuzko‘l"]
            },
            {
                "question": "Dunyodagi eng mashhur telefon markalaridan biri?",
                "answer": "Apple",
                "options": ["Apple", "Samsung", "Nokia", "Huawei"]
            },
            {
                "question": "O‘zbekiston hududida qadimiy qal’alardan biri — Topraqqal’a qayerda?",
                "answer": "Qoraqalpog‘iston",
                "options": ["Qoraqalpog‘iston", "Buxoro", "Samarqand", "Surxondaryo"]
            },
            {
                "question": "Dunyodagi eng mashhur futbol klublaridan biri?",
                "answer": "Real Madrid",
                "options": ["Real Madrid", "Barcelona", "Milan", "Manchester United"]
            },
            {
                "question": "O‘zbekistonning mashhur milliy ashulachisi?",
                "answer": "Yulduz Usmonova",
                "options": ["Yulduz Usmonova", "Sevara Nazarkhan", "Ozodbek Nazarbekov", "Botir Zokirov"]
            },
            {
                "question": "Dunyodagi eng mashhur tog‘?",
                "answer": "Everest",
                "options": ["Kilimanjaro", "Everest", "Elbrus", "Montblan"]
            },
            {
                "question": "O‘zbekistonning mashhur milliy taomlaridan biri?",
                "answer": "Norin",
                "options": ["Norin", "Palov", "Somsa", "Lag‘mon"]
            },
            {
                "question": "Dunyodagi eng mashhur kinoteatrlardan biri — Hollywood qayerda?",
                "answer": "AQSh",
                "options": ["AQSh", "Angliya", "Fransiya", "Italiya"]
            },
            {
                "question": "O‘zbekistonda mashhur milliy o‘yinlardan biri?",
                "answer": "Ko‘pkari",
                "options": ["Ko‘pkari", "Shaxmat", "Basketbol", "futbol"]
            },
            {
                "question": "Dunyodagi eng mashhur ko‘rfaz?",
                "answer": "Bengal",
                "options": ["Meksika", "Bengal", "Pers", "Aden"]
            },
            {
                "question": "O‘zbekistonning mashhur shaharlaridan biri — Qo‘qon qaysi viloyatda?",
                "answer": "Farg‘ona",
                "options": ["Farg‘ona", "Andijon", "Namangan", "Toshkent"]
            },
            {
                "question": "Dunyodagi eng mashhur qasrlardan biri — Kreml qayerda?",
                "answer": "Moskva",
                "options": ["Berlin", "Moskva", "Parij", "Pekin"]
            },
            {
                "question": "O‘zbekistonning mashhur milliy cholg‘u asbobi?",
                "answer": "G‘ijjak",
                "options": ["G‘ijjak", "Skripka", "Pianino", "Gitara"]
            },
            {
                "question": "Dunyodagi eng mashhur muzliklardan biri?",
                "answer": "Grenlandiya",
                "options": ["Grenlandiya", "Antarktida", "Alp", "And"]
            },
            {
                "question": "Dunyodagi eng mashhur teatrlaridan biri — Bolshoy teatri qayerda?",
                "answer": "Moskva",
                "options": ["Moskva", "London", "Parij", "Berlin"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri?",
                "answer": "Abdulla Qahhor",
                "options": ["Abdulla Qahhor", "Cho‘lpon", "Oybek", "Pirimqul Qodirov"]
            },
            {
                "question": "Dunyodagi eng mashhur muzeylardan biri — Luvr qayerda?",
                "answer": "Parij",
                "options": ["London", "Parij", "Berlin", "Madrid"]
            },
            {
                "question": "O‘zbekistonning mashhur qo‘shiqchilaridan biri?",
                "answer": "Ozodbek Nazarbekov",
                "options": ["Ozodbek Nazarbekov", "Yulduz Usmonova", "Botir Zokirov", "Munojot Yo‘lchiyeva"]
            },
            {
                "question": "Dunyodagi eng mashhur poyga musobaqasi?",
                "answer": "Formula 1",
                "options": ["Formula 1", "Moto GP", "Rally Dakar", "IndyCar"]
            },
            {
                "question": "O‘zbekistonning mashhur milliy kiyimlaridan biri?",
                "answer": "Do‘ppi",
                "options": ["Do‘ppi", "Kimono", "Sharf", "Jinsi"]
            },
            {
                "question": "Dunyodagi eng mashhur stadionlardan biri — Kamp Nou qayerda?",
                "answer": "Barselona",
                "options": ["Barselona", "Madrid", "London", "Rim"]
            },
            {
                "question": "O‘zbekistonning mashhur milliy raqslaridan biri?",
                "answer": "Tanovar",
                "options": ["Tanovar", "Vals", "Sirtaki", "Rumba"]
            },
            {
                "question": "Dunyodagi eng mashhur futbolchilaridan biri — Cristiano Ronaldo qaysi davlatdan?",
                "answer": "Portugaliya",
                "options": ["Portugaliya", "Ispaniya", "Braziliya", "Italiya"]
            },
            {
                "question": "Dunyodagi eng mashhur minoralardan biri — CN Tower qayerda?",
                "answer": "Kanada",
                "options": ["AQSh", "Kanada", "Fransiya", "Angliya"]
            },
            {
                "question": "Qarshi shahar qaysi viloyat markazi?",
                "answer": "Qashqadaryo",
                "options": ["Qashqadaryo", "Buxoro", "Jizzax", "Namangan"]
            },
            {
                "question": "Dunyodagi eng mashhur muzlatilgan qahva nomi?",
                "answer": "Frappe",
                "options": ["Frappe", "Latte", "Amerikano", "Espresso"]
            },
            {
                "question": "O‘zbekistonning shimoliy viloyatlaridan biri?",
                "answer": "Qoraqalpog‘iston",
                "options": ["Qoraqalpog‘iston", "Samarqand", "Buxoro", "Andijon"]
            },
            {
                "question": "Dunyodagi eng mashhur telefon ixtirochisi kim?",
                "answer": "Aleksandr Bell",
                "options": ["Nikola Tesla", "Tomas Edison", "Aleksandr Bell", "Nyuton"]
            },
            {
                "question": "O‘zbekiston milliy sport turi?",
                "answer": "Kurash",
                "options": ["Kurash", "Futbol", "Basketbol", "Shaxmat"]
            },
            {
                "question": "Dunyodagi eng mashhur minoralardan biri — Eiffel minorasi qaysi shaharda?",
                "answer": "Parij",
                "options": ["London", "Berlin", "Parij", "Rim"]
            },
            {
                "question": "O‘zbekiston milliy libosida bosh kiyim qanday ataladi?",
                "answer": "Do‘ppi",
                "options": ["Sharf", "Do‘ppi", "Kalpak", "Shlyapa"]
            },
            {
                "question": "Dunyoning eng mashhur futbol musobaqasi?",
                "answer": "Jahon chempionati",
                "options": ["Jahon chempionati", "Olimpiada", "Yevropa Ligasi", "Osiyo Kubogi"]
            },
            {
                "question": "O‘zbekiston hududidagi eng mashhur suv omborlaridan biri — Chorvoq qaysi viloyatda joylashgan?",
                "answer": "Toshkent viloyati",
                "options": ["Toshkent viloyati", "Namangan viloyati", "Andijon viloyati", "Samarqand viloyati"]
            },
            {
                "question": "Dunyoning eng katta yarim oroli?",
                "answer": "Arabiston yarim oroli",
                "options": ["Arabiston yarim oroli", "Iberiya", "Skandinaviya", "Hindiston yarim oroli"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan qadimiy madrasalardan biri — Ko‘kaldosh qayerda joylashgan?",
                "answer": "Toshkent",
                "options": ["Toshkent", "Buxoro", "Xiva", "Samarqand"]
            },
            {
                "question": "Dunyoning eng uzun qirg‘oq chizig‘iga ega davlat?",
                "answer": "Kanada",
                "options": ["Kanada", "Rossiya", "Avstraliya", "AQSh"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaharlaridan biri — Shahrisabz qaysi vohada joylashgan?",
                "answer": "Qashqadaryo vohasi",
                "options": ["Qashqadaryo vohasi", "Surxondaryo vohasi", "Zarafshon vohasi", "Farg‘ona vohasi"]
            },
            {
                "question": "Dunyoning eng katta muzliklari qaysi hududda joylashgan?",
                "answer": "Antarktida",
                "options": ["Antarktida", "Grenlandiya", "Shimoliy qutb", "Islandiya"]
            },
            {
                "question": "Buyuk astronom Galiley qanday ixtirosi bilan mashhur?",
                "answer": "Teleskopni takomillashtirish",
                "options": ["Teleskopni takomillashtirish", "Kompasni ixtiro qilish", "Bug‘ mashinasi", "Telefon"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Pirimqul Qodirov mashhur asari?",
                "answer": "Avlodlar dovoni",
                "options": ["Avlodlar dovoni", "Yulduzli tunlar", "Sarob", "O‘tkan kunlar"]
            }
        ]

        quiz_4 = [
            # Diniy savollar 50ta
            {
                "question": "Payg‘ambarimiz (s.a.v.)ning otlaridan biri 'Qasvo' qaysi voqeada ishlatilgan?",
                "answer": "Hijratda",
                "options": ["Hijratda", "Badr jangida", "Uhud jangida", "Vido hajida"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ning onalari Omina qaysi joyda vafot etgan?",
                "answer": "Abvo",
                "options": ["Abvo", "Makka", "Madina", "Toyĭf"]
            },
            {
                "question": "Qur’onda zikr qilingan eng uzun oyat qaysi?",
                "answer": "Baqara surasi 282-oyat",
                "options": ["Baqara surasi 282-oyat", "Maaida surasi 5-oyat", "Tavba surasi 100-oyat", "Niso surasi 12-oyat"]
            },
            {
                "question": "Payg‘ambarimizning sevikli qizlari kim edi?",
                "answer": "Fotima (r.a.)",
                "options": ["Ruqayya", "Zaynab", "Ummu Kulsum", "Fotima (r.a.)"]
            },
            {
                "question": "Payg‘ambarimiz Muhammad (s.a.v.)ning otalari ismlari nima edi?",
                "answer": "Abdulloh",
                "options": ["Abu Talib", "Abdulmuttalib", "Abdulloh", "Hamza"]
            },
            {
                "question": "Onalari ismlari nima edi?",
                "answer": "Omina",
                "options": ["Omina", "Oyshe", "Xadicha", "Aminah"]
            },
            {
                "question": "Payg‘ambarimizga birinchi iymon keltirgan ayol kim?",
                "answer": "Xadicha",
                "options": ["Omina", "Xadicha", "Ayshe", "Fotima"]
            },
            {
                "question": "Payg‘ambarimizga birinchi iymon keltirgan erkak kim?",
                "answer": "Abu Bakr",
                "options": ["Umar", "Usmon", "Ali", "Abu Bakr"]
            },
            {
                "question": "Payg‘ambarimizga birinchi iymon keltirgan bola kim?",
                "answer": "Ali ibn Abu Tolib",
                "options": ["Hasan", "Husayn", "Ali ibn Abu Tolib", "Zayd"]
            },
            {
                "question": "Qur’onda nechta juz mavjud?",
                "answer": "30",
                "options": ["7", "60", "114", "30"]
            },
            {
                "question": "Qur’onda nechta oyat bor?",
                "answer": "6236",
                "options": ["7000", "6200", "6236", "6000"]
            },
            {
                "question": "Qur’onda nechta payg‘ambar nomi zikr qilingan?",
                "answer": "25",
                "options": ["15", "20", "25", "30"]
            },
            {
                "question": "Islomda birinchi farz qilingan ibodat nima?",
                "answer": "Namoz",
                "options": ["Ro‘za", "Haj", "Namoz", "Zakot"]
            },
            {
                "question": "Qur’on nozil bo‘la boshlagan kecha qanday ataladi?",
                "answer": "Qadr kechasi",
                "options": ["Qadr kechasi", "Baraat kechasi", "Miraj kechasi", "Ramazon kechasi"]
            },
            {
                "question": "Islomda eng muqaddas oy qaysi?",
                "answer": "Ramazon",
                "options": ["Muharram", "Ramazon", "Sha’bon", "Zulhijja"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ning hijratlari qaysi shaharga bo‘lgan?",
                "answer": "Madina",
                "options": ["Quddus", "Madina", "Toyĭf", "Damashq"]
            },
            {
                "question": "Islomda g‘usl nima?",
                "answer": "Butun tanani suv bilan yuvish",
                "options": ["Faqat qo‘lni yuvish", "Faqat yuzni yuvish", "Butun tanani suv bilan yuvish", "Faqat oyoqni yuvish"]
            },
            {
                "question": "Qur’onni kim jamlagan va bir mushaf shakliga keltirgan?",
                "answer": "Usmon ibn Affon",
                "options": ["Umar ibn Xattob", "Abu Bakr", "Usmon ibn Affon", "Ali ibn Abu Tolib"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ga eng ko‘p hadis rivoyat qilgan sahoba kim?",
                "answer": "Abu Hurayra",
                "options": ["Abu Bakr", "Abu Hurayra", "Umar", "Anas ibn Molik"]
            },
            {
                "question": "Islomda “sadaqa” nima?",
                "answer": "Ko‘ngilli yordam va ehson",
                "options": ["Mol-dunyodan farz zakot", "Ko‘ngilli yordam va ehson", "Ro‘za", "Namoz"]
            },
            {
                "question": "Namozda birinchi o‘qiladigan sura qaysi?",
                "answer": "Fotiha surasi",
                "options": ["Fotiha surasi", "Ikhlos surasi", "Baqara surasi", "Yosin surasi"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.) nechta farzandlari bo‘lgan?",
                "answer": "7",
                "options": ["5", "6", "7", "9"]
            },
            {
                "question": "Islomda birinchi mo‘jiza qaysi?",
                "answer": "Qur’on",
                "options": ["Mi’roj", "Qur’on", "Suvdan chiqish", "Olovdan najot"]
            },
            {
                "question": "Musulmonlar oy taqvimidan foydalanadi. U qaysi taqvim?",
                "answer": "Hijriy taqvim",
                "options": ["Hijriy taqvim", "Milodiy taqvim", "Yulian taqvim", "Qadimiy rim taqvimi"]
            },
            {
                "question": "“Zam-zam” suvi qayerda joylashgan?",
                "answer": "Makka",
                "options": ["Madina", "Quddus", "Makka", "Damashq"]
            },
            {
                "question": "Haj ibodatida Safa va Marva oralig‘ida qilinadigan amaliyot nima?",
                "answer": "Sa’y",
                "options": ["Sa’y", "Tavof", "Tahallul", "Wuquf"]
            },
            {
                "question": "Payg‘ambarimizning oxirgi hajlari qanday nom olgan?",
                "answer": "Xutbatul vido’ (Vido haj)",
                "options": ["Ummrah", "Xutbatul vido’ (Vido haj)", "Hijrat haji", "Birinchi haj"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.) qabr joylari qayerda?",
                "answer": "Madina",
                "options": ["Makka", "Madina", "Quddus", "Badr"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.) qaysi yil tug‘ilgan?",
                "answer": "Fil yili",
                "options": ["Fil yili", "Hijrat yili", "Badr yili", "Uhud yili"]
            },
            {
                "question": "Qur’on oyatlari qaysi farishta tomonidan keltirilgan?",
                "answer": "Jabroil (a.s.)",
                "options": ["Mikoil", "Isrofil", "Jabroil (a.s.)", "Azroil"]
            },
            {
                "question": "Musulmonlarning ikkinchi eng muqaddas shahri?",
                "answer": "Madina",
                "options": ["Madina", "Quddus", "Damashq", "Bag‘dod"]
            },
            {
                "question": "Namozda o‘tirib salom berishdan oldingi duo nima deb ataladi?",
                "answer": "Tashahhud",
                "options": ["Tashahhud", "Taslim", "Takbir", "Qiroat"]
            },
            {
                "question": "Qur’onda qaysi payg‘ambar ko‘proq zikr qilingan?",
                "answer": "Muso (a.s.)",
                "options": ["Iso (a.s.)", "Ibrohim (a.s.)", "Muso (a.s.)", "Nuh (a.s.)"]
            },
            {
                "question": "Ka’baning ustiga yopiladigan qoplamaning nomi?",
                "answer": "Kisva",
                "options": ["Kisva", "Hirm", "Libos", "Paranda"]
            },
            {
                "question": "“Baqara” so‘zi qanday ma’noni anglatadi?",
                "answer": "Sigir",
                "options": ["Kitob", "Sigir", "Odam", "Qo‘y"]
            },
            {
                "question": "Qur’ondagi oxirgi nozil bo‘lgan oyat qaysi suradan?",
                "answer": "Maaida surasi",
                "options": ["Baqara surasi", "Tavba surasi", "Maaida surasi", "Nahl surasi"]
            },
            {
                "question": "Makkada joylashgan qora tosh qanday nomlanadi?",
                "answer": "Hajar ul-Asvad",
                "options": ["Safa", "Marva", "Hajar ul-Asvad", "Maqom Ibrohim"]
            },
            {
                "question": "Musulmonlarning birinchi qiblasi qayer edi?",
                "answer": "Quddusdagi Masjidul-Aqso",
                "options": ["Makka", "Madina", "Quddusdagi Masjidul-Aqso", "Bag‘dod"]
            },
            {
                "question": "Payg‘ambarimizning eng yaqin do‘stlari qanday ataladi?",
                "answer": "Ashob",
                "options": ["Ashob", "Tobiin", "Tabaa tobiin", "Salaf"]
            },
            {
                "question": "Payg‘ambarimizning sevikli nabiralari kimlar?",
                "answer": "Hasan va Husayn",
                "options": ["Ali va Hasan", "Hasan va Husayn", "Umar va Usmon", "Abu Bakr va Ali"]
            },
            {
                "question": "Payg‘ambarimizning eng yaqin yordamchilari nechta xalifa bo‘lgan?",
                "answer": "4",
                "options": ["2", "3", "4", "5"]
            },
            {
                "question": "Payg‘ambarimizning birinchi vahiydan keyin kim tasalli bergan?",
                "answer": "Xadicha",
                "options": ["Omina", "Xadicha", "Ali", "Abu Bakr"]
            },
            {
                "question": "Miraj kechasida Payg‘ambarimizga qaysi ibodat farz qilindi?",
                "answer": "Namoz",
                "options": ["Ro‘za", "Zakot", "Namoz", "Haj"]
            },
            {
                "question": "Ka’bani birinchi bo‘lib kim qurgan?",
                "answer": "Ibrohim (a.s.) va Ismoil (a.s.)",
                "options": ["Muso (a.s.)", "Ibrohim (a.s.) va Ismoil (a.s.)", "Nuh (a.s.)", "Iso (a.s.)"]
            },
            {
                "question": "Payg‘ambarimizning otalarining bobolari kim edi?",
                "answer": "Abdulmuttalib",
                "options": ["Abu Talib", "Abdulmuttalib", "Hamza", "Abbos"]
            },
            {
                "question": "Islom tarixida birinchi shahid kim edi?",
                "answer": "Somayya",
                "options": ["Xadicha", "Somayya", "Bilol", "Yasir"]
            },
            {
                "question": "Payg‘ambarimizning hijratdan oldin ko‘chib o‘tgan joyi?",
                "answer": "Toyĭf",
                "options": ["Quddus", "Toyĭf", "Badr", "Uhud"]
            },
            {
                "question": "Payg‘ambarimizning birinchi vahiydan keyin Makkadan tashqarida da’vat qilgan shahri?",
                "answer": "Toyĭf",
                "options": ["Quddus", "Toyĭf", "Madina", "Hunayn"]
            },
            {
                "question": "Payg‘ambarimizning eng yaqin amakilari kim edi?",
                "answer": "Abu Tolib",
                "options": ["Abu Tolib", "Hamza", "Abbos", "Abu Lahab"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ning hijratlarida yo‘lboshchilari kim bo‘lgan?",
                "answer": "Abu Bakr",
                "options": ["Ali", "Umar", "Abu Bakr", "Usmon"]
            },
            # Fanga oid savollar 100ta
            {
                "question": "O‘zbekiston hududidagi mashhur maqbaralardan biri — Ismoil Somoniy maqbarasi qayerda?",
                "answer": "Buxoro",
                "options": ["Buxoro", "Samarqand", "Xiva", "Andijon"]
            },
            {
                "question": "Buyuk yozuvchi Abdulla Qodiriy mashhur asarlaridan biri?",
                "answer": "O‘tkan kunlar",
                "options": ["O‘tkan kunlar", "Mehrobdan chayon", "Sarob", "Yulduzli tunlar"]
            },
            {
                "question": "Yevropadagi eng mashhur futbol klublaridan biri — Real Madrid qaysi davlatda?",
                "answer": "Ispaniya",
                "options": ["Ispaniya", "Italiya", "Fransiya", "Angliya"]
            },
            {
                "question": "O‘zbekiston hududidagi eng katta ko‘l?",
                "answer": "Aral dengizi",
                "options": ["Aral dengizi", "Aydarko‘l", "Sarezko‘l", "Tuzko‘l"]
            },
            {
                "question": "Dunyoning eng baland hayvonlaridan biri?",
                "answer": "Jirafa",
                "options": ["Jirafa", "Fil", "Gepard", "Arslon"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Jaloliddin Manguberdi qaysi asrda yashagan?",
                "answer": "XIII asr",
                "options": ["XIII asr", "XI asr", "XIV asr", "XV asr"]
            },
            {
                "question": "Dunyoning eng katta arxipelaglari qayerda joylashgan?",
                "answer": "Janubi-Sharqiy Osiyo",
                "options": ["Janubi-Sharqiy Osiyo", "Shimoliy Amerika", "Afrika", "Yevropa"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan mashhur yodgorlik — Guri Amir maqbarasi kimga bag‘ishlangan?",
                "answer": "Amir Temur",
                "options": ["Amir Temur", "Ulug‘bek", "Alisher Navoiy", "Ibn Sino"]
            },
            {
                "question": "Dunyodagi eng chuqur okean?",
                "answer": "Tinch okeani",
                "options": ["Tinch okeani", "Atlantika okeani", "Hind okeani", "Shimoliy muz okeani"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Abdulla Qodiriy qaysi davr adibi?",
                "answer": "XX asr boshlarida",
                "options": ["XX asr boshlarida", "XV asrda", "XVIII asrda", "XIX asrda"]
            },
            {
                "question": "Eng qadimgi yozuvlardan biri — mixxat qayerda paydo bo‘lgan?",
                "answer": "Shumer",
                "options": ["Shumer", "Misr", "Xitoy", "Hindiston"]
            },
            {
                "question": "O‘zbekistonning milliy o‘yinlaridan biri?",
                "answer": "Ko‘pkari",
                "options": ["Ko‘pkari", "Futbol", "Shaxmat", "Basketbol"]
            },
            {
                "question": "Dunyoning eng mashhur san’at muzeylaridan biri — Prado qayerda joylashgan?",
                "answer": "Madrid",
                "options": ["Madrid", "Parij", "Berlin", "Rim"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur tarixiy obidalaridan biri — Minorai Jam qayerda joylashgan?",
                "answer": "Afg‘oniston bilan chegarada",
                "options": ["Afg‘oniston bilan chegarada", "Buxoro", "Samarqand", "Xorazm"]
            },
            {
                "question": "Dunyoning eng baland tog‘ dovonlaridan biri?",
                "answer": "Torong-La",
                "options": ["Torong-La", "Elbrus", "Altay", "Ural"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Alisher Navoiy qaysi asrda yashagan?",
                "answer": "XV asr",
                "options": ["XV asr", "XVI asr", "XIV asr", "XIII asr"]
            },
            {
                "question": "Dunyoning eng katta ichki daryosiz hududi qayerda joylashgan?",
                "answer": "Mongoliya",
                "options": ["Mongoliya", "Liviya", "Avstraliya", "Kanada"]
            },
            {
                "question": "Quyoshdan eng uzoq joylashgan sayyora qaysi?",
                "answer": "Neptun",
                "options": ["Yupiter", "Uran", "Neptun", "Saturn"]
            },
            {
                "question": "Buyuk Britaniyaning rasmiy valyutasi?",
                "answer": "Funt sterling",
                "options": ["Funt sterling", "Yevro", "Dollar", "Frank"]
            },
            {
                "question": "O‘zbekistonda eng yirik gaz koni?",
                "answer": "Sho‘rtan",
                "options": ["Sho‘rtan", "Muborak", "Qandim", "Gazli"]
            },
            {
                "question": "AQShning eng katta shtati maydon jihatdan?",
                "answer": "Alyaska",
                "options": ["Texas", "Kaliforniya", "Alyaska", "Nevada"]
            },
            {
                "question": "Yerning qaysi qatlamida magma mavjud?",
                "answer": "Mantiya",
                "options": ["Mantiya", "Qobiq", "Yadro", "Atmosfera"]
            },
            {
                "question": "Qaysi davlatni 'Tuliplar mamlakati' deb atashadi?",
                "answer": "Niderlandiya",
                "options": ["Belgiya", "Niderlandiya", "Daniya", "Avstriya"]
            },
            {
                "question": "O‘zbekiston Konstitutsiyasi nechta bobdan iborat?",
                "answer": "6",
                "options": ["6", "7", "5", "8"]
            },
            {
                "question": "O‘zbekistonda eng yirik issiqlik elektr stansiyasi?",
                "answer": "Talimarjon IES",
                "options": ["Talimarjon IES", "Sirdaryo IES", "Novoangren IES", "Navoiy IES"]
            },
            {
                "question": "Qaysi olim 'harakatning uchinchi qonuni'ni kashf qilgan?",
                "answer": "Nyuton",
                "options": ["Nyuton", "Galiley", "Arximed", "Paskal"]
            },
            {
                "question": "O‘zbekistonda eng yirik toshko‘mir koni?",
                "answer": "Sharg‘un",
                "options": ["Sharg‘un", "Angren", "Boysun", "Baysun"]
            },
            {
                "question": "Dunyoning eng chuqur okean joyi?",
                "answer": "Mariana chuqurligi",
                "options": ["Mariana chuqurligi", "Filippin chuqurligi", "Tonga chuqurligi", "Puerto-Riko chuqurligi"]
            },
            {
                "question": "Yer yuzida eng ko‘p maydonni egallagan davlat?",
                "answer": "Rossiya",
                "options": ["Kanada", "AQSh", "Rossiya", "Xitoy"]
            },
            {
                "question": "O‘zbekistondagi eng uzun kanal?",
                "answer": "Amu-Buxoro",
                "options": ["Amu-Buxoro", "Amu-Qorako‘l", "Amu-Zang", "Qizilqum kanali"]
            },
            {
                "question": "Qaysi yulduz 'qutb yulduzi' deb ataladi?",
                "answer": "Polaris",
                "options": ["Sirius", "Polaris", "Vega", "Antares"]
            },
            {
                "question": "Qaysi metall 'eng yengil metall' hisoblanadi?",
                "answer": "Litiy",
                "options": ["Litiy", "Natriy", "Alyuminiy", "Berilliy"]
            },
            {
                "question": "O‘zbekistonda eng ko‘p koni mavjud bo‘lgan foydali qazilma?",
                "answer": "Oltin",
                "options": ["Oltin", "Gaz", "Ko‘mir", "Mis"]
            },
            {
                "question": "Qadimgi Bobil minorasi qayerda joylashgan edi?",
                "answer": "Mesopotamiya",
                "options": ["Misr", "Mesopotamiya", "Gretsiya", "Hindiston"]
            },
            {
                "question": "Yer yuzida eng katta yarim orol?",
                "answer": "Arabiston",
                "options": ["Arabiston", "Skandinaviya", "Iberiya", "Hindiston"]
            },
            {
                "question": "Qaysi davlatning poytaxti Ottava?",
                "answer": "Kanada",
                "options": ["Kanada", "Avstraliya", "AQSh", "Meksika"]
            },
            {
                "question": "O‘zbekiston mustaqillik ramzi sifatida nechta yulduz bayroqda tasvirlangan?",
                "answer": "12",
                "options": ["12", "14", "10", "16"]
            },
            {
                "question": "Buyuk geografik kashfiyotlar davrida Hindistonga dengiz yo‘lini kim topgan?",
                "answer": "Vasko da Gama",
                "options": ["Magellan", "Kolumb", "Vasko da Gama", "Diaz"]
            },
            {
                "question": "Quyosh tizimidagi eng issiq sayyora?",
                "answer": "Venera",
                "options": ["Venera", "Mars", "Yupiter", "Merkuriy"]
            },
            {
                "question": "O‘zbekistonda eng katta daryo havzasi?",
                "answer": "Amudaryo",
                "options": ["Sirdaryo", "Amudaryo", "Zarafshon", "Chirchiq"]
            },
            {
                "question": "AQShning birinchi Prezidenti kim?",
                "answer": "Jorj Vashington",
                "options": ["Jorj Vashington", "Avraam Linkoln", "Tomas Jefferson", "Jeyms Madison"]
            },
            {
                "question": "Yerning eng yaqin yulduz qo‘shnisi?",
                "answer": "Proksima Kentavra",
                "options": ["Sirius", "Proksima Kentavra", "Vega", "Betelgeyze"]
            },
            {
                "question": "Qaysi yozuvchi 'Urush va tinchlik' romanini yozgan?",
                "answer": "Lev Tolstoy",
                "options": ["Lev Tolstoy", "Dostoyevskiy", "Pushkin", "Lermontov"]
            },
            {
                "question": "Qaysi dengiz eng sho‘r suvli hisoblanadi?",
                "answer": "O‘lik dengiz",
                "options": ["O‘lik dengiz", "Qora dengiz", "Kaspiy dengizi", "Adriatika dengizi"]
            },
            {
                "question": "Yer yuzida eng katta ko‘rfaz?",
                "answer": "Bengal ko‘rfazi",
                "options": ["Bengal ko‘rfazi", "Meksika ko‘rfazi", "Pers ko‘rfazi", "Aden ko‘rfazi"]
            },
            {
                "question": "O‘zbekiston hududidagi eng qadimiy universitet?",
                "answer": "Mirzo Ulug‘bek madrasasi",
                "options": ["Mirzo Ulug‘bek madrasasi", "Registon madrasasi", "Ko‘kaldosh madrasasi", "Sherdor madrasasi"]
            },
            {
                "question": "Qaysi davlat 'osmon mamlakati' deb ataladi?",
                "answer": "Qirg‘iziston",
                "options": ["Qirg‘iziston", "Mongoliya", "Nepal", "Tibet"]
            },
            {
                "question": "Qaysi hayvon tuxum qo‘yib, sut bilan boqadi?",
                "answer": "Utka (platypus)",
                "options": ["Utka (platypus)", "Kenguru", "Tovuq", "Qush"]
            },
            {
                "question": "Qaysi olim nisbiylik nazariyasini yaratgan?",
                "answer": "Albert Eynshteyn",
                "options": ["Albert Eynshteyn", "Nyuton", "Galiley", "Planck"]
            },
            {
                "question": "O‘zbekiston hududidan o‘tadigan eng yirik tog‘ tizmasi?",
                "answer": "Tyan-Shan",
                "options": ["Tyan-Shan", "Gimolay", "Alp", "And"]
            },
            {
                "question": "Qaysi davlatda eng ko‘p vaqt mintaqalari mavjud?",
                "answer": "Rossiya",
                "options": ["Rossiya", "Kanada", "AQSh", "Avstraliya"]
            },
            {
                "question": "Qaysi davlat poytaxti Anqara?",
                "answer": "Turkiya",
                "options": ["Turkiya", "Eron", "Suriya", "Gretsiya"]
            },
            {
                "question": "Yer sharining eng chuqur ko‘li?",
                "answer": "Baykal",
                "options": ["Baykal", "Tanganika", "Viktoriya", "Aral"]
            },
            {
                "question": "Sharq mutafakkiri Beruniy qaysi sohada mashhur?",
                "answer": "Astronomiya",
                "options": ["Astronomiya", "Matematika", "Tibbiyot", "Adabiyot"]
            },
            {
                "question": "Qaysi davlat 'g‘o‘za mamlakati' deb ataladi?",
                "answer": "O‘zbekiston",
                "options": ["O‘zbekiston", "AQSh", "Hindiston", "Braziliya"]
            },
            {
                "question": "Qaysi yevropa davlatida eng ko‘p orollar bor?",
                "answer": "Shvetsiya",
                "options": ["Shvetsiya", "Norvegiya", "Gretsiya", "Italiya"]
            },
            {
                "question": "Quyoshdan keyin eng yorqin yulduz?",
                "answer": "Sirius",
                "options": ["Sirius", "Vega", "Antares", "Proksima Kentavra"]
            },
            {
                "question": "Buyuk ipak yo‘li Yevropani qaysi qit’a bilan bog‘lagan?",
                "answer": "Osiyo",
                "options": ["Osiyo", "Afrika", "Amerika", "Avstraliya"]
            },
            {
                "question": "Qaysi mamlakatda eng baland bino joylashgan?",
                "answer": "Birlashgan Arab Amirliklari",
                "options": ["Birlashgan Arab Amirliklari", "AQSh", "Xitoy", "Saudiya Arabistoni"]
            },
            {
                "question": "O‘zbekiston qaysi davlat bilan eng uzun chegaraga ega?",
                "answer": "Qozog‘iston",
                "options": ["Qozog‘iston", "Tojikiston", "Qirg‘iziston", "Turkmaniston"]
            },
            {
                "question": "Qaysi olim 'Tabiatshunoslik otasi' deb ataladi?",
                "answer": "Aristotel",
                "options": ["Aristotel", "Platon", "Sokrat", "Pifagor"]
            },
            {
                "question": "Yerning eng issiq joyi qaysi cho‘l?",
                "answer": "Lut cho‘li",
                "options": ["Lut cho‘li", "Sahroi Kabir", "Karakum", "Gobi"]
            },
            {
                "question": "Qaysi davlatning poytaxti Braziliya shahri?",
                "answer": "Braziliya",
                "options": ["Argentina", "Braziliya", "Meksika", "Kolumbiya"]
            },
            {
                "question": "Dunyodagi eng katta arxipelag qaysi?",
                "answer": "Indoneziya",
                "options": ["Filippin", "Indoneziya", "Maldiv", "Shvetsiya"]
            },
            {
                "question": "Markaziy Osiyoda eng katta maydonga ega davlat?",
                "answer": "Qozog‘iston",
                "options": ["Qozog‘iston", "O‘zbekiston", "Turkmaniston", "Tojikiston"]
            },
            {
                "question": "Qaysi olimning qonunlari suyuqliklar mexanikasini tushuntiradi?",
                "answer": "Arximed",
                "options": ["Nyuton", "Arximed", "Pascal", "Ohm"]
            },
            {
                "question": "O‘zbekiston Respublikasi davlat gerbida qaysi tog‘ tasvirlangan?",
                "answer": "Humo tog‘i emas, Hazrati Sulton",
                "options": ["Hazrati Sulton", "Tyan-Shan", "Bobotog‘", "Chimyon"]
            },
            {
                "question": "Shimoliy Afrikadagi eng katta shahar?",
                "answer": "Qohira",
                "options": ["Qohira", "Aljir", "Kasablanka", "Tunis"]
            },
            {
                "question": "Yevropa Ittifoqiga a’zo davlatlar soni?",
                "answer": "27",
                "options": ["25", "27", "30", "28"]
            },
            {
                "question": "O‘zbekistonda eng ko‘p oltin qazib olinadigan joy?",
                "answer": "Muruntov",
                "options": ["Muruntov", "Olmaliq", "Zarafshon", "Qizilqum"]
            },
            {
                "question": "Buyuk geografik kashfiyotlar davrida dunyoni birinchi bo‘lib aylanib chiqqan dengizchi?",
                "answer": "Magellan",
                "options": ["Magellan", "Kolumb", "Vasko da Gama", "Hudson"]
            },
            {
                "question": "Yer kurrasida eng katta tekislik?",
                "answer": "Amazon tekisligi",
                "options": ["Amazon tekisligi", "Sibir tekisligi", "Afrika tekisligi", "O‘zbekiston tekisligi"]
            },
            {
                "question": "Qaysi davlat 'Shamol tegirmonlari mamlakati' deb ataladi?",
                "answer": "Niderlandiya",
                "options": ["Niderlandiya", "Daniya", "Norvegiya", "Belgiya"]
            },
            {
                "question": "Buyuk Ipak yo‘li O‘zbekistonning qaysi viloyati orqali Xitoyga chiqadi?",
                "answer": "Farg‘ona vodiysi",
                "options": ["Farg‘ona vodiysi", "Qashqadaryo", "Xorazm", "Navoiy"]
            },
            {
                "question": "Dunyodagi eng uzun temir yo‘l magistrali?",
                "answer": "Transsibir magistrali",
                "options": ["Transsibir magistrali", "Transamerika", "Transafrika", "Yevropa-Osiyo"]
            },
            {
                "question": "Buyuk rus shoiri Pushkin qaysi asar bilan mashhur?",
                "answer": "Yevgeniy Onegin",
                "options": ["Yevgeniy Onegin", "Urush va tinchlik", "Qizil qalpoqcha", "Otello"]
            },
            {
                "question": "O‘zbekistonning eng yirik metallurgiya kombinati?",
                "answer": "Olmaliq KMK",
                "options": ["Olmaliq KMK", "Navoiy KMK", "Angren KMK", "Talimarjon KMK"]
            },
            {
                "question": "Buyuk fransuz inqilobi qachon boshlangan?",
                "answer": "1789",
                "options": ["1789", "1776", "1812", "1848"]
            },
            {
                "question": "Qaysi davlat 'Kengurular mamlakati' deb ataladi?",
                "answer": "Avstraliya",
                "options": ["Avstraliya", "Yangi Zelandiya", "Janubiy Afrika", "Kanada"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan qadimiy astronomik rasadxonani kim qurgan?",
                "answer": "Mirzo Ulug‘bek",
                "options": ["Mirzo Ulug‘bek", "Ibn Sino", "Beruniy", "Al-Xorazmiy"]
            },
            {
                "question": "Qaysi davlatning poytaxti Dushanbe?",
                "answer": "Tojikiston",
                "options": ["Tojikiston", "Qirg‘iziston", "Afg‘oniston", "Turkmaniston"]
            },
            {
                "question": "Osiyo qit’asining janubi-g‘arbiy qismi qaysi nom bilan ataladi?",
                "answer": "Yaqin Sharq",
                "options": ["Yaqin Sharq", "Markaziy Osiyo", "Uzoq Sharq", "Kavkaz"]
            },
            {
                "question": "Qaysi davlatda eng ko‘p musulmon aholi yashaydi?",
                "answer": "Indoneziya",
                "options": ["Indoneziya", "Turkiya", "Hindiston", "Pokiston"]
            },
            {
                "question": "O‘zbekiston hududidagi eng katta suv ombori?",
                "answer": "Tuyamo‘yin",
                "options": ["Tuyamo‘yin", "Chorvoq", "Qoratepa", "To‘dako‘l"]
            },
            {
                "question": "Qaysi davlatni 'Qadimiy sivilizatsiyalar vatani' deb atashadi?",
                "answer": "Misr",
                "options": ["Misr", "Xitoy", "Hindiston", "Bobil"]
            },
            {
                "question": "Yer kurrasidagi eng baland plato?",
                "answer": "Tibet",
                "options": ["Tibet", "Pamir", "And", "Altay"]
            },
            {
                "question": "Buyuk Aleksandr qaysi mamlakat hukmdori edi?",
                "answer": "Makedoniya",
                "options": ["Makedoniya", "Rim", "Sparta", "Bobil"]
            },
            {
                "question": "O‘zbekistonda eng katta yog‘och ishlovchi kombinat qayerda joylashgan?",
                "answer": "Qo‘qon",
                "options": ["Qo‘qon", "Andijon", "Namangan", "Buxoro"]
            },
            {
                "question": "Qaysi davlatning poytaxti Nayrobi?",
                "answer": "Keniya",
                "options": ["Keniya", "Efiopiya", "Uganda", "Tanzaniya"]
            },
            {
                "question": "Shimoliy qutbni birinchi bo‘lib kim kashf qilgan?",
                "answer": "Robert Piri",
                "options": ["Robert Piri", "Magellan", "Amundsen", "Kolumb"]
            },
            {
                "question": "Qaysi davlat 'Alp tog‘lari mamlakati' deb ataladi?",
                "answer": "Shveytsariya",
                "options": ["Shveytsariya", "Avstriya", "Fransiya", "Italiya"]
            },
            {
                "question": "O‘zbekiston Respublikasida Prezident lavozimi nechchi yil muddatga saylanadi?",
                "answer": "7 yil",
                "options": ["5 yil", "7 yil", "6 yil", "4 yil"]
            },
            {
                "question": "Qaysi davlatda Sahara cho‘li joylashgan?",
                "answer": "Jazoir",
                "options": ["Jazoir", "Misr", "Sudan", "Liviya"]
            },
            {
                "question": "Buyuk astronom Galiley qanday asbobni takomillashtirgan?",
                "answer": "Teleskop",
                "options": ["Teleskop", "Kompas", "Soat", "Termometr"]
            },
            {
                "question": "Qaysi davlatning rasmiy tili ispan tili emas?",
                "answer": "Braziliya",
                "options": ["Braziliya", "Argentina", "Kolumbiya", "Meksika"]
            },
            {
                "question": "O‘zbekistonning eng katta tabiiy gaz eksportchisi bo‘lgan davri?",
                "answer": "Sovet davri",
                "options": ["Sovet davri", "1991-yil", "2000-yillar", "2010-yillar"]
            },
            {
                "question": "Yer yuzida eng baland vodiy?",
                "answer": "Pamir",
                "options": ["Pamir", "Tibet", "And", "Himalay"]
            },
            {
                "question": "O‘zbekistonning qadimiy shaharlari ichida qaysi biri 'Oqshahr' deb ataladi?",
                "answer": "Shahrisabz",
                "options": ["Shahrisabz", "Buxoro", "Xiva", "Urganch"]
            },
            {
                "question": "Qaysi davlatning poytaxti Karakas?",
                "answer": "Venesuela",
                "options": ["Venesuela", "Kolumbiya", "Ekvador", "Peru"]
            },
            {
                "question": "O‘zbekiston Respublikasida mustaqillik e’lon qilingan joy?",
                "answer": "Oliy Kengash",
                "options": ["Oliy Kengash", "Senat", "Prezident qarorgohi", "Adliya vazirligi"]
            }
        ]
    
        quiz_5 = [
            # Diniy savollar 50ta
            {
                "question": "Musulmonlarning muqaddas shaharlari nechta?",
                "answer": "Uchta",
                "options": ["Uchta", "Ikkita", "To‘rt", "Bitta"]
            },
            {
                "question": "Uch muqaddas shahardan biri?",
                "answer": "Madina",
                "options": ["Madina", "Buxoro", "Samarqand", "Bag‘dod"]
            },
            {
                "question": "Uch muqaddas shahardan yana biri?",
                "answer": "Quddus",
                "options": ["Quddus", "Karbalo", "Damashq", "Najaf"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) sevimli xurmo bog‘lari qayerda bo‘lgan?",
                "answer": "Madina",
                "options": ["Madina", "Makka", "Quddus", "Toyĭf"]
            },
            {
                "question": "Musulmonlar uchun haftaning eng muhim kuni?",
                "answer": "Juma",
                "options": ["Juma", "Dushanba", "Payshanba", "Yakshanba"]
            },
            {
                "question": "Namozning asosiy shartlaridan biri?",
                "answer": "Tahorat",
                "options": ["Tahorat", "Safar", "Ro‘za", "Haj"]
            },
            {
                "question": "Musulmonlar uchun eng ko‘p ishlatiladigan duo iborasi?",
                "answer": "Bismillahir rohmanir rohiym",
                "options": ["Bismillahir rohmanir rohiym", "Alhamdulillah", "Subhanalloh", "La ilaha illalloh"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ning qabr joylari qayerda?",
                "answer": "Madina",
                "options": ["Madina", "Makka", "Quddus", "Badr"]
            },
            {
                "question": "Payg‘ambarimizga eng ko‘p hadis rivoyat qilgan sahoba?",
                "answer": "Abu Hurayra",
                "options": ["Abu Hurayra", "Anas ibn Molik", "Abu Bakr", "Umar"]
            },
            {
                "question": "Islomda eng katta bayramlardan biri?",
                "answer": "Qurbon hayiti",
                "options": ["Qurbon hayiti", "Ro‘za hayiti", "Navro‘z", "Mehnat bayrami"]
            },
            {
                "question": "Namozda sajdadan keyin qisqa o‘tirish nima deyiladi?",
                "answer": "Jalsa",
                "options": ["Jalsa", "Ruku", "Qiyom", "Taslim"]
            },
            {
                "question": "Namozda sajda qilish uchun nima ishlatiladi?",
                "answer": "Peshona",
                "options": ["Peshona", "Qo‘l", "Oyog‘", "Tizzalar"]
            },
            {
                "question": "Musulmonlarning asosiy ibodat kuni?",
                "answer": "Juma",
                "options": ["Juma", "Shanba", "Yakshanba", "Dushanba"]
            },
            {
                "question": "Qur’onning eng boshidagi sura?",
                "answer": "Fotiha",
                "options": ["Fotiha", "Baqara", "Ikhlos", "Nas"]
            },
            {
                "question": "Qur’onning eng uzun surasi?",
                "answer": "Baqara",
                "options": ["Baqara", "Niso", "Yusuf", "Ali Imron"]
            },
            {
                "question": "Qur’onning eng qisqa suralaridan biri?",
                "answer": "Ikhlos",
                "options": ["Ikhlos", "Kavsar", "Falaq", "Nas"]
            },
            {
                "question": "Musulmonlar kuniga necha mahal namoz o‘qiydi?",
                "answer": "5",
                "options": ["5", "3", "4", "6"]
            },
            {
                "question": "Islom dinida odamlarni ezgulikka chorlovchi kishiga nima deyiladi?",
                "answer": "Da’vatchi",
                "options": ["Da’vatchi", "Qori", "Imom", "Muazzin"]
            },
            {
                "question": "Qur’onda eng ko‘p zikr qilingan payg‘ambar?",
                "answer": "Muso (a.s.)",
                "options": ["Muso", "Ibrohim", "Iso", "Yusuf"]
            },
            {
                "question": "Qur’onda eng mashhur duo?",
                "answer": "Rabbana atina fid-dunya hasanah",
                "options": ["Rabbana atina fid-dunya hasanah", "La ilaha illalloh", "Astaghfirulloh", "Alhamdulillah"]
            },
            {
                "question": "Islomda poklanishning eng oddiy shakli?",
                "answer": "Tahorat",
                "options": ["Tahorat", "G‘usl", "Tayammum", "Istinjo"]
            },
            {
                "question": "Qur’on oyatlari kim tomonidan keltirilgan?",
                "answer": "Jabroil (a.s.)",
                "options": ["Jabroil", "Mikoil", "Isrofil", "Azroil"]
            },
            {
                "question": "Namozni ado etish uchun qaysi joy eng afzal?",
                "answer": "Masjid",
                "options": ["Masjid", "Uy", "Ko‘cha", "Bozor"]
            },
            {
                "question": "Musulmonlar uchun eng yaxshi ibora?",
                "answer": "Subhanalloh",
                "options": ["Subhanalloh", "Alhamdulillah", "Astaghfirulloh", "Bismillah"]
            },
            {
                "question": "Qur’onni qaysi tilda o‘qish farz?",
                "answer": "Arab tili",
                "options": ["Arab tili", "Fors tili", "O‘zbek tili", "Turk tili"]
            },
            {
                "question": "Qur’on oyatlarini eslab yod olish nima deb ataladi?",
                "answer": "Hifz",
                "options": ["Hifz", "Qiroat", "Tilovat", "Tafsir"]
            },
            {
                "question": "Qur’onni tushuntirib beradigan ilim?",
                "answer": "Tafsir",
                "options": ["Tafsir", "Hadis", "Fiqh", "Lug‘at"]
            },
            {
                "question": "Qur’on oyatlarini talaffuz bilan o‘qish?",
                "answer": "Tilovat",
                "options": ["Tilovat", "Hifz", "Qiroat", "Tafsir"]
            },
            {
                "question": "Islomda farz amallardan biri?",
                "answer": "Ro‘za",
                "options": ["Ro‘za", "Tahorat", "Salom", "Sadaqa"]
            },
            {
                "question": "Islomda farz amallardan yana biri?",
                "answer": "Haj",
                "options": ["Haj", "Salom", "Tasbeh", "Juma"]
            },
            {
                "question": "Islomda Allohga yaqinlashish uchun qilinadigan qo‘shimcha ibodat?",
                "answer": "Nafl",
                "options": ["Nafl", "Farz", "Sunnat", "Witr"]
            },
            {
                "question": "Musulmonlarda kechasi uxlamasdan ibodat qilish?",
                "answer": "Tahajjud",
                "options": ["Tahajjud", "Tarovih", "Witr", "Qunut"]
            },
            {
                "question": "Musulmonlarda peshindan keyin ado etiladigan namoz?",
                "answer": "Asr",
                "options": ["Asr", "Shom", "Bomdod", "Xufton"]
            },
            {
                "question": "Musulmonlarda shomdan keyin ado etiladigan namoz?",
                "answer": "Xufton",
                "options": ["Xufton", "Asr", "Tarovih", "Witr"]
            },
            {
                "question": "Musulmonlarda eng qisqa zikr?",
                "answer": "Alloh",
                "options": ["Alloh", "Hu", "Haqq", "Subhan"]
            },
            {
                "question": "Allohning sifatlaridan biri?",
                "answer": "Rahmon",
                "options": ["Rahmon", "Rahim", "Samad", "Alim"]
            },
            {
                "question": "Allohning sifatlaridan yana biri?",
                "answer": "Rahim",
                "options": ["Rahim", "Rahmon", "Qahhor", "Aziz"]
            },
            {
                "question": "Allohning sifatlaridan yana biri?",
                "answer": "G‘affor",
                "options": ["G‘affor", "Latif", "Hakim", "Alim"]
            },
            {
                "question": "Allohning sifatlaridan yana biri?",
                "answer": "Qahhor",
                "options": ["Qahhor", "Samad", "Nur", "Latif"]
            },
            {
                "question": "Qur’onning boshlanishi qanday ibora bilan boshlanadi?",
                "answer": "Bismillahir rohmanir rohiym",
                "options": ["Bismillahir rohmanir rohiym", "Alhamdulillah", "Subhanalloh", "La ilaha illalloh"]
            },
            {
                "question": "Payg‘ambarimizning sevimli ichimliklari?",
                "answer": "Suv va sut",
                "options": ["Suv va sut", "Asal", "Sharbat", "Xurmo suvi"]
            },
            {
                "question": "Payg‘ambarimizning sevimli mevalaridan biri?",
                "answer": "Xurmo",
                "options": ["Xurmo", "Anjir", "Uzum", "Anor"]
            },
            {
                "question": "Payg‘ambarimizning sevimli kiyimlari?",
                "answer": "Oddiy oq kiyim",
                "options": ["Oddiy oq kiyim", "Qimmat libos", "Qora kiyim", "Yashil kiyim"]
            },
            {
                "question": "Payg‘ambarimizning sevimli ibodatlari?",
                "answer": "Namoz",
                "options": ["Namoz", "Ro‘za", "Duo", "Zakot"]
            },
            {
                "question": "Musulmonlarda eng mashhur qo‘shiq o‘rnida aytiladigan narsalar?",
                "answer": "Zikr",
                "options": ["Zikr", "Madhiya", "Qo‘shiq", "Marsiya"]
            },
            {
                "question": "Musulmonlarning eng katta ibodat joyi?",
                "answer": "Masjidul Haram",
                "options": ["Masjidul Haram", "Masjidun Nabaviy", "Masjidul Aqso", "Quba masjidi"]
            },
            {
                "question": "Musulmonlarning ikkinchi eng katta ibodat joyi?",
                "answer": "Masjidun Nabaviy",
                "options": ["Masjidun Nabaviy", "Masjidul Haram", "Masjidul Aqso", "Quba masjidi"]
            },
            {
                "question": "Musulmonlarning uchinchi eng katta ibodat joyi?",
                "answer": "Masjidul Aqso",
                "options": ["Masjidul Aqso", "Masjidul Haram", "Masjidun Nabaviy", "Quba masjidi"]
            },
            {
                "question": "Qur’onni qaysi farishta Payg‘ambarimizga olib kelgan?",
                "answer": "Jabroil (a.s.)",
                "options": ["Jabroil", "Mikoil", "Azroil", "Isrofil"]
            },
            {
                "question": "Musulmonlarning eng muhim kitobi?",
                "answer": "Qur’on",
                "options": ["Qur’on", "Hadis", "Tavrot", "Injil"]
            },
            # Fanga oid savollar 100ta
            {
                "question": "Dunyoning eng mashhur muzeylaridan biri — Britaniya muzeyi qayerda?",
                "answer": "London",
                "options": ["London", "Berlin", "Parij", "Madrid"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Alisher Navoiy nechanchi asrda yashagan?",
                "answer": "15-asr",
                "options": ["15-asr", "14-asr", "16-asr", "17-asr"]
            },
            {
                "question": "Dunyoning eng mashhur teatrlaridan biri — Bolshoy teatri qayerda?",
                "answer": "Moskva",
                "options": ["Moskva", "London", "Parij", "Berlin"]
            },
            {
                "question": "Dunyoning eng mashhur tog‘laridan biri — Montblan qayerda joylashgan?",
                "answer": "Fransiya va Italiya",
                "options": ["Fransiya va Italiya", "Shveytsariya", "Avstriya", "Germaniya"]
            },
            {
                "question": "Dunyoning eng mashhur sharsharalaridan biri — Iguasu qayerda joylashgan?",
                "answer": "Braziliya va Argentina",
                "options": ["Braziliya va Argentina", "Peru va Boliviya", "Kolumbiya va Venesuela", "Meksika va AQSh"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Abdulla Qodiriy mashhur asari?",
                "answer": "O‘tkan kunlar",
                "options": ["O‘tkan kunlar", "Mehrobdan chayon", "Sarob", "Yulduzli tunlar"]
            },
            {
                "question": "Dunyoning eng mashhur orollaridan biri — Sumatra qayerda joylashgan?",
                "answer": "Indoneziya",
                "options": ["Indoneziya", "Filippin", "Malayziya", "Singapur"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Ibn Sino qaysi sohada mashhur?",
                "answer": "Tibbiyot",
                "options": ["Tibbiyot", "Matematika", "Adabiyot", "Kimyo"]
            },
            {
                "question": "Dunyoning eng mashhur daryolaridan biri — Yanszi qaysi davlatdan oqib o‘tadi?",
                "answer": "Xitoy",
                "options": ["Xitoy", "Hindiston", "Rossiya", "Mongoliya"]
            },
            {
                "question": "O‘zbekistonning mashhur shoirlaridan biri — Cho‘lpon mashhur romani?",
                "answer": "Kecha va kunduz",
                "options": ["Kecha va kunduz", "O‘tkan kunlar", "Sarob", "Shaytanat"]
            },
            {
                "question": "Dunyoning eng mashhur teatrlaridan biri — Metropolitan Opera qayerda joylashgan?",
                "answer": "Nyu-York",
                "options": ["Nyu-York", "London", "Moskva", "Parij"]
            },
            {
                "question": "YUNESKO tomonidan jahon merosi ro‘yxatiga kiritilgan O‘zbekiston shaharlari qaysilar?",
                "answer": "Samarqand, Buxoro, Xiva, Shahrisabz",
                "options": ["Samarqand, Buxoro, Xiva, Shahrisabz", "Toshkent, Andijon, Namangan", "Qo‘qon, Jizzax, Guliston", "Termiz, Qarshi, Nukus"]
            },
            {
                "question": "Dunyoning eng katta vodiylaridan biri — Grand Kanyon qayerda joylashgan?",
                "answer": "AQSh",
                "options": ["AQSh", "Kanada", "Meksika", "Braziliya"]
            },
            {
                "question": "Yevropa va Osiyoni bog‘lab turuvchi mashhur ko‘prik qayerda joylashgan?",
                "answer": "Turkiya",
                "options": ["Turkiya", "Rossiya", "Fransiya", "Angliya"]
            },
            {
                "question": "O‘zbekistonning milliy bog‘laridan biri — Zomin milliy bog‘i qaysi viloyatda joylashgan?",
                "answer": "Jizzax",
                "options": ["Jizzax", "Namangan", "Farg‘ona", "Surxondaryo"]
            },
            {
                "question": "Dunyoning eng mashhur futbol jamoalaridan biri — 'Bavariya' qaysi shaharda joylashgan?",
                "answer": "Myunxen",
                "options": ["Myunxen", "Berlin", "Dortmund", "Hamburg"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy yodgorliklaridan biri — Qizil minor masjidi qayerda?",
                "answer": "Xiva",
                "options": ["Xiva", "Buxoro", "Toshkent", "Samarqand"]
            },
            {
                "question": "Dunyodagi eng katta arxipelag davlat?",
                "answer": "Indoneziya",
                "options": ["Indoneziya", "Filippin", "Shvetsiya", "Malayziya"]
            },
            {
                "question": "Buyuk olim Muhammad al-Xorazmiy qaysi fan asoschisi?",
                "answer": "Algebra",
                "options": ["Algebra", "Geometriya", "Astronomiya", "Kimyo"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan qadimiy Budda ibodatxonasi?",
                "answer": "Fayoztepa",
                "options": ["Fayoztepa", "Shohi Zinda", "Registon", "Qoratepa"]
            },
            {
                "question": "Dunyoning eng baland sharsharasi Anxel qaysi mamlakatda joylashgan?",
                "answer": "Venesuela",
                "options": ["Venesuela", "Braziliya", "Argentina", "Kolumbiya"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan eng baland tog‘ cho‘qqisi?",
                "answer": "Hazrati Sulton",
                "options": ["Hazrati Sulton", "Chimyon", "Bobotog‘", "Somoni cho‘qqisi"]
            },
            {
                "question": "Yevropadagi eng katta ko‘l?",
                "answer": "Ladoga",
                "options": ["Ladoga", "Onega", "Viktoriya", "Kaspiy"]
            },
            {
                "question": "O‘zbekiston hududidagi qadimiy madaniy markazlardan biri — Termiz qaysi daryo bo‘yida joylashgan?",
                "answer": "Amudaryo",
                "options": ["Amudaryo", "Sirdaryo", "Zarafshon", "Chirchiq"]
            },
            {
                "question": "Dunyodagi eng ko‘p orolga ega davlat?",
                "answer": "Shvetsiya",
                "options": ["Shvetsiya", "Norvegiya", "Indoneziya", "Yaponiya"]
            },
            {
                "question": "O‘zbekiston hududidagi qadimiy qal’alardan biri — Qo‘yqirilgan qal’a qayerda joylashgan?",
                "answer": "Qoraqalpog‘iston",
                "options": ["Qoraqalpog‘iston", "Buxoro", "Xorazm", "Samarqand"]
            },
            {
                "question": "Dunyodagi eng mashhur rasm galereyalaridan biri — Prado muzeyi qayerda joylashgan?",
                "answer": "Ispaniya",
                "options": ["Ispaniya", "Italiya", "Fransiya", "Angliya"]
            },
            {
                "question": "O‘zbekistonning milliy musiqiy asboblaridan biri?",
                "answer": "Doira",
                "options": ["Doira", "G‘ijjak", "Pianino", "Gitara"]
            },
            {
                "question": "Afrikadagi eng uzun daryo?",
                "answer": "Nil",
                "options": ["Nil", "Kongo", "Niger", "Zambezi"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur arxeologik yodgorliklardan biri?",
                "answer": "Topraqqal’a",
                "options": ["Topraqqal’a", "Ayazqal’a", "Qo‘yqirilgan qal’a", "Mug‘ qal’a"]
            },
            {
                "question": "Dunyodagi eng mashhur teatrlaridan biri — La Skala qaysi shaharda joylashgan?",
                "answer": "Milan",
                "options": ["Milan", "Parij", "London", "Vena"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Abdulla Qahhorning mashhur asari?",
                "answer": "Sarob",
                "options": ["Sarob", "Anor", "Sinchalak", "O‘tkan kunlar"]
            },
            {
                "question": "Shimoliy Amerikadagi eng uzun daryo?",
                "answer": "Missisipi",
                "options": ["Missisipi", "Amazonka", "Orinoko", "Parana"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur tarixiy me’moriy majmualardan biri — Registon?",
                "answer": "Samarqand",
                "options": ["Samarqand", "Buxoro", "Xiva", "Toshkent"]
            },
            {
                "question": "Dunyodagi eng baland tog‘ tizmasi?",
                "answer": "Gimolay",
                "options": ["Gimolay", "Alp", "And", "Tyan-Shan"]
            },
            {
                "question": "O‘zbekistonning mashhur shoirlaridan biri — Cho‘lponning mashhur asari?",
                "answer": "Kecha va kunduz",
                "options": ["Kecha va kunduz", "Yulduzli tunlar", "O‘tkan kunlar", "Sarob"]
            },
            {
                "question": "Dunyodagi eng mashhur sharsharalardan biri — Viktoriya qayerda joylashgan?",
                "answer": "Zambiya va Zimbabve",
                "options": ["Zambiya va Zimbabve", "Braziliya va Argentina", "Venesuela", "Kanada va AQSh"]
            },
            {
                "question": "O‘zbekiston hududidagi qadimiy shaharlaridan biri?",
                "answer": "Buxoro",
                "options": ["Buxoro", "Samarqand", "Xiva", "Shahrisabz"]
            },
            {
                "question": "Dunyodagi eng mashhur universitetlardan biri — Garvard qaysi davlatda joylashgan?",
                "answer": "AQSh",
                "options": ["AQSh", "Angliya", "Kanada", "Avstraliya"]
            },
            {
                "question": "Dunyoning eng katta ichki dengizi?",
                "answer": "Kaspiy",
                "options": ["Kaspiy", "Aral", "Qora dengiz", "Oq dengiz"]
            },
            {
                "question": "Afrikadagi eng katta ko‘l?",
                "answer": "Viktoriya",
                "options": ["Viktoriya", "Tanganika", "Malavi", "Chad"]
            },
            {
                "question": "O‘zbekistonning mashhur shoirlaridan biri — Erkin Vohidov mashhur she’riy turkumi?",
                "answer": "Tong nafasi",
                "options": ["Tong nafasi", "Ruhlar isyoni", "O‘zbekiston", "Sarob"]
            },
            {
                "question": "Dunyoning eng mashhur orollardan biri — Madagaskar qayerda joylashgan?",
                "answer": "Hind okeani",
                "options": ["Hind okeani", "Tinch okeani", "Atlantika okeani", "Shimoliy muz okeani"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Tohir Malik mashhur romani?",
                "answer": "Shaytanat",
                "options": ["Shaytanat", "Dunyoning ishlari", "Yulduzli tunlar", "Sarob"]
            },
            {
                "question": "Dunyoning eng mashhur teatrlaridan biri — Katta teatr qaysi shaharda joylashgan?",
                "answer": "Moskva",
                "options": ["Moskva", "London", "Parij", "Rim"]
            },
            {
                "question": "Dunyoning eng mashhur sharsharalaridan biri — Niagara qaysi ikki davlat chegarasida?",
                "answer": "AQSh va Kanada",
                "options": ["AQSh va Kanada", "Braziliya va Argentina", "Venesuela", "Zambiya va Zimbabve"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Abdulla Qodiriy mashhur romani?",
                "answer": "Mehrobdan chayon",
                "options": ["Mehrobdan chayon", "O‘tkan kunlar", "Sarob", "Kecha va kunduz"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Ibn Sino qaysi asarda tibbiy bilimlarni jamlagan?",
                "answer": "Tib qonunlari",
                "options": ["Tib qonunlari", "Shohnoma", "Xamsa", "Qutadg‘u bilig"]
            },
            {
                "question": "Yer kurrasidagi eng baland plato qaysi?",
                "answer": "Tibet platosi",
                "options": ["Tibet platosi", "Pamir", "Altay", "And"]
            },
            {
                "question": "Dunyoning eng yirik metall ishlab chiqaruvchilaridan biri?",
                "answer": "Xitoy",
                "options": ["Xitoy", "AQSh", "Rossiya", "Hindiston"]
            },
            {
                "question": "O‘zbekiston hududidagi qadimiy qal’alardan biri — Ayazqal’a qaysi hududda joylashgan?",
                "answer": "Qoraqalpog‘iston",
                "options": ["Qoraqalpog‘iston", "Buxoro", "Samarqand", "Namangan"]
            },
            {
                "question": "Buyuk astronom Kopernik qanday nazariyasi bilan mashhur?",
                "answer": "Geliosentrik nazariya",
                "options": ["Geliosentrik nazariya", "Geosentrik nazariya", "Atom nazariyasi", "Evolyutsiya nazariyasi"]
            },
            {
                "question": "O‘zbekistonning mashhur shaharlaridan biri — Nukus qaysi hudud markazi?",
                "answer": "Qoraqalpog‘iston",
                "options": ["Qoraqalpog‘iston", "Buxoro", "Qashqadaryo", "Xorazm"]
            },
            {
                "question": "Afrikadagi eng baland tog‘ cho‘qqisi?",
                "answer": "Kilimanjaro",
                "options": ["Kilimanjaro", "Elbrus", "Atlas", "Drakensberg"]
            },
            {
                "question": "Shimoliy Amerikadagi eng katta ko‘l?",
                "answer": "Yuqori ko‘l",
                "options": ["Yuqori ko‘l", "Michigan", "Ontario", "Eri"]
            },
            {
                "question": "Buyuk yozuvchi Abdulla Oripov mashhur asarlaridan biri?",
                "answer": "Jannatga yo‘l",
                "options": ["Jannatga yo‘l", "Tong nafasi", "Sarob", "Kecha va kunduz"]
            },
            {
                "question": "Dunyoning eng mashhur sharsharalaridan biri — Iguasu qaysi davlatlarda joylashgan?",
                "answer": "Braziliya va Argentina",
                "options": ["Braziliya va Argentina", "Venesuela", "Kanada va AQSh", "Kolumbiya va Peru"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaharlaridan biri — Qarshi qaysi davrda tashkil topgan?",
                "answer": "Miloddan avvalgi davrda",
                "options": ["Miloddan avvalgi davrda", "IX asrda", "XIV asrda", "XVIII asrda"]
            },
            {
                "question": "Osiyodagi eng baland tog‘ cho‘qqisi?",
                "answer": "Everest",
                "options": ["Everest", "K2", "Kangchenjunga", "Makalu"]
            },
            {
                "question": "Dunyodagi eng mashhur teatr binosi — Sidney Opera House qayerda joylashgan?",
                "answer": "Avstraliya",
                "options": ["Avstraliya", "Yangi Zelandiya", "Kanada", "AQSh"]
            },
            {
                "question": "O‘zbekistonning eng katta gaz konlaridan biri?",
                "answer": "Sho‘rtan",
                "options": ["Sho‘rtan", "Qandim", "Muborak", "Olmaliq"]
            },
            {
                "question": "Dunyoning eng mashhur universitetlaridan biri — Kembridj qaysi davlatda joylashgan?",
                "answer": "Angliya",
                "options": ["Angliya", "AQSh", "Kanada", "Avstraliya"]
            },
            {
                "question": "Afrikadagi eng katta daryo havzasi?",
                "answer": "Kongo",
                "options": ["Kongo", "Nil", "Niger", "Zambezi"]
            },
            {
                "question": "Buyuk yozuvchi Erkin Vohidov mashhur asarlaridan biri?",
                "answer": "Ruhlar isyoni",
                "options": ["Ruhlar isyoni", "O'zbegim", "O‘zbekiston", "Sarob"]
            },
            {
                "question": "Dunyoning eng katta ichki ko‘li?",
                "answer": "Kaspiy",
                "options": ["Kaspiy", "Baykal", "Viktoriya", "Aral"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Beruniy qaysi sohalarda mashhur?",
                "answer": "Matematika va astronomiya",
                "options": ["Matematika va astronomiya", "Kimyo va tibbiyot", "Adabiyot va san’at", "Geografiya va tarix"]
            },
            {
                "question": "Janubiy Amerikadagi eng katta mamlakat?",
                "answer": "Braziliya",
                "options": ["Braziliya", "Argentina", "Kolumbiya", "Peru"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur shoirlardan biri — Bobur qayerda tug‘ilgan?",
                "answer": "Andijon",
                "options": ["Andijon", "Samarqand", "Toshkent", "Xiva"]
            },
            {
                "question": "Dunyoning eng mashhur sport musobaqalaridan biri — Olimpiada dastlab qayerda boshlangan?",
                "answer": "Yunoniston",
                "options": ["Yunoniston", "Italiya", "Fransiya", "Misr"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — O‘tkir Hoshimovning mashhur asari?",
                "answer": "Ikki eshik orasi",
                "options": ["Ikki eshik orasi", "Dunyoning ishlari", "Sarob", "Anor"]
            },
            {
                "question": "Osiyodagi eng katta orol?",
                "answer": "Borneo",
                "options": ["Borneo", "Sumatra", "Yava", "Saxalin"]
            },
            {
                "question": "Dunyoning eng mashhur qal’alaridan biri — Alhambra qayerda joylashgan?",
                "answer": "Ispaniya",
                "options": ["Ispaniya", "Italiya", "Fransiya", "Portugaliya"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur yodgorliklardan biri — Ismoil Somoniy maqbarasi qayerda joylashgan?",
                "answer": "Buxoro",
                "options": ["Buxoro", "Samarqand", "Xiva", "Shahrisabz"]
            },
            {
                "question": "Shimoliy Amerikadagi eng baland tog‘?",
                "answer": "Denali",
                "options": ["Denali", "Logan", "Orizaba", "Rainier"]
            },
            {
                "question": "Dunyoning eng mashhur universitetlaridan biri — Sorbonna qayerda joylashgan?",
                "answer": "Parij",
                "options": ["Parij", "London", "Berlin", "Madrid"]
            },
            {
                "question": "Dunyoning eng mashhur sharsharalaridan biri — Dettifoss qayerda joylashgan?",
                "answer": "Islandiya",
                "options": ["Islandiya", "Norvegiya", "Kanada", "AQSh"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur san’at maktablaridan biri?",
                "answer": "Bekzod san’at maktabi",
                "options": ["Bekzod san’at maktabi", "Ilhom san’at maktabi", "Usto", "Kamolot"]
            },
            {
                "question": "Janubiy Amerikadagi eng mashhur tog‘ tizmasi?",
                "answer": "And",
                "options": ["And", "Syerra-Madre", "Patagoniya", "Altiplano"]
            },
            {
                "question": "Dunyoning eng mashhur cho‘llaridan biri — Atakama qayerda joylashgan?",
                "answer": "Chili",
                "options": ["Chili", "Argentina", "Peru", "Boliviya"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Cho‘lponning mashhur she’riy to‘plamlaridan biri?",
                "answer": "Buloqlar",
                "options": ["Buloqlar", "Tong nafasi", "O‘zbekiston", "Sarob"]
            },
            {
                "question": "Afrikadagi eng mashhur sharsharalardan biri — Tugela qayerda joylashgan?",
                "answer": "Janubiy Afrika",
                "options": ["Janubiy Afrika", "Namibiya", "Kongo", "Zimbabve"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur shahar — Andijon qaysi vohada joylashgan?",
                "answer": "Farg‘ona vodiysi",
                "options": ["Farg‘ona vodiysi", "Qashqadaryo", "Surxondaryo", "Zarafshon"]
            },
            {
                "question": "Dunyoning eng mashhur sportchilaridan biri — Muhammad Ali qaysi sport turi bo‘yicha mashhur?",
                "answer": "Boks",
                "options": ["Boks", "Futbol", "Basketbol", "Tennis"]
            },
            {
                "question": "Dunyodagi eng uzun daryo qaysi ikki davlat hududidan oqib o‘tadi?",
                "answer": "Misr va Sudan",
                "options": ["Misr va Sudan", "Braziliya va Peru", "Xitoy va Hindiston", "Rossiya va Qozog‘iston"]
            },
            {
                "question": "Dunyoning eng katta ko‘llaridan biri — Baykal qayerda joylashgan?",
                "answer": "Rossiya",
                "options": ["Rossiya", "Mongoliya", "Qozog‘iston", "Xitoy"]
            },
            {
                "question": "Buyuk geografik kashfiyotlar davrida Hindistonga dengiz yo‘lini topgan kim?",
                "answer": "Vasko da Gama",
                "options": ["Vasko da Gama", "Kolumb", "Magellan", "Hudson"]
            },
            {
                "question": "O‘zbekiston hududidagi qadimiy buddaviy yodgorliklardan biri — Zurmala stupasi qayerda?",
                "answer": "Termez",
                "options": ["Termez", "Samarqand", "Xiva", "Toshkent"]
            },
            {
                "question": "Dunyoning eng katta orollaridan biri — Madagaskar qaysi okeanda joylashgan?",
                "answer": "Hind okeani",
                "options": ["Hind okeani", "Tinch okeani", "Atlantika okeani", "Shimoliy muz okeani"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Utkir Hoshimov mashhur hikoyasi?",
                "answer": "Dunyoning ishlari",
                "options": ["Dunyoning ishlari", "Bahor qaytmaydi", "Ikki eshik orasi", "Shum bola"]
            },
            {
                "question": "Dunyoning eng katta aholi yashaydigan oroli?",
                "answer": "Yava",
                "options": ["Yava", "Sumatra", "Bali", "Filippin oroli"]
            },
            {
                "question": "O‘zbekiston hududidagi qadimiy qal’alardan biri — Devxona qayerda joylashgan?",
                "answer": "Surxondaryo",
                "options": ["Surxondaryo", "Buxoro", "Qashqadaryo", "Xorazm"]
            },
            {
                "question": "Dunyoning eng baland shahri?",
                "answer": "La-Pas",
                "options": ["La-Pas", "Katmandu", "Quito", "Bogota"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Al-Farg‘oniy asosan qaysi fan bilan shug‘ullangan?",
                "answer": "Astronomiya",
                "options": ["Astronomiya", "Matematika", "Kimyo", "Fizika"]
            },
            {
                "question": "Dunyoning eng uzun yerosti daryosi?",
                "answer": "Perto Princeso",
                "options": ["Perto Princeso", "Nil", "Amazonka", "Yanszi"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur tarixiy obidalaridan biri — Ko‘hna Ark qayerda joylashgan?",
                "answer": "Xiva",
                "options": ["Xiva", "Buxoro", "Samarqand", "Shahrisabz"]
            },
            {
                "question": "Dunyoning eng mashhur san’at muzeylaridan biri — Uffizi galereyasi qayerda joylashgan?",
                "answer": "Florensiya",
                "options": ["Florensiya", "Rim", "Venetsiya", "Milan"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Erkin Vohidovning mashhur dostoni?",
                "answer": "Sadoqat",
                "options": ["Sadoqat", "Ruhlar isyoni", "Tong nafasi", "O‘zbekiston"]
            },
            {
                "question": "Dunyoning eng katta cho‘llaridan biri — Kalahari qaysi qit’ada joylashgan?",
                "answer": "Afrika",
                "options": ["Afrika", "Osiyo", "Janubiy Amerika", "Avstraliya"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan qadimiy shahar qal’alaridan biri — Qo‘yqirilgan qal’a qaysi vohada joylashgan?",
                "answer": "Ellikqal’a",
                "options": ["Ellikqal’a", "Buxoro vohasi", "Zarafshon vohasi", "Farg‘ona vodiysi"]
            },
            {
                "question": "Dunyoning eng mashhur orollaridan biri — Shpitsbergen qaysi davlat hududida joylashgan?",
                "answer": "Norvegiya",
                "options": ["Norvegiya", "Daniya", "Islandiya", "Shvetsiya"]
            }
        ]
            
        quiz_6 = [
            # Diniy savollar 50ta
            {
                "question": "Musulmonlarning muqaddas shaharlari nechta?",
                "answer": "Uchta",
                "options": ["Uchta", "Ikki", "To‘rt", "Bitta"]
            },
            {
                "question": "Uch muqaddas shahardan biri?",
                "answer": "Madina",
                "options": ["Madina", "Buxoro", "Samarqand", "Bag‘dod"]
            },
            {
                "question": "Uch muqaddas shahardan yana biri?",
                "answer": "Quddus",
                "options": ["Quddus", "Karbalo", "Damashq", "Najaf"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) sevimli xurmo bog‘lari qayerda bo‘lgan?",
                "answer": "Madina",
                "options": ["Madina", "Makka", "Quddus", "Toyĭf"]
            },
            {
                "question": "Musulmonlar uchun haftaning eng muhim kuni?",
                "answer": "Juma",
                "options": ["Juma", "Dushanba", "Payshanba", "Yakshanba"]
            },
            {
                "question": "Namozning asosiy shartlaridan biri?",
                "answer": "Tahorat",
                "options": ["Tahorat", "Safar", "Ro‘za", "Haj"]
            },
            {
                "question": "Musulmonlar uchun eng ko‘p ishlatiladigan duo iborasi?",
                "answer": "Bismillahir rohmanir rohiym",
                "options": ["Bismillahir rohmanir rohiym", "Alhamdulillah", "Subhanalloh", "La ilaha illalloh"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ning qabr joylari qayerda?",
                "answer": "Madina",
                "options": ["Madina", "Makka", "Quddus", "Badr"]
            },
            {
                "question": "Payg‘ambarimizga eng ko‘p hadis rivoyat qilgan sahoba?",
                "answer": "Abu Hurayra",
                "options": ["Abu Hurayra", "Anas ibn Molik", "Abu Bakr", "Umar"]
            },
            {
                "question": "Islomda eng katta bayramlardan biri?",
                "answer": "Qurbon hayiti",
                "options": ["Qurbon hayiti", "Ro‘za hayiti", "Navro‘z", "Mehnat bayrami"]
            },
            {
                "question": "Namozda sajdadan keyin qisqa o‘tirish nima deyiladi?",
                "answer": "Jalsa",
                "options": ["Jalsa", "Ruku", "Qiyom", "Taslim"]
            },
            {
                "question": "Namozda sajda qilish uchun nima ishlatiladi?",
                "answer": "Peshona",
                "options": ["Peshona", "Qo‘l", "Oyog‘", "Tizzalar"]
            },
            {
                "question": "Musulmonlarning asosiy ibodat kuni?",
                "answer": "Juma",
                "options": ["Juma", "Shanba", "Yakshanba", "Dushanba"]
            },
            {
                "question": "Qur’onning eng boshidagi sura?",
                "answer": "Fotiha",
                "options": ["Fotiha", "Baqara", "Ikhlos", "Nas"]
            },
            {
                "question": "Qur’onning eng uzun surasi?",
                "answer": "Baqara",
                "options": ["Baqara", "Niso", "Yusuf", "Ali Imron"]
            },
            {
                "question": "Qur’onning eng qisqa suralaridan biri?",
                "answer": "Ikhlos",
                "options": ["Ikhlos", "Kavsar", "Falaq", "Nas"]
            },
            {
                "question": "Musulmonlar kuniga necha mahal namoz o‘qiydi?",
                "answer": "5",
                "options": ["5", "3", "4", "6"]
            },
            {
                "question": "Islom dinida odamlarni ezgulikka chorlovchi kishiga nima deyiladi?",
                "answer": "Da’vatchi",
                "options": ["Da’vatchi", "Qori", "Imom", "Muazzin"]
            },
            {
                "question": "Qur’onda eng ko‘p zikr qilingan payg‘ambar?",
                "answer": "Muso (a.s.)",
                "options": ["Muso", "Ibrohim", "Iso", "Yusuf"]
            },
            {
                "question": "Qur’onda eng mashhur duo?",
                "answer": "Rabbana atina fid-dunya hasanah",
                "options": ["Rabbana atina fid-dunya hasanah", "La ilaha illalloh", "Astaghfirulloh", "Alhamdulillah"]
            },
            {
                "question": "Islomda poklanishning eng oddiy shakli?",
                "answer": "Tahorat",
                "options": ["Tahorat", "G‘usl", "Tayammum", "Istinjo"]
            },
            {
                "question": "Qur’on oyatlari kim tomonidan keltirilgan?",
                "answer": "Jabroil (a.s.)",
                "options": ["Jabroil", "Mikoil", "Isrofil", "Azroil"]
            },
            {
                "question": "Namozni ado etish uchun qaysi joy eng afzal?",
                "answer": "Masjid",
                "options": ["Masjid", "Uy", "Ko‘cha", "Bozor"]
            },
            {
                "question": "Musulmonlar uchun eng yaxshi ibora?",
                "answer": "Subhanalloh",
                "options": ["Subhanalloh", "Alhamdulillah", "Astaghfirulloh", "Bismillah"]
            },
            {
                "question": "Qur’onni qaysi tilda o‘qish farz?",
                "answer": "Arab tili",
                "options": ["Arab tili", "Fors tili", "O‘zbek tili", "Turk tili"]
            },
            {
                "question": "Qur’on oyatlarini eslab yod olish nima deb ataladi?",
                "answer": "Hifz",
                "options": ["Hifz", "Qiroat", "Tilovat", "Tafsir"]
            },
            {
                "question": "Qur’onni tushuntirib beradigan ilim?",
                "answer": "Tafsir",
                "options": ["Tafsir", "Hadis", "Fiqh", "Lug‘at"]
            },
            {
                "question": "Qur’on oyatlarini talaffuz bilan o‘qish?",
                "answer": "Tilovat",
                "options": ["Tilovat", "Hifz", "Qiroat", "Tafsir"]
            },
            {
                "question": "Islomda farz amallardan biri?",
                "answer": "Ro‘za",
                "options": ["Ro‘za", "Tahorat", "Salom", "Sadaqa"]
            },
            {
                "question": "Islomda farz amallardan yana biri?",
                "answer": "Haj",
                "options": ["Haj", "Salom", "Tasbeh", "Juma"]
            },
            {
                "question": "Islomda Allohga yaqinlashish uchun qilinadigan qo‘shimcha ibodat?",
                "answer": "Nafl",
                "options": ["Nafl", "Farz", "Sunnat", "Witr"]
            },
            {
                "question": "Musulmonlarda kechasi uxlamasdan ibodat qilish?",
                "answer": "Tahajjud",
                "options": ["Tahajjud", "Tarovih", "Witr", "Qunut"]
            },
            {
                "question": "Musulmonlarda peshindan keyin ado etiladigan namoz?",
                "answer": "Asr",
                "options": ["Asr", "Shom", "Bomdod", "Xufton"]
            },
            {
                "question": "Musulmonlarda shomdan keyin ado etiladigan namoz?",
                "answer": "Xufton",
                "options": ["Xufton", "Asr", "Tarovih", "Witr"]
            },
            {
                "question": "Musulmonlarda eng qisqa zikr?",
                "answer": "Alloh",
                "options": ["Alloh", "Hu", "Haqq", "Subhan"]
            },
            {
                "question": "Allohning sifatlaridan biri?",
                "answer": "Rahmon",
                "options": ["Rahmon", "Rahim", "Samad", "Alim"]
            },
            {
                "question": "Allohning sifatlaridan yana biri?",
                "answer": "Rahim",
                "options": ["Rahim", "Rahmon", "Qahhor", "Aziz"]
            },
            {
                "question": "Allohning sifatlaridan yana biri?",
                "answer": "G‘affor",
                "options": ["G‘affor", "Latif", "Hakim", "Alim"]
            },
            {
                "question": "Allohning sifatlaridan yana biri?",
                "answer": "Qahhor",
                "options": ["Qahhor", "Samad", "Nur", "Latif"]
            },
            {
                "question": "Qur’onning boshlanishi qanday ibora bilan boshlanadi?",
                "answer": "Bismillahir rohmanir rohiym",
                "options": ["Bismillahir rohmanir rohiym", "Alhamdulillah", "Subhanalloh", "La ilaha illalloh"]
            },
            {
                "question": "Payg‘ambarimizning sevimli ichimliklari?",
                "answer": "Suv va sut",
                "options": ["Suv va sut", "Asal", "Sharbat", "Xurmo suvi"]
            },
            {
                "question": "Payg‘ambarimizning sevimli mevalaridan biri?",
                "answer": "Xurmo",
                "options": ["Xurmo", "Anjir", "Uzum", "Anor"]
            },
            {
                "question": "Payg‘ambarimizning sevimli kiyimlari?",
                "answer": "Oddiy oq kiyim",
                "options": ["Oddiy oq kiyim", "Qimmat libos", "Qora kiyim", "Yashil kiyim"]
            },
            {
                "question": "Payg‘ambarimizning sevimli ibodatlari?",
                "answer": "Namoz",
                "options": ["Namoz", "Ro‘za", "Duo", "Zakot"]
            },
            {
                "question": "Musulmonlarda eng mashhur qo‘shiq o‘rnida aytiladigan narsalar?",
                "answer": "Zikr",
                "options": ["Zikr", "Madhiya", "Qo‘shiq", "Marsiya"]
            },
            {
                "question": "Musulmonlarning eng katta ibodat joyi?",
                "answer": "Masjidul Haram",
                "options": ["Masjidul Haram", "Masjidun Nabaviy", "Masjidul Aqso", "Quba masjidi"]
            },
            {
                "question": "Musulmonlarning ikkinchi eng katta ibodat joyi?",
                "answer": "Masjidun Nabaviy",
                "options": ["Masjidun Nabaviy", "Masjidul Haram", "Masjidul Aqso", "Quba masjidi"]
            },
            {
                "question": "Musulmonlarning uchinchi eng katta ibodat joyi?",
                "answer": "Masjidul Aqso",
                "options": ["Masjidul Aqso", "Masjidul Haram", "Masjidun Nabaviy", "Quba masjidi"]
            },
            {
                "question": "Qur’onni qaysi farishta Payg‘ambarimizga olib kelgan?",
                "answer": "Jabroil (a.s.)",
                "options": ["Jabroil", "Mikoil", "Azroil", "Isrofil"]
            },
            {
                "question": "Musulmonlarning eng muhim kitobi?",
                "answer": "Qur’on",
                "options": ["Qur’on", "Hadis", "Tavrot", "Injil"]
            },
            # Fanga oid savollar 100ta
            {
                "question": "Kompyuter klaviaturasida 'Esc' tugmasi odatda qaysi burchakda joylashgan?",
                "answer": "Yuqori chap burchak",
                "options": ["Yuqori chap burchak", "Yuqori o‘ng burchak", "Pastki chap burchak", "Pastki o‘ng burchak"]
            },
            {
                "question": "Rubik kubigini kim ixtiro qilgan?",
                "answer": "Ernő Rubik",
                "options": ["Ernő Rubik", "Nikola Tesla", "Tim Berners-Lee", "Alan Turing"]
            },
            {
                "question": "HTML tilida gipermurojaat yaratish uchun qaysi teg ishlatiladi?",
                "answer": "<a>",
                "options": ["<a>", "<link>", "<href>", "<url>"]
            },
            {
                "question": "Toshkent metropoliteni qaysi yilda ishga tushirilgan?",
                "answer": "1977",
                "options": ["1977", "1984", "1969", "1991"]
            },
            {
                "question": "O‘zbekistonda 'Alpomish' dostoni qaysi og‘zaki ijod turiga mansub?",
                "answer": "Epos",
                "options": ["Epos", "Lyirika", "Doston drama", "Novella"]
            },
            {
                "question": "Qaysi gaz Yer atmosferasida eng ko‘p uchraydi?",
                "answer": "Azot",
                "options": ["Azot", "Kislorod", "Argon", "Karbonat angidrid"]
            },
            {
                "question": "SI tizimida elektr tok kuchining birliksi?",
                "answer": "Amper",
                "options": ["Amper", "Volt", "Om", "Vatt"]
            },
            {
                "question": "Chopar (courier) xizmatlarida 'ETA' qisqartmasi odatda nimani anglatadi?",
                "answer": "Taxminiy yetib kelish vaqti",
                "options": ["Taxminiy yetib kelish vaqti", "Eng tez adres", "Elektron tranzit ariza", "Yuk turi"]
            },
            {
                "question": "Qaysi musiqiy asbob torli cholg‘u hisoblanadi?",
                "answer": "Skripka",
                "options": ["Skripka", "Fleyta", "Klarnet", "Baraban"]
            },
            {
                "question": "Qog‘ozning A4 formatida uzun tomoni taxminan nechaga teng?",
                "answer": "297 mm",
                "options": ["297 mm", "210 mm", "300 mm", "250 mm"]
            },
            {
                "question": "Dunyoning eng kichik qit’asi qaysi?",
                "answer": "Avstraliya",
                "options": ["Avstraliya", "Yevropa", "Antarktida", "Afrika"]
            },
            {
                "question": "DNS qisqartmasi kompyuter tarmoqlarida nimani anglatadi?",
                "answer": "Domain Name System",
                "options": ["Domain Name System", "Data Network Service", "Digital Node Server", "Dynamic Name Source"]
            },
            {
                "question": "Fizikada 'harorat'ni o‘lchash uchun xalqaro birlik tizimidagi asosiy birlik qaysi?",
                "answer": "Kelvin",
                "options": ["Kelvin", "Selsiy", "Farengeyt", "Rankin"]
            },
            {
                "question": "Qaysi shaxs zamonaviy 'Vikipediya' loyihasining hammuassisi sifatida tanilgan?",
                "answer": "Jimmi Uels",
                "options": ["Jimmi Uels", "Mark Sukerberg", "Sergey Brin", "Lerri Peyj"]
            },
            {
                "question": "O‘zbek tilida 'q' va 'k' tovushlari farqlanishi fonetik jihatdan nimaga bog‘liq?",
                "answer": "Til orqa va til oldi artikulyatsiyasiga",
                "options": ["Til orqa va til oldi artikulyatsiyasiga", "Lab-lab artikulyatsiyasiga", "Burun rezonansiga", "Tanglay yumshoqligiga"]
            },
            {
                "question": "Fotosintez jarayonida o‘simliklar asosan qaysi gazni yutadi?",
                "answer": "Karbonat angidrid",
                "options": ["Karbonat angidrid", "Kislorod", "Azot", "Vodorod"]
            },
            {
                "question": "O‘zbekistonda milliy valyuta — so‘m qaysi yilda joriy qilingan?",
                "answer": "1994",
                "options": ["1994", "1991", "1992", "1996"]
            },
            {
                "question": "Qaysi futbol qoidasi 'o‘yindan tashqari holat'ni belgilaydi?",
                "answer": "Ofsayd",
                "options": ["Ofsayd", "Penalti", "Aut", "Korner"]
            },
            {
                "question": "Matnda yangi satrga o‘tish belgisi qanday yoziladi (ko‘p dasturlash tillarida)?",
                "answer": "\\n",
                "options": ["\\n", "\\t", "\\r", "\\b"]
            },
            {
                "question": "Qaysi ko‘paytirish natijasi to‘g‘ri: 9 × 7 = ?",
                "answer": "63",
                "options": ["63", "56", "72", "64"]
            },
            {
                "question": "Toshkentdagi Mustaqillik maydonida qaysi ramziy obida joylashgan?",
                "answer": "Baxtiyor ona va bolakay haykali",
                "options": ["Baxtiyor ona va bolakay haykali", "Temuriylar haykali", "Qaldirg‘och haykali", "Amir Temur haykali"]
            },
            {
                "question": "Qaysi yirik adabiy janr voqeaband nasriy asar hisoblanadi?",
                "answer": "Roman",
                "options": ["Roman", "G‘azal", "She’r", "Doston"]
            },
            {
                "question": "Kimyo darsida H2O formulasi qaysi moddagi ifodalaydi?",
                "answer": "Suv",
                "options": ["Suv", "Vodorod peroksid", "Metan", "Oksigen"]
            },
            {
                "question": "Qaysi so‘z imlo jihatidan to‘g‘ri yozilgan?",
                "answer": "Muammo",
                "options": ["Muammo", "Muammoh", "Muaamo", "Muama"]
            },
            {
                "question": "Qaysi shahar 'shamollar shahri' laqabiga ega?",
                "answer": "Chicago",
                "options": ["Chicago", "Seul", "Berlin", "Madrid"]
            },
            {
                "question": "Algoritm nima?",
                "answer": "Muammoni yechish uchun aniq qadamlar ketma-ketligi",
                "options": ["Muammoni yechish uchun aniq qadamlar ketma-ketligi", "Kompyuter qurilmasi", "Ma’lumotlar bazasi", "Dasturiy interfeys"]
            },
            {
                "question": "Quyosh tizimidagi eng katta sayyora qaysi?",
                "answer": "Yupiter",
                "options": ["Yupiter", "Saturn", "Yer", "Uran"]
            },
            {
                "question": "Qaysi davlat 'qahva vatani' hisoblanadi?",
                "answer": "Efiopiya",
                "options": ["Efiopiya", "Braziliya", "Kolumbiya", "Vyetnam"]
            },
            {
                "question": "Buyuk ipak yo‘lining asosiy markazlaridan biri bo‘lgan shahar?",
                "answer": "Buxoro",
                "options": ["Buxoro", "Samarqand", "Xiva", "Urganch"]
            },
            {
                "question": "Qaysi davlatning poytaxti Ulan-Bator?",
                "answer": "Mongoliya",
                "options": ["Mongoliya", "Qozog‘iston", "Qirg‘iziston", "Rossiya"]
            },
            {
                "question": "Sharq mutafakkiri Al-Xorazmiy qaysi fan asoschisi?",
                "answer": "Algebra",
                "options": ["Algebra", "Geometriya", "Astronomiya", "Kimyo"]
            },
            {
                "question": "Qaysi davlatda 'Machu-Pikchu' yodgorligi joylashgan?",
                "answer": "Peru",
                "options": ["Peru", "Meksika", "Boliviya", "Argentina"]
            },
            {
                "question": "Yer kurrasidagi eng katta chuchuk suv ko‘li qaysi?",
                "answer": "Baykal",
                "options": ["Baykal", "Viktoriya", "Tanganika", "Kaspiy"]
            },
            {
                "question": "Buyuk Britaniyaning milliy valyutasi nima?",
                "answer": "Funt sterling",
                "options": ["Funt sterling", "Yevro", "Dollar", "Frank"]
            },
            {
                "question": "O‘zbekistonning eng shimoliy viloyati qaysi?",
                "answer": "Qoraqalpog‘iston",
                "options": ["Qoraqalpog‘iston", "Surxondaryo", "Andijon", "Jizzax"]
            },
            {
                "question": "Qaysi sport turida 'Ace' atamasi ishlatiladi?",
                "answer": "Tennis",
                "options": ["Tennis", "Futbol", "Basketbol", "Boks"]
            },
            {
                "question": "Dunyodagi eng baland tog‘ cho‘qqisi qaysi ikki davlat chegarasida joylashgan?",
                "answer": "Nepal va Xitoy",
                "options": ["Nepal va Xitoy", "Hindiston va Pokiston", "Rossiya va Gruziya", "Eron va Turkiya"]
            },
            {
                "question": "Kim ilk bo‘lib Oyga qadam qo‘ygan?",
                "answer": "Nil Armstrong",
                "options": ["Nil Armstrong", "Yuriy Gagarin", "Buz Oldrin", "Germanning Titov"]
            },
            {
                "question": "Yer yuzidagi eng baland poytaxt shahar?",
                "answer": "La-Pas",
                "options": ["La-Pas", "Katmandu", "Quito", "Bogota"]
            },
            {
                "question": "Qaysi davlatda eng ko‘p orollar mavjud?",
                "answer": "Shvetsiya",
                "options": ["Shvetsiya", "Indoneziya", "Filippin", "Yaponiya"]
            },
            {
                "question": "Buyuk Ipak yo‘li asosan qaysi ikki qit’ani bog‘lagan?",
                "answer": "Osiyo va Yevropa",
                "options": ["Osiyo va Yevropa", "Osiyo va Afrika", "Yevropa va Amerika", "Osiyo va Janubiy Amerika"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan eng baland suv ombori?",
                "answer": "Tuyamo‘yin",
                "options": ["Tuyamo‘yin", "Chorvoq", "Andijon", "To‘dako‘l"]
            },
            {
                "question": "Parijdagi mashhur muzey nomi?",
                "answer": "Luvr",
                "options": ["Luvr", "Eremitaj", "Britaniya muzeyi", "Metropoliten muzeyi"]
            },
            {
                "question": "Yer yuzidagi eng katta arxipelag?",
                "answer": "Indoneziya",
                "options": ["Indoneziya", "Filippin", "Malayziya", "Gretsiya"]
            },
            {
                "question": "O‘zbekistonning milliy bog‘i nomi?",
                "answer": "Navro‘z bog‘i",
                "options": ["Navro‘z bog‘i", "Zafar bog‘i", "Amir Temur bog‘i", "Mustaqillik bog‘i"]
            },
            {
                "question": "Dunyodagi eng uzun tog‘ tizmasi?",
                "answer": "And tog‘lari",
                "options": ["And tog‘lari", "Alp", "Gimolay", "Ural"]
            },
            {
                "question": "Qaysi sport turida 'Knockout' atamasi ishlatiladi?",
                "answer": "Boks",
                "options": ["Boks", "Regbi", "Futbol", "Basketbol"]
            },
            {
                "question": "O‘zbekiston hududidagi eng qadimiy yozuv topilgan joy?",
                "answer": "Mug‘ tog‘i",
                "options": ["Mug‘ tog‘i", "Termiz", "Samarqand", "Xorazm"]
            },
            {
                "question": "Qaysi shahar 'shamollar shahri' deb ataladi?",
                "answer": "Chicago",
                "options": ["Chicago", "London", "Parij", "Berlin"]
            },
            {
                "question": "Eng mashhur yunon faylasufi?",
                "answer": "Platon",
                "options": ["Platon", "Aristotel", "Sokrat", "Pifagor"]
            },
            {
                "question": "Dunyodagi eng katta cho‘l qaysi qit’ada joylashgan?",
                "answer": "Afrika",
                "options": ["Afrika", "Osiyo", "Janubiy Amerika", "Avstraliya"]
            },
            {
                "question": "Qaysi davlatning poytaxti Seul?",
                "answer": "Janubiy Koreya",
                "options": ["Janubiy Koreya", "Xitoy", "Yaponiya", "Tayvan"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy qal’alaridan biri?",
                "answer": "Ayazqal’a",
                "options": ["Ayazqal’a", "Ark", "Qo‘yqirilgan qal’a", "Topraqqal’a"]
            },
            {
                "question": "Qaysi futbol jamoasi 'qizil iblislar' laqabi bilan mashhur?",
                "answer": "Manchester United",
                "options": ["Manchester United", "Liverpool", "Chelsea", "Arsenal"]
            },
            {
                "question": "O‘zbekistonda ishlab chiqariladigan mashhur avtomobil markasi?",
                "answer": "Chevrolet",
                "options": ["Chevrolet", "Hyundai", "Lada", "Toyota"]
            },
            {
                "question": "Yer sharidagi eng uzun daryo Janubiy Amerikada joylashgan. Bu qaysi?",
                "answer": "Amazonka",
                "options": ["Amazonka", "Nil", "Orinoko", "Parana"]
            },
            {
                "question": "O‘zbekistonning mashhur bog‘laridan biri — Amir Temur xiyoboni qayerda joylashgan?",
                "answer": "Toshkent",
                "options": ["Toshkent", "Samarqand", "Buxoro", "Namangan"]
            },
            {
                "question": "Dunyodagi eng katta hayvon qaysi turga mansub?",
                "answer": "Kit",
                "options": ["Kit", "Fil", "Akula", "Jirafa"]
            },
            {
                "question": "Qaysi davlatning milliy bayrog‘ida zarang bargi tasvirlangan?",
                "answer": "Kanada",
                "options": ["Kanada", "Avstraliya", "Shvetsiya", "Norvegiya"]
            },
            {
                "question": "Dunyodagi eng katta yarim orol?",
                "answer": "Arabiston yarim oroli",
                "options": ["Arabiston yarim oroli", "Iberiya", "Skandinaviya", "Hindiston"]
            },
            {
                "question": "O‘zbekistonning mashhur san’atkorlaridan biri?",
                "answer": "Ozodbek Nazarbekov",
                "options": ["Ozodbek Nazarbekov", "Yulduz Usmonova", "Munojot Yo‘lchiyeva", "Sevara Nazarkhan"]
            },
            {
                "question": "Qaysi shahar 'sehrli shahar' nomi bilan mashhur?",
                "answer": "Venetsiya",
                "options": ["Venetsiya", "Parij", "Rim", "Madrid"]
            },
            {
                "question": "Dunyodagi eng katta davlat maydon bo‘yicha?",
                "answer": "Rossiya",
                "options": ["Rossiya", "AQSh", "Xitoy", "Kanada"]
            },
            {
                "question": "O‘zbekistonning eng katta viloyati maydon bo‘yicha?",
                "answer": "Navoiy",
                "options": ["Navoiy", "Buxoro", "Qashqadaryo", "Surxondaryo"]
            },
            {
                "question": "Yer yuzida eng katta yarim yopiq dengiz?",
                "answer": "Qora dengiz",
                "options": ["Qora dengiz", "Oq dengiz", "O‘lik dengiz", "Aral dengizi"]
            },
            {
                "question": "Buyuk olim Pifagor qaysi fanda mashhur?",
                "answer": "Matematika",
                "options": ["Matematika", "Astronomiya", "Fizika", "Kimyo"]
            },
            {
                "question": "O‘zbekistonning eng mashhur teatrlaridan biri?",
                "answer": "Navoi opera va balet teatri",
                "options": ["Navoi opera va balet teatri", "Ilhom teatri", "Yosh tomoshabinlar teatri", "Qo‘qon teatri"]
            },
            {
                "question": "Qaysi davlatda 'Machu-Pikchu' joylashgan?",
                "answer": "Peru",
                "options": ["Peru", "Meksika", "Boliviya", "Ekvador"]
            },
            {
                "question": "Dunyodagi eng katta ichki dengiz?",
                "answer": "Kaspiy",
                "options": ["Kaspiy", "Oq dengiz", "Qora dengiz", "Aral dengizi"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Jaloliddin Manguberdi qaysi shahar yaqinida tug‘ilgan?",
                "answer": "Urgench",
                "options": ["Urgench", "Buxoro", "Andijon", "Termiz"]
            },
            {
                "question": "Dunyodagi eng katta orol?",
                "answer": "Grenlandiya",
                "options": ["Grenlandiya", "Yangi Gvineya", "Sumatra", "Madagaskar"]
            },
            {
                "question": "Yer sharidagi eng katta okean oqimi?",
                "answer": "Golfstrim",
                "options": ["Golfstrim", "Kuro-Sio", "Labrador", "Antarktika oqimi"]
            },
            {
                "question": "Buyuk olim Arximed qaysi shahar fuqarosi bo‘lgan?",
                "answer": "Sirakuza",
                "options": ["Afina", "Rim", "Sirakuza", "Sparta"]
            },
            {
                "question": "O‘zbekiston hududidagi eng qadimiy me’moriy majmualardan biri?",
                "answer": "Shohi Zinda",
                "options": ["Shohi Zinda", "Registon", "Gur Amir", "Minorai Kalon"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Pirimqul Qodirovning mashhur romani?",
                "answer": "Yulduzli tunlar",
                "options": ["Yulduzli tunlar", "Avlodlar dovoni", "Sarob", "Qiyomat"]
            },
            {
                "question": "Dunyodagi eng mashhur minoralardan biri — Pisa minorasi qaysi mamlakatda joylashgan?",
                "answer": "Italiya",
                "options": ["Italiya", "Ispaniya", "Fransiya", "Gretsiya"]
            },
            {
                "question": "Yer sharida eng ko‘p aholiga ega davlat?",
                "answer": "Xitoy",
                "options": ["Xitoy", "Hindiston", "AQSh", "Indoneziya"]
            },
            {
                "question": "O‘zbekistonning mashhur me’moriy yodgorliklaridan biri — Gur Amir maqbarasi qayerda?",
                "answer": "Samarqand",
                "options": ["Samarqand", "Buxoro", "Toshkent", "Shahrisabz"]
            },
            {
                "question": "Dunyodagi eng katta orol?",
                "answer": "Grenlandiya",
                "options": ["Skandinaviya", "Iberiya", "Arabiston", "Grenlandiya"]
            },
            {
                "question": "Qaysi olim tortishish qonunini yaratgan?",
                "answer": "Isaak Nyuton",
                "options": ["Isaak Nyuton", "Galiley", "Kopernik", "Paskal"]
            },
            {
                "question": "O‘zbekistonning eng mashhur tarixiy obidalaridan biri — Registon maydoni qayerda?",
                "answer": "Samarqand",
                "options": ["Samarqand", "Buxoro", "Xiva", "Toshkent"]
            },
            {
                "question": "Dunyoning eng kichik qit’asi?",
                "answer": "Avstraliya",
                "options": ["Avstraliya", "Yevropa", "Antarktida", "Janubiy Amerika"]
            },
            {
                "question": "O‘zbekistonning milliy teatrlaridan biri?",
                "answer": "Ilhom teatri",
                "options": ["Ilhom teatri", "Bolshoy teatr", "Yosh tomoshabinlar teatri", "Qo‘qon teatri"]
            },
            {
                "question": "Dunyodagi eng baland vulqon?",
                "answer": "Ojos del Salado",
                "options": ["Ojos del Salado", "Etna", "Fudziyama", "Kilimanjaro"]
            },
            {
                "question": "Qaysi shoir 'O‘zbekiston — Vatanim manim' she’rini yozgan?",
                "answer": "Abdulla Oripov",
                "options": ["Abdulla Oripov", "Erkin Vohidov", "Cho‘lpon", "Pirimqul Qodirov"]
            },
            {
                "question": "Yer sharidagi eng uzun tog‘ tizmalari qaysi qit’ada?",
                "answer": "Janubiy Amerika",
                "options": ["Janubiy Amerika", "Osiyo", "Afrika", "Shimoliy Amerika"]
            },
            {
                "question": "O‘zbekistonning mashhur me’moriy yodgorliklaridan biri — Ichan qal’a qayerda?",
                "answer": "Xiva",
                "options": ["Xiva", "Buxoro", "Samarqand", "Toshkent"]
            },
            {
                "question": "Dunyodagi eng mashhur opera teatrlardan biri — La Skala qayerda?",
                "answer": "Milan",
                "options": ["Milan", "Parij", "London", "Vena"]
            },
            {
                "question": "O‘zbekistonning mashhur qo‘lyozma kitoblaridan biri?",
                "answer": "Devonu lug‘otit turk",
                "options": ["Devonu lug‘otit turk", "Shohnoma", "Qutadg‘u bilig", "Al-Jome’ as-sahih"]
            },
            {
                "question": "Dunyodagi eng uzun devorlardan biri?",
                "answer": "Xitoy devori",
                "options": ["Xitoy devori", "Berlin devori", "Hadrian devori", "Bobil devori"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Jaloliddin Manguberdi qaysi daryodan kechib o‘tgan?",
                "answer": "Indus",
                "options": ["Indus", "Amudaryo", "Sirdaryo", "Zarafshon"]
            },
            {
                "question": "Dunyodagi eng katta futbol stadionlaridan biri — Marakana qayerda joylashgan?",
                "answer": "Braziliya",
                "options": ["Braziliya", "Argentina", "Meksika", "Ispaniya"]
            },
            {
                "question": "Yer sharidagi eng katta yarim yopiq ko‘rfaz?",
                "answer": "Bengal ko‘rfazi",
                "options": ["Bengal ko‘rfazi", "Meksika ko‘rfazi", "Pers ko‘rfazi", "Aden ko‘rfazi"]
            },
            {
                "question": "Dunyoning eng mashhur arxitekturalaridan biri — Kolizey qayerda?",
                "answer": "Rim",
                "options": ["Rim", "Parij", "Afina", "Madrid"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Amir Temur qabrini qayerda topish mumkin?",
                "answer": "Samarqand",
                "options": ["Samarqand", "Shahrisabz", "Toshkent", "Xiva"]
            },
            {
                "question": "Dunyodagi eng mashhur futbol klublaridan biri — Barcelona qaysi mamlakatda?",
                "answer": "Ispaniya",
                "options": ["Ispaniya", "Italiya", "Fransiya", "Angliya"]
            },
            {
                "question": "Dunyodagi eng mashhur universitetlardan biri — Oksford qayerda joylashgan?",
                "answer": "Angliya",
                "options": ["Angliya", "AQSh", "Kanada", "Avstraliya"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Al-Farg‘oniy qaysi fan sohasida mashhur?",
                "answer": "Astronomiya",
                "options": ["Astronomiya", "Matematika", "Kimyo", "Tibbiyot"]
            },
            {
                "question": "Yer sharidagi eng mashhur tog‘ dovonlaridan biri?",
                "answer": "Torong-La",
                "options": ["Torong-La", "Altay", "Pamir", "And"]
            },
            {
                "question": "O‘zbekistonning mashhur me’moriy obidalaridan biri — Minorai Kalon qayerda joylashgan?",
                "answer": "Buxoro",
                "options": ["Buxoro", "Samarqand", "Xiva", "Shahrisabz"]
            }
        ]

        quiz_7 = [
            # Diniy savollar 50ta
            {
                "question": "Qur’onda qaysi oyatda 'Dindan zo‘rlab kiritish yo‘q' deb marhamat qilingan?",
                "answer": "Baqara surasi 256-oyat",
                "options": ["Baqara 256", "Yunus 10", "Niso 34", "Maida 5"]
            },
            {
                "question": "Haj ibodatining asosiy ruknlaridan biri Arafotda turish nima deb ataladi?",
                "answer": "Wuquf",
                "options": ["Wuquf", "Sa’y", "Tavof", "Tahallul"]
            },
            {
                "question": "Qur’onda eng ko‘p zikr qilingan oy nomi?",
                "answer": "Rahmat",
                "options": ["Rahmat", "Jahannam", "Jannat", "Iymon"]
            },
            {
                "question": "Islomda oxirgi payg‘ambar kim?",
                "answer": "Muhammad (s.a.v.)",
                "options": ["Iso (a.s.)", "Muso (a.s.)", "Muhammad (s.a.v.)", "Ibrohim (a.s.)"]
            },
            {
                "question": "Payg‘ambarimizning eng ko‘p farzandlari kimdan bo‘lgan?",
                "answer": "Xadicha onamiz",
                "options": ["Oyshe", "Xadicha onamiz", "Mariya", "Sofiya"]
            },
            {
                "question": "Qur’onda birinchi bo‘lib nozil qilingan oyat qaysi suradan?",
                "answer": "Alaq surasi",
                "options": ["Alaq surasi", "Fotiha surasi", "Baqara surasi", "Ikhlos surasi"]
            },
            {
                "question": "Namozda ruku va sajda necha marta takrorlanadi?",
                "answer": "Har rak’atda bittadan",
                "options": ["Har rak’atda bittadan", "Har ikki rak’atda", "Faqat farzlarda", "Faqat sunnatda"]
            },
            {
                "question": "Payg‘ambarimizga vahiy kelganida uni dastlab kim yozib olgan?",
                "answer": "Zayd ibn Sobit",
                "options": ["Ali ibn Abu Tolib", "Umar ibn Xattob", "Zayd ibn Sobit", "Usmon ibn Affon"]
            },
            {
                "question": "Namozning oxirgi rak’atida o‘qiladigan duo nomi?",
                "answer": "Attahiyyot",
                "options": ["Attahiyyot", "Salavot", "Dua qunut", "Qiroat"]
            },
            {
                "question": "Namozda qo‘llarni ko‘tarib aytiladigan ibora nima?",
                "answer": "Takbir",
                "options": ["Tahlil", "Takbir", "Tahmid", "Tasbih"]
            },
            {
                "question": "Payg‘ambarimizning onalaridan so‘ng tarbiyalagan shaxs kim?",
                "answer": "Abu Tolib",
                "options": ["Abu Bakr", "Abu Tolib", "Hamza", "Abbos"]
            },
            {
                "question": "Payg‘ambarimizning eng yaqin sut onalari kim edi?",
                "answer": "Halima Sa’diyya",
                "options": ["Omina", "Halima Sa’diyya", "Xadicha", "Ayshe"]
            },
            {
                "question": "Musulmonlar uchun eng muqaddas kechalardan biri Laylatul-Qadr qaysi surada zikr qilingan?",
                "answer": "Qadr surasi",
                "options": ["Qadr surasi", "Baqara surasi", "Ikhlos surasi", "Niso surasi"]
            },
            {
                "question": "“Yosin” surasi Qur’onda nechanchi sura?",
                "answer": "36-surasi",
                "options": ["30-surasi", "36-surasi", "40-surasi", "50-surasi"]
            },
            {
                "question": "Zam-zam qudug‘ini kim qazib chiqargan?",
                "answer": "Abdulmuttalib",
                "options": ["Abdulmuttalib", "Abu Tolib", "Ali ibn Abu Tolib", "Hamza"]
            },
            {
                "question": "“Siyrat” so‘zi qanday ma’noni anglatadi?",
                "answer": "Payg‘ambar hayoti",
                "options": ["Qur’on tafsiri", "Payg‘ambar hayoti", "Fiqh ilmi", "Hadis ilmi"]
            },
            {
                "question": "Islomning ikkinchi ustuni nima?",
                "answer": "Namoz",
                "options": ["Ro‘za", "Zakot", "Namoz", "Haj"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ning nabiralaridan Husayn (r.a.) qayerda shahid bo‘lgan?",
                "answer": "Karbalo",
                "options": ["Makka", "Madina", "Karbalo", "Quddus"]
            },
            {
                "question": "“Ahlul-bayt” atamasi kimlarga nisbatan ishlatiladi?",
                "answer": "Payg‘ambar oilasi",
                "options": ["Sahobalar", "Payg‘ambar oilasi", "Musulmonlar", "Tabi’inlar"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ning sevimli otlari ismi nima edi?",
                "answer": "Duldul",
                "options": ["Buroq", "Duldul", "Qasva", "Sakb"]
            },
            {
                "question": "“Alhamdulillahi rabbil ‘alamin” qaysi surada keladi?",
                "answer": "Fotiha surasi",
                "options": ["Ikhlos surasi", "Fotiha surasi", "Baqara surasi", "Rahmon surasi"]
            },
            {
                "question": "Hadislar to‘plangan eng mashhur oltita kitob qanday ataladi?",
                "answer": "Kutubus Sitta",
                "options": ["Kutubus Sitta", "Tafsirlar", "Musnad", "Fiqh kitoblari"]
            },
            {
                "question": "Hadis ilmining eng mashhur to‘plovchilaridan biri kim?",
                "answer": "Imom Buxoriy",
                "options": ["Imom Termiziy", "Imom Buxoriy", "Imom Muslim", "Imom Abu Hanifa"]
            },
            {
                "question": "Payg‘ambarimizning oxirgi xutbalari qaysi hajda aytilgan?",
                "answer": "Vido haji",
                "options": ["Ummra", "Hijrat haji", "Vido haji", "Birinchi haj"]
            },
            {
                "question": "Payg‘ambarimizning eng sevimli asboblari qaysi edi?",
                "answer": "Asa",
                "options": ["Qilich", "Asa", "Bayroq", "Xanjar"]
            },
            {
                "question": "Qur’onda qaysi hayvon ismi bilan sura nomlangan?",
                "answer": "Fil",
                "options": ["Arslon", "Fil", "Bo‘ri", "Ot"]
            },
            {
                "question": "Qur’onda qaysi daryo nomi zikr qilingan?",
                "answer": "Furot",
                "options": ["Nil", "Furot", "Dajla", "Sirdaryo"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ning hijrat yo‘lida yashirangan g‘or nomi?",
                "answer": "Saur g‘ori",
                "options": ["Hiro g‘ori", "Saur g‘ori", "Hunayn g‘ori", "Uhud g‘ori"]
            },
            {
                "question": "Islom tarixida birinchi azonni aytgan sahoba kim?",
                "answer": "Bilol Habashiy",
                "options": ["Abu Hurayra", "Ali", "Bilol Habashiy", "Abu Bakr"]
            },
            {
                "question": "Musulmonlar uchun har hafta eng muhim kun qaysi?",
                "answer": "Juma kuni",
                "options": ["Payshanba", "Juma kuni", "Shanba", "Yakshanba"]
            },
            {
                "question": "Qur’onda zikr qilingan eng qadimiy payg‘ambarlardan biri?",
                "answer": "Nuh (a.s.)",
                "options": ["Nuh (a.s.)", "Muso (a.s.)", "Iso (a.s.)", "Ibrohim (a.s.)"]
            },
            {
                "question": "“Ar-Rahmon” surasida necha marta “Qaysi ne’matlaringizni inkor qilasizlar?” oyati kelgan?",
                "answer": "31 marta",
                "options": ["20 marta", "25 marta", "31 marta", "40 marta"]
            },
            {
                "question": "Qur’onda eng ko‘p zikr qilingan shahar?",
                "answer": "Makka",
                "options": ["Makka", "Madina", "Quddus", "Damashq"]
            },
            {
                "question": "Islomda “Hijoma” nimaga aytiladi?",
                "answer": "Qon chiqarib davolash",
                "options": ["Duo", "Qon chiqarib davolash", "Zikr", "Ro‘za"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ning eng yaqin safdoshlari to‘rt kishi qanday ataladi?",
                "answer": "Xulafoi roshidin",
                "options": ["Ashob", "Xulafoi roshidin", "Tabi’inlar", "Imomlar"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ning birinchi masjidlari qayerda qurilgan?",
                "answer": "Qubo masjidi",
                "options": ["Masjidul-Haram", "Qubo masjidi", "Masjidun Nabaviy", "Masjidul-Aqso"]
            },
            {
                "question": "“Asr” surasi nechta oyatdan iborat?",
                "answer": "3",
                "options": ["2", "3", "4", "5"]
            },
            {
                "question": "Qur’onda zikr qilingan jannatlardan biri nomi?",
                "answer": "Adn bog‘i",
                "options": ["Firdaus", "Adn bog‘i", "Rayhon", "Sidra"]
            },
            {
                "question": "Qur’onda zikr qilingan do‘zax nomlaridan biri?",
                "answer": "Jahannam",
                "options": ["Jahannam", "Nar", "Saqor", "Hutamah"]
            },
            {
                "question": "Namozning vitir qismida maxsus duo nima deb ataladi?",
                "answer": "Qunut duosi",
                "options": ["Qunut duosi", "Attahiyyot", "Salavot", "Tasbih"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ning hijratdan keyingi ilk jangi?",
                "answer": "Badr jangi",
                "options": ["Uhud jangi", "Badr jangi", "Xandaq jangi", "Hunayn jangi"]
            },
            {
                "question": "Uhud jangida Payg‘ambarimizning tishlari singanini eshitamiz. Qaysi jang edi bu?",
                "answer": "Uhud jangi",
                "options": ["Badr jangi", "Uhud jangi", "Xandaq jangi", "Hunayn jangi"]
            },
            {
                "question": "Islomda odamni poklash uchun qilinadigan tozalash nima deb ataladi?",
                "answer": "G‘usl",
                "options": ["Tahorat", "Tayammum", "G‘usl", "Poklanish"]
            },
            {
                "question": "Tayammum qachon qilinadi?",
                "answer": "Suv topilmaganda",
                "options": ["Suv topilmaganda", "Bayramda", "Namozdan keyin", "Hajda"]
            },
            {
                "question": "Payg‘ambarimizning tug‘ilgan kuni qanday ataladi?",
                "answer": "Mavlud",
                "options": ["Navro‘z", "Mavlud", "Hijrat", "Laylatul Qadr"]
            },
            {
                "question": "Payg‘ambarimizning eng mashhur qilichlaridan biri?",
                "answer": "Zulfikor",
                "options": ["Zulfikor", "Qilichul haq", "Samsom", "Duldul"]
            },
            {
                "question": "Payg‘ambarimizning eng mashhur bayroqlari qaysi rangda bo‘lgan?",
                "answer": "Qora",
                "options": ["Oq", "Qora", "Yashil", "Qizil"]
            },
            {
                "question": "Payg‘ambarimizning jiyani, keyinchalik to‘rtinchi xalifa kim edi?",
                "answer": "Ali ibn Abu Tolib",
                "options": ["Ali ibn Abu Tolib", "Umar ibn Xattob", "Usmon ibn Affon", "Abu Bakr"]
            },
            {
                "question": "Qur’onda necha marta “Bismillahir rohmanir rohiym” so‘zi keladi?",
                "answer": "114 marta",
                "options": ["112 marta", "113 marta", "114 marta", "115 marta"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur dengiz nomi?",
                "answer": "Qizil dengiz",
                "options": ["Qora dengiz", "Qizil dengiz", "O‘lik dengiz", "Furot"]
            },
            # Fanga oid savollar 100ta
            {
                "question": "Yer yuzida eng baland tog‘ tizmasi qaysi?",
                "answer": "Gimolay",
                "options": ["Alp", "And", "Gimolay", "Kavkaz"]
            },
            {
                "question": "Buyuk Ipak yo‘li O‘zbekistondan qaysi davlatga chiqib ketgan?",
                "answer": "Xitoy",
                "options": ["Turkiya", "Rossiya", "Xitoy", "Eron"]
            },
            {
                "question": "Qaysi sport turi O‘zbekistonning milliy sporti hisoblanadi?",
                "answer": "Kurash",
                "options": ["Kurash", "Boks", "Futbol", "Tennis"]
            },
            {
                "question": "Dunyodagi eng katta qit’a?",
                "answer": "Osiyo",
                "options": ["Osiyo", "Afrika", "Yevropa", "Amerika"]
            },
            {
                "question": "O‘zbekiston davlat madhiyasi muallifi kim?",
                "answer": "Abdulla Oripov",
                "options": ["Erkin Vohidov", "Cho‘lpon", "Abdulla Oripov", "Oybek"]
            },
            {
                "question": "O‘zbekiston poytaxti qaysi shaharda joylashgan?",
                "answer": "Toshkent",
                "options": ["Toshkent", "Samarqand", "Buxoro", "Andijon"]
            },
            {
                "question": "Yer yuzidagi eng uzun daryo?",
                "answer": "Nil",
                "options": ["Nil", "Amazonka", "Yanszi", "Missisipi"]
            },
            {
                "question": "Buyuk yozuvchi Alisher Navoiy nechta tilni bilgan?",
                "answer": "3 dan ortiq",
                "options": ["2", "3 dan ortiq", "1", "4"]
            },
            {
                "question": "O‘zbekiston Respublikasi davlat bayrog‘ida nechta yulduz bor?",
                "answer": "12",
                "options": ["12", "10", "11", "14"]
            },
            {
                "question": "Yer yuzida eng katta cho‘l?",
                "answer": "Sahroi Kabir",
                "options": ["Sahroi Kabir", "Atakama", "Gobi", "Karakum"]
            },
            {
                "question": "Shaxmat o‘yinida eng kuchli dona qaysi?",
                "answer": "Ferz",
                "options": ["Shah", "Ferz", "Ot", "Ladya"]
            },
            {
                "question": "O‘zbekiston Respublikasi mustaqillik kuni qachon?",
                "answer": "1-sentyabr",
                "options": ["8-dekabr", "1-sentyabr", "21-mart", "9-may"]
            },
            {
                "question": "Yer sharidagi eng katta okean?",
                "answer": "Tinch okeani",
                "options": ["Tinch okeani", "Atlantika okeani", "Hind okeani", "Shimoliy Muz okeani"]
            },
            {
                "question": "Buyuk yozuvchi Abdulla Qodiriy mashhur asari?",
                "answer": "O‘tkan kunlar",
                "options": ["O‘tkan kunlar", "Kecha va kunduz", "Dunyoning ishlari", "Qiyomat"]
            },
            {
                "question": "Qaysi sport turida Jahon chempionati eng ko‘p tomoshabin yig‘adi?",
                "answer": "Futbol",
                "options": ["Futbol", "Basketbol", "Shaxmat", "Boks"]
            },
            {
                "question": "Yer yuzidagi eng baland cho‘qqi?",
                "answer": "Everest",
                "options": ["Everest", "Elbrus", "K2", "Montblan"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat tili?",
                "answer": "O‘zbek tili",
                "options": ["Rus tili", "O‘zbek tili", "Qoraqalpoq tili", "Ingliz tili"]
            },
            {
                "question": "Qaysi sport turida Ronaldo mashhur bo‘lgan?",
                "answer": "Futbol",
                "options": ["Futbol", "Basketbol", "Regbi", "Boks"]
            },
            {
                "question": "Buyuk yozuvchi Chingiz Aytmatovning asari?",
                "answer": "Qiyomat",
                "options": ["Qiyomat", "Shohnoma", "Kecha va kunduz", "Urush va tinchlik"]
            },
            {
                "question": "Yer sharida eng katta orol?",
                "answer": "Grenlandiya",
                "options": ["Grenlandiya", "Madagaskar", "Sumatra", "Yangi Gvineya"]
            },
            {
                "question": "O‘zbekiston davlat gerbida qanotini yozgan qush qaysi?",
                "answer": "Humo qushi",
                "options": ["Humo qushi", "Lochin", "Qaldirg‘och", "Burgut"]
            },
            {
                "question": "Buyuk yozuvchi O‘tkir Hoshimov mashhur asari?",
                "answer": "Dunyoning ishlari",
                "options": ["Dunyoning ishlari", "Yulduzli tunlar", "Qiyomat", "Kecha va kunduz"]
            },
            {
                "question": "Yer sharida eng katta yarim orol?",
                "answer": "Arabiston yarim oroli",
                "options": ["Arabiston yarim oroli", "Skandinaviya", "Iberiya", "Hindiston yarim oroli"]
            },
            {
                "question": "Buyuk yozuvchi Firdavsiyning mashhur asari?",
                "answer": "Shohnoma",
                "options": ["Shohnoma", "Xamsa", "Devonu lug‘otit turk", "Qutadg‘u bilig"]
            },
            {
                "question": "O‘zbekistonning eng katta shahri?",
                "answer": "Toshkent",
                "options": ["Samarqand", "Andijon", "Toshkent", "Namangan"]
            },
            {
                "question": "Yer sharida eng baland sharshara?",
                "answer": "Anxel",
                "options": ["Niagara", "Victoria", "Iguasu", "Anxel"]
            },
            {
                "question": "Buyuk yozuvchi Pirimqul Qodirov mashhur asari?",
                "answer": "Yulduzli tunlar",
                "options": ["Yulduzli tunlar", "Kecha va kunduz", "Shohnoma", "Qiyomat"]
            },
            {
                "question": "O‘zbekiston hududida nechta viloyat bor?",
                "answer": "12 + Qoraqalpog‘iston",
                "options": ["11", "12 + Qoraqalpog‘iston", "13", "14"]
            },
            {
                "question": "Yer sharida eng baland tog‘ cho‘qqisi?",
                "answer": "Everest",
                "options": ["Everest", "Elbrus", "Montblan", "Hazrati Sulton"]
            },
            {
                "question": "Buyuk yozuvchi Tohir Malik mashhur asari?",
                "answer": "Shaytanat",
                "options": ["Shaytanat", "Qiyomat", "Dunyoning ishlari", "O‘tkan kunlar"]
            },
            {
                "question": "O‘zbekiston Respublikasining Konstitutsiya kuni qachon?",
                "answer": "8-dekabr",
                "options": ["8-dekabr", "1-sentyabr", "21-mart", "9-may"]
            },
            {
                "question": "Yer sharida eng katta qit’a?",
                "answer": "Osiyo",
                "options": ["Afrika", "Yevropa", "Osiyo", "Amerika"]
            },
            {
                "question": "Buyuk yozuvchi Erkin Vohidov mashhur asari?",
                "answer": "Ruhlar isyoni",
                "options": ["Ruhlar isyoni", "Shohnoma", "O‘tkan kunlar", "Qutadg‘u bilig"]
            },
            {
                "question": "Buyuk yozuvchi Cho‘lpon mashhur asari?",
                "answer": "Kecha va kunduz",
                "options": ["Kecha va kunduz", "Shohnoma", "Xamsa", "Yulduzli tunlar"]
            },
            {
                "question": "O‘zbekiston davlat madhiyasi musiqasini kim bastalagan?",
                "answer": "Mutal Burhonov",
                "options": ["Mutal Burhonov", "Mansur Toshmatov", "Ortiq Otajonov", "Botir Zokirov"]
            },
            {
                "question": "Yer sharidagi eng katta ichki suv havzasi?",
                "answer": "Kaspiy dengizi",
                "options": ["Oq dengiz", "Qora dengiz", "Kaspiy dengizi", "Aral dengizi"]
            },
            {
                "question": "Buyuk yozuvchi O‘tkir Hoshimovning yana bir mashhur asari?",
                "answer": "Ikki eshik orasi",
                "options": ["Ikki eshik orasi", "Dunyoning ishlari", "Shaytanat", "Qiyomat"]
            },
            {
                "question": "O‘zbekiston davlat gerbidagi bug‘doy nimani bildiradi?",
                "answer": "Hosildorlik va farovonlik",
                "options": ["Hosildorlik va farovonlik", "Barqarorlik", "Ona tabiat", "Adolat"]
            },
            {
                "question": "Yer sharidagi eng sovuq qit’a?",
                "answer": "Antarktida",
                "options": ["Antarktida", "Osiyo", "Yevropa", "Afrika"]
            },
            {
                "question": "Buyuk yozuvchi Abdulla Qahhor mashhur asari?",
                "answer": "Sarob",
                "options": ["Sarob", "Shohnoma", "O‘tkan kunlar", "Kecha va kunduz"]
            },
            {
                "question": "Yer sharidagi eng katta orollar arxipelagi?",
                "answer": "Indoneziya",
                "options": ["Indoneziya", "Filippin", "Maldiv", "Shvetsiya"]
            },
            {
                "question": "Yer sharidagi eng chuqur ko‘l?",
                "answer": "Baykal",
                "options": ["Baykal", "Tanganika", "Viktoriya", "Kaspiy"]
            },
            {
                "question": "Buyuk yozuvchi Lev Tolstoy qaysi asarni yozgan?",
                "answer": "Anna Karenina",
                "options": ["Urush va tinchlik", "Anna Karenina", "Jinoyat va jazo", "Qariya va dengiz"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan eng qadimiy shahar?",
                "answer": "Samarqand",
                "options": ["Samarqand", "Buxoro", "Xiva", "Termiz"]
            },
            {
                "question": "Buyuk yozuvchi Dostoyevskiyning mashhur asari?",
                "answer": "Aka-uka Karamazovlar",
                "options": ["Aka-uka Karamazovlar", "O‘tkan kunlar", "Shohnoma", "Yulduzli tunlar"]
            },
            {
                "question": "O‘zbekistonning eng katta shaharlardan keyingi ikkinchi shahri?",
                "answer": "Samarqand",
                "options": ["Samarqand", "Andijon", "Buxoro", "Namangan"]
            },
            {
                "question": "Yer sharidagi eng baland tog‘ cho‘qqisi qaysi davlatda joylashgan?",
                "answer": "Nepal",
                "options": ["Nepal", "Hindiston", "Xitoy", "Butan"]
            },
            {
                "question": "Buyuk yozuvchi Cho‘lponning ismi aslida qanday bo‘lgan?",
                "answer": "Abdulhamid Sulaymon o‘g‘li",
                "options": ["Abdulhamid Sulaymon o‘g‘li", "Abdulla Qodiriy", "Erkin Vohidov", "O‘tkir Hoshimov"]
            },
            {
                "question": "O‘zbekiston hududidagi eng baland tog‘ tizmasi?",
                "answer": "Tyan-Shan",
                "options": ["Tyan-Shan", "Pamir", "Altay", "Ural"]
            },
            {
                "question": "Yer sharidagi eng mashhur orollardan biri — Madagaskar qaysi okeanda joylashgan?",
                "answer": "Hind okeani",
                "options": ["Hind okeani", "Tinch okeani", "Atlantika okeani", "Shimoliy muz okeani"]
            },
            {
                "question": "Buyuk yozuvchi Abdulla Qodiriyning asl ismi?",
                "answer": "Abdulla Qodiriy Yoqub o‘g‘li",
                "options": ["Abdulla Qodiriy Yoqub o‘g‘li", "Abdulla Qahhor", "Cho‘lpon", "Abdulla Oripov"]
            },
            {
                "question": "O‘zbekistonning eng katta tog‘ konlaridan biri?",
                "answer": "Olmaliq",
                "options": ["Olmaliq", "Muruntov", "Sho‘rtan", "Qandim"]
            },
            {
                "question": "Yer sharida eng katta yarim yopiq dengiz?",
                "answer": "Qora dengiz",
                "options": ["Qora dengiz", "Oq dengiz", "O‘lik dengiz", "Kaspiy"]
            },
            {
                "question": "Buyuk yozuvchi Pushkinning mashhur asari?",
                "answer": "Yevgeniy Onegin",
                "options": ["Yevgeniy Onegin", "Shohnoma", "Kecha va kunduz", "Urush va tinchlik"]
            },
            {
                "question": "Yer sharidagi eng uzun devor?",
                "answer": "Xitoy devori",
                "options": ["Xitoy devori", "Berlin devori", "Hadrian devori", "Bobil devori"]
            },
            {
                "question": "Buyuk yozuvchi Ernest Xeminguey mashhur asari?",
                "answer": "Qariya va dengiz",
                "options": ["Qariya va dengiz", "Jarayon", "Sariq devni minib", "Shohnoma"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat tili qaysi?",
                "answer": "O‘zbek tili",
                "options": ["O‘zbek tili", "Rus tili", "Ingliz tili", "Qoraqalpoq tili"]
            },
            {
                "question": "Buyuk yozuvchi Navoiy tug‘ilgan yil?",
                "answer": "1441",
                "options": ["1441", "1451", "1430", "1420"]
            },
            {
                "question": "O‘zbekiston Respublikasining pul birligi?",
                "answer": "So‘m",
                "options": ["So‘m", "Rubl", "Tiyin", "Dollar"]
            },
            {
                "question": "Buyuk yozuvchi Pirimqul Qodirov qaysi asarni yozgan?",
                "answer": "Avlodlar dovoni",
                "options": ["Avlodlar dovoni", "Yulduzli tunlar", "Sarob", "Shaytanat"]
            },
            {
                "question": "Yer sharidagi eng uzun daryo Osiyoda joylashgan. U qaysi?",
                "answer": "Yanszi",
                "options": ["Yanszi", "Amudaryo", "Ganga", "Sirdaryo"]
            },
            {
                "question": "Buyuk yozuvchi Firdavsiy qaysi asar muallifi?",
                "answer": "Shohnoma",
                "options": ["Shohnoma", "Devonu lug‘otit turk", "Xamsa", "O‘tkan kunlar"]
            },
            {
                "question": "O‘zbekiston Respublikasi ramzlaridan biri?",
                "answer": "Davlat bayrog‘i",
                "options": ["Davlat bayrog‘i", "Qur’on", "Shohnoma", "Davlat kutubxonasi"]
            },
            {
                "question": "Buyuk yozuvchi Shakespeare mashhur asari?",
                "answer": "Otello",
                "options": ["Otello", "Hamlet", "Shohnoma", "Urush va tinchlik"]
            },
            {
                "question": "O‘zbekiston Respublikasida mustaqillik kuni qachon nishonlanadi?",
                "answer": "1-sentyabr",
                "options": ["8-dekabr", "9-may", "1-sentyabr", "21-mart"]
            },
            {
                "question": "Yer sharidagi eng katta ichki ko‘l?",
                "answer": "Kaspiy",
                "options": ["Kaspiy", "Baykal", "Viktoriya", "Tanganika"]
            },
            {
                "question": "Buyuk yozuvchi Erkin Vohidovning mashhur she’riy turkumi?",
                "answer": "Tong nafasi",
                "options": ["Tong nafasi", "Oltin vodiydan", "Sarob", "Shohnoma"]
            },
            {
                "question": "O‘zbekiston hududidagi eng yirik daryo?",
                "answer": "Amudaryo",
                "options": ["Amudaryo", "Sirdaryo", "Zarafshon", "Chirchiq"]
            },
            {
                "question": "Buyuk yozuvchi Abdulla Qahhor mashhur hikoyasi?",
                "answer": "Anor",
                "options": ["Anor", "Sarob", "Shohnoma", "Dunyoning ishlari"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat madhiyasi muallifi?",
                "answer": "Abdulla Oripov",
                "options": ["Mutal Burhonov", "Cho‘lpon", "Abdulla Oripov", "Erkin Vohidov"]
            },
            {
                "question": "Yer sharida eng baland tog‘ qaysi davlatlarda joylashgan?",
                "answer": "Nepal va Xitoy",
                "options": ["Hindiston", "Butan", "Nepal va Xitoy", "Pokiston"]
            },
            {
                "question": "Buyuk yozuvchi Navoiy mashhur asarlari turkumi?",
                "answer": "Xamsa",
                "options": ["Xamsa", "Shohnoma", "Qutadg‘u bilig", "Devonu lug‘otit turk"]
            },
            {
                "question": "O‘zbekiston Respublikasining milliy valyutasi?",
                "answer": "So‘m",
                "options": ["So‘m", "Tiyin", "Rubl", "Dollar"]
            },
            {
                "question": "Yer sharidagi eng katta sharshara?",
                "answer": "Anxel",
                "options": ["Viktoriya", "Niagara", "Anxel", "Angel"]
            },
            {
                "question": "O‘zbekiston Respublikasining milliy sporti?",
                "answer": "Kurash",
                "options": ["Kurash", "Futbol", "Boks", "Shaxmat"]
            },
            {
                "question": "Yer sharidagi eng qadimiy yozuv turi?",
                "answer": "Mixxat",
                "options": ["Mixxat", "Lotin", "Arab yozuvi", "Sanskrit"]
            },
            {
                "question": "Buyuk yozuvchi Cho‘lpon mashhur she’riy turkumi?",
                "answer": "Buloqlar",
                "options": ["Buloqlar", "Sarob", "Tong nafasi", "Shohnoma"]
            },
            {
                "question": "O‘zbekiston Respublikasi davlat gerbida nechta yulduz aks etgan?",
                "answer": "12",
                "options": ["10", "11", "12", "14"]
            },
            {
                "question": "Yer sharidagi eng baland platosi?",
                "answer": "Tibet",
                "options": ["Pamir", "And", "Altay", "Tibet"]
            },
            {
                "question": "O‘zbekiston Respublikasining milliy ramzlaridan biri?",
                "answer": "Gerb",
                "options": ["Gerb", "Qur’on", "Shohnoma", "Bayt"]
            },
            {
                "question": "O‘zbekiston Respublikasining milliy valyutasi joriy etilgan yil?",
                "answer": "1994-yil",
                "options": ["1994-yil", "1991-yil", "1992-yil", "1993-yil"]
            },
            {
                "question": "Yer sharidagi eng katta ichki dengiz?",
                "answer": "Qora dengiz",
                "options": ["Qora dengiz", "Adriatika", "Oq dengiz", "O‘lik dengiz"]
            },
            {
                "question": "Buyuk yozuvchi Erkin Vohidov tug‘ilgan yili?",
                "answer": "1936-yil",
                "options": ["1936-yil", "1940-yil", "1930-yil", "1945-yil"]
            },
            {
                "question": "O‘zbekistonning milliy taomlaridan biri?",
                "answer": "Palov",
                "options": ["Palov", "Somsa", "Lag‘mon", "Norin"]
            },
            {
                "question": "Yer sharidagi eng baland binolardan biri?",
                "answer": "Burj Xalifa",
                "options": ["Burj Xalifa", "Eiffel minorasi", "CN Tower", "Big Ben"]
            },
            {
                "question": "Buyuk yozuvchi Abdulla Oripov mashhur she’riy asari?",
                "answer": "O‘zbekiston — Vatanim manim",
                "options": ["O‘zbekiston — Vatanim manim", "Tong nafasi", "Shohnoma", "Sarob"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat madhiyasi qachon qabul qilingan?",
                "answer": "1992-yil",
                "options": ["1992-yil", "1991-yil", "1993-yil", "1994-yil"]
            },
            {
                "question": "Buyuk yozuvchi Abdulla Qahhor mashhur qissasi?",
                "answer": "O‘g‘ri",
                "options": ["O‘g‘ri", "Sarob", "Anor", "Shohnoma"]
            },
            {
                "question": "O‘zbekistonning eng yirik oltin koni?",
                "answer": "Muruntov",
                "options": ["Muruntov", "Olmaliq", "Zarafshon", "Qizilqum"]
            },
            {
                "question": "Yer sharidagi eng mashhur sharsharalardan biri?",
                "answer": "Niagara",
                "options": ["Niagara", "Anxel", "Victoria", "Iguasu"]
            },
            {
                "question": "Buyuk yozuvchi O‘tkir Hoshimovning mashhur qissasi?",
                "answer": "Ikki eshik orasi",
                "options": ["Ikki eshik orasi", "Dunyoning ishlari", "Shohnoma", "Kecha va kunduz"]
            },
            {
                "question": "O‘zbekiston Respublikasining Konstitutsiyasi nechta bo‘limdan iborat?",
                "answer": "6",
                "options": ["6", "5", "7", "8"]
            },
            {
                "question": "Yer sharida eng baland tog‘ dovoni?",
                "answer": "Thorong La",
                "options": ["Thorong La", "And", "Altay", "Tyan-Shan"]
            },
            {
                "question": "O‘zbekiston hududidan oqib o‘tuvchi eng yirik daryo?",
                "answer": "Amudaryo",
                "options": ["Amudaryo", "Sirdaryo", "Zarafshon", "Chirchiq"]
            },
            {
                "question": "Yer sharidagi eng katta orollar davlati?",
                "answer": "Indoneziya",
                "options": ["Indoneziya", "Filippin", "Yaponiya", "Madagaskar"]
            },
            {
                "question": "Buyuk yozuvchi Alisher Navoiy qaysi shaharda tug‘ilgan?",
                "answer": "Xirot",
                "options": ["Xirot", "Buxoro", "Samarqand", "Toshkent"]
            },
            {
                "question": "O‘zbekiston davlat gerbidagi Humo qushi nimani bildiradi?",
                "answer": "Erkinlik",
                "options": ["Erkinlik", "Adolat", "Hosildorlik", "Ona tabiat"]
            },
            {
                "question": "Yer sharidagi eng uzun daryo Afrikada joylashgan. Bu qaysi?",
                "answer": "Nil",
                "options": ["Nil", "Amazonka", "Yanszi", "Ganga"]
            },
            {
                "question": "Buyuk yozuvchi Pirimqul Qodirov mashhur romani?",
                "answer": "Avlodlar dovoni",
                "options": ["Avlodlar dovoni", "Yulduzli tunlar", "Sarob", "Shohnoma"]
            },
            {
                "question": "O‘zbekiston Respublikasida Konstitutsiya kuni qachon?",
                "answer": "8-dekabr",
                "options": ["8-dekabr", "1-sentyabr", "21-mart", "9-may"]
            }
        ]
    
        quiz_8 = [
            # Diniy savollar 50ta
            {
                "question": "Qur’onda zikr qilingan eng mashhur do‘zax darvozalari nechta?",
                "answer": "7",
                "options": ["7", "6", "8", "5"]
            },
            {
                "question": "Qur’onda suralarning eng ko‘p oyatga ega bo‘lgani qaysi?",
                "answer": "Baqara surasi",
                "options": ["Baqara surasi", "Niso surasi", "A’rof surasi", "Yusuf surasi"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ning sevimli taomlaridan biri?",
                "answer": "Asal",
                "options": ["Xurmo", "Asal", "Sut", "Non"]
            },
            {
                "question": "Hijratdan keyin Madinada qurilgan eng mashhur masjid qaysi?",
                "answer": "Masjidun Nabaviy",
                "options": ["Masjidun Nabaviy", "Masjid Qubo", "Masjid Aqso", "Masjid Qiblatayn"]
            },
            {
                "question": "Islom tarixida birinchi yozilgan sahifa nima deb ataladi?",
                "answer": "Suhufa",
                "options": ["Musnad", "Suhufa", "Kitob", "Sahifa"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) onalari qaysi qabiladan edi?",
                "answer": "Banu Zuhra",
                "options": ["Banu Zuhra", "Quraysh", "Banu Hashim", "Banu Taim"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.) tug‘ilgan yil 'Fil yili' deb atalishiga sabab nima?",
                "answer": "Abraha fil qo‘shini Ka’baga yurishi",
                "options": ["Abraha fil qo‘shini Ka’baga yurishi", "Makka zilzilasi", "Islom tarqalishi", "Hijrat boshlanishi"]
            },
            {
                "question": "Qur’onda zikr qilingan eng qisqa oyat qaysi?",
                "answer": "Muddaasir 4-oyat",
                "options": ["Ikhlos 1-oyat", "Muddaasir 4-oyat", "Fotiha 7-oyat", "Nas 6-oyat"]
            },
            {
                "question": "Payg‘ambarimizga (s.a.v.) yaqin bo‘lgan va o‘z qo‘llarida tarbiyalangan sahoba kim?",
                "answer": "Zayd ibn Horisa",
                "options": ["Zayd ibn Horisa", "Usoma ibn Zayd", "Ali ibn Abu Tolib", "Bilol"]
            },
            {
                "question": "Payg‘ambarimizga (s.a.v.) ilk bo‘lib namozni o‘rgatgan farishta kim?",
                "answer": "Jabroil (a.s.)",
                "options": ["Jabroil (a.s.)", "Mikoil (a.s.)", "Isrofil (a.s.)", "Azroil (a.s.)"]
            },
            {
                "question": "Islomda 'Ahlus-suffa' kimlar edi?",
                "answer": "Masjidi Nabaviyda yashagan sahobalar",
                "options": ["Masjidi Nabaviyda yashagan sahobalar", "Ashoblar", "To‘rt xalifa", "Ansorlar"]
            },
            {
                "question": "Qur’onda zikr qilingan eng uzun so‘z qaysi?",
                "answer": "Fa-asqaynākumūhu",
                "options": ["Fa-asqaynākumūhu", "Al-mutasābiqūna", "Yastabshirūna", "Al-mustaqīm"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ning bobolari Abdulmuttalibning ismi aslida nima edi?",
                "answer": "Shayba",
                "options": ["Shayba", "Qosim", "Nofe", "Haris"]
            },
            {
                "question": "Qur’onda suralar necha xil guruhga bo‘linadi?",
                "answer": "Makkiy va Madaniy",
                "options": ["Makkiy va Madaniy", "Katta va kichik", "Uzoq va qisqa", "Arabiy va Ajamiy"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ning hijratdan keyin qaysi yahudiy qabilalari bilan sulh tuzilgan?",
                "answer": "Banu Qurayza, Banu Nazir, Banu Qaynuqo’",
                "options": ["Banu Qurayza, Banu Nazir, Banu Qaynuqo’", "Banu Taim, Banu Zuhra", "Banu Hashim, Banu Umayya", "Banu Tamim, Banu Sulaym"]
            },
            {
                "question": "Islom tarixidagi birinchi muallim kim edi?",
                "answer": "Mus’ab ibn Umayr",
                "options": ["Mus’ab ibn Umayr", "Zayd ibn Sobit", "Ibn Mas’ud", "Ali ibn Abu Tolib"]
            },
            {
                "question": "Badr jangida musulmonlarning soni nechta edi?",
                "answer": "313",
                "options": ["313", "500", "1000", "300"]
            },
            {
                "question": "Qur’onda eng ko‘p zikr qilingan qush nomi?",
                "answer": "Hudhud",
                "options": ["Hudhud", "Tovus", "Qaldirg‘och", "Bulbul"]
            },
            {
                "question": "Qur’onda eng mashhur duo oyati qaysi surada?",
                "answer": "Baqara 201",
                "options": ["Baqara 201", "Yunus 85", "Niso 100", "Maida 90"]
            },
            {
                "question": "Payg‘ambarimizga (s.a.v.) qarshi bo‘lgan amakilardan biri kim edi?",
                "answer": "Abu Lahab",
                "options": ["Abu Lahab", "Hamza", "Abbos", "Abu Tolib"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) eng mashhur bayroqlari nomi?",
                "answer": "Uqob",
                "options": ["Uqob", "Zulfikor", "Rayat", "Saqr"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur tog‘ nomi?",
                "answer": "Tur tog‘i",
                "options": ["Tur tog‘i", "Uhud tog‘i", "Arafot tog‘i", "Safa"]
            },
            {
                "question": "Uhud jangida musulmonlarga qarshi nechta mushrik qatnashgan?",
                "answer": "3000",
                "options": ["1000", "2000", "3000", "4000"]
            },
            {
                "question": "Islom tarixida birinchi yozilgan konstitutsiya qaysi?",
                "answer": "Madinai Munavvara Konstitutsiyasi",
                "options": ["Madinai Munavvara Konstitutsiyasi", "Hijoz Qonuni", "Badr Qoidalari", "Uhud Nizomi"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ga o‘z jonini fido qilgan yosh sahoba kim?",
                "answer": "Ali ibn Abu Tolib",
                "options": ["Ali ibn Abu Tolib", "Usmon ibn Affon", "Umar ibn Xattob", "Abu Bakr"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur ichimlik?",
                "answer": "Sharob (jannatdagi)",
                "options": ["Sharob (jannatdagi)", "Suv", "Asal", "Sut"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ga berilgan eng mashhur laqab?",
                "answer": "Al-Amin",
                "options": ["Al-Amin", "As-Siddiq", "Al-Faruq", "Zunnurayn"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur daraxt?",
                "answer": "Zaytun",
                "options": ["Zaytun", "Anjir", "Xurmo", "Uzum"]
            },
            {
                "question": "Musulmonlarga hijrat qilish farz bo‘lgan joy?",
                "answer": "Madina",
                "options": ["Madina", "Makka", "Quddus", "Badr"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur daryo nomi?",
                "answer": "Nil",
                "options": ["Nil", "Furot", "Dajla", "Zamzam"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.) birinchi g‘azotda qatnashganmi?",
                "answer": "Ha",
                "options": ["Ha", "Yo‘q", "Faqat keyin", "Bilmaymiz"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur baliq nomi?",
                "answer": "Nun (baliq)",
                "options": ["Nun (baliq)", "Qizil baliq", "Oq baliq", "Dengiz baliq"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur shamol?",
                "answer": "Sarsar",
                "options": ["Sarsar", "Samum", "Sabaa", "Hurof"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur yulduz?",
                "answer": "Shuro",
                "options": ["Shuro", "Zuhra", "Tug‘ro", "Parvoz"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) eng sevimli qizi kim edi?",
                "answer": "Fotima",
                "options": ["Ruqayya", "Ummu Kulsum", "Zaynab", "Fotima"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur qush hikoyasi qaysi surada?",
                "answer": "Namli surasi (Sulaymon va Hudhud)",
                "options": ["Namli surasi (Sulaymon va Hudhud)", "Yusuf surasi", "Maryam surasi", "Tavba surasi"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur sayohat voqeasi qaysi surada?",
                "answer": "Isro surasi",
                "options": ["Isro surasi", "Rahmon surasi", "Niso surasi", "Yasin surasi"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ga birinchi yozuv vositasi sifatida qaysi narsa ishlatilgan?",
                "answer": "Qalam",
                "options": ["Qalam", "To‘qmoq", "Taxta", "Suyak"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur ziyorat joyi?",
                "answer": "Ka’ba",
                "options": ["Ka’ba", "Quddus", "Uhud", "Arafot"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) eng mashhur jang taktikasi qaysi jangda qo‘llangan?",
                "answer": "Xandaq jangi",
                "options": ["Uhud jangi", "Badr jangi", "Xandaq jangi", "Hunayn jangi"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur so‘zlardan biri?",
                "answer": "Taqvo",
                "options": ["Taqvo", "Duo", "Ilm", "Sabr"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur meva?",
                "answer": "Anjir",
                "options": ["Anjir", "Uzum", "Xurmo", "Zaytun"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) oxirgi va’zlari qaysi voqeada bo‘lgan?",
                "answer": "Vido haji",
                "options": ["Uhud jangi", "Vido haji", "Hijrat", "Badr jangi"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur ko‘l?",
                "answer": "Kavsar",
                "options": ["Kavsar", "Tiberiya", "O‘lik dengiz", "Firdaus"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur qavm qaysi?",
                "answer": "Ad qavmi",
                "options": ["Ad qavmi", "Samud qavmi", "Quraysh qavmi", "Qavmi Lut"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur qabila?",
                "answer": "Quraysh",
                "options": ["Quraysh", "Banu Hashim", "Ansorlar", "Muhajirlar"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur jannat darvozasi nomi?",
                "answer": "Rayyon",
                "options": ["Rayyon", "Firdaus", "Adn", "Na’im"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur duo?",
                "answer": "Rabbana atina fid-dunya hasanah",
                "options": ["Rabbana atina fid-dunya hasanah", "La ilaha illalloh", "Bismillah", "Subhanalloh"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.) sahobalarining hijratdan oldingi yashash joylari qanday atalardi?",
                "answer": "Makka",
                "options": ["Makka", "Madina", "Quddus", "Toyĭf"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur payg‘ambar duosi qaysi?",
                "answer": "Nuh (a.s.)ning duosi",
                "options": ["Nuh (a.s.)ning duosi", "Ibrohim (a.s.)ning duosi", "Muso (a.s.)ning duosi", "Iso (a.s.)ning duosi"]
            },
            # Fanga oid savollar 100ta
            {
                "question": "O‘zbekiston Respublikasining Konstitutsiyasi qachon qabul qilingan?",
                "answer": "1992-yil 8-dekabr",
                "options": ["1992-yil 8-dekabr", "1991-yil 1-sentyabr", "1993-yil 31-avgust", "1994-yil 20-iyun"]
            },
            {
                "question": "Yer sharidagi eng mashhur cho‘llardan biri?",
                "answer": "Sahroi Kabir",
                "options": ["Gobi", "Atakama", "Lut cho‘li", "Sahroi Kabir"]
            },
            {
                "question": "Buyuk yozuvchi Abdulla Qahhor mashhur hikoyalaridan biri?",
                "answer": "O‘g‘ri",
                "options": ["O‘g‘ri", "Anor", "Sarob", "Shohnoma"]
            },
            {
                "question": "O‘zbekiston Respublikasining birinchi Prezidenti kim?",
                "answer": "Islom Karimov",
                "options": ["Islom Karimov", "Shavkat Mirziyoyev", "Abdulla Qodiriy", "Cho‘lpon"]
            },
            {
                "question": "O‘zbekiston davlat gerbidagi bug‘doy va paxta ramzi nimani bildiradi?",
                "answer": "Farovonlik va hosildorlik",
                "options": ["Farovonlik va hosildorlik", "Adolat", "Erkinlik", "Barqarorlik"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat ramzlaridan biri?",
                "answer": "Bayroq",
                "options": ["Bayroq", "Gerb", "Madhiy", "Konstitutsiya"]
            },
            {
                "question": "Yer sharida eng katta tog‘ tizmalari qaysi qit’ada joylashgan?",
                "answer": "Osiyo",
                "options": ["Osiyo", "Afrika", "Yevropa", "Amerika"]
            },
            {
                "question": "Buyuk yozuvchi Firdavsiy mashhur eposi?",
                "answer": "Shohnoma",
                "options": ["Shohnoma", "Devonu lug‘otit turk", "Xamsa", "Sarob"]
            },
            {
                "question": "O‘zbekiston Respublikasining milliy sport turi?",
                "answer": "Kurash",
                "options": ["Kurash", "Futbol", "Boks", "Tennis"]
            },
            {
                "question": "Buyuk yozuvchi Cho‘lpon mashhur dramasi?",
                "answer": "Yorqinoy",
                "options": ["Yorqinoy", "Kecha va kunduz", "Shohnoma", "Tong nafasi"]
            },
            {
                "question": "O‘zbekiston Respublikasining Konstitutsiyasi nechta moddadan iborat?",
                "answer": "128",
                "options": ["128", "121", "130", "100"]
            },
            {
                "question": "O‘zbekiston Respublikasida qabul qilingan birinchi Konstitutsiya qachon e’lon qilingan?",
                "answer": "1992-yil",
                "options": ["1992-yil", "1991-yil", "1993-yil", "1994-yil"]
            },
            {
                "question": "Yer sharidagi eng mashhur tog‘ cho‘qqilaridan biri?",
                "answer": "Elbrus",
                "options": ["Elbrus", "Everest", "Kilimanjaro", "Montblan"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat madhiyasi musiqasini kim bastalagan?",
                "answer": "Mutal Burhonov",
                "options": ["Mutal Burhonov", "Abdulla Oripov", "Botir Zokirov", "Erkin Vohidov"]
            },
            {
                "question": "Yer sharidagi eng katta tog‘ tizmasi qaysi?",
                "answer": "And tog‘lari",
                "options": ["And tog‘lari", "Alp", "Gimolay", "Tyan-Shan"]
            },
            {
                "question": "Buyuk yozuvchi Abdulla Qodiriy mashhur romani?",
                "answer": "O‘tkan kunlar",
                "options": ["O‘tkan kunlar", "Mehrobdan chayon", "Sarob", "Qiyomat"]
            },
            {
                "question": "O‘zbekistonning eng katta viloyati hududi bo‘yicha?",
                "answer": "Qashqadaryo",
                "options": ["Qashqadaryo", "Buxoro", "Surxondaryo", "Navoiy"]
            },
            {
                "question": "Buyuk yozuvchi Cho‘lpon mashhur she’rlaridan biri?",
                "answer": "Ona tilim",
                "options": ["Ona tilim", "Sarob", "Tong nafasi", "Shohnoma"]
            },
            {
                "question": "O‘zbekiston davlat bayrog‘idagi yashil rang nimani anglatadi?",
                "answer": "Tabiat va yangilanish",
                "options": ["Tabiat va yangilanish", "Hosildorlik", "Adolat", "Farovonlik"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan eng mashhur me’moriy obidalaridan biri?",
                "answer": "Registon",
                "options": ["Registon", "Ark", "Ko‘kaldosh", "Hazrati Imam"]
            },
            {
                "question": "Yer sharidagi eng mashhur muz saroyi qaysi davlatda?",
                "answer": "Rossiya",
                "options": ["Rossiya", "Kanada", "Norvegiya", "Shvetsiya"]
            },
            {
                "question": "Buyuk yozuvchi O‘tkir Hoshimov mashhur qissalaridan biri?",
                "answer": "Ikki eshik orasi",
                "options": ["Ikki eshik orasi", "Dunyoning ishlari", "Yulduzli tunlar", "Shohnoma"]
            },
            {
                "question": "O‘zbekiston davlat gerbidagi paxta nimani bildiradi?",
                "answer": "Boylik va farovonlik",
                "options": ["Boylik va farovonlik", "Hosildorlik", "Adolat", "Ona tabiat"]
            },
            {
                "question": "Buyuk yozuvchi Pirimqul Qodirov mashhur asarlaridan biri?",
                "answer": "Yulduzli tunlar",
                "options": ["Yulduzli tunlar", "Avlodlar dovoni", "Sarob", "Shohnoma"]
            },
            {
                "question": "O‘zbekiston Respublikasining eng katta shaharlaridan biri?",
                "answer": "Namangan",
                "options": ["Namangan", "Andijon", "Buxoro", "Samarqand"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat bayrog‘idagi oq rang nimani anglatadi?",
                "answer": "Poklik va tinchlik",
                "options": ["Poklik va tinchlik", "Adolat", "Hosildorlik", "Barqarorlik"]
            },
            {
                "question": "Yer sharida eng sovuq dengiz?",
                "answer": "Sibir",
                "options": ["O‘lik dengiz", "Qora dengiz", "Kaspiy", "Sibir"]
            },
            {
                "question": "Buyuk yozuvchi Navoiy mashhur dostonlaridan biri?",
                "answer": "Layli va Majnun",
                "options": ["Layli va Majnun", "Shohnoma", "Farhod va Shirin", "Sarob"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat bayrog‘ida nechta rang mavjud?",
                "answer": "4",
                "options": ["3", "4", "5", "2"]
            },
            {
                "question": "O‘zbekiston Respublikasining Konstitutsiyasi nechta bobdan iborat?",
                "answer": "26",
                "options": ["26", "25", "30", "22"]
            },
            {
                "question": "Buyuk yozuvchi Cho‘lpon mashhur she’riy turkumlaridan biri?",
                "answer": "Buloqlar",
                "options": ["Buloqlar", "Tong nafasi", "Shohnoma", "Sarob"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat gerbidagi quyosh nimani bildiradi?",
                "answer": "Kelajak va baxt",
                "options": ["Kelajak va baxt", "Adolat", "Farovonlik", "Tabiat"]
            },
            {
                "question": "Buyuk yozuvchi O‘tkir Hoshimov mashhur romani?",
                "answer": "Dunyoning ishlari",
                "options": ["Dunyoning ishlari", "Ikki eshik orasi", "Shohnoma", "Sarob"]
            },
            {
                "question": "O‘zbekiston Respublikasining Konstitutsiyasi nechta modda o‘z ichiga olgan?",
                "answer": "128",
                "options": ["128", "130", "121", "115"]
            },
            {
                "question": "O‘zbekiston Respublikasining mustaqilligi qachon e’lon qilingan?",
                "answer": "1991-yil 1-sentyabr",
                "options": ["1991-yil 1-sentyabr", "1992-yil 8-dekabr", "1990-yil 20-iyun", "1994-yil 21-mart"]
            },
            {
                "question": "O‘zbekiston Respublikasining Konstitutsiyasi nechta qismdan iborat?",
                "answer": "6",
                "options": ["6", "5", "7", "8"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat bayrog‘idagi ko‘k rang nimani bildiradi?",
                "answer": "Osmon va tinchlik",
                "options": ["Osmon va tinchlik", "Adolat", "Hosildorlik", "Ona tabiat"]
            },
            {
                "question": "Buyuk yozuvchi Cho‘lpon mashhur romani?",
                "answer": "Kecha va kunduz",
                "options": ["Kecha va kunduz", "Shohnoma", "Sarob", "Oltin vodiydan"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat madhiyasi so‘zlarini kim yozgan?",
                "answer": "Abdulla Oripov",
                "options": ["Abdulla Oripov", "Erkin Vohidov", "Cho‘lpon", "O‘tkir Hoshimov"]
            },
            {
                "question": "O‘zbekiston Respublikasining davlat gerbidagi Humo qushi nimani bildiradi?",
                "answer": "Baxt va erkinlik",
                "options": ["Baxt va erkinlik", "Adolat", "Tabiat", "Hosildorlik"]
            },
            {
                "question": "Yer sharida eng katta arxipelag qaysi?",
                "answer": "Indoneziya",
                "options": ["Indoneziya", "Filippin", "Maldiv", "Yaponiya"]
            },
            {
                "question": "O‘zbekiston Respublikasining Konstitutsiya mualliflaridan biri kim?",
                "answer": "Islom Karimov",
                "options": ["Islom Karimov", "Shavkat Mirziyoyev", "Abdulla Qodiriy", "Cho‘lpon"]
            },
            {
                "question": "Yer sharida eng uzun metro tarmog‘i qaysi shaharda?",
                "answer": "Pekin",
                "options": ["Pekin", "London", "Moskva", "Nyu-York"]
            },
            {
                "question": "O‘zbekiston Respublikasi bayrog‘idagi 12 yulduz nimani bildiradi?",
                "answer": "Viloyatlar va Qoraqalpog‘istonni",
                "options": ["Viloyatlar va Qoraqalpog‘istonni", "12 oy", "12 xalq", "12 ramz"]
            },
            {
                "question": "Eng qadimiy shaharlaridan biri — Ur qaysi davlat hududida joylashgan?",
                "answer": "Iroq",
                "options": ["Iroq", "Eron", "Suriya", "Misr"]
            },
            {
                "question": "O‘zbek adabiyotining “Cho‘lpon” taxallusi ma’nosi nima?",
                "answer": "Tong yulduzi",
                "options": ["Tong yulduzi", "Oy", "Yorug‘lik", "Quyosh"]
            },
            {
                "question": "Yer sharidagi eng baland mustaqil minora?",
                "answer": "Tokio minorasi",
                "options": ["Tokio minorasi", "Eiffel minorasi", "CN Tower", "Burj Xalifa"]
            },
            {
                "question": "O‘zbekistonning eng yirik shaharlaridan biri Farg‘ona qaysi viloyat markazi?",
                "answer": "Farg‘ona viloyati",
                "options": ["Farg‘ona viloyati", "Andijon viloyati", "Namangan viloyati", "Toshkent viloyati"]
            },
            {
                "question": "Yer sharidagi eng chuqur joy — Mariana chuqurligi qaysi okeanda?",
                "answer": "Tinch okeani",
                "options": ["Tinch okeani", "Hind okeani", "Atlantika okeani", "Shimoliy muz okeani"]
            },
            {
                "question": "O‘zbekiston Respublikasining asosiy qonuni nima?",
                "answer": "Konstitutsiya",
                "options": ["Konstitutsiya", "Madhiy", "Gerb", "Bayroq"]
            },
            {
                "question": "Dunyoning eng mashhur sharsharalaridan biri — Viktoriya qayerda joylashgan?",
                "answer": "Zambiya va Zimbabve",
                "options": ["Zambiya va Zimbabve", "Braziliya va Argentina", "Venesuela", "AQSh va Kanada"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur tarixiy shahar — Samarqand qachon asos solingan?",
                "answer": "2700 yil avval",
                "options": ["2700 yil avval", "2000 yil avval", "1500 yil avval", "1000 yil avval"]
            },
            {
                "question": "Dunyoning eng mashhur universitetlaridan biri — Tokio universiteti qayerda joylashgan?",
                "answer": "Yaponiya",
                "options": ["Yaponiya", "Xitoy", "Janubiy Koreya", "Singapur"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Cho‘lpon mashhur asari?",
                "answer": "Yorqinoy",
                "options": ["Yorqinoy", "Kecha va kunduz", "Buloqlar", "Tong nafasi"]
            },
            {
                "question": "Dunyoning eng mashhur san’at muzeylaridan biri — Luvr qayerda joylashgan?",
                "answer": "Parij",
                "options": ["Parij", "London", "Madrid", "Berlin"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaharlaridan biri — Urganch qaysi vohada joylashgan?",
                "answer": "Xorazm vohasi",
                "options": ["Xorazm vohasi", "Farg‘ona vohasi", "Surxondaryo vohasi", "Qashqadaryo vohasi"]
            },
            {
                "question": "Dunyoning eng mashhur tog‘ cho‘qqilaridan biri — Montblan qayerda joylashgan?",
                "answer": "Fransiya va Italiya",
                "options": ["Fransiya va Italiya", "Shveytsariya", "Avstriya", "Ispaniya"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Tohir Malik mashhur kitobi?",
                "answer": "Shaytanat",
                "options": ["Shaytanat", "O‘tkan kunlar", "Yulduzli tunlar", "Sarob"]
            },
            {
                "question": "Osiyodagi eng mashhur daryolardan biri?",
                "answer": "Ganga",
                "options": ["Ganga", "Yanszi", "Amur", "Mekong"]
            },
            {
                "question": "Dunyoning eng mashhur sportchilaridan biri — Usayn Bolt qaysi sport turi bo‘yicha mashhur?",
                "answer": "Yugurish",
                "options": ["Yugurish", "Futbol", "Tennis", "Suzish"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur qadimiy qal’alardan biri — Topraqqal’a qaysi davrga oid?",
                "answer": "Kushon davriga",
                "options": ["Kushon davriga", "Temuriylar davriga", "Arab xalifaligi davriga", "Sovet davriga"]
            },
            {
                "question": "Dunyoning eng mashhur minoralaridan biri — Burj Xalifa qayerda joylashgan?",
                "answer": "BAA",
                "options": ["BAA", "Saudiya Arabistoni", "Katar", "Kuvayt"]
            },
            {
                "question": "O‘zbekistonning mashhur shoirlaridan biri — G‘afur G‘ulom mashhur asari?",
                "answer": "Shum bola",
                "options": ["Shum bola", "Sarob", "Anor", "O‘tkan kunlar"]
            },
            {
                "question": "Shimoliy Amerikadagi eng katta ko‘rfaz?",
                "answer": "Meksika ko‘rfazi",
                "options": ["Meksika ko‘rfazi", "Bengal ko‘rfazi", "Pers ko‘rfazi", "Aden ko‘rfazi"]
            },
            {
                "question": "Dunyoning eng baland vulqon?",
                "answer": "Etna",
                "options": ["Ojos del Salado", "Etna", "Fudziyama", "Vezuviy"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Oybek mashhur romani?",
                "answer": "Navoiy",
                "options": ["Navoiy", "Sarob", "Kecha va kunduz", "Yulduzli tunlar"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur tarixiy yodgorliklardan biri — Minorai Kalon qayerda?",
                "answer": "Buxoro",
                "options": ["Buxoro", "Samarqand", "Xiva", "Toshkent"]
            },
            {
                "question": "Dunyoning eng mashhur orollardan biri — Bali qaysi davlatda joylashgan?",
                "answer": "Indoneziya",
                "options": ["Indoneziya", "Filippin", "Malayziya", "Tailand"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur maqbaralardan biri — Shohizinda majmuasi qayerda joylashgan?",
                "answer": "Samarqand",
                "options": ["Samarqand", "Buxoro", "Xiva", "Shahrisabz"]
            },
            {
                "question": "Dunyoning eng mashhur futbol jamoalaridan biri — Juventus qayerda joylashgan?",
                "answer": "Italiya",
                "options": ["Italiya", "Ispaniya", "Fransiya", "Angliya"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaxsi — Mirzo Ulug‘bek qaysi sohaga ko‘proq hissa qo‘shgan?",
                "answer": "Astronomiya",
                "options": ["Astronomiya", "Matematika", "Tibbiyot", "Kimyo"]
            },
            {
                "question": "Osiyodagi eng katta ko‘rfaz?",
                "answer": "Bengal ko‘rfazi",
                "options": ["Bengal ko‘rfazi", "Pers ko‘rfazi", "Meksika ko‘rfazi", "Aden ko‘rfazi"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — O‘tkir Hoshimov mashhur qissasi?",
                "answer": "Bahor qaytmaydi",
                "options": ["Bahor qaytmaydi", "Ikki eshik orasi", "Dunyoning ishlari", "Sarob"]
            },
            {
                "question": "Dunyoning eng mashhur tog‘ tizmalardan biri — Alp qaysi qit’ada joylashgan?",
                "answer": "Yevropa",
                "options": ["Yevropa", "Osiyo", "Janubiy Amerika", "Afrika"]
            },
            {
                "question": "O‘zbekistonning mashhur shoirlaridan biri — Erkin Vohidov mashhur dramasi?",
                "answer": "Oltin devor",
                "options": ["Oltin devor", "Sarob", "Shohnoma", "Yulduzli tunlar"]
            },
            {
                "question": "Dunyoning eng mashhur sharsharalaridan biri — Seljalandsfoss qayerda joylashgan?",
                "answer": "Islandiya",
                "options": ["Islandiya", "Norvegiya", "Shvetsiya", "Finlyandiya"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur tarixiy majmualardan biri — Ichan qal’a qayerda joylashgan?",
                "answer": "Xiva",
                "options": ["Xiva", "Buxoro", "Samarqand", "Andijon"]
            },
            {
                "question": "Dunyoning eng mashhur futbol jamoalaridan biri — PSG qayerda joylashgan?",
                "answer": "Parij",
                "options": ["Parij", "Madrid", "Milan", "Manchester"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Cho‘lpon mashhur she’ri?",
                "answer": "Ona tilim",
                "options": ["Ona tilim", "Tong nafasi", "Sarob", "Ruhlar isyoni"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur tarixiy obidalardan biri — Ark qal’asi qayerda joylashgan?",
                "answer": "Buxoro",
                "options": ["Buxoro", "Samarqand", "Toshkent", "Shahrisabz"]
            },
            {
                "question": "Dunyoning eng mashhur minoralaridan biri — Big Ben qayerda joylashgan?",
                "answer": "London",
                "options": ["London", "Parij", "Berlin", "Madrid"]
            },
            {
                "question": "O‘zbekistonning mashhur shoirlaridan biri — Abdulla Oripov mashhur dostoni?",
                "answer": "Sohibqiron",
                "options": ["Sohibqiron", "Sarob", "Jannatga yo‘l", "O‘zbekiston"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Pirimqul Qodirov mashhur kitobi?",
                "answer": "Qora ko‘zlar",
                "options": ["Qora ko‘zlar", "Avlodlar dovoni", "Yulduzli tunlar", "Sarob"]
            },
            {
                "question": "Dunyoning eng mashhur muzliklaridan biri — Vatnajokull qayerda joylashgan?",
                "answer": "Islandiya",
                "options": ["Islandiya", "Norvegiya", "Kanada", "Grenlandiya"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy obidalaridan biri — Bibi Xonim masjidi qayerda joylashgan?",
                "answer": "Samarqand",
                "options": ["Samarqand", "Buxoro", "Xiva", "Toshkent"]
            },
            {
                "question": "Dunyoning eng mashhur futbol jamoalaridan biri — Milan qayerda joylashgan?",
                "answer": "Italiya",
                "options": ["Italiya", "Ispaniya", "Fransiya", "Angliya"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Abdulla Qahhor mashhur qissasi?",
                "answer": "Oltin yulduz",
                "options": ["Oltin yulduz", "Sarob", "Anor", "Sinchalak"]
            },
            {
                "question": "Osiyodagi eng usun tog‘ tizmasi?",
                "answer": "Himolay",
                "options": ["Tyan-Shan", "Pamir", "Altay", "Himolay"]
            },
            {
                "question": "O‘zbekistonning mashhur shoirlaridan biri — Erkin Vohidov mashhur she’ri?",
                "answer": "Nido",
                "options": ["Nido", "Ruhlar isyoni", "Tong nafasi", "O‘zbekiston"]
            },
            {
                "question": "Dunyoning eng mashhur sharsharalaridan biri — Plitvice qayerda joylashgan?",
                "answer": "Xorvatiya",
                "options": ["Xorvatiya", "Sloveniya", "Chexiya", "Serbiya"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur tarixiy qal’alardan biri — Ayazqal’a qayerda joylashgan?",
                "answer": "Qoraqalpog‘iston",
                "options": ["Qoraqalpog‘iston", "Buxoro", "Xorazm", "Samarqand"]
            },
            {
                "question": "Dunyoning eng mashhur sportchilardan biri — Diego Maradona qaysi davlat fuqarosi edi?",
                "answer": "Argentina",
                "options": ["Argentina", "Braziliya", "Ispaniya", "Urugvay"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Tohir Malik mashhur hikoyasi?",
                "answer": "So‘nggi o‘q",
                "options": ["So‘nggi o‘q", "Shaytanat", "Sarob", "Bahor qaytmaydi"]
            },
            {
                "question": "Dunyoning eng mashhur orollardan biri — Yangi Gvineya qaysi okeanda joylashgan?",
                "answer": "Tinch okeani",
                "options": ["Tinch okeani", "Hind okeani", "Atlantika okeani", "Shimoliy muz okeani"]
            },
            {
                "question": "O‘zbekistonning mashhur shoirlaridan biri — G‘afur G‘ulom mashhur she’ri?",
                "answer": "Sen yetim emassan",
                "options": ["Sen yetim emassan", "Shum bola", "Sarob", "Yulduzli tunlar"]
            },
            {
                "question": "Dunyoning eng mashhur minoralaridan biri — Ostankino minorasi qayerda joylashgan?",
                "answer": "Moskva",
                "options": ["Moskva", "Sankt-Peterburg", "Novosibirsk", "Minsk"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — Cho‘lpon mashhur hikoyasi?",
                "answer": "Sevgi va hayot",
                "options": ["Sevgi va hayot", "Yorqinoy", "Kecha va kunduz", "Buloqlar"]
            },
            {
                "question": "Dunyoning eng mashhur teatrlaridan biri — Bolshoy teatri qaysi shaharda joylashgan?",
                "answer": "Moskva",
                "options": ["Moskva", "Parij", "London", "Berlin"]
            },
            {
                "question": "O‘zbekistonning mashhur tarixiy shaharlaridan biri — Jizzax qaysi yo‘lda muhim nuqta bo‘lgan?",
                "answer": "Buyuk Ipak yo‘li",
                "options": ["Buyuk Ipak yo‘li", "Arab savdo yo‘li", "Buyuk ipak dengiz yo‘li", "Yevropa savdo yo‘li"]
            },
            {
                "question": "Buyuk geografik kashfiyotlar davrida Amerikani ochgan kishi kim?",
                "answer": "Xristofor Kolumb",
                "options": ["Xristofor Kolumb", "Vasko da Gama", "Magellan", "Amerigo Vespucci"]
            }
        ]
    
        quiz_9 = [
            # Diniy savollar 50ta
            {
                "question": "Qur’onda zikr qilingan eng mashhur baxtsiz qavm?",
                "answer": "Ad qavmi",
                "options": ["Ad", "Samud", "Qavmi Lut", "Fir’avn"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur to‘g‘ri so‘zli payg‘ambar?",
                "answer": "Idris (a.s.)",
                "options": ["Idris", "Ibrohim", "Muso", "Iso"]
            },
            {
                "question": "Qur’onda eng ko‘p takrorlangan oyat qaysi?",
                "answer": "Ar-Rahmon surasi 13-oyat",
                "options": ["Ar-Rahmon 13", "Baqara 255", "Ikhlos 1", "Nas 6"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur duo kimniki?",
                "answer": "Ibrohim (a.s.) duosi",
                "options": ["Muso (a.s.)", "Ibrohim (a.s.)", "Iso (a.s.)", "Nuh (a.s.)"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur ayol kim?",
                "answer": "Maryam (r.a.)",
                "options": ["Xadicha", "Maryam", "Fotima", "Oyshe"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur qush voqeasi?",
                "answer": "Fil surasi",
                "options": ["Fil surasi", "Ankabut surasi", "Namli surasi", "Taha surasi"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur hayvon?",
                "answer": "Tuya",
                "options": ["Ot", "Sigir", "Tuya", "Qoy"]
            },
            {
                "question": "Payg‘ambarimizning eng mashhur mo‘jizalaridan biri?",
                "answer": "Oy ikkiga bo‘linishi",
                "options": ["Oy ikkiga bo‘linishi", "Mi’roj", "Qur’on", "Barchasi to‘g‘ri"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur taom?",
                "answer": "Manna va Salvo",
                "options": ["Manna va Salvo", "Asal", "Xurmo", "Sut"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur dengiz voqeasi?",
                "answer": "Muso (a.s.)ning Qizil dengizni yorib o‘tishi",
                "options": ["Muso (a.s.) Qizil dengizni yorib o‘tishi", "Nuh (a.s.) to‘foni", "Yunus (a.s.) baliq voqeasi", "Iso (a.s.) mo‘jizasi"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur ibora?",
                "answer": "La ilaha illalloh",
                "options": ["Bismillah", "Allohu akbar", "La ilaha illalloh", "Subhanalloh"]
            },
            {
                "question": "Islom tarixida yozilgan eng qadimiy tafsir kitobi?",
                "answer": "Tabariy tafsiri",
                "options": ["Tabariy tafsiri", "Qurtubiy tafsiri", "Ibn Kasir tafsiri", "Bayzoviy tafsiri"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ga berilgan eng mashhur muhr yozuvi?",
                "answer": "Muhammad Rasululloh",
                "options": ["Muhammad Rasululloh", "Al-Amin", "Al-Faruq", "As-Siddiq"]
            },
            {
                "question": "Islomda hadislarni yozishga ruxsat berilgan davrda kim xalifa edi?",
                "answer": "Umar ibn Abdulaziz",
                "options": ["Abu Bakr", "Umar ibn Abdulaziz", "Usmon", "Ali"]
            },
            {
                "question": "Hadis ilmining mashhur to‘plovchilaridan biri Termiziy qaysi yurtlik edi?",
                "answer": "Termiz",
                "options": ["Buxoro", "Termiz", "Nishopur", "Qufa"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur payg‘ambar sinovlaridan biri?",
                "answer": "Ibrohim (a.s.) o‘g‘lini qurbon qilish voqeasi",
                "options": ["Muso (a.s.)ning sinovi", "Nuh (a.s.) sinovi", "Ibrohim (a.s.) qurbonlik voqeasi", "Iso (a.s.) sinovi"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur sura ismlari nechta?",
                "answer": "114 ta",
                "options": ["110 ta", "112 ta", "114 ta", "116 ta"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur o‘qituvchi sifatida kim eslatilgan?",
                "answer": "Alloh taolo",
                "options": ["Alloh taolo", "Muso (a.s.)", "Iso (a.s.)", "Muhammad (s.a.v.)"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur janglardan biri?",
                "answer": "Hunayn jangi",
                "options": ["Uhud jangi", "Badr jangi", "Hunayn jangi", "Xandaq jangi"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur oyat kursi?",
                "answer": "Baqara 255-oyat",
                "options": ["Baqara 255-oyat", "Rahmon 13-oyat", "Fotiha 1-oyat", "Nas 6-oyat"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur inson ismi bo‘lmagan sura?",
                "answer": "Yusuf surasi",
                "options": ["Yusuf surasi", "Maryam surasi", "Muso surasi", "Ibrohim surasi"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur hikmatli odam?",
                "answer": "Luqmon",
                "options": ["Luqmon", "Hud", "Sho‘ayb", "Sulaymon"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur hukmdor payg‘ambar?",
                "answer": "Sulaymon (a.s.)",
                "options": ["Sulaymon (a.s.)", "Muso (a.s.)", "Ibrohim (a.s.)", "Nuh (a.s.)"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur jodugarlar voqeasi qaysi payg‘ambar bilan bog‘liq?",
                "answer": "Muso (a.s.)",
                "options": ["Muso (a.s.)", "Iso (a.s.)", "Ibrohim (a.s.)", "Yusuf (a.s.)"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur ism egasi bo‘lgan podshoh?",
                "answer": "Fir’avn",
                "options": ["Namrud", "Fir’avn", "Qorun", "Homon"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur boy odam?",
                "answer": "Qorun",
                "options": ["Qorun", "Fir’avn", "Abu Lahab", "Homon"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur duo so‘zlari?",
                "answer": "Rabbana",
                "options": ["Rabbana", "Bismillah", "Subhanalloh", "Alhamdulillah"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur qudrat belgisi?",
                "answer": "To‘fon",
                "options": ["To‘fon", "Zilzila", "Shamol", "Yomg‘ir"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur sahro nomi?",
                "answer": "Sina",
                "options": ["Sina", "Hijoz", "Najd", "Sahro"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur jannat daryosi?",
                "answer": "Kavsar",
                "options": ["Kavsar", "Rayhon", "Adn", "Firdaus"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur farishta ovozi?",
                "answer": "Isrofilning suri",
                "options": ["Isrofilning suri", "Jabroilning vahiy ovozi", "Mikoilning chaqirig‘i", "Azroilning ovozi"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur ota va farzand voqeasi?",
                "answer": "Ibrohim va Ismoil (qurbonlik)",
                "options": ["Ibrohim va Ismoil", "Nuh va o‘g‘li", "Ya’qub va Yusuf", "Muso va onasi"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur ayollar surasi?",
                "answer": "Niso surasi",
                "options": ["Niso surasi", "Maryam surasi", "Mujodala surasi", "Nur surasi"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur voqealardan biri?",
                "answer": "Ashobi Kahf",
                "options": ["Ashobi Kahf", "Hudhud hikoyasi", "Fil voqeasi", "Mi’roj"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur payg‘ambar sabri?",
                "answer": "Ayyub (a.s.)",
                "options": ["Ayyub (a.s.)", "Yunus (a.s.)", "Ibrohim (a.s.)", "Muso (a.s.)"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur qurol?",
                "answer": "Qilich",
                "options": ["Qilich", "Asa", "O‘q-yoy", "Qalqon"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur jannat bog‘i?",
                "answer": "Firdaus",
                "options": ["Firdaus", "Adn", "Rayhon", "Na’im"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur gunoh?",
                "answer": "Shirk",
                "options": ["Shirk", "Kibr", "Hasad", "Yolg‘on"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur dushman?",
                "answer": "Iblis",
                "options": ["Iblis", "Fir’avn", "Abu Lahab", "Qorun"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur go‘zal joy?",
                "answer": "Jannat",
                "options": ["Jannat", "Firdaus", "Adn", "Na’im"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur duo iborasi?",
                "answer": "Astaghfirulloh",
                "options": ["Astaghfirulloh", "Alhamdulillah", "Subhanalloh", "La ilaha illalloh"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur jannat sifatlari?",
                "answer": "Oq sut, toza suv, asal va sharob daryolari",
                "options": ["Oq sut, suv, asal, sharob", "Faqat suv", "Faqat asal", "Faqat sharob"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur payg‘ambar sodiqligi?",
                "answer": "Idris (a.s.)",
                "options": ["Idris (a.s.)", "Ibrohim (a.s.)", "Iso (a.s.)", "Muso (a.s.)"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur do‘zax darvozasi?",
                "answer": "Saqor",
                "options": ["Saqor", "Hutamah", "Jahannam", "Laza"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur halol oziq-ovqat?",
                "answer": "Halol go‘sht",
                "options": ["Halol go‘sht", "Suv", "Non", "Meva"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur ma’rifat belgisi?",
                "answer": "Ilm",
                "options": ["Ilm", "Duo", "Iymon", "Taqvo"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur ibodat uyi?",
                "answer": "Ka’ba",
                "options": ["Ka’ba", "Masjid Aqso", "Masjid Nabaviy", "Masjid Qubo"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur duo qiluvchi payg‘ambar?",
                "answer": "Zakariyo (a.s.)",
                "options": ["Zakariyo (a.s.)", "Yunus (a.s.)", "Muso (a.s.)", "Ibrohim (a.s.)"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur sabrli qavm?",
                "answer": "Ashobi Kahf",
                "options": ["Ashobi Kahf", "Bani Isroil", "Ansor", "Muhajirlar"]
            },
            {
                "question": "Qur’onda zikr qilingan eng mashhur mo‘jizaviy qush?",
                "answer": "Hudhud",
                "options": ["Hudhud", "Ankabut", "Fil", "Qarg‘a"]
            },
            # Fanga oid savollar 100ta
            {
                "question": "Qaysi davlatning poytaxti Addis-Abeba?",
                "answer": "Efiopiya",
                "options": ["Efiopiya", "Sudan", "Nigeriya", "Uganda"]
            },
            {
                "question": "O‘zbekiston hududidagi eng qadimiy buddaviylik yodgorligi?",
                "answer": "Fayoztepa",
                "options": ["Topraq-qal’a", "Qiziltepa", "Fayoztepa", "Qal’aliqir"]
            },
            {
                "question": "Dunyodagi eng ko‘p rasmiy tilga ega mamlakat?",
                "answer": "Janubiy Afrika",
                "options": ["Kanada", "Shveytsariya", "Janubiy Afrika", "Belgiya"]
            },
            {
                "question": "Yer yuzidagi eng baland faol vulqon?",
                "answer": "Kilimanjaro",
                "options": ["Fudziyama", "Kilimanjaro", "Etna", "Vezuviy"]
            },
            {
                "question": "O‘zbekistonda 'Qatag‘on qurbonlari xotirasi kuni' qachon?",
                "answer": "31-avgust",
                "options": ["9-may", "8-dekabr", "31-avgust", "1-sentyabr"]
            },
            {
                "question": "Dunyodagi eng katta yarim yopiq dengiz?",
                "answer": "Kaspiy dengizi",
                "options": ["O‘lik dengiz", "Qora dengiz", "Adriatika dengizi", "Kaspiy dengizi"]
            },
            {
                "question": "'1984' romanining muallifi kim?",
                "answer": "Jorj Oruell",
                "options": ["F. Kafka", "Jorj Oruell", "E. Xeminguey", "Ch. Dikkens"]
            },
            {
                "question": "Yaponiyaning milliy pul birligi?",
                "answer": "Yen",
                "options": ["Won", "Peso", "Dollar", "Yen"]
            },
            {
                "question": "Markaziy Osiyodagi eng chuqur ko‘l?",
                "answer": "Issiqko‘l",
                "options": ["Sarezko‘l", "Issiqko‘l", "Qorako‘l", "Aydarko‘l"]
            },
            {
                "question": "Ibn Sinoning mashhur asari?",
                "answer": "Tib qonunlari",
                "options": ["Xamsa", "Avesto", "Tib qonunlari", "Donishnoma"]
            },
            {
                "question": "Qaysi davlat 'Tinch okeani orollari federatsiyasi' deb ataladi?",
                "answer": "Mikroneziya",
                "options": ["Mikroneziya", "Fiji", "Tonga", "Kiribati"]
            },
            {
                "question": "Eng uzoq yashovchi daraxt turi?",
                "answer": "Sekvoyya",
                "options": ["Tol", "Sekvoyya", "Eman", "Qayin"]
            },
            {
                "question": "Yevropada 'Qora o‘lim' deb atalgan ofat nima edi?",
                "answer": "Vabo",
                "options": ["Gripp", "Tif", "Chechak", "Vabo"]
            },
            {
                "question": "Al-Xorazmiy mashhur asari?",
                "answer": "Al-jabr va al-muqobala",
                "options": ["Bayt ul-hikma", "Al-jabr va al-muqobala", "Tib qonunlari", "Qutadg‘u bilig"]
            },
            {
                "question": "Osiyodagi eng kichik davlat?",
                "answer": "Maldiv orollari",
                "options": ["Butan", "Bruney", "Maldiv orollari", "Nepal"]
            },
            {
                "question": "Dunyoning eng baland platosi?",
                "answer": "Tibet platosi",
                "options": ["Altay", "And", "Tibet platosi", "Pamir"]
            },
            {
                "question": "Qadimgi Mesopotamiya qaysi hududda joylashgan edi?",
                "answer": "Ikki daryo oralig‘i",
                "options": ["Arabiston", "Ikki daryo oralig‘i", "Eron", "Misr"]
            },
            {
                "question": "'Jarayon' romanining muallifi kim?",
                "answer": "Frans Kafka",
                "options": ["Frans Kafka", "Balzak", "Alber Kamyu", "Sartre"]
            },
            {
                "question": "Ulug‘bek rasadxonasi qaysi shaharda joylashgan?",
                "answer": "Samarqand",
                "options": ["Xiva", "Samarqand", "Buxoro", "Toshkent"]
            },
            {
                "question": "Qaysi davlatning poytaxti Naypyido?",
                "answer": "Myanma",
                "options": ["Kambodja", "Laos", "Myanma", "Malayziya"]
            },
            {
                "question": "Yevropadagi eng baland tog‘?",
                "answer": "Elbrus",
                "options": ["Montblan", "Elbrus", "Alp", "Kavkaz"]
            },
            {
                "question": "O‘zbekiston hududidagi eng qadimiy shahar?",
                "answer": "Termiz",
                "options": ["Buxoro", "Xiva", "Samarqand", "Termiz"]
            },
            {
                "question": "Yer sharining eng yirik ko‘rfazi?",
                "answer": "Bengal ko‘rfazi",
                "options": ["Aden ko‘rfazi", "Meksika ko‘rfazi", "Pers ko‘rfazi", "Bengal ko‘rfazi"]
            },
            {
                "question": "Qaysi davlatda Machu-Pikchu joylashgan?",
                "answer": "Peru",
                "options": ["Boliviya", "Peru", "Argentina", "Meksika"]
            },
            {
                "question": "Buyuk astronom Ptolemey qaysi shaharda yashagan?",
                "answer": "Iskandariya",
                "options": ["Iskandariya", "Afina", "Rim", "Qohira"]
            },
            {
                "question": "Yer yuzidagi eng baland sharshara?",
                "answer": "Anxel",
                "options": ["Niagara", "Victoria", "Anxel", "Iguasu"]
            },
            {
                "question": "Markaziy Osiyodagi eng baland cho‘qqi?",
                "answer": "Somoni cho‘qqisi",
                "options": ["Bobotog‘", "Somoni cho‘qqisi", "Hazrati Sulton", "Tyan-Shan"]
            },
            {
                "question": "O‘zbekiston hududidan o‘tgan qadimiy daryo?",
                "answer": "Oks (Amudaryo)",
                "options": ["Sirdaryo", "Oks (Amudaryo)", "Zarafshon", "Chirchiq"]
            },
            {
                "question": "Yer sharidagi eng sovuq aholi punkti?",
                "answer": "Oymyakon",
                "options": ["Yakutsk", "Oymyakon", "Norilsk", "Reykyavik"]
            },
            {
                "question": "Qaysi yozuvchi 'Sarguzashtlar oroli' asarini yozgan?",
                "answer": "Robert Luis Stivenson",
                "options": ["Daniel Defo", "Robert Luis Stivenson", "Jek London", "Mark Tven"]
            },
            {
                "question": "Buyuk Ipak yo‘li orqali O‘zbekistonga kelgan mashhur sayyoh?",
                "answer": "Marko Polo",
                "options": ["Ibn Battuta", "Marko Polo", "Kolumb", "Hudson"]
            },
            {
                "question": "Yer kurrasidagi eng katta tekislik?",
                "answer": "Amazon tekisligi",
                "options": ["Afrika tekisligi", "Amazon tekisligi", "Sibir tekisligi", "Kanada tekisligi"]
            },
            {
                "question": "Qaysi davlatda Viktoriya sharsharasi joylashgan?",
                "answer": "Zambiya va Zimbabve",
                "options": ["Tanzaniya", "Zambiya va Zimbabve", "Uganda", "Mozambik"]
            },
            {
                "question": "Qaysi yozuvchi 'Qariya va dengiz' asarini yozgan?",
                "answer": "Ernest Xeminguey",
                "options": ["Ernest Xeminguey", "Dreiser", "Balzak", "London"]
            },
            {
                "question": "Dunyodagi eng katta ko‘prik qaysi davlatda?",
                "answer": "Xitoy",
                "options": ["AQSh", "Xitoy", "Fransiya", "Kanada"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan eng katta qo‘rg‘on?",
                "answer": "Toproq qal’a",
                "options": ["Toproq qal’a", "Ayazqal’a", "Ark", "Xiva qal’asi"]
            },
            {
                "question": "Qaysi davlatning milliy sporti kriket?",
                "answer": "Hindiston",
                "options": ["Hindiston", "Avstraliya", "Angliya", "Pokiston"]
            },
            {
                "question": "Yer yuzidagi eng uzun devor?",
                "answer": "Xitoy devori",
                "options": ["Xitoy devori", "Hadrian devori", "Berlin devori", "Bobil devori"]
            },
            {
                "question": "Dunyodagi eng katta orollardan biri — Yangi Gvineya qaysi okeanda joylashgan?",
                "answer": "Tinch okeani",
                "options": ["Hind okeani", "Tinch okeani", "Atlantika okeani", "Shimoliy muz okeani"]
            },
            {
                "question": "O‘zbekiston hududidagi eng mashhur maqbara?",
                "answer": "Shohi Zinda",
                "options": ["Shohi Zinda", "Ismoil Somoniy maqbarasi", "Gur Amir", "Hazrati Imam"]
            },
            {
                "question": "Qaysi yozuvchi 'Xamsa'ni yaratgan?",
                "answer": "Alisher Navoiy",
                "options": ["Bobur", "Cho‘lpon", "Alisher Navoiy", "Shakespeare"]
            },
            {
                "question": "Qaysi davlatni 'Ko‘l mamlakati' deb atashadi?",
                "answer": "Finlyandiya",
                "options": ["Shvetsiya", "Norvegiya", "Finlyandiya", "Islandiya"]
            },
            {
                "question": "Yer yuzidagi eng chuqur okean joyi?",
                "answer": "Mariana chuqurligi",
                "options": ["Puerto-Riko chuqurligi", "Tonga chuqurligi", "Filippin chuqurligi", "Mariana chuqurligi"]
            },
            {
                "question": "Qaysi yozuvchi 'Faust' asarini yozgan?",
                "answer": "Gyote",
                "options": ["Gyote", "Shiller", "Balzak", "Hamsun"]
            },
            {
                "question": "Dunyoning eng katta daryosi suv hajmi bo‘yicha?",
                "answer": "Amazonka",
                "options": ["Amazonka", "Nil", "Yanszi", "Missisipi"]
            },
            {
                "question": "Qaysi davlat poytaxti Karakas?",
                "answer": "Venesuela",
                "options": ["Kolumbiya", "Venesuela", "Ekvador", "Peru"]
            },
            {
                "question": "Yer sharidagi eng ko‘p muzliklar qaysi qit’ada?",
                "answer": "Antarktida",
                "options": ["Antarktida", "Shimoliy Amerika", "Osiyo", "Yevropa"]
            },
            {
                "question": "Qaysi yozuvchi 'Otello' tragediyasini yozgan?",
                "answer": "Shakespeare",
                "options": ["Shakespeare", "Tolstoy", "Chexov", "Dante"]
            },
            {
                "question": "Buyuk Britaniya qaysi qit’ada joylashgan?",
                "answer": "Yevropa",
                "options": ["Avstraliya", "Osiyo", "Yevropa", "Afrika"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan qadimiy qal’alar majmuasi?",
                "answer": "Ellikqal’a",
                "options": ["Ellikqal’a", "Ark", "Ko‘kaldosh", "Ayazqal’a"]
            },
            {
                "question": "Qaysi yozuvchi 'Don Kixot' asarini yozgan?",
                "answer": "Servantes",
                "options": ["Servantes", "Shakespeare", "Balzak", "Gyote"]
            },
            {
                "question": "Yer kurrasida eng ko‘p aholiga ega shahar?",
                "answer": "Tokio",
                "options": ["Shanxay", "Tokio", "Mumbay", "Meksiko"]
            },
            {
                "question": "Qaysi davlatda Amazonka daryosi oqib o‘tadi?",
                "answer": "Braziliya",
                "options": ["Braziliya", "Argentina", "Peru", "Kolumbiya"]
            },
            {
                "question": "O‘zbekiston hududidagi eng qadimiy maqbara?",
                "answer": "Ismoil Somoniy maqbarasi",
                "options": ["Shohi Zinda", "Ismoil Somoniy maqbarasi", "Gur Amir", "Hazrati Imam"]
            },
            {
                "question": "Qaysi yozuvchi 'Qiyomat' romanini yozgan?",
                "answer": "Chingiz Aytmatov",
                "options": ["Chingiz Aytmatov", "Oybek", "Cho‘lpon", "Erkin Vohidov"]
            },
            {
                "question": "Dunyodagi eng katta okean oqimi?",
                "answer": "Gulfstrim",
                "options": ["Gulfstrim", "Oyashio", "Peru oqimi", "Bengal oqimi"]
            },
            {
                "question": "Afrikaning eng katta davlati maydon jihatdan?",
                "answer": "Jazoir",
                "options": ["Misr", "Efiopiya", "Jazoir", "Nigeriya"]
            },
            {
                "question": "Qaysi davlatning poytaxti Islombul (Istanbul emas, tarixda)?",
                "answer": "Vizantiya imperiyasi",
                "options": ["Vizantiya imperiyasi", "Usmoniylar davlati", "Rim", "Sparta"]
            },
            {
                "question": "Buyuk olim Beruniy qaysi shaharda tug‘ilgan?",
                "answer": "Xorazm",
                "options": ["Xorazm", "Buxoro", "Samarqand", "Nishopur"]
            },
            {
                "question": "Yer sharidagi eng katta orol davlati?",
                "answer": "Avstraliya",
                "options": ["Avstraliya", "Madagaskar", "Grenlandiya", "Yangi Zelandiya"]
            },
            {
                "question": "Qaysi yozuvchi 'Anna Karenina' asarini yozgan?",
                "answer": "Lev Tolstoy",
                "options": ["Lev Tolstoy", "Dostoyevskiy", "Pushkin", "Chexov"]
            },
            {
                "question": "Buyuk olim Arximed qayerda tug‘ilgan?",
                "answer": "Sirakuza",
                "options": ["Afina", "Sirakuza", "Rim", "Iskandariya"]
            },
            {
                "question": "O‘zbekiston hududidagi eng baland tog‘ cho‘qqisi?",
                "answer": "Hazrati Sulton",
                "options": ["Hazrati Sulton", "Somoni cho‘qqisi", "Bobotog‘", "Chimyon"]
            },
            {
                "question": "Yer kurrasida eng issiq joy qaysi cho‘l?",
                "answer": "Lut cho‘li",
                "options": ["Lut cho‘li", "Sahroi Kabir", "Gobi", "Karakum"]
            },
            {
                "question": "Qaysi yozuvchi 'Qizil va qora' romanini yozgan?",
                "answer": "Stendal",
                "options": ["Stendal", "Balzak", "Flaubert", "Gyote"]
            },
            {
                "question": "Dunyodagi eng chuqur ko‘l?",
                "answer": "Baykal",
                "options": ["Baykal", "Tanganika", "Viktoriya", "Chad"]
            },
            {
                "question": "O‘zbek xalq dostonlaridan biri?",
                "answer": "Alpomish",
                "options": ["Alpomish", "Manas", "Shohnoma", "Qutadg‘u bilig"]
            },
            {
                "question": "Qaysi davlatning poytaxti Buenos-Ayres?",
                "answer": "Argentina",
                "options": ["Argentina", "Braziliya", "Urugvay", "Paragvay"]
            },
            {
                "question": "Buyuk Ipak yo‘lining asosiy markazlaridan biri?",
                "answer": "Samarqand",
                "options": ["Samarqand", "Buxoro", "Xiva", "Urganch"]
            },
            {
                "question": "Qaysi yozuvchi 'Jinoyat va jazo' romanini yozgan?",
                "answer": "Dostoyevskiy",
                "options": ["Dostoyevskiy", "Tolstoy", "Pushkin", "Gogol"]
            },
            {
                "question": "Yer kurrasida eng baland tog‘ tizmasi?",
                "answer": "Gimolay",
                "options": ["Gimolay", "And", "Alp", "Kavkaz"]
            },
            {
                "question": "Buyuk yozuvchi Gyote qaysi asari bilan mashhur?",
                "answer": "Faust",
                "options": ["Faust", "Otello", "Anna Karenina", "Qariya va dengiz"]
            },
            {
                "question": "Qaysi davlat 'Ko‘llar mamlakati' deb ataladi?",
                "answer": "Finlyandiya",
                "options": ["Shvetsiya", "Finlyandiya", "Norvegiya", "Islandiya"]
            },
            {
                "question": "Dunyodagi eng uzun daryo?",
                "answer": "Nil",
                "options": ["Nil", "Amazonka", "Yanszi", "Missisipi"]
            },
            {
                "question": "Qaysi yozuvchi 'Sariq devni minib' asarini yozgan?",
                "answer": "Xudoyberdi To‘xtaboyev",
                "options": ["Xudoyberdi To‘xtaboyev", "Erkin Vohidov", "O‘tkir Hoshimov", "Abdulla Qahhor"]
            },
            {
                "question": "Yer sharida eng katta muzliklar massivi?",
                "answer": "Antarktida",
                "options": ["Antarktida", "Grenlandiya", "Arktika", "Kanada"]
            },
            {
                "question": "Buyuk mutafakkir Platon qaysi shaharda tug‘ilgan?",
                "answer": "Afina",
                "options": ["Rim", "Afina", "Sparta", "Delphi"]
            },
            {
                "question": "Qaysi davlatda Kilimanjaro tog‘i joylashgan?",
                "answer": "Tanzaniya",
                "options": ["Keniya", "Uganda", "Efiopiya", "Tanzaniya"]
            },
            {
                "question": "O‘zbekistonning eng katta suv omborlaridan biri?",
                "answer": "Chorvoq",
                "options": ["Tuyamo‘yin", "Chorvoq", "To‘dako‘l", "Qoratepa"]
            },
            {
                "question": "Qaysi yozuvchi 'Urush va tinchlik' asarini yozgan?",
                "answer": "Lev Tolstoy",
                "options": ["Lev Tolstoy", "Pushkin", "Chexov", "Dostoyevskiy"]
            },
            {
                "question": "Dunyoning eng sovuq qit’asi?",
                "answer": "Antarktida",
                "options": ["Antarktida", "Osiyo", "Shimoliy Amerika", "Yevropa"]
            },
            {
                "question": "Buyuk astronom Kopernik qanday nazariya yaratgan?",
                "answer": "Geotsentrik emas, geliosentrik",
                "options": ["Geliosentrik", "Atom", "Kvark", "Nisbiylik"]
            },
            {
                "question": "Qaysi davlatda Burj Xalifa minorasi joylashgan?",
                "answer": "BAA",
                "options": ["BAA", "Saudiya Arabistoni", "Qatar", "Kuvayt"]
            },
            {
                "question": "O‘zbekiston hududidagi eng qadimiy teatr?",
                "answer": "Navoi nomidagi teatr",
                "options": ["Navoi nomidagi teatr", "Yosh tomoshabinlar teatri", "Ilhom teatri", "Qo‘qon teatri"]
            },
            {
                "question": "Qaysi yozuvchi 'Qutadg‘u bilig' asarini yozgan?",
                "answer": "Yusuf Xos Hojib",
                "options": ["Yusuf Xos Hojib", "Mahmud Qoshg‘ariy", "Navoiy", "Beruniy"]
            },
            {
                "question": "Yer yuzidagi eng katta orol?",
                "answer": "Grenlandiya",
                "options": ["Grenlandiya", "Madagaskar", "Yangi Gvineya", "Sumatra"]
            },
            {
                "question": "Qaysi davlatda Viktoriya ko‘li joylashgan?",
                "answer": "Afrika (Keniya, Tanzaniya, Uganda)",
                "options": ["Afrika (Keniya, Tanzaniya, Uganda)", "Zambiya", "Efiopiya", "Mozambik"]
            },
            {
                "question": "Buyuk olim Nyuton qaysi qonunlari bilan mashhur?",
                "answer": "Harakat qonunlari",
                "options": ["Gravitatsiya qonuni", "Harakat qonunlari", "Issiqlik qonuni", "Suyuqlik qonunlari"]
            },
            {
                "question": "Qaysi yozuvchi 'Shohnoma'ni yozgan?",
                "answer": "Firdavsiy",
                "options": ["Firdavsiy", "Navoiy", "Bobur", "Beruniy"]
            },
            {
                "question": "Yer kurrasida eng katta tog‘ tizmasi qaysi qit’ada?",
                "answer": "Janubiy Amerika (And)",
                "options": ["Janubiy Amerika (And)", "Osiyo (Gimolay)", "Yevropa (Alp)", "Afrika (Atlas)"]
            },
            {
                "question": "Qaysi yozuvchi 'Shaytonatlar' romanini yozgan?",
                "answer": "Tohir Malik",
                "options": ["Tohir Malik", "Pirimqul Qodirov", "O‘tkir Hoshimov", "Abdulla Qahhor"]
            },
            {
                "question": "Qaysi davlatda Petra shahri joylashgan?",
                "answer": "Iordaniya",
                "options": ["Iordaniya", "Suriya", "Livan", "Misr"]
            },
            {
                "question": "Dunyodagi eng katta yarim orollardan biri — Iberiya yarim oroli qaysi davlatlarga tegishli?",
                "answer": "Ispaniya va Portugaliya",
                "options": ["Fransiya va Italiya", "Ispaniya va Portugaliya", "Turkiya va Gretsiya", "Angliya va Irlandiya"]
            },
            {
                "question": "Dunyoning eng mashhur tog‘ cho‘qqilaridan biri — K2 qayerda joylashgan?",
                "answer": "Pokiston va Xitoy",
                "options": ["Pokiston va Xitoy", "Nepal va Xitoy", "Hindiston va Tibet", "Butan va Hindiston"]
            },
            {
                "question": "O‘zbekistonning mashhur yozuvchilaridan biri — O‘tkir Hoshimov mashhur asari?",
                "answer": "Ikki eshik orasi",
                "options": ["Ikki eshik orasi", "Dunyoning ishlari", "Sarob", "Shaytanat"]
            },
            {
                "question": "Afrikadagi eng katta davlat maydon bo‘yicha?",
                "answer": "Jazoir",
                "options": ["Jazoir", "Misr", "Sudan", "Efiopiya"]
            },
            {
                "question": "O‘zbekiston hududidagi qadimiy yodgorliklardan biri — Shohi Zinda majmuasi qayerda?",
                "answer": "Samarqand",
                "options": ["Samarqand", "Buxoro", "Xiva", "Toshkent"]
            },
            {
                "question": "Dunyoning eng mashhur minoralaridan biri — CN Tower qayerda joylashgan?",
                "answer": "Kanada",
                "options": ["Kanada", "AQSh", "Fransiya", "Germaniya"]
            },
            {
                "question": "Buyuk olim Arximedning mashhur iborasi?",
                "answer": "Menga tayanch nuqta bering, men Yer sharini ko‘taraman",
                "options": ["Menga tayanch nuqta bering, men Yer sharini ko‘taraman", "Bilim kuchdir", "Men o‘ylayman, demak men borman", "Hammasi oqimda"]
            },
            {
                "question": "O‘zbekistonning mashhur shaharlaridan biri — Qo‘qon qaysi tarixiy davrda xonlik markazi bo‘lgan?",
                "answer": "XVIII-XIX asr",
                "options": ["XVIII-XIX asr", "XVI asr", "XIV-XV asr", "XX asr"]
            }
        ]
   
        quiz_10 = [
            # Diniy savollar 50ta
            {
                "question": "Qur’onda eng qisqa sura?",
                "answer": "Kavsar",
                "options": ["Kavsar", "Ikhlos", "Nas", "Falaq"]
            },
            {
                "question": "Qur’on oyatlari necha xil suralardan iborat?",
                "answer": "Makkiy va Madaniy",
                "options": ["Makkiy va Madaniy", "Uzoq va qisqa", "Katta va kichik", "Arabiy va Ajamiy"]
            },
            {
                "question": "Namoz oxirida chap va o‘ng tomonga qarab nima aytiladi?",
                "answer": "Salom",
                "options": ["Salom", "Taslim", "Takbir", "Dua"]
            },
            {
                "question": "Namozda ruku’dan keyin nima qilinadi?",
                "answer": "Sajda",
                "options": ["Sajda", "Qiyom", "Jalsa", "Salom"]
            },
            {
                "question": "Islomning ikkinchi ustuni nima?",
                "answer": "Namoz",
                "options": ["Namoz", "Ro‘za", "Haj", "Zakot"]
            },
            {
                "question": "Islomning uchinchi ustuni nima?",
                "answer": "Zakot",
                "options": ["Zakot", "Haj", "Ro‘za", "Namoz"]
            },
            {
                "question": "Islomning to‘rtinchi ustuni nima?",
                "answer": "Ro‘za",
                "options": ["Ro‘za", "Zakot", "Haj", "Shahodat"]
            },
            {
                "question": "Islomning beshinchi ustuni nima?",
                "answer": "Haj",
                "options": ["Haj", "Ro‘za", "Zakot", "Namoz"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) tug‘ilgan yillari qanday ataladi?",
                "answer": "Fil yili",
                "options": ["Fil yili", "Hijrat yili", "Ramazon yili", "Isro yili"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.) nechchi yoshlarida payg‘ambar bo‘lganlar?",
                "answer": "40 yosh",
                "options": ["40 yosh", "30 yosh", "25 yosh", "50 yosh"]
            },
            {
                "question": "Payg‘ambarimizning birinchi vahiy qabul qilgan joylari?",
                "answer": "Hiro g‘ori",
                "options": ["Hiro g‘ori", "Saur g‘ori", "Uhud tog‘i", "Tur tog‘i"]
            },
            {
                "question": "Hajda Safa va Marva oralig‘ida yurish amali nima deb ataladi?",
                "answer": "Sa’y",
                "options": ["Sa’y", "Tavof", "Wuquf", "Tahallul"]
            },
            {
                "question": "Ka’bani aylanib yurish amali nima?",
                "answer": "Tavof",
                "options": ["Tavof", "Sa’y", "Wuquf", "Qasr"]
            },
            {
                "question": "Arafotda turish amali nima deb ataladi?",
                "answer": "Wuquf",
                "options": ["Wuquf", "Tavof", "Sa’y", "Tahallul"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ning ota tarafdan bobolari kim?",
                "answer": "Abdulmuttalib",
                "options": ["Abdulmuttalib", "Abu Tolib", "Hamza", "Abbos"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) amakilaridan islom dushmani bo‘lgani kim edi?",
                "answer": "Abu Lahab",
                "options": ["Abu Lahab", "Abu Tolib", "Hamza", "Abbos"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) amakilaridan musulmon bo‘lgani kim edi?",
                "answer": "Hamza",
                "options": ["Hamza", "Abu Tolib", "Abu Lahab", "Abbos"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) amakilaridan yana musulmon bo‘lgani kim edi?",
                "answer": "Abbos",
                "options": ["Abbos", "Hamza", "Abu Lahab", "Abu Tolib"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) hijrat chog‘ida yashiringan g‘or nomi?",
                "answer": "Saur g‘ori",
                "options": ["Saur g‘ori", "Hiro g‘ori", "Uhud g‘ori", "Tur tog‘i"]
            },
            {
                "question": "Musulmonlarga birinchi azonni aytgan sahoba kim?",
                "answer": "Bilol Habashiy",
                "options": ["Bilol Habashiy", "Abu Hurayra", "Ali", "Umar"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) eng yaqin do‘stlari va birinchi xalifa kim?",
                "answer": "Abu Bakr",
                "options": ["Abu Bakr", "Umar", "Usmon", "Ali"]
            },
            {
                "question": "Payg‘ambarimizdan (s.a.v.) keyingi ikkinchi xalifa kim?",
                "answer": "Umar ibn Xattob",
                "options": ["Umar ibn Xattob", "Abu Bakr", "Usmon", "Ali"]
            },
            {
                "question": "Payg‘ambarimizdan (s.a.v.) keyingi uchinchi xalifa kim?",
                "answer": "Usmon ibn Affon",
                "options": ["Usmon ibn Affon", "Ali ibn Abu Tolib", "Umar ibn Xattob", "Abu Bakr"]
            },
            {
                "question": "Payg‘ambarimizdan (s.a.v.) keyingi to‘rtinchi xalifa kim?",
                "answer": "Ali ibn Abu Tolib",
                "options": ["Ali ibn Abu Tolib", "Usmon ibn Affon", "Umar ibn Xattob", "Abu Bakr"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) eng mashhur asboblaridan biri?",
                "answer": "Asa",
                "options": ["Asa", "Qilich", "Qalqon", "Bayroq"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) eng mashhur qilichlari?",
                "answer": "Zulfikor",
                "options": ["Zulfikor", "Samsom", "Saqb", "Qasvo"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) sevimli otlari?",
                "answer": "Qasvo",
                "options": ["Qasvo", "Duldul", "Sakb", "Uqob"]
            },
            {
                "question": "Qur’onning nechanchi surasi Yosin?",
                "answer": "36-surasi",
                "options": ["36-surasi", "30-surasi", "40-surasi", "50-surasi"]
            },
            {
                "question": "Qur’onning nechanchi surasi Rahmon?",
                "answer": "55-surasi",
                "options": ["55-surasi", "50-surasi", "60-surasi", "65-surasi"]
            },
            {
                "question": "Qur’onning nechanchi surasi Ikhlos?",
                "answer": "112-surasi",
                "options": ["112-surasi", "110-surasi", "114-surasi", "111-surasi"]
            },
            {
                "question": "Qur’onning nechanchi surasi Nas?",
                "answer": "114-surasi",
                "options": ["114-surasi", "113-surasi", "112-surasi", "111-surasi"]
            },
            {
                "question": "Qur’onning nechanchi surasi Falaq?",
                "answer": "113-surasi",
                "options": ["113-surasi", "114-surasi", "112-surasi", "111-surasi"]
            },
            {
                "question": "Qur’onning nechanchi surasi Kavsar?",
                "answer": "108-surasi",
                "options": ["108-surasi", "109-surasi", "107-surasi", "110-surasi"]
            },
            {
                "question": "Qur’onda eng uzun oyat qaysi surada?",
                "answer": "Baqara 282-oyat",
                "options": ["Baqara 282-oyat", "Maida 5-oyat", "Niso 12-oyat", "Ali Imron 100-oyat"]
            },
            {
                "question": "Qur’onning birinchi so‘zi nima?",
                "answer": "Iqro’",
                "options": ["Iqro’", "Bismillah", "Alhamdu", "Qul"]
            },
            {
                "question": "Qur’onning eng oxirgi nozil bo‘lgan surasi?",
                "answer": "Nasr surasi",
                "options": ["Nasr surasi", "Maida surasi", "Tavba surasi", "Baqara surasi"]
            },
            {
                "question": "Qur’on oyatlarida eng ko‘p qaytarilgan kalima?",
                "answer": "Rahmat",
                "options": ["Rahmat", "Ilm", "Sabr", "Taqvo"]
            },
            {
                "question": "Ramazon kechasida eng fazilatli kecha qaysi?",
                "answer": "Laylatul Qadr",
                "options": ["Laylatul Qadr", "Laylatul Bara’a", "Laylatul Hijrat", "Laylatul Mawlid"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ning oxirgi hajlari qanday nomlanadi?",
                "answer": "Vido haji",
                "options": ["Vido haji", "Hijrat haji", "Birinchi haj", "Umra"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.) hijrat qilgan yilda musulmon taqvimi boshlanganmi?",
                "answer": "Ha",
                "options": ["Ha", "Yo‘q", "Faqat Ramazonda", "Faqat Hajda"]
            },
            {
                "question": "Ramazonda kechqurun o‘qiladigan namoz?",
                "answer": "Tarovih",
                "options": ["Tarovih", "Tahajjud", "Witr", "Juma"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) sevimli ichimliklaridan biri?",
                "answer": "Asal suvi",
                "options": ["Asal suvi", "Suv", "Sut", "Xurmo sharbat"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) sevimli taomlaridan biri?",
                "answer": "Xurmo",
                "options": ["Xurmo", "Non", "Asal", "Sut"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) sevimli hayvonlaridan biri?",
                "answer": "Mushuk",
                "options": ["Mushuk", "It", "Sigir", "Qoy"]
            },
            {
                "question": "Payg‘ambarimizning (s.a.v.) eng mashhur hadislaridan biri?",
                "answer": "Din nasihatdir",
                "options": ["Din nasihatdir", "Ilm farzdir", "Sabr imondandir", "Duo qalb qurolidir"]
            },
            {
                "question": "Qur’onning eng mashhur duo oyati?",
                "answer": "Baqara 201",
                "options": ["Baqara 201", "Yunus 85", "Niso 100", "Tavba 90"]
            },
            {
                "question": "Musulmonlar uchun eng muhim duo kalimasi?",
                "answer": "Amin",
                "options": ["Amin", "Subhanalloh", "Alhamdulillah", "Allohu akbar"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ga birinchi bo‘lib iymon keltirgan erkak?",
                "answer": "Abu Bakr",
                "options": ["Abu Bakr", "Ali", "Umar", "Usmon"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ga birinchi bo‘lib iymon keltirgan ayol?",
                "answer": "Xadicha",
                "options": ["Xadicha", "Ayshe", "Hafsa", "Maryam"]
            },
            {
                "question": "Payg‘ambarimiz (s.a.v.)ga birinchi bo‘lib iymon keltirgan bola?",
                "answer": "Ali ibn Abu Tolib",
                "options": ["Ali ibn Abu Tolib", "Hasan", "Husayn", "Abbos"]
            },
            # Fanga oid savollar 100ta
            {
                "question": "Buyuk ipak yo‘li nechta qit’ani bog‘lagan?",
                "answer": "2 qit’a - Osiyo va Yevropa",
                "options": ["Afrika va Osiyo", "2 qit’a - Osiyo va Yevropa", "Amerika va Osiyo", "Yevropa va Afrika"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan eng baland cho‘qqi nechchi metr?",
                "answer": "4643 metr",
                "options": ["4643 metr", "5120 metr", "4300 metr", "4790 metr"]
            },
            {
                "question": "Dunyodagi eng qadimiy yozuv tizimlaridan biri?",
                "answer": "Mixxat",
                "options": ["Lotin yozuvi", "Mixxat", "Arab yozuvi", "Sanskrit"]
            },
            {
                "question": "Qaysi davlat 'Inkalar imperiyasi'ning vatani?",
                "answer": "Peru",
                "options": ["Peru", "Meksika", "Boliviya", "Ekvador"]
            },
            {
                "question": "Qaysi yozuvchi 'Ilahi komediya' asarini yozgan?",
                "answer": "Dante Aligyeriy",
                "options": ["Gyote", "Balzak", "Dante Aligyeriy", "Shiller"]
            },
            {
                "question": "O‘zbekistonda eng katta tabiiy gaz konlaridan biri?",
                "answer": "Qandim",
                "options": ["Sho‘rtan", "Muborak", "Qandim", "Gazli"]
            },
            {
                "question": "Yer sharining eng quruq cho‘li?",
                "answer": "Atakama",
                "options": ["Gobi", "Atakama", "Lut cho‘li", "Sahroi Kabir"]
            },
            {
                "question": "Qaysi davlat 'Suvoqlar mamlakati' sifatida mashhur?",
                "answer": "Misr",
                "options": ["Misr", "Yaponiya", "Xitoy", "Gretsiya"]
            },
            {
                "question": "Sharq mutafakkiri Forobiy qaysi sohada mashhur?",
                "answer": "Falsafa",
                "options": ["Matematika", "Falsafa", "Tibbiyot", "Astronomiya"]
            },
            {
                "question": "Buyuk fransuz yozuvchisi Viktor Gyugoning mashhur asari?",
                "answer": "Notre-Dame qozoni (Quasimodo)",
                "options": ["Urush va tinchlik", "Notre-Dame qozoni (Quasimodo)", "Otello", "Don Kixot"]
            },
            {
                "question": "Qaysi davlatning milliy sporti 'Gaelik futboli'?",
                "answer": "Irlandiya",
                "options": ["Irlandiya", "Shotlandiya", "Angliya", "Vels"]
            },
            {
                "question": "Yer sharidagi eng sovuq okean?",
                "answer": "Shimoliy Muz okeani",
                "options": ["Atlantika", "Tinch okeani", "Shimoliy Muz okeani", "Hind okeani"]
            },
            {
                "question": "Buyuk Aleksandrning ustozlaridan biri kim edi?",
                "answer": "Aristotel",
                "options": ["Aristotel", "Platon", "Sokrat", "Pifagor"]
            },
            {
                "question": "O‘zbekistonda eng katta suv omborlaridan biri?",
                "answer": "Tuyamo‘yin",
                "options": ["Chorvoq", "To‘dako‘l", "Tuyamo‘yin", "Bo‘zsuv"]
            },
            {
                "question": "Qaysi yozuvchi 'Madam Bovari' romanini yozgan?",
                "answer": "Gustav Flaubert",
                "options": ["Balzak", "Stendal", "Gustav Flaubert", "Tolstoy"]
            },
            {
                "question": "Qaysi davlat poytaxti Suva?",
                "answer": "Fiji",
                "options": ["Fiji", "Kiribati", "Tonga", "Mikroneziya"]
            },
            {
                "question": "Dunyoning eng baland tog‘ dovoni?",
                "answer": "Thorong La (Nepal)",
                "options": ["Thorong La (Nepal)", "Tyan-Shan", "And", "Altay"]
            },
            {
                "question": "Qaysi yozuvchi 'Odyssey' asarini yozgan?",
                "answer": "Gomer",
                "options": ["Gomer", "Vergiliy", "Sofokl", "Aristotel"]
            },
            {
                "question": "Qaysi davlat poytaxti Tashkent?",
                "answer": "O‘zbekiston",
                "options": ["Tojikiston", "O‘zbekiston", "Qozog‘iston", "Turkmaniston"]
            },
            {
                "question": "Yer yuzidagi eng katta tog‘ tizmasi qaysi?",
                "answer": "And tog‘lari",
                "options": ["And tog‘lari", "Gimolay", "Alp", "Kavkaz"]
            },
            {
                "question": "Qaysi yozuvchi 'Qonli uy' dramasini yozgan?",
                "answer": "Garcia Lorka",
                "options": ["Garcia Lorka", "Kafka", "Dikkens", "Pushkin"]
            },
            {
                "question": "Dunyoning eng qadimiy shaharlardan biri - Quddus qaysi hududda?",
                "answer": "Falastin",
                "options": ["Misr", "Falastin", "Livan", "Suriya"]
            },
            {
                "question": "Sharq mutafakkiri Mahmud Qoshg‘ariy mashhur asari?",
                "answer": "Devonu lug‘otit turk",
                "options": ["Qutadg‘u bilig", "Devonu lug‘otit turk", "Xamsa", "Shohnoma"]
            },
            {
                "question": "Qaysi davlatda Angkor-Vat ibodatxonasi joylashgan?",
                "answer": "Kambodja",
                "options": ["Kambodja", "Hindiston", "Indoneziya", "Vyetnam"]
            },
            {
                "question": "Yer sharining eng baland poytaxt shahri?",
                "answer": "La-Pas (Boliviya)",
                "options": ["La-Pas (Boliviya)", "Quito", "Katmandu", "Karakas"]
            },
            {
                "question": "Qaysi yozuvchi 'Shifo ilmi' asarini yozgan?",
                "answer": "Ibn Sino",
                "options": ["Ibn Sino", "Beruniy", "Navoiy", "Qoshg‘ariy"]
            },
            {
                "question": "Dunyodagi eng katta ko‘ldan ham kattaroq yopiq suv havzasi?",
                "answer": "Kaspiy dengizi",
                "options": ["O‘lik dengiz", "Kaspiy dengizi", "Qora dengiz", "Aral dengizi"]
            },
            {
                "question": "Qaysi davlat poytaxti Katmandu?",
                "answer": "Nepal",
                "options": ["Butan", "Nepal", "Hindiston", "Pokiston"]
            },
            {
                "question": "Buyuk yunon dramaturgi Sofokl mashhur asari?",
                "answer": "Shoh Edip",
                "options": ["Shoh Edip", "Odyssey", "Iliada", "Qizil va qora"]
            },
            {
                "question": "Yer kurrasida eng ko‘p vulqonlar joylashgan davlat?",
                "answer": "Indoneziya",
                "options": ["Indoneziya", "Yaponiya", "Italiya", "Meksika"]
            },
            {
                "question": "O‘zbek xalqining eng mashhur eposlaridan biri?",
                "answer": "Alpomish",
                "options": ["Alpomish", "Shohnoma", "Manas", "Qutadg‘u bilig"]
            },
            {
                "question": "Dunyoning eng yirik arxipelagi?",
                "answer": "Indoneziya",
                "options": ["Filippin", "Indoneziya", "Yaponiya", "Maldiv"]
            },
            {
                "question": "Buyuk yunon faylasufi Sokrat nima bilan mashhur?",
                "answer": "Dialogik usul",
                "options": ["Dialogik usul", "Astronomiya", "Tibbiyot", "Adabiyot"]
            },
            {
                "question": "Qaysi davlat poytaxti Ulan-Bator?",
                "answer": "Mongoliya",
                "options": ["Mongoliya", "Rossiya", "Qozog‘iston", "Tojikiston"]
            },
            {
                "question": "Yer yuzidagi eng sho‘r suvli dengiz?",
                "answer": "O‘lik dengiz",
                "options": ["O‘lik dengiz", "Kaspiy", "Qora dengiz", "Adriatika"]
            },
            {
                "question": "Qaysi yozuvchi 'Gulliverning sayohatlari' asarini yozgan?",
                "answer": "Jonatan Svift",
                "options": ["Mark Tven", "Jonatan Svift", "Defo", "Balzak"]
            },
            {
                "question": "Buyuk alloma Beruniy mashhur asari?",
                "answer": "Qadimgi xalqlardan qolgan yodgorliklar",
                "options": ["Qadimgi xalqlardan qolgan yodgorliklar", "Shohnoma", "Xamsa", "Devonu lug‘otit turk"]
            },
            {
                "question": "Dunyoning eng katta sharsharasi suv hajmi bo‘yicha?",
                "answer": "Inga sharsharasi",
                "options": ["Niagara", "Victoria", "Inga sharsharasi", "Iguasu"]
            },
            {
                "question": "Qaysi davlat 'ko‘plab orollar mamlakati' deb ataladi?",
                "answer": "Filippin",
                "options": ["Filippin", "Yaponiya", "Norvegiya", "Indoneziya"]
            },
            {
                "question": "Yer kurrasidagi eng baland minoralardan biri - CN Tower qayerda joylashgan?",
                "answer": "Kanada",
                "options": ["Kanada", "AQSh", "Xitoy", "BAA"]
            },
            {
                "question": "Qaysi yozuvchi 'Yuz yil yolg‘izlik' asarini yozgan?",
                "answer": "Gabriel Garsia Markes",
                "options": ["Gabriel Garsia Markes", "Borges", "Isabel Allende", "Mario Vargas Losa"]
            },
            {
                "question": "Sharq mutafakkiri Yusuf Xos Hojib asari?",
                "answer": "Qutadg‘u bilig",
                "options": ["Qutadg‘u bilig", "Devonu lug‘otit turk", "Shohnoma", "Xamsa"]
            },
            {
                "question": "Yer kurrasidagi eng katta yarim orol?",
                "answer": "Arabiston yarim oroli",
                "options": ["Arabiston yarim oroli", "Iberiya", "Skandinaviya", "Hindiston yarim oroli"]
            },
            {
                "question": "Qaysi yozuvchi 'Forslar' tragediyasini yozgan?",
                "answer": "Aysxil",
                "options": ["Sofokl", "Evripid", "Aysxil", "Aristofan"]
            },
            {
                "question": "Yer yuzidagi eng baland ko‘prik — Millau Viaduct qaysi davlatda?",
                "answer": "Fransiya",
                "options": ["AQSh", "Fransiya", "Xitoy", "Italiya"]
            },
            {
                "question": "O‘zbekiston hududida necha xil iqlim tipi mavjud?",
                "answer": "3",
                "options": ["2", "3", "4", "5"]
            },
            {
                "question": "Qaysi davlatning rasmiy poytaxti va hukumat poytaxti turlicha shaharlarda joylashgan?",
                "answer": "Janubiy Afrika",
                "options": ["Janubiy Afrika", "Braziliya", "Avstraliya", "Kanada"]
            },
            {
                "question": "Qaysi yozuvchi 'Choliqushi' romanini yozgan?",
                "answer": "Reshod Nuri Guntekin",
                "options": ["Reshod Nuri Guntekin", "Orxon Pamuk", "Nazim Hikmat", "Tolstoy"]
            },
            {
                "question": "Yer yuzida eng baland daryo sharsharasi qaysi?",
                "answer": "Anxel",
                "options": ["Niagara", "Victoria", "Anxel", "Iguasu"]
            },
            {
                "question": "Qaysi davlatda eng qadimiy parlament — Alting mavjud?",
                "answer": "Islandiya",
                "options": ["Islandiya", "Norvegiya", "Angliya", "Shvetsiya"]
            },
            {
                "question": "Buyuk yozuvchi Alber Kamyu mashhur asari?",
                "answer": "Begona",
                "options": ["Begona", "Jarayon", "Sariq devni minib", "Shohnoma"]
            },
            {
                "question": "Sharq mutafakkiri Umar Xayyom nima bilan mashhur?",
                "answer": "Ruboiatlar",
                "options": ["Ruboiatlar", "Shohnoma", "Xamsa", "Qutadg‘u bilig"]
            },
            {
                "question": "Qaysi davlatning poytaxti Valetta?",
                "answer": "Malta",
                "options": ["Malta", "Kipr", "Andorra", "San-Marino"]
            },
            {
                "question": "Yer sharida eng uzun orol zanjiri?",
                "answer": "Kuril orollari",
                "options": ["Kuril orollari", "Aleut orollari", "Filippin orollari", "Malay arxipelagi"]
            },
            {
                "question": "Qaysi yozuvchi 'Karamazov aka-ukalari' asarini yozgan?",
                "answer": "Dostoyevskiy",
                "options": ["Dostoyevskiy", "Tolstoy", "Gogol", "Chexov"]
            },
            {
                "question": "Qaysi davlatda Mo‘g‘ul imperiyasi paydo bo‘lgan?",
                "answer": "Mongoliya",
                "options": ["Mongoliya", "Xitoy", "Rossiya", "Qozog‘iston"]
            },
            {
                "question": "Buyuk yunon olimi Pifagor mashhur asari?",
                "answer": "Pifagor teoremasi",
                "options": ["Pifagor teoremasi", "Arximed qonuni", "Nyuton qonuni", "Eynshteyn nazariyasi"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan eng qadimiy karvonsaroy qoldiqlari?",
                "answer": "Raboti Malik",
                "options": ["Raboti Malik", "Ko‘hna Urganch", "Ark", "Ellikqal’a"]
            },
            {
                "question": "Yer sharidagi eng katta ichki cho‘l?",
                "answer": "Gobi",
                "options": ["Gobi", "Karakum", "Kizilqum", "Sahroi Kabir"]
            },
            {
                "question": "Qaysi yozuvchi 'Falsafiy maktublar' asarini yozgan?",
                "answer": "Volter",
                "options": ["Volter", "Russo", "Gyote", "Makiavelli"]
            },
            {
                "question": "Qaysi davlatning milliy sporti regbi?",
                "answer": "Yangi Zelandiya",
                "options": ["Yangi Zelandiya", "Janubiy Afrika", "Avstraliya", "Angliya"]
            },
            {
                "question": "Buyuk mutafakkir Alisher Navoiyning tug‘ilgan yili?",
                "answer": "1441",
                "options": ["1441", "1501", "1397", "1456"]
            },
            {
                "question": "Yer sharidagi eng katta sho‘r ko‘l?",
                "answer": "Qaspiy dengizi",
                "options": ["Qaspiy dengizi", "O‘lik dengiz", "Tuzko‘l", "Qora dengiz"]
            },
            {
                "question": "Qaysi yozuvchi 'Chol va dengiz' asarini yozgan?",
                "answer": "Ernest Xeminguey",
                "options": ["Ernest Xeminguey", "Jek London", "Mark Tven", "Balzak"]
            },
            {
                "question": "O‘zbekiston hududidagi eng yirik mis koni?",
                "answer": "Olmaliq",
                "options": ["Olmaliq", "Angren", "Qizilqum", "Zarafshon"]
            },
            {
                "question": "Dunyodagi eng qadimiy shahar sifatida tanilgan?",
                "answer": "Jerixo",
                "options": ["Quddus", "Jerixo", "Afina", "Damashq"]
            },
            {
                "question": "Qaysi yozuvchi 'Qizil chiroqlar' asarini yozgan?",
                "answer": "Abdulla Qahhor",
                "options": ["Abdulla Qahhor", "Cho‘lpon", "Oybek", "Erkin Vohidov"]
            },
            {
                "question": "Yer sharidagi eng chuqur vodiy?",
                "answer": "Kolorado Kanyoni",
                "options": ["Kolorado Kanyoni", "Yarlung", "Pamir", "Hindukush"]
            },
            {
                "question": "Buyuk faylasuf Platon mashhur asari?",
                "answer": "Davlat",
                "options": ["Davlat", "Etika", "Dialoglar", "Metafizika"]
            },
            {
                "question": "Qaysi davlatning poytaxti Ashxobod?",
                "answer": "Turkmaniston",
                "options": ["Turkmaniston", "Tojikiston", "O‘zbekiston", "Qozog‘iston"]
            },
            {
                "question": "Sharq mutafakkiri Ibn Xaldun nima bilan mashhur?",
                "answer": "Tarixshunoslik asoschisi",
                "options": ["Tarixshunoslik asoschisi", "Astronomiya", "Tibbiyot", "Matematika"]
            },
            {
                "question": "Qaysi yozuvchi 'Sho‘rodan qolgan odamlar' asarini yozgan?",
                "answer": "Pirimqul Qodirov",
                "options": ["Pirimqul Qodirov", "O‘tkir Hoshimov", "Tahir Malik", "Navoiy"]
            },
            {
                "question": "Yer sharidagi eng qadimiy teatr binolaridan biri?",
                "answer": "Afina Dionis teatri",
                "options": ["Afina Dionis teatri", "Rim Kolizey", "Bolshoy teatr", "London Globe"]
            },
            {
                "question": "Qaysi davlatning milliy sporti hurling?",
                "answer": "Irlandiya",
                "options": ["Irlandiya", "Angliya", "Shotlandiya", "Kanada"]
            },
            {
                "question": "Yer sharida eng katta ko‘rfaz?",
                "answer": "Bengal ko‘rfazi",
                "options": ["Bengal ko‘rfazi", "Meksika ko‘rfazi", "Aden ko‘rfazi", "Pers ko‘rfazi"]
            },
            {
                "question": "Qaysi davlatda 'Terrakota askarlari' topilgan?",
                "answer": "Xitoy",
                "options": ["Xitoy", "Yaponiya", "Koreya", "Hindiston"]
            },
            {
                "question": "Buyuk yozuvchi Balzak mashhur asari?",
                "answer": "Inson komediyasi",
                "options": ["Inson komediyasi", "Anna Karenina", "Jarayon", "Urush va tinchlik"]
            },
            {
                "question": "Qaysi davlatning poytaxti Vena?",
                "answer": "Avstriya",
                "options": ["Avstriya", "Shveytsariya", "Germaniya", "Chexiya"]
            },
            {
                "question": "Yer sharidagi eng katta cho‘l qaysi?",
                "answer": "Antarktida cho‘li",
                "options": ["Antarktida cho‘li", "Sahroi Kabir", "Gobi", "Atakama"]
            },
            {
                "question": "Qaysi yozuvchi 'Manas' eposi bilan mashhur?",
                "answer": "Qirg‘iz xalqi",
                "options": ["Qirg‘iz xalqi", "O‘zbek xalqi", "Qozoq xalqi", "Turkman xalqi"]
            },
            {
                "question": "Buyuk yunon faylasufi Aristotel mashhur asari?",
                "answer": "Metafizika",
                "options": ["Metafizika", "Dialoglar", "Davlat", "Etika"]
            },
            {
                "question": "Qaysi davlatning poytaxti Bogota?",
                "answer": "Kolumbiya",
                "options": ["Kolumbiya", "Venesuela", "Ekvador", "Peru"]
            },
            {
                "question": "Sharq mutafakkiri Al-Kindiy nima bilan mashhur?",
                "answer": "Islom falsafasi asoschisi",
                "options": ["Islom falsafasi asoschisi", "Astronom", "Tibbiyotchi", "Matematik"]
            },
            {
                "question": "Qaysi yozuvchi 'O‘tkan kunlar' romanini yozgan?",
                "answer": "Abdulla Qodiriy",
                "options": ["Abdulla Qodiriy", "Cho‘lpon", "Oybek", "Tahir Malik"]
            },
            {
                "question": "Yer sharidagi eng yirik plato?",
                "answer": "Tibet platosi",
                "options": ["Tibet platosi", "Pamir", "And", "Altay"]
            },
            {
                "question": "Qaysi davlat 'Ko‘hna Rim davlati'ning markazi edi?",
                "answer": "Italiya",
                "options": ["Italiya", "Gretsiya", "Fransiya", "Ispaniya"]
            },
            {
                "question": "Buyuk mutafakkir Erkin Vohidov mashhur asari?",
                "answer": "Ruhlar isyoni",
                "options": ["Ruhlar isyoni", "O‘tkan kunlar", "Shohnoma", "Qiyomat"]
            },
            {
                "question": "Buyuk yunon tarixchisi Gerodot qaysi asari bilan mashhur?",
                "answer": "Tarix",
                "options": ["Tarix", "Davlat", "Dialoglar", "Shohnoma"]
            },
            {
                "question": "Yer sharidagi eng baland vodiy qaysi davlat hududida joylashgan?",
                "answer": "Nepal",
                "options": ["Nepal", "Tibet", "Butan", "Hindiston"]
            },
            {
                "question": "Qaysi yozuvchi 'Otamdan qolgan dalalar' asarini yozgan?",
                "answer": "O‘tkir Hoshimov",
                "options": ["O‘tkir Hoshimov", "Pirimqul Qodirov", "Tahir Malik", "Cho‘lpon"]
            },
            {
                "question": "Dunyoning eng katta okean oroli qaysi?",
                "answer": "Yangi Gvineya",
                "options": ["Yangi Gvineya", "Sumatra", "Borneo", "Madagaskar"]
            },
            {
                "question": "Sharq mutafakkiri Ibn Rushd nima bilan mashhur?",
                "answer": "Aristotel falsafasini sharhlash",
                "options": ["Aristotel falsafasini sharhlash", "Astronomiya", "Tibbiyot", "Adabiyot"]
            },
            {
                "question": "Qaysi davlatda Teotiuakan shahri joylashgan?",
                "answer": "Meksika",
                "options": ["Meksi  ka", "Peru", "Boliviya", "Ekvador"]
            },
            {
                "question": "Dunyoning eng mashhur sharsharalaridan biri — Tugela qaysi davlatda joylashgan?",
                "answer": "Janubiy Afrika",
                "options": ["Janubiy Afrika", "Namibiya", "Keniya", "Zimbabve"]
            },
            {
                "question": "O‘zbekiston hududida joylashgan qadimiy shaharlaridan biri — Termiz qaysi viloyatda?",
                "answer": "Surxondaryo",
                "options": ["Surxondaryo", "Buxoro", "Samarqand", "Xorazm"]
            },
            {
                "question": "Dunyoning eng katta ko‘rfazlaridan biri?",
                "answer": "Bengal ko‘rfazi",
                "options": ["Bengal ko‘rfazi", "Meksika ko‘rfazi", "Pers ko‘rfazi", "Aden ko‘rfazi"]
            },
            {
                "question": "Buyuk yozuvchi Abdulla Qahhor mashhur asarlaridan biri?",
                "answer": "Anor",
                "options": ["Anor", "Sarob", "O‘tkan kunlar", "Sinchalak"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur masjidlardan biri — Hazrati Imom majmuasi qayerda joylashgan?",
                "answer": "Toshkent",
                "options": ["Toshkent", "Samarqand", "Buxoro", "Andijon"]
            },
            {
                "question": "Dunyoning eng mashhur muzeylaridan biri — Eremitaj qayerda joylashgan?",
                "answer": "Sankt-Peterburg",
                "options": ["Sankt-Peterburg", "Moskva", "Parij", "Berlin"]
            },
            {
                "question": "O‘zbekiston hududidagi mashhur qal’alardan biri — Ark qaysi shaharda?",
                "answer": "Buxoro",
                "options": ["Buxoro", "Samarqand", "Xiva", "Shahrisabz"]
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
