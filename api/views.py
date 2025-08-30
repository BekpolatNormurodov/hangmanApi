from rest_framework.views import APIView
from rest_framework.response import Response
import random





class TasodifyAPI(APIView):
    def get(self, request):
        names = "Abbos", "Abdulaziz", "Abdulloh", "Abror", "Adham", "Akbar", "Akmal", "Alisher", "Amir", "Amirbek", "Amirxon", "Anvar", "Asad", "Asliddin", "Asror", "Azamat", "Azimjon", "Aziz", "Azizbek", "Baxtiyor", "Bekmurod", "Bekzod", "Bilol", "Bobur", "Botir", "Davron", "Dilshod", "Elyor", "Ergash", "Erkin", "Farruh", "Farrux", "Farhod", "Fayzulla", "Firdavs", "Habib", "Habibulloh", "Hakim", "Hamid", "Hamza", "Hasan", "Hasanboy", "Hikmat", "Hikmatulloh", "Hojiakbar", "Humoyun", "Husan", "Husanboy", "Husniddin", "Ilhom", "Iskandar", "Islom", "Ismoil", "Ibrohim", "Jamol", "Jamshid", "Jaloliddin", "Jasur", "Javlon", "Javohir", "Karim", "Kamoliddin", "Komil", "Laziz", "Lochin", "Lutfulla", "Madamin", "Mahmud", "Malik", "Mansur", "Mashrab", "Mirjalol", "Mirkomil", "Mironshoh", "Murod", "Muhriddin", "Muhammad", "Muzaffar", "Najmiddin", "Nodir", "Nurbek", "Nuriddin", "Odil", "Olim", "Oybek", "Qahhor", "Qahramon", "Qobil", "Qodir", "Qosim", "Qurbon", "Quvonch", "Rahim", "Rashid", "Ravshan", "Rustam", "Rustamjon", "Samandar", "Sanjar", "Sardor", "Sarvar", "Said", "Shahboz", "Shahriyor", "Shahzod", "Shams", "Shamsiddin", "Shavkat", "Sherali", "Sherzod", "Shodiyor", "Shodmon", "Shokir", "Shohjahon", "Shohruh", "Siroj", "Sirojiddin", "Sobir", "Sobit", "Sodiq", "Sohib", "Suhrob", "Sulton", "Temur", "Tohir", "Tolib", "Ubaydulla", "Ubaydulloh", "Ulug'bek", "Umid", "Umar", "Usmon", "Valijon", "Vohid", "Xayrulloh", "Xojiakbar", "Xolmat", "Xudoyor", "Xurshid", "Yahyo", "Yodgor", "Yoqub", "Yunus", "Yusuf", "Zafar", "Zavqiddin", "Zayniddin", "Zohid", "Zokir", "Adolat", "Aziza", "Barno", "Dilafruz", "Dildora", "Dilnoza", "Feruza", "Fotima", "Gulbahor", "Gulchehra", "Gulhayo", "Gulnora", "Gulnoza", "Gulsanam", "Gulshan", "Gulruh", "Humora", "Husniya", "Iroda", "Kamola", "Kumush", "Lobar", "Malohat", "Manzura", "Mashhura", "Maftuna", "Mehribon", "Muhayyo", "Mubina", "Mukarram", "Muqaddas", "Munira", "Munisa", "Mushtariy", "Nilufar", "Nigora", "Nodira", "Nozima", "Ozoda", "Oysara", "Oygul", "Parizoda", "Rano", "Rayhona", "Ruxshona", "Saida", "Saodat", "Sanobar", "Shahlo", "Shahzoda", "Shamsiya", "Shoira", "Shukrona", "Surayyo", "Umida", "Xadicha", "Xalima", "Xilola", "Xosiyat", "Xurriyat", "Zarnigor", "Zebo", "Zilola", "Ziyoda", "Zuhra", "Madina", "Mahliyo", "Malika", "Mehriniso", "Muslima", "Nasiba", "Nafisa", "Nafosat", "Nargiza", "Nigina", "Robiya", "Sabina", "Sanam", "Shahrizoda", "Sitora", "Sadoqat", "Sohiba", "Tahmina", "Tomaris", "Zaynab", "Zulfiya", "Zarina", "Zarifa", "Asal", "Barchinoy", "Dilorom", "Dilshoda", "Firuza", "Gulandon", "Gulsara", "Halima", "Hanifa", "Husnora", "Jamila", "Karima", "Komila", "Lola", "Marhabo", "Munavvar", "Oysuluv", "Rano", "Sabohat", "Shirin", "Shohista", "Xonzoda", "Xurshida", "Zebiniso", "Dilnora", "Guljahon", "Guljamol", "Husniyo", "Iymona", "Latofat", "Nigoh", "Ruxsora", "Sabrina", "Shaxnoza", "Shodiyona", "Shohsanam", "Umriniso", "Xumora", "Zubayda", "Zulayho"
        colors = "Oq", "Qora", "Qizil", "Ko'k", "Yashil", "Sariq", "Malla", "Pushti", "Moviy", "Zangori", "Binafsha", "Kulrang", "Jigarrang"
        calendar = "Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr", "Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba", "Bahor", "Yoz", "Kuz", "Qish"
        animals = "It", "Mushuk", "Ot", "Sigir", "Qo'y", "Eshak", "Tovuq", "Xo'roz", "O'rdak", "G'oz", "Qo'zi", "Buqa", "Baliq", "Quyon", "Sher", "Arslon", "Yo'lbars", "Tulki", "Bo'ri", "Ayiq", "Chumchuq", "Qaldirg'och", "Qarg'a", "Qurbaqa", "Maymun", "Fil", "Jirafa", "Kapalak", "Asalari", "Chayon", "Ilon", "Sichqon", "Jayron", "Bug'u", "Burgut", "Qirg'iy", "Turna", "Tovus", "Toychoq", "Bo'taloq", "Echkichi", "Akula", "Delfin", "Timsah", "Pingvin", "Qoplon", "Tustovuq", "Baqa", "Tulpor", "Chittak", "Laylak", "Boyo'g'li", "Ohu", "Qunduz", "Bo'rsiq", "Kaptar", "Lochin", "Ko'rsichqon", "Toshbaqa", "Kalamush", "Tuya", "Qo'y", "Jayra", "Panda", "Koala", "Shilliqurt", "Qirg'ovul", "Kaklik", "O'rdak", "Chumoli", "Bo'g'mailon", "Mushuk", "Xo'tik", "Turna"
        fruit = "Olma", "Anor", "Uzum", "Nok", "Shaftoli", "Gilos", "Olcha", "Shaftoli", "Banan", "Apelsin", "Mandarin", "Limon", "Kivi", "Ananas", "Mango", "Papayya", "Avokado", "Kokos", "Injir", "Xurmo", "Tut", "Behi", "Qulupnay", "Malina", "Chernika", "Smorodina", "O'rik"
        vegetables = "Kartoshka", "Piyoz", "Sarimsoq", "Sabzi", "Bodring", "Pomidor", "Baqlajon", "Qalampir", "Karam", "Gulkaram", "Qovoq", "Kadi", "Turp", "Rediska", "Sholg'om", "Ismaloq", "Kashnich", "Ukrop", "Shivit", "Petrushka", "Zanjabil"
        ovqatlar = "Palov", "Kabob", "Sho'rva", "Mastava", "Dimlama", "Chuchvara", "Manti", "Norin", "Lag'mon", "Honim", "Barak", "Somsa", "Qazi", "Shashlik", "Jigar", "Beshbarmoq", "Halim", "Sumalak", "Burger", "Xotdog", "Shaurma", "Donar", "Lavash", "Pizza", "Sendvich", "Chizburger"
        obhavo = "Quyosh", "Bulut", "Yomg'ir", "Qor", "Shamol", "Jala", "Bo'ron", "Tornado", "Chaqmoq", "Momaqaldiroq", "Dovul"
        transport = "Mashina", "Avtobus", "Poyezd", "Samolyot", "Kema", "Traktor", "Velosiped", "Mototsikl", "Metro", "Skuter", "Tramvay", "Avtomobil"
        osimliklar = "Gul", "Lola", "Chinor", "Tol", "Terak", "Qayin", "Tut", "Kaktus"
        ichimlik = "Choy", "Qahva", "Sut", "Sharbat", "Suv", "Kefir", "Kompot", "CocaCola", "Pepsi", "Fanta", "Limonad", "Mors"
        fan = "Matematika", "Fizika", "Kimyo", "Biologiya", "Geografiya", "Astronomiya", "Informatika", "Tarix", "Adabiyot", "Tilshunoslik", "Psixologiya", "Iqtisodiyot", "Falsafa", "Huquq", "Tibbiyot", "Ekologiya", "Musiqa", "San'at", "Texnologiya", "Muhandislik", "Robototexnika", "Nanotexnologiya", "Genetika", "Geologiya", "Agronomiya"
        vaqt = "Sekund", "Minut", "Soat", "Kun", "Hafta", "Oy", "Yil", "Asr", "Tong", "Kech", "Tun"
        qurollar = "Qilich", "Nayza", "Kamon", "Xanjar", "Pichoq", "Qamchi", "Bolta", "Qalqon", "Miltiq", "Pistolet", "Avtomat", "Snayper", "Patron", "Granata", "Mina", "Raketa", "Yadro", "Zambarak", "Pulimyot", "Elektroshoker"
        musiqa_asboblari = "Doira", "Karnay", "Surnay", "G'ijjak", "Tanbur", "Dutor", "Rubob", "Tor", "Gitara", "Pianino", "Skripka", "Saksofon", "Baraban"
        oila_va_qarindoshlar = "Ota", "Ona", "Bola", "O'g'il", "Qiz", "Aka", "Uka", "Opa", "Singil", "Amaki", "Tog'a", "Xola", "Amma", "Buvi", "Bobo", "Kelin", "Kuyov", "Er", "Xotin", "Jiyan", "Nevara", "Chaqaloq", "Qaynona", "Qaynota", "Qaynuka", "Qaynsingil", "Qaynopa", "Nevara", "O'gayona", "O'gayota", "O'gayuka", "O'gayaka", "O'gayopa", "Buvijon", "Bobojon", "Opajon", "Akajon", "Ukajon", "Onajon", "Qizaloq", "Enaga", "Amakivachcha", "Qudag'ay", "Quda", "Qaynona", "Qaynota"
        human_body = "Bosh", "Soch", "Peshona", "Ko'z", "Qosh", "Kiprik", "Burun", "Lab", "Og'iz", "Tish", "Til", "Yonoq", "Jag'", "Quloq", "Bo'yin", "Tomoq", "Yelka", "Qo'l", "Bilak", "Kaft", "Barmoq", "Tirnoq", "Yurak", "O'pka", "Jigar", "Oshqozon", "Buyrak", "Ichak", "Bel", "Qorin", "Son", "Tizza", "Oyoq", "Tovon", "Skelet", "Suyak", "Muskul", "Tomir", "Asab", "Teri", "Qon", "Miya", "Umurtqa", "Qovurg'a"
        sports = "Futbol", "Boks", "Kurash", "Tennis", "Shaxmat", "Shashka", "Basketbol", "Voleybol", "Dzyudo", "Taekvondo", "Karate", "Sambo", "Suzish", "Gimnastika", "Velosport", "Handbol", "Xokkey", "Amerika futzal", "Beysbol", "Golf", "Bilyard", "O'qotish", "Yugurish", "Avtopoyga"
        maktab_anjomlar = "Daftar", "Qalam", "Ruchka", "Chizg'ich", "O'chirg'ich", "Qalamdon", "sumka", "Jild", "Doska", "Marker", "Bo'yoq", "Kley", "Qaychi", "Sirkul", "Proyektor", "Bo'r", "Jurnal", "Kitob", "Alifbo", "Kundalik"
        jobs = "O'qituvchi", "Shifokor", "Haydovchi", "Dehqon", "Oshpaz", "Quruvchi", "Tikuvchi", "Sartarosh", "Politsiya", "Harbiy", "Hamshira", "Sotuvchi", "Elektrik", "Santexnik", "Hisobchi", "Farmatsevt", "Muhandis", "Advokat", "Dasturchi", "Aktyor", "Qo'shiqchi", "Rassom", "Dizayner", "Fotograf", "Jurnalist", "Kutubxonachi", "Imom", "Ofitsiant", "Kassir", "Bankir", "Tadbirkor", "Mashinasoz", "Mexanik", "Fermer", "Veterinar", "Temirchi", "Duradgor", "Haykaltarosh", "Geodezist", "Tarjimon", "Professor", "Psixolog", "Arxitektor", "Astronom", "Robototexnik", "Hayvonotshunos", "Hacker", "Arxeolog", "O'rmonchi", "Iqtisodchi", "SMM", "Operator", "Rejissyor", "Musiqachi", "Dirijyor", "Sportchi", "Futbolchi", "Bokschi", "Kurashchi", "Trener", "Hakim", "Massajchi", "Hamomchi", "Instruktor", "Usta", "Elektrotexnik", "Energetik", "Konchi", "Neftchi", "Kimyogar", "Biolog", "Fizik", "Ximik", "Direktor", "Dekan", "Advokat", "Sudya", "Prokuror", "Notarius", "Banker", "Pochtalyon", "Uchuvchi", "Styuardessa", "Dengizchi"
        nature = "Quyosh", "Oy", "Yulduz", "Bulut", "Yomg'ir", "Qor", "Shamol", "Tog'", "Daraxt", "Gul", "O't", "Suv", "Ko'l", "Daryo", "Okean", "Cho'l", "Dasht", "O'rmon", "Tuproq", "Tosh", "Qoya", "Chashma", "Soy", "Vodiy", "Jar", "Ko'k", "Osmon", "Kamalak", "Nur", "Barg", "Shox", "Ildiz", "Giyoh", "Lola", "Chinor", "Terak", "Tol", "O'rik", "Chaman", "Bog'", "Gulzor", "O'tloq", "Dashtzor", "Cho'qqi", "Sahro", "Qumtepa", "Shag'al", "Ko'mir", "Neft", "Oltin", "Kumush", "Mis", "Qoyatosh", "Orol", "Sharshara", "G'or", "Buloq", "Bo'ron", "Jala", "Chaqmoq", "Momaqaldiroq", "Tornado", "Sel", "Zilzila", "Vulqon", "Lava", "Muzlik", "Aysberg", "Sahro", "Qum", "Dengiz"
        birds = "Qaldirg'och", "Bulbul", "Kaptar", "To'ti", "Qarg'a", "Turna", "Qirg'iy", "Burgut", "Boyqush", "Chumchuq", "Tovus", "Bedana", "O'rdak", "G'oz", "Tovuq", "Xo'roz", "Laylak", "Kaklik", "Qizilishton", "Qizilqanot"
        phones = "Apple", "Samsung", "Huawei", "Xiaomi", "Oppo", "Vivo", "Realme", "OnePlus", "Honor", "Motorola", "Nokia", "Sony", "Pixel", "ZTE", "Tecno", "Infinix", "Micromax", "Panasonic", "Philips", "Siemens"
        uzb_regions = "Toshkent", "Samarqand", "Buxoro", "Xiva", "Urganch", "Nukus", "Andijon", "Namangan", "Farg'ona", "Qo'qon", "Marg'ilon", "Qarshi", "Shahrisabz", "Guliston", "Termiz", "Chirchiq", "Olmaliq", "Angren", "Bekobod", "Zarafshon", "Denov", "Asaka", "Pop", "Chust", "Rishton", "Koson", "Kitob", "Zomin", "Parkent", "Zangiota", "Chortoq", "Yangiqo'rg'on", "Paxtakor", "Boysun", "Nurafshon", "G'ijduvon", "Chiroqchi", "Sherobod", "Uchqo'rg'on", "Bo'stonliq", "Olot", "To'rako'rg'on", "Bektemir", "Yashnobod", "MirzoUlug'bek", "Shayxontohur", "Yakkasaroy", "Uchtepa", "Yunusobod", "Sergeli", "Chilonzor", "Mirobod", "Hazorasp", "Xonqa", "Yangiariq", "Xonobod", "Paxtaobod", "Oltinko'l", "Baliqchi", "Jalaquduq", "Izboskan", "Xo'jaobod", "Uychi", "Norin", "To'raqo'rg'on", "Kosonsoy", "Davlatobod", "Do'stlik", "Mirzacho'l", "Forish", "Yangiobod", "Gagarin", "O'rtaChirchiq", "Yangiyo'l", "Qibray", "Ohangaron", "QuyiChirchiq", "Qamashi", "Dehqonobod", "Nishon", "Registon", "ShohiZinda", "Ichanqal'a", "Chorsu", "Aydarko'l", "Beldersoy", "Chimgan"
        countries = "Amerika", "Rossiya", "Xitoy", "Turkiya", "Koreya", "Hindiston", "Yaponiya", "Italiya", "Fransiya", "Angliya", "Germaniya", "Ispaniya", "Kanada", "Braziliya", "Saudiya", "Misr", "Afrika", "Argentina", "Isroil", "Qatar", "Ukraina", "Turkmaniston", "O'zbekiston", "Qozog'iston", "Qirg'iziston", "Tojikiston", "Avstraliya", "Indoneziya", "Meksika", "Shveysariya", "Shotlandiya", "Tailand", "Singapur", "Niderlandiya", "Shvetsiya", "Norvegiya", "Finlyandiya", "Avstriya", "Belgiya", "Polsha", "Gretsiya", "Chexiya", "Vengriya", "Portugaliya", "Irlandiya", "Zelandiya", "Marokash", "Filippin", "Vetnam", "Malayziya", "Pokiston", "Eron", "Iroq", "Kuvayt", "Oman", "Iordaniya", "Livan", "Suriya", "Afgoniston", "Bangladesh", "ShriLanka", "Nepal", "Myanma", "Kambodja", "Laos", "Efiopiya", "Keniya", "Tanzaniya", "Uganda", "Nigeriya", "Gana", "Senegal", "Kamerun", "Kongo", "Angola", "Zambiya", "Zimbabve", "Madagaskar", "Mozambik", "Botsvana", "Namibiya", "Islandiya", "Litva", "Latviya", "Estoniya", "Gruziya", "Armaniston", "Ozarbayjon", "Moldova", "Belarus", "Serbiya", "Bosniya", "Xorvatiya", "Sloveniya", "Slovakiya", "Boliviya", "Paragvay", "Urugvay", "Chili", "Peru"
        kiyim_kichaklar = "Ko'ylak", "Shim", "Kostyum", "Poyabzal", "Etik", "Krossovka", "Tufli", "Futbolka", "Mayka", "Jinsi", "Kurtka", "Pidjak", "Sharf", "Paypoq", "Shapka", "Qo'lqop", "Kepka", "Chopon", "Kofta", "Sviter", "Halat", "Yubka", "Ro'mol","Kamzul"
        oshxona_buyumlar = "Tarelka", "Lagan", "Piyola", "Kosa", "Choynak", "Stakan", "Likopcha", "Patnis", "Bakal", "Termos", "Qoshiq", "Vilka", "Pichoq", "Cho'mich", "Qirg'ich", "Elak", "Taxtacha", "Qozon", "Kastryulka", "Tova", "Qazan", "Samovar", "Banka", "Tog'ora", "Qopqoq", "Gazplita", "Duxovka", "muzlatgich", "Multivarka", "Mikser", "Blender", "Sochiq", "Fartuk", "O'choq", "Savat"
        cars = "Chevrolet", "Daewoo", "Nexia", "Spark", "Matiz", "Damas", "Tiko", "Lacetti", "Gentra", "Kobalt", "Malibu", "Tracker", "Kaptiva", "Onix", "Epika", "Orlando", "Toyota", "Kamry", "Prado", "Lexus", "Honda", "Kia", "Optima", "Sportage", "Sorento", "Hyundai", "Sonata", "Elantra", "SantaFe", "MercedesBenz", "BMW", "Audi", "Volkswagen", "Polo", "Golf", "Ford", "Focus", "Mustang", "Nissan", "Patrol", "XTrail", "Outlander", "Lancer", "Suzuki", "RangeRover", "LandRover", "Jaguar", "Tesla", "Cybertruck", "Ferrari", "Lamborghini", "Bugatti", "RollsRoyce", "Bentley", "Maserati", "BWD", "Chazor"
        his_tuygular =  "Sevgi", "Muhabbat", "Mehr", "Oqibat", "Sadoqat", "Do'stlik", "Ishonch", "Umid", "Shodlik", "Quvonch", "Baxt", "Hursandchilik", "Hayrat", "Faxr", "G'urur", "Qiziqish", "Sog'inch", "Orzu", "Havas", "Samimiyat", "Qo'rquv", "Vahima", "Xavotirlanish", "Tashvish", "Iztirob", "Alam", "G'am", "Hasrat", "Yolg'izlik", "Jahldorlik", "G'azab", "Nafrat", "Hasad", "Achinish", "Afsuslanish", "Uyat", "Xijolat", "Ishonchsizlik", "Motam", "Qayg'u", "Hayajon", "O'kinch", "Xafalik", "G'araz", "Umidsizlik", "Shubha", "Iztirob", "Vijdon"
        produxtalar = "Go'sht", "Baliq", "Yog'", "Saryog'", "Un", "Non", "Makaron", "Guruch", "Mosh", "Noxat", "Loviya", "Tuxum", "Sut", "Qatiq", "Qaymoq", "Tvorog", "Pishloq", "Kolbasa", "Sosiska", "Qand", "Shakar", "Asal", "Choy", "Qahva", "Tuz", "Murch", "Zira", "Kashnich", "Ukrop", "Sirke", "Ketchup", "Mayonez"
        movies = "Titanik", "Avatar", "Terminator", "Rambo", "Rokki", "Gladiator", "Spartak", "Jasur yurak", "Matritsa", "Yulduzlararo", "GarriPotter", "Uzuklarhukmdori", "Xobbit", "O'rgimchakodam", "Supermen", "Betmen", "Temirodam", "Qasoskorlar", "QoraPantera", "Forsaj", "Transformatorlar", "Yuradavri", "KingKong", "Godzilla", "Qirolsher", "Uydayolg'iz", "Tarzan", "Alovuddin", "Muzlikdavri", "Shrek", "Madagaskar", "KungFuPanda", "Muzyurak", "TomvaJerri", "Pokémon", "Kalmaro'yini", "Qamoqdanqochish", "Taxtlaro'yini", "Mahalladaduvduvgap", "Abdullajon", "Shumbola"
        diniy = "Alloh", "Quron", "Hadis", "Islom", "Iymon", "Musulmon", "Ummat", "Duo", "Namoz", "Ro'za", "Haj", "Zakot", "Sadaqa", "Halol", "Harom", "Qibla", "Masjid", "Azon", "Ibodat", "Sajda", "Ruku", "Qiyom", "Takbir", "Tasbeh", "Tahorat", "G'usl", "Tayammum", "Imom", "Muazzin", "Jamoat", "Vitr", "Sunnat", "Farz", "Nafl", "Tarovih", "Janoza", "Sura", "Oyat", "Juz", "Tajvid", "Qiroat", "Tafsir", "Tazkiya", "Zikr", "Tasavvuf", "Tarbiya", "Shirk", "Kufr", "Munofiq", "Taqvo", "Sabr", "Shukr", "Adolat", "Tavba", "Payg'ambar", "Sahoba", "Ramazon", "Hayit", "Hijrat", "Inshaalloh", "Alhamdulillah", "Subhanalloh", "Lailahaillalloh", "Astagfirulloh", "Jannat", "Do'zax", "Mahshar", "Sirat", "Qazo", "Qadar" # 70 
        zvaniya = "Askar", "Kichikserjant", "Serjant", "Kattaserjant", "KichikLeytenant", "Leytenant", "KattaLeytenant", "Kapitan", "Mayyor", "Podpolkovnik", "Polkovnik", "Generalmayor", "GeneralLeytenant", "GeneralPolkovnik", "General"
        inson_haraktirlari = "Mehribon", "Sadoqatli", "Halol", "Adolatli", "Sabrli", "Shukrli", "Ishchan", "Mehnatkash", "Jasur", "Oqko'ngil", "Samimiy", "Tashabbuskor", "Sahiy", "Fidoiy", "Mard", "Muloyim", "Iymonli", "Oqibatli", "G'ururli", "Qadrdon", "O'zgaruvchan", "Topqir", "Tezkor", "Yordamchi", "Masuliyatli", "Qanoatli", "Xushmuomala", "Kamtar", "O'jar", "Maqtanchoq", "Mag'rur", "Ikkiyuzlamachi", "Adolatsiz", "Yolg'onchi", "Xasis", "Ochko'z", "Qo'rqoq", "Dangasa", "Jahldor", "Hasadchi", "Beparvo", "Qo'pol", "Nozik", "Oqil", "Tarbiyali", "Odobli", "Ishonchli", "O'ylovchan", "Sergap", "Hayolparast", "Hazilkash", "Xushchaqchaq"
        games = "Shaxmat", "Shashka", "Domino", "Narda", "Karta", "Futbol", "Basketbol", "Voleybol", "Tennis", "Badminton", "Bilyard", "Bowling", "PUBG", "Durak", "FIFA", "PES", "ClashofClans", "ClashRoyale", "CandyCrush", "AngryBirds"
        cities = "Parij", "London", "Dubai", "Tokio", "Roma", "Istanbul", "Madrid", "Berlin", "Maskva", "Pekin", "Shanxay", "Toshkent", "Samarqand", "Bali", "Antaliya", "Seul", "Bangkok", "Barselona", "LasVegas", "HongKong", "LosAngeles", "Sidney", "Florensiya", "Granada", "Sevilya", "Valensiya", "Bilbao", "Lyon", "Shiraz", "Qohira", "Budapesht", "Colombo", "KualaLumpur", "SanFransisko", "RiodeJaneyro", "Kasablanka", "Marakesh", "SanktPeterburg", "Mexiko" # 40
        banks = "Xalq", "Agro", "Mikrokredit", "Aloqa", "Ipoteka", "Turon", "Asaka", "Tenge", "Kapital", "Universal", "Hamkor", "Anor", "Davr", "Uzum", "Savdogar", "OrientFinans", "IpakYo'li", "Garant", "Infin", "Markaziy"
        futbol_jamoalar = "RealMadrid", "Barselona", "Atletiko", "Sevilla", "Valensia", "Villarreal", "Liverpool", "Chelsea", "Arsenal", "Tottenham", "Newcastle", "AstonVilla", "Everton", "WestHam", "Bavariya", "Borussia", "Juventus", "Inter", "Milan", "Napoli", "Roma", "Lazio", "PSG", "Ajax", "Porto", "Benfica", "Galatasaray",  "Lokomotiv", "AlHilal", "AlNassr", "Paxtakor", "Navbahor", "Bunyodkor", "Nasaf"
        football_players = "Pele", "Maradona", "Zidane", "Ronaldo", "Ronaldinho", "Karlos", "Pirlo", "Beckham", "Raul", "Henry", "DelPiero", "Kaka", "Eto'o", "Drogba", "Shevchenko", "Torres", "Rooney", "Lampard", "Gerrard", "Xavi", "Iniesta", "Casillas", "Puyol", "Neuer", "DaniAlves", "Marcelo", "Pique", "Ramos", "Vidic", "Terry", "Ferdinand", "Nesta", "Cannavaro", "Buffon", "Cristiano", "Messi", "Neymar", "Suarez", "Bale", "Lewandowski", "Benzema", "Ibragimovich", "Mbappe", "Haaland", "DeBruyne", "Modric", "Kroos", "Muller", "Schweinsteiger", "Robben", "Ribery", "O'zil", "Hazard", "Griezmann", "Kane", "Mane", "Salah", "Aubameyang", "Cavani", "Aguero", "DiMaria", "Dybala", "Coutinho", "DavidVilla", "Hierro", "Sanchez", "Navas", "Courtois"
        sifatlar = "katta", "kichik", "uzun", "qisqa", "baland", "past", "issiq", "sovuq", "qalin", "yupqa", "keng", "tor", "tez", "sekin", "yangi", "eski", "chiroyli", "xunuk", "yumshoq", "qattiq"
        oq = "qor", "sut", "bo'r", "un", "paxta", "tuz", "shakar", "kefir", "qog'oz", "yog'"  
        qora = "ko'mir", "qahva", "choy", "tun", "ruchka"  
        qizil = "olcha", "gilos", "anor", "atirgul", "qon", "qizilolma"  
        yashil = "barg", "maysa", "ko'kat", "ismaloq", "bodring", "kivi", "archa"  
        sariq = "limon", "banan", "jo'xori", "kungaboqar", "asal", "sabzi", "oltin"  
        kok = "osmon", "dengiz", "ruchka", "choy"
        osmon = "quyosh", "oy", "bulut", "yulduz", "samolyot", "raketa", "osmon", "qush", "kamalak", "parashyut"
        shirinlik = "shokolad", "konfet", "tort", "pechenye", "pahlava", "murabbo", "shakar", "medavoy", "vafli"
        joy = "maktab", "kasalxona", "bozor", "uy", "kutubxona", "park", "masjid", "oshxona", "stadion", "teatr"
        mebel = "stol", "stul", "divan", "kreslo", "karovat", "javon", "eshik", "deraza", "gilam", "oyna"
        quyosh_tizimi = "yer", "oy", "quyosh", "mars", "venera", "yupiter", "saturn", "uran", "neptun", "merkuriY", "platon", "asteroid", "kometa", "orbitA", "atmosfera", "meteorit", "yulduz", "galaktika", "koinot", "kosmos"
        matematika = "Son", "Raqam", "Nol", "Bir", "Ikki", "Uch", "To'rt", "Besh", "Olti", "Yetti", "Sakkiz", "To'qqiz", "O'n", "Yuz", "Ming", "Million", "Milliard", "Juft", "Toq", "Qo'shish", "Ayirish", "Ko'paytirish", "Bo'lish", "Qoldiq", "Foiz", "Daraja", "Kvadrat", "Kub", "IldizOsti", "Yig'indi", "Ayirma", "Kasr", "Musbat", "Manfiy", "NaturalSon", "Butunson", "Ratsionalson", "Irratsionalson", "Radius", "Diametr", "Aylana", "Doira", "Perimetr", "Yuza", "Hajm", "Uchburchak", "To'rtburchak", "To'g'riburchak", "O'tkirburchak", "O'tmasburchak", "Paralel", "Perpendikulyar", "Chiziq", "Koordinata", "Grafik", "Formula", "Misol", "Masala", "Javob", "Tenglama", "Tengsizlik", "Funksiya", "Qiymat", "Logarifm", "Trigonometrik", "Sinus", "Kosinus", "Tangens", "Kotangens", "Pifagor", "Determinant", "Vektor", "Hisoblash", "Proportsiya", "Diagramma", "Faktorial", "Mediana", "Limit", "Integral", "Hosila" # 80         
        fizika = "Modda", "Jism", "Zarra", "Atom", "Molekula", "Proton", "Neytron", "Elektron", "Massa", "Hajm", "Zichlik", "Tezlik", "Tezlanish", "Vaqt", "Energiya", "Ish", "Quvvat", "Harakat", "Inersiya", "Kuch", "Tortish kuchi", "Gravitatsiya", "Ishqalanish", "Impuls", "Moment", "Bosim", "Og'irlik", "Arximedkuchi", "Prujina", "Taranglikkuchi", "Blok", "Harorat", "Termometr", "Issiqlik", "Qaynash", "Erish", "Bug'lanish", "Kondensatsiya", "Sublimatsiya", "Kaloriya", "Kelvin", "Tselsiy", "Farengeyt", "Tok", "Kuchlanish", "Qarshilik", "Ampermetr", "Voltmetr", "Galvanometr", "Generator", "Transformator", "Elektromagnit", "Magnitmaydon", "Tokkuchi", "Kondensator", "Induktsiya", "Elektrod", "Elektr", "Dielektrik", "Yoruglik", "Nurlanish", "Refleksiya", "Sinish", "Linza", "Oyna", "Mikroskop", "Teleskop", "Spektr", "Lazer", "Tovush", "Chastota", "Amplituda", "To'lqin", "Uzunlik", "Rezonans", "Vibratsiya", "Akustika", "Infratovush", "Ultratovush", "Termodinamika", "Konveksiya", "Radiatsiya", "Sig'imi", "O'tkazuvchanlik", "Entropiya", "Supero'tkazgich", "Dispersiya", "Interferensiya", "Difraksiya", "Kvant", "Foton", "Yadro", "Alfa", "Beta", "Gamma", "Relativlik", "Qoratuynuk", "Kvars" # 100
        kimyo = "Modda", "Element", "Atom", "Molekula", "Proton", "Neytron", "Elektron", "Izotop", "Ion", "Kation", "Anion", "Gaz", "Suyuqlik", "Plazma", "Uglerod", "Vodorod", "Kislorod", "Azot", "Metan", "Etan", "Propan", "Butan", "Natriy", "Kaliy", "Kaltsiy", "Magniy", "Alyuminiy", "Temir", "Mis", "Rux", "Qalay", "Qo'rg'oshin", "Oltin", "Kumush", "Platina", "Xlor", "Ftor", "Brom", "Yod", "Sul'fur", "Fosfor", "Silikon", "Benzol", "Spirt", "Glyukoza", "Suxaroza", "Oqsil", "Uglevod", "Polimer", "Plastik", "Kauchuk", "Teflon", "Aralashma", "Birikma", "Reaksiya", "Reagent", "Mahsulot", "Katalizator", "Yonish", "Neytrallash", "Oksidlanish", "Qaytarilish", "Eritma", "Erituvchi", "Kislota", "Konsentratsiya", "Diffuziya", "Distillatsiya", "Filtratsiya", "Kristallanish", "Bug'lanish", "Kondensatsiya", "Endotermik", "Ekzotermik", "Probirka", "Kolba", "Byureta", "Pipetka", "Termometr", "Laboratoriya" # 80
        metall = "Oltin", "Kumush", "Mis", "Temir", "Rux", "Qalay", "Qo'rg'oshin", "Alyuminiy", "Platina", "Titan", "Nikel", "Xrom"
        metros = "Olmazor", "Chilonzor", "MirzoUlug'bek", "Novza", "Milliybog'", "Xalqlardo'stligi", "O'zbekiston", "Kosmonavtlar", "Paxtakor", "Mustaqillikmaydoni", "AmirTemur", "HamidOlimjon", "Pushkin", "BuyukIpakyo'li", "Beruniy", "Tinchlik", "Chorsu", "G'afurG'ulom", "AlisherNavoiy", "Oybek", "Toshkent", "Mashinasozlar", "Do'stlik", "Mingo'rik", "YunusRajabiy", "AbdullaQodiriy", "Minor", "Bodomzor", "Shahriston", "Yunusobod", "Turkiston", "Texnopark", "Yashnobod", "Tuzel", "Olmos", "Rohat", "Yangibozor", "Qo'yliq", "Matonat", "Tolariq", "Qiyot", "Xonobod", "Turon", "Chinor", "Qipchoq" 
        company = "Uzcard", "Humo", "Beeline", "Ucell", "Mobiuz", "Uzmobile", "Uztelecom", "Apple", "Samsung", "Huawei", "Nokia", "Sony", "LG", "HP", "Dell", "Asus", "Acer", "Artel", "Akfa", "Google", "Amazon", "Facebook", "Intel", "Nike", "Adidas", "Puma", "Zara", "Gucci", "Prada", "Rolex", "Canon", "Nikon", "Panasonic", "Bosch", "Nestle", "CocaCola", "Pepsi", "McDonalds", "Disney", "Pixar", "Marvel", "Fox", "Starbucks", "Lenovo", "Microsoft", "Epam", "Netflix", "Tesla", "SpaceX", "Toshiba", "Hitachi", "Yandex", "Alibaba" 
        program = "Oson", "Click", "Payme", "Paynet", "IMO", "OLX", "Clock", "Word", "Excel", "Zoom", "Gmail", "Google", "Browser", "Telegram", "Messenger", "WhatsApp", "Instagram", "Facebook", "YouTube", "Calendar", "Gallery", "Calculator", "Viber", "Skype", "Shazam", "Netflix", "Chrome", "MXPlayer", "Canva", "Twitter", "WeChat", "MyTaxi", "YandexGo", "GooglePlay", "PlayMarket", "AppStore", "GoogleMaps", "VoiceRecorder", "PowerPoint", "AnyDesk", "CapCut", "ChatGPT", "Telegraph", "Snapchat", "BigoLive", "AliExpress", "Amazon", "ZoodMall", "UzumMarket" # 50
        programming = "R", "Go", "PHP", "CSS", "Git", "SQL", "JSON", "XML", "Dart", "Rust", "Ruby", "Java", "Sass", "Less", "HTML", "Nodejs", "Linux", "Swift", "Vue", "jQuery", "Oracle", "MySQL", "Python", "React", "GSAP", "Flask", "Redis", "Vue", "Nextjs", "Nuxtjs", "MongoDB", "Chartjs", "Threejs", "Docker", "GitHub", "GitLab", "aHost", "Heroku", "Netlify", "Vercel", "Railway", "Firebase", "SQLite", "Tailwind", "Angular", "Django", "Spring", "Laravel", "Symfony", "NestJS", "FastAPI", "Expressjs", "Bootstrap", "Postman", "WebStorm", "PhpStorm", "CLion", "Xcode", "VSCode", "Brackets", "Webpack", "Matlab", "Kotlin", "Kalkulyator", "VisualStudio", "PyCharm", "Nextjs", "ObjectiveC", "IntelliJ IDEA", "AndroidStudio", "SublimeText", "CodeBlocks", "DigitalOcean", "JupyterNotebook", "PostgreSQL", "GoogleCloud", "WebSocket" # 80
        tecnology = "Soat", "Radio", "GPS", "WiFi", "iOS", "VPN", "iPad", "iPhone", "Dron", "Robot", "Kamera", "Planshet", "Android", "SIMkarta", "Naushnik", "Quloqchin", "Fleshka", "Windows", "Laptop", "Monitor", "Printer", "Skaner", "Server", "Router", "Kompyuter", "Smartfon", "Kalkulyator", "Televizor", "Muzlatgich", "Kirmashina", "Changyutgich", "Mikropech", "Gazplita", "Ventilyator", "Termometr", "Bankomat", "Navigator", "Notebook", "Klaviatura", "Protsessor", "Bluetooth", "Internet", "Zaryadlagich", "PowerBank", "Smartwatch", "Konditsioner", "PlayStation", "Desktop", "Modem" # 50      
        B____r = "Bozor","Bahor","Bobir","Bemor","Bahodir","Baxtiyor","Bunyodkor", "Barqaror"
        T____t = "Toshkent","Transport","Tabiat","Talant","Taxt","Targ'ibot"
        K____t = "Kredit","Kafolat","Konsert","Konspekt","Kamolot"
        M____t = "Mehnat","Maslahat","Muloqot","Mahsulot","Murojaat","Muvaffaqiyat","Munosabat","Madaniyat"
        P____t = "Pasport","Paket","Poytaxt","Patent","Plakat","Parlament"
        S____t = "Siyosat","Sifat","Samolyot","Savlat","Sharbat","Sanat","Sadoqat"
        Y____z = "Yulduz","Yuz","Yoz","Yalpiz","Yolg'iz"
        H____m = "Hokim","Hammom","Halim","Hujum","Hajm"
        X____r = "Xabar","Xaridor","Xarakter","Xamir","Xumor","Xizmatkor"
        Ch____a = "Chashma","Choyxona","Chizma","Choliqush","Chilla"
        Sh____r = "Shahar","Shifokor","Shakar","Shior","Shukur"
        Q____q = "Qishloq","Quloq","Qirq","Qovoq","Qayiq","Qarmoq","Qirqmoq","Qizaloq"
        A____a = "Ariza","Aloqa","Apteka","Antena","Arava","Aziza"
        B____a = "Bola","Bog'cha","Binafsha","Boshqa","Barcha","Bahora","Baraka"
        K____a = "Ko'cha","Kassa","Kamera","Kutubxona","Komila","Kamola","Kema"
        M____a = "Mashina","Musiqa","Mahalla","Muallima","Madina","Malika","Maftuna"
        D____n = "Do'kon","Dasturxon","Darmon","Dehqon","Doston","Davron"
        F____l = "Futbol","Fayl","Fasl","Fil","Fozil"
        E____t = "Effekt","Eksport","Element","Eksperiment","Etiket","Eshmat"
        M____n = "Magazin","Makon","Mehribon","Mikrofon","Musulmon", "Mehmon"
        Ma_____ = "Maktab","Malika","Mashina","Mahalla","Maqola","Madina","Mavsum","Mahsulot","Maqsad"
        Bo_____ = "Bozor","Bolalar","Bog'cha","Boshliq","Boylik","Bolta","Borliq","Bodom"
        Ta_____ = "Talaba","Talim","Tabiat","Taom","Taqvim","Tayyor","Tadbirkor","Tarix","Taxt","Tarmoq"
        Sa_____ = "Sabzi","Samolyot","Samarqand","Salom","San'at","Saroy","Sayohat","Savdo","Saboq"
        Di_____ = "Dildora","Diqqat","Dilbar","Dindor","Dialog","Didor"
        Al_____ = "Alisher","Alvido","Alanga","Albatta","Aloqa","Alpomish","Alkogol","Algebra"
        Yo_____ = "Yozuv","Yulduz","Yorqin","Yolg'iz","Yor","Yoz","Yog'och","Yodgor","Yorug'lik","Yoshlar"
        Qi_____ = "Qish","Qizil","Qishloq","Qiyin","Qizaloq","Qimmat","Qiyofa","Qiruvchi","Qiyos"
        Na_____ = "Navro'z","Nargiza","Nafis","Nasiba","Namangan","Nafaqa","Navoiy"
        Hu_____ = "Hurmat","Hokim","Humor","Hujjat","Hujum","Humo","Hunar","Hukumdor"
        Za_____ = "Zarafshon","Zarina","Zarur","Zafar","Ziyo","Zamon","Zamonaviy","Ziyofat","Ziyorat"
        Ol_____ = "Olma","Olov","Oltin","Olim","Olmos","Oltiariq","Oltinsoy","Oliy"
        Ka_____ = "Karim","Kamol","Kamalak","Katta","Kafolat","Kamera","Kassir"
        Mu_____ = "Murod","Muborak","Muallim","Mustaqillik","Musiqa","Muqaddas","Murojaat","Munozara","Muhabbat"
        Ra_____ = "Rahmat","Ravon","Rasul","Ramazon","Rang","Rasm","Ravshan","Rano","Rasululloh"
        Lo_____ = "Lola","Lozim","Loyiha","Loqayd","Lochin"
        Te_____ = "Telefon","Televizor","Temir","Tepalik","Teatr","Tezlik","Texnika","Teshik","Tenglik"
        Su_____ = "Suv","Sut","Suyanchiq","Sulton","Surat","Sunnat"
        Ni_____ = "Nima","Nishon","Niyat","Nilufar","Nishab","Niqob","Nigor","Nizom","Nimadir","Nihol"
        La_____ = "Lab","Lampa","Lavozim","Lazzat","Latifa","Lashkar","Laptop","Lagan"




        lvl_1 = {
            "category": "Ism",
            "word": random.choice(names),
        }

        lvl_2 = {
            "category": "Rang",
            "word": random.choice(colors),
        }

        lvl_3 = {
            "category": "Kalendar",
            "word": random.choice(calendar),
        }

        lvl_4 = {
            "category": "Hayvon",
            "word": random.choice(animals),
        }

        lvl_5 = {
            "category": "Meva",
            "word": random.choice(fruit),
        }

        lvl_6 = {
            "category": "Sabzavot",
            "word": random.choice(vegetables),
        }

        lvl_7 = {
            "category": "Ovqat",
            "word": random.choice(ovqatlar),
        }

        lvl_8 = {
            "category": "Ob-Havo",
            "word": random.choice(obhavo),
        }

        lvl_9 = {
            "category": "Transport turlari",
            "word": random.choice(transport),
        }

        lvl_10 = {
            "category": "Ovqat",
            "word": random.choice(osimliklar),
        }

        lvl_11 = {
            "category": "Ichimlik",
            "word": random.choice(ichimlik),
        }

        lvl_12 = {
            "category": "Fan",
            "word": random.choice(fan),
        }

        lvl_13 = {
            "category": "Vaqt",
            "word": random.choice(vaqt),
        }

        lvl_14 = {
            "category": "Qurol",
            "word": random.choice(qurollar),
        }

        lvl_15 = {
            "category": "Musiqa Asbobi",
            "word": random.choice(musiqa_asboblari),
        }

        lvl_16 =  {
            "category": "Oila azosi yoki Qarindosh",
            "word": random.choice(oila_va_qarindoshlar),
        }

        lvl_17 = {
            "category": "Inson tana azolari",
            "word": random.choice(human_body),
        }

        lvl_18 = {
            "category": "Sport turi",
            "word": random.choice(sports),
        }
        
        lvl_19 = {
            "category": "Maktab anjomi",
            "word": random.choice(maktab_anjomlar),
        }

        lvl_20 = {
            "category": "Kasb",
            "word": random.choice(jobs),
        }

        lvl_21 = {
            "category": "Tabiat",
            "word": random.choice(names),
        }

        lvl_22 = {
            "category": "Qush",
            "word": random.choice(birds),
        }

        lvl_23 = {
            "category": "Telefon",
            "word": random.choice(phones),
        }

        lvl_24 = {
            "category": "Uzb Shahar-tumanlar",
            "word": random.choice(uzb_regions),
        }

        lvl_25 = {
            "category": "Davlatlar",
            "word": random.choice(countries),
        }

        lvl_26 = {
            "category": "Kiyim-Kichak",
            "word": random.choice(kiyim_kichaklar),
        }

        lvl_27 = {
            "category": "Oshxona buyumlar",
            "word": random.choice(oshxona_buyumlar),
        }

        lvl_28 = {
            "category": "Moshina",
            "word": random.choice(cars),
        }

        lvl_29 = {
            "category": "His-tuyg'u",
            "word": random.choice(his_tuygular),
        }

        lvl_30 = {
            "category": "Produxta",
            "word": random.choice(produxtalar),
        }

        lvl_31 = {
            "category": "Kino nomi",
            "word": random.choice(movies),
        }

        lvl_32 = {
            "category": "Islomiy so'zlar",
            "word": random.choice(diniy),
        }

        lvl_33 = {
            "category": "Unvon",
            "word": random.choice(zvaniya),
        }

        lvl_34 = {
            "category": "Inson haraktiri",
            "word": random.choice(inson_haraktirlari),
        }

        lvl_35 = {
            "category": "O'yin",
            "word": random.choice(games),
        }

        lvl_36 = {
            "category": "Mashhur Shahar",
            "word": random.choice(cities),
        }

        lvl_37 = {
            "category": "Bank",
            "word": random.choice(banks),
        }

        lvl_38 = {
            "category": "Futbol klub",
            "word": random.choice(futbol_jamoalar),
        }

        lvl_39 = {
            "category": "Futbolchi",
            "word": random.choice(football_players),
        }

        lvl_40 = {
            "category": "Sifat",
            "word": random.choice(sifatlar),
        }

        lvl_41 = {
            "category": "Oq rang",
            "word": random.choice(oq),
        }

        lvl_42 = {
            "category": "Qora rang",
            "word": random.choice(qora),
        }

        lvl_43 = {
            "category": "Qizil rang",
            "word": random.choice(qizil),
        }

        lvl_44 = {
            "category": "Sariq rang",
            "word": random.choice(sariq),
        }

        lvl_45 = {
            "category": "Yashil rang",
            "word": random.choice(yashil),
        }

        lvl_46 = {
            "category": "Ko'k rang",
            "word": random.choice(kok),
        }

        lvl_47 = {
            "category": "Osmon",
            "word": random.choice(osmon),
        }

        lvl_48 = {
            "category": "Shirinlik",
            "word": random.choice(shirinlik),
        }

        lvl_49 = {
            "category": "Joy (bino)",
            "word": random.choice(joy),
        }

        lvl_50 = {
            "category": "Mebel",
            "word": random.choice(mebel),
        }

        lvl_51 = {
            "category": "Quyosh tizimi",
            "word": random.choice(quyosh_tizimi),
        }

        lvl_52 = {
            "category": "Matematika",
            "word": random.choice(matematika),
        }

        lvl_53 = {
            "category": "Fizika",
            "word": random.choice(fizika),
        }

        lvl_54 = {
            "category": "Kimyo",
            "word": random.choice(kimyo),
        }

        lvl_55 = {
            "category": "Metall",
            "word": random.choice(metall),
        }

        lvl_56 = {
            "category": "Metro bekati",
            "word": random.choice(metros),
        }

        lvl_57 = {
            "category": "Kampaniya",
            "word": random.choice(company),
        }

        lvl_58 = {
            "category": "Kerakli Dasturlar",
            "word": random.choice(program),
        }

        lvl_59 = {
            "category": "Dasturlash",
            "word": random.choice(programming),
        }

        lvl_60 = {
            "category": "Texnologiya",
            "word": random.choice(tecnology),
        }

        lvl_61 = {
            "category": "B____R",
            "word": random.choice(B____r),
        }

        lvl_62 = {
            "category": "T____T",
            "word": random.choice(T____t),
        }

        lvl_63 = {
            "category": "K____T",
            "word": random.choice(K____t),
        }

        lvl_64 = {
            "category": "M____T",
            "word": random.choice(M____t),
        }

        lvl_65 = {
            "category": "P____T",
            "word": random.choice(P____t),
        }

        lvl_66 = {
            "category": "S____T",
            "word": random.choice(S____t),
        }

        lvl_67 = {
            "category": "Y____Z",
            "word": random.choice(Y____z),
        }

        lvl_68 = {
            "category": "H____M",
            "word": random.choice(H____m),
        }

        lvl_69 = {
            "category": "X____R",
            "word": random.choice(X____r),
        }

        lvl_70 = {
            "category": "CH____A",
            "word": random.choice(Ch____a),
        }

        lvl_71 = {
            "category": "SH____R",
            "word": random.choice(Sh____r),
        }

        lvl_72 = {
            "category": "Q____Q",
            "word": random.choice(Q____q),
        }

        lvl_73 = {
            "category": "A____A",
            "word": random.choice(A____a),
        }

        lvl_74 = {
            "category": "B____A",
            "word": random.choice(B____a),
        }

        lvl_75 = {
            "category": "K____A",
            "word": random.choice(K____a),
        }

        lvl_76 = {
            "category": "M____A",
            "word": random.choice(M____a),
        }

        lvl_77 = {
            "category": "D____N",
            "word": random.choice(D____n),
        }

        lvl_78 = {
            "category": "F____L",
            "word": random.choice(F____l),
        }

        lvl_79 = {
            "category": "E____T",
            "word": random.choice(E____t),
        }

        lvl_80 = {
            "category": "M____N",
            "word": random.choice(M____n),
        }

        lvl_81 = {
            "category": "MA____",
            "word": random.choice(Ma_____),
        }

        lvl_82 = {
            "category": "BO____",
            "word": random.choice(Bo_____),
        }

        lvl_83 = {
            "category": "TA____",
            "word": random.choice(Ta_____),
        }

        lvl_84 = {
            "category": "SA____",
            "word": random.choice(Sa_____),
        }

        lvl_85 = {
            "category": "DI____",
            "word": random.choice(Di_____),
        }

        lvl_86 = {
            "category": "AL____",
            "word": random.choice(Al_____),
        }

        lvl_87 = {
            "category": "YO____",
            "word": random.choice(Yo_____),
        }

        lvl_88 = {
            "category": "QI____",
            "word": random.choice(Qi_____),
        }

        lvl_89 = {
            "category": "NA____",
            "word": random.choice(Na_____),
        }

        lvl_90 = {
            "category": "HU____",
            "word": random.choice(Hu_____),
        }

        lvl_91 = {
            "category": "ZA____",
            "word": random.choice(Za_____),
        }

        lvl_92 = {
            "category": "OL____",
            "word": random.choice(Ol_____),
        }

        lvl_93 = {
            "category": "KA____",
            "word": random.choice(Ka_____),
        }

        lvl_94 = {
            "category": "MU____",
            "word": random.choice(Mu_____),
        }

        lvl_95 = {
            "category": "RA____",
            "word": random.choice(Ra_____),
        }

        lvl_96 = {
            "category": "LO____",
            "word": random.choice(Lo_____),
        }

        lvl_97 = {
            "category": "TE____",
            "word": random.choice(Te_____),
        }

        lvl_98 = {
            "category": "SU____",
            "word": random.choice(Su_____),
        }

        lvl_99 = {
            "category": "NI____",
            "word": random.choice(Ni_____),
        }

        lvl_100 = {
            "category": "LA____",
            "word": random.choice(La_____),
        }



        lvl_1 = name_json

        lvl_2 = color_json

        lvl_3 = calendar_json

        lvl_4 = animal_json

        lvl_5 = fruit_json

        lvl_6 = vegetable_json

        lvl_7 = ovqat_json

        lvl_8 = obhavo_json

        lvl_9 = transport_json

        lvl_10 = osimlik_json

        lvl_11= ichimlik_json

        lvl_12= fan_json

        lvl_13 = vaqt_json

        lvl_14 = qurol_json

        lvl_15 = musiqa_asbob_json

        lvl_16 = oila_va_qarindosh_json

        lvl_17 = human_body_json

        lvl_18 = sport_json

        lvl_19 = maktab_anjom_json

        lvl_20 = job_json

        lvl_21 = nature_json

        lvl_22 = bird_json

        lvl_23 = phone_json

        lvl_24 = uzb_region_json

        lvl_25 = country_json

        lvl_26 = kiyim_kichak_json

        lvl_27 = oshxona_buyumlar

        lvl_28 = car_json

        lvl_29 = his_tuygu_json

        lvl_30 = produxta_json

        lvl_31 = movie_json

        lvl_32 = diniy_json

        lvl_33 = zvaniya_json

        lvl_34 = inson_haraktir_json

        lvl_35 = game_json

        lvl_36 = city_json

        lvl_37 = bank_json

        lvl_38 = futbol_jamoa_json

        lvl_39 = football_player_json

        lvl_40 = sifat_json

        lvl_41 = oq_json

        lvl_42 = qora_json

        lvl_43 = qizil_json

        lvl_44 = sa_json

        lvl_45 = yashil_json

        lvl_46 = kok_json

        lvl_47 = osmon_json

        lvl_48 = shirinlik_js

        lvl_50 = mebel_json

        lvl_51 = quyosh_tizim_json

        lvl_52 = matematika_json

        lvl_53 = fizika_json

        lvl_54 = kimyo_json

        lvl_55 = metall_json

        lvl_56 = metro_json

        lvl_57 = company_json

        lvl_58 = program_json

        lvl_59 = programming_json

        lvl_60 = tecnology_json

        lvl_61 = b_r_json

        lvl_62 = t_t_json

        lvl_63 = k_t_json

        lvl_64 = m_t_json

        lvl_65 = p_t_json

        lvl_66 = s_t_json

        lvl_67 = y_z_json

        lvl_68 = h_m_json

        lvl_69 = x_r_json

        lvl_70 = ch_a_json

        lvl_71 = Sh_r_json

        lvl_72 = q_q_json

        lvl_73 = a_a_json

        lvl_74 = b_a_json

        lvl_75 = k_a_json

        lvl_76 = m_a_json

        lvl_77 = d_n_json

        lvl_78 = f_l_json

        lvl_79 = e_t_json

        lvl_80 = m_n_json

        lvl_81 = ma_json

        lvl_82 = bo_json

        lvl_83 = ta_json

        lvl_84 = sa_json

        lvl_85 = di_json

        lvl_86 = al_json

        lvl_87 = yo_json

        lvl_88 = qi_json

        lvl_89 = na_json

        lvl_90 = hu_json

        lvl_91 = za_json

        lvl_92 = ol_json

        lvl_93 = ka_json

        lvl_94 = mu_json

        lvl_95 = ra_json

        lvl_96 = lo_json

        lvl_97 = te_json

        lvl_98 = su_json

        lvl_99 = ni_json

        lvl_100 = la_json

        return Response(tecnology) 