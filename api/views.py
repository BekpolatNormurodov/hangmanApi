from rest_framework.views import APIView
from rest_framework.response import Response
import random





class HangmanApiView(APIView):
    def get(self, request):
        names = ["Abbos", "Abdulaziz", "Abdulloh", "Abror", "Adham", "Akbar", "Akmal", "Alisher", "Amir", "Amirbek", "Amirxon", "Anvar", "Asad", "Asliddin", "Asror", "Azamat", "Azimjon", "Aziz", "Azizbek", "Baxtiyor", "Bekmurod", "Bekzod", "Bilol", "Bobur", "Botir", "Davron", "Dilshod", "Elyor", "Ergash", "Erkin", "Farruh", "Farrux", "Farhod", "Fayzulla", "Firdavs", "Habib", "Habibulloh", "Hakim", "Hamid", "Hamza", "Hasan", "Hasanboy", "Hikmat", "Hikmatulloh", "Hojiakbar", "Humoyun", "Husan", "Husanboy", "Husniddin", "Ilhom", "Iskandar", "Islom", "Ismoil", "Ibrohim", "Jamol", "Jamshid", "Jaloliddin", "Jasur", "Javlon", "Javohir", "Karim", "Kamoliddin", "Komil", "Laziz", "Lochin", "Lutfulla", "Madamin", "Mahmud", "Malik", "Mansur", "Mashrab", "Mirjalol", "Mirkomil", "Mironshoh", "Murod", "Muhriddin", "Muhammad", "Muzaffar", "Najmiddin", "Nodir", "Nurbek", "Nuriddin", "Odil", "Olim", "Oybek", "Qahhor", "Qahramon", "Qobil", "Qodir", "Qosim", "Qurbon", "Quvonch", "Rahim", "Rashid", "Ravshan", "Rustam", "Rustamjon", "Samandar", "Sanjar", "Sardor", "Sarvar", "Said", "Shahboz", "Shahriyor", "Shahzod", "Shams", "Shamsiddin", "Shavkat", "Sherali", "Sherzod", "Shodiyor", "Shodmon", "Shokir", "Shohjahon", "Shohruh", "Siroj", "Sirojiddin", "Sobir", "Sobit", "Sodiq", "Sohib", "Suhrob", "Sulton", "Temur", "Tohir", "Tolib", "Ubaydulla", "Ubaydulloh", "Ulug'bek", "Umid", "Umar", "Usmon", "Valijon", "Vohid", "Xayrulloh", "Xojiakbar", "Xolmat", "Xudoyor", "Xurshid", "Yahyo", "Yodgor", "Yoqub", "Yunus", "Yusuf", "Zafar", "Zavqiddin", "Zayniddin", "Zohid", "Zokir", "Adolat", "Aziza", "Barno", "Dilafruz", "Dildora", "Dilnoza", "Feruza", "Fotima", "Gulbahor", "Gulchehra", "Gulhayo", "Gulnora", "Gulnoza", "Gulsanam", "Gulshan", "Gulruh", "Humora", "Husniya", "Iroda", "Kamola", "Kumush", "Lobar", "Malohat", "Manzura", "Mashhura", "Maftuna", "Mehribon", "Muhayyo", "Mubina", "Mukarram", "Muqaddas", "Munira", "Munisa", "Mushtariy", "Nilufar", "Nigora", "Nodira", "Nozima", "Ozoda", "Oysara", "Oygul", "Parizoda", "Rano", "Rayhona", "Ruxshona", "Saida", "Saodat", "Sanobar", "Shahlo", "Shahzoda", "Shamsiya", "Shoira", "Shukrona", "Surayyo", "Umida", "Xadicha", "Xalima", "Xilola", "Xosiyat", "Xurriyat", "Zarnigor", "Zebo", "Zilola", "Ziyoda", "Zuhra", "Madina", "Mahliyo", "Malika", "Mehriniso", "Muslima", "Nasiba", "Nafisa", "Nafosat", "Nargiza", "Nigina", "Robiya", "Sabina", "Sanam", "Shahrizoda", "Sitora", "Sadoqat", "Sohiba", "Tahmina", "Tomaris", "Zaynab", "Zulfiya", "Zarina", "Zarifa", "Asal", "Barchinoy", "Dilorom", "Dilshoda", "Firuza", "Gulandon", "Gulsara", "Halima", "Hanifa", "Husnora", "Jamila", "Karima", "Komila", "Lola", "Marhabo", "Munavvar", "Oysuluv", "Rano", "Sabohat", "Shirin", "Shohista", "Xonzoda", "Xurshida", "Zebiniso", "Dilnora", "Guljahon", "Guljamol", "Husniyo", "Iymona", "Latofat", "Nigoh", "Ruxsora", "Sabrina", "Shaxnoza", "Shodiyona", "Shohsanam", "Umriniso", "Xumora", "Zubayda", "Zulayho"]
        colors = ["Oq", "Qora", "Qizil", "Ko'k", "Yashil", "Sariq", "Malla", "Pushti", "Moviy", "Zangori", "Binafsha", "Kulrang", "Jigarrang"]
        calendar = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr", "Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba", "Bahor", "Yoz", "Kuz", "Qish"]
        animals = ["It", "Mushuk", "Ot", "Sigir", "Qo'y", "Eshak", "Tovuq", "Xo'roz", "O'rdak", "G'oz", "Qo'zi", "Buqa", "Baliq", "Quyon", "Sher", "Arslon", "Yo'lbars", "Tulki", "Bo'ri", "Ayiq", "Chumchuq", "Qaldirg'och", "Qarg'a", "Qurbaqa", "Maymun", "Fil", "Jirafa", "Kapalak", "Asalari", "Chayon", "Ilon", "Sichqon", "Jayron", "Bug'u", "Burgut", "Qirg'iy", "Turna", "Tovus", "Toychoq", "Bo'taloq", "Echkichi", "Akula", "Delfin", "Timsah", "Pingvin", "Qoplon", "Tustovuq", "Baqa", "Tulpor", "Chittak", "Laylak", "Boyo'g'li", "Ohu", "Qunduz", "Bo'rsiq", "Kaptar", "Lochin", "Ko'rsichqon", "Toshbaqa", "Kalamush", "Tuya", "Qo'y", "Jayra", "Panda", "Koala", "Shilliqurt", "Qirg'ovul", "Kaklik", "O'rdak", "Chumoli", "Bo'g'mailon", "Mushuk", "Xo'tik", "Turna"]
        fruit = ["Olma", "Anor", "Uzum", "Nok", "Shaftoli", "Gilos", "Olcha", "Shaftoli", "Banan", "Apelsin", "Mandarin", "Limon", "Kivi", "Ananas", "Mango", "Papayya", "Avokado", "Kokos", "Injir", "Xurmo", "Tut", "Behi", "Qulupnay", "Malina", "Chernika", "Smorodina", "O'rik"]
        vegetables = ["Kartoshka", "Piyoz", "Sarimsoq", "Sabzi", "Bodring", "Pomidor", "Baqlajon", "Qalampir", "Karam", "Gulkaram", "Qovoq", "Kadi", "Turp", "Rediska", "Sholg'om", "Ismaloq", "Kashnich", "Ukrop", "Shivit", "Petrushka", "Zanjabil"]
        human_body = ["Bosh", "Soch", "Peshona", "Ko'z", "Qosh", "Kiprik", "Burun", "Lab", "Og'iz", "Tish", "Til", "Yonoq", "Jag'", "Quloq", "Bo'yin", "Tomoq", "Yelka", "Qo'l", "Bilak", "Kaft", "Barmoq", "Tirnoq", "Yurak", "O'pka", "Jigar", "Oshqozon", "Buyrak", "Ichak", "Bel", "Qorin", "Son", "Tizza", "Oyoq", "Tovon", "Skelet", "Suyak", "Muskul", "Tomir", "Asab", "Teri", "Qon", "Miya", "Umurtqa", "Qovurg'a"]
        ovqatlar = ["Palov", "Kabob", "Sho'rva", "Mastava", "Dimlama", "Chuchvara", "Manti", "Norin", "Lag'mon", "Honim", "Barak", "Somsa", "Qazi", "Shashlik", "Jigar", "Beshbarmoq", "Halim", "Sumalak", "Burger", "Xotdog", "Shaurma", "Donar", "Lavash", "Pizza", "Sendvich", "Chizburger"]
        oila_va_qarindoshlar = ["Ota", "Ona", "Bola", "O'g'il", "Qiz", "Aka", "Uka", "Opa", "Singil", "Amaki", "Tog'a", "Xola", "Amma", "Buvi", "Bobo", "Kelin", "Kuyov", "Er", "Xotin", "Jiyan", "Nevara", "Chaqaloq", "Qaynona", "Qaynota", "Qaynuka", "Qaynsingil", "Qaynopa", "Nevara", "O'gayona", "O'gayota", "O'gayuka", "O'gayaka", "O'gayopa", "Buvijon", "Bobojon", "Opajon", "Akajon", "Ukajon", "Onajon", "Qizaloq", "Enaga", "Amakivachcha", "Qudag'ay", "Quda", "Qaynona", "Qaynota"]
        sports = ["Futbol", "Boks", "Kurash", "Tennis", "Shaxmat", "Shashka", "Basketbol", "Voleybol", "Dzyudo", "Taekvondo", "Karate", "Sambo", "Suzish", "Gimnastika", "Velosport", "Handbol", "Xokkey", "Amerika futzal", "Beysbol", "Golf", "Bilyard", "O'qotish", "Yugurish", "Avtopoyga"]
        maktab_anjomlar = ["Daftar", "Qalam", "Ruchka", "Chizg'ich", "O'chirg'ich", "Qalamdon", "sumka", "Jild", "Doska", "Marker", "Bo'yoq", "Kley", "Qaychi", "Sirkul", "Proyektor", "Bo'r", "Jurnal", "Kitob", "Alifbo", "Kundalik"]
        jobs = ["O'qituvchi", "Shifokor", "Haydovchi", "Dehqon", "Oshpaz", "Quruvchi", "Tikuvchi", "Sartarosh", "Politsiya", "Harbiy", "Hamshira", "Sotuvchi", "Elektrik", "Santexnik", "Hisobchi", "Farmatsevt", "Muhandis", "Advokat", "Dasturchi", "Aktyor", "Qo'shiqchi", "Rassom", "Dizayner", "Fotograf", "Jurnalist", "Kutubxonachi", "Imom", "Ofitsiant", "Kassir", "Bankir", "Tadbirkor", "Mashinasoz", "Mexanik", "Fermer", "Veterinar", "Temirchi", "Duradgor", "Haykaltarosh", "Geodezist", "Tarjimon", "Professor", "Psixolog", "Arxitektor", "Astronom", "Robototexnik", "Hayvonotshunos", "Hacker", "Arxeolog", "O'rmonchi", "Iqtisodchi", "SMM", "Operator", "Rejissyor", "Musiqachi", "Dirijyor", "Sportchi", "Futbolchi", "Bokschi", "Kurashchi", "Trener", "Hakim", "Massajchi", "Hamomchi", "Instruktor", "Usta", "Elektrotexnik", "Energetik", "Konchi", "Neftchi", "Kimyogar", "Biolog", "Fizik", "Ximik", "Direktor", "Dekan", "Advokat", "Sudya", "Prokuror", "Notarius", "Banker", "Pochtalyon", "Uchuvchi", "Styuardessa", "Dengizchi"]
        nature = ["Quyosh", "Oy", "Yulduz", "Bulut", "Yomg'ir", "Qor", "Shamol", "Tog'", "Daraxt", "Gul", "O't", "Suv", "Ko'l", "Daryo", "Okean", "Cho'l", "Dasht", "O'rmon", "Tuproq", "Tosh", "Qoya", "Chashma", "Soy", "Vodiy", "Jar", "Ko'k", "Osmon", "Bahor", "Yoz", "Kuz", "Qish", "Kamalak", "Nur", "Tong", "Shom", "Soyabon", "Barg", "Shox", "Ildiz", "Giyoh", "Lola", "Chinor", "Terak", "Tol", "O'rik", "Chaman", "Bog'", "Gulzor", "O'tloq", "Dashtzor", "Cho'qqi", "Sahro", "Qumtepa", "Shag'al", "Ko'mir", "Neft", "Oltin", "Kumush", "Mis", "Qoyatosh", "Orol", "Sharshara", "G'or", "Buloq", "Bo'ron", "Jala", "Chaqmoq", "Momaqaldiroq", "Tornado", "Sel", "Zilzila", "Vulqon", "Lava", "Muzlik", "Aysberg", "Sahro", "Qum", "Dengiz"]
        birds = ["Qaldirg'och", "Bulbul", "Kaptar", "To'ti", "Qarg'a", "Turna", "Qirg'iy", "Burgut", "Boyqush", "Chumchuq", "Tovus", "Bedana", "O'rdak", "G'oz", "Tovuq", "Xo'roz", "Laylak", "Kaklik", "Qizilishton", "Qizilqanot"]
        phones = ["Apple", "Samsung", "Huawei", "Xiaomi", "Oppo", "Vivo", "Realme", "OnePlus", "Honor", "Motorola", "Nokia", "Sony", "Pixel", "ZTE", "Tecno", "Infinix", "Micromax", "Panasonic", "Philips", "Siemens"]
        uzb_regions = ["Toshkent", "Samarqand", "Buxoro", "Xiva", "Urganch", "Nukus", "Andijon", "Namangan", "Farg'ona", "Qo'qon", "Marg'ilon", "Qarshi", "Shahrisabz", "Guliston", "Termiz", "Chirchiq", "Olmaliq", "Angren", "Bekobod", "Zarafshon", "Denov", "Asaka", "Pop", "Chust", "Rishton", "Koson", "Kitob", "Zomin", "Parkent", "Zangiota", "Chortoq", "Yangiqo'rg'on", "Paxtakor", "Boysun", "Nurafshon", "G'ijduvon", "Chiroqchi", "Sherobod", "Uchqo'rg'on", "Bo'stonliq", "Olot", "To'rako'rg'on", "Bektemir", "Yashnobod", "MirzoUlug'bek", "Shayxontohur", "Yakkasaroy", "Uchtepa", "Yunusobod", "Sergeli", "Chilonzor", "Mirobod", "Hazorasp", "Xonqa", "Yangiariq", "Xonobod", "Paxtaobod", "Oltinko'l", "Baliqchi", "Jalaquduq", "Izboskan", "Xo'jaobod", "Uychi", "Norin", "To'raqo'rg'on", "Kosonsoy", "Davlatobod", "Do'stlik", "Mirzacho'l", "Forish", "Yangiobod", "Gagarin", "O'rtaChirchiq", "Yangiyo'l", "Qibray", "Ohangaron", "QuyiChirchiq", "Qamashi", "Dehqonobod", "Nishon", "Registon", "ShohiZinda", "Ichanqal'a", "Chorsu", "Aydarko'l", "Beldersoy", "Chimgan"]
        countries = ["Amerika", "Rossiya", "Xitoy", "Turkiya", "Koreya", "Hindiston", "Yaponiya", "Italiya", "Fransiya", "Angliya", "Germaniya", "Ispaniya", "Kanada", "Braziliya", "Saudiya", "Misr", "Afrika", "Argentina", "Isroil", "Qatar", "Ukraina", "Turkmaniston", "O'zbekiston", "Qozog'iston", "Qirg'iziston", "Tojikiston", "Avstraliya", "Indoneziya", "Meksika", "Shveysariya", "Shotlandiya", "Tailand", "Singapur", "Niderlandiya", "Shvetsiya", "Norvegiya", "Finlyandiya", "Avstriya", "Belgiya", "Polsha", "Gretsiya", "Chexiya", "Vengriya", "Portugaliya", "Irlandiya", "Zelandiya", "Marokash", "Filippin", "Vetnam", "Malayziya", "Pokiston", "Eron", "Iroq", "Kuvayt", "Oman", "Iordaniya", "Livan", "Suriya", "Afgoniston", "Bangladesh", "ShriLanka", "Nepal", "Myanma", "Kambodja", "Laos", "Efiopiya", "Keniya", "Tanzaniya", "Uganda", "Nigeriya", "Gana", "Senegal", "Kamerun", "Kongo", "Angola", "Zambiya", "Zimbabve", "Madagaskar", "Mozambik", "Botsvana", "Namibiya", "Islandiya", "Litva", "Latviya", "Estoniya", "Gruziya", "Armaniston", "Ozarbayjon", "Moldova", "Belarus", "Serbiya", "Bosniya", "Xorvatiya", "Sloveniya", "Slovakiya", "Boliviya", "Paragvay", "Urugvay", "Chili", "Peru"]
        kiyim_kichaklar = ["Ko'ylak", "Shim", "Kostyum", "Poyabzal", "Etik", "Krossovka", "Tufli", "Futbolka", "Mayka", "Jinsi", "Kurtka", "Pidjak", "Sharf", "Paypoq", "Shapka", "Qo'lqop", "Kepka", "Chopon", "Kofta", "Sviter", "Halat", "Yubka", "Ro'mol","Kamzul"]
        oshxona_buyumlar = ["Tarelka", "Lagan", "Piyola", "Kosa", "Choynak", "Stakan", "Likopcha", "Patnis", "Bakal", "Termos", "Qoshiq", "Vilka", "Pichoq", "Cho'mich", "Qirg'ich", "Elak", "Taxtacha", "Qozon", "Kastryulka", "Tova", "Qazan", "Samovar", "Banka", "Tog'ora", "Qopqoq", "Gazplita", "Duxovka", "muzlatgich", "Multivarka", "Mikser", "Blender", "Sochiq", "Fartuk", "O'choq", "Savat"]
        cars = ["Chevrolet", "Daewoo", "Nexia", "Spark", "Matiz", "Damas", "Tiko", "Lacetti", "Gentra", "Kobalt", "Malibu", "Tracker", "Kaptiva", "Onix", "Epika", "Orlando", "Toyota", "Kamry", "Prado", "Lexus", "Honda", "Kia", "Optima", "Sportage", "Sorento", "Hyundai", "Sonata", "Elantra", "SantaFe", "MercedesBenz", "BMW", "Audi", "Volkswagen", "Polo", "Golf", "Ford", "Focus", "Mustang", "Nissan", "Patrol", "XTrail", "Outlander", "Lancer", "Suzuki", "RangeRover", "LandRover", "Jaguar", "Tesla", "Cybertruck", "Ferrari", "Lamborghini", "Bugatti", "RollsRoyce", "Bentley", "Maserati", "BWD", "Chazor"]
        his_tuygular = [ "Sevgi", "Muhabbat", "Mehr", "Oqibat", "Sadoqat", "Do'stlik", "Ishonch", "Umid", "Shodlik", "Quvonch", "Baxt", "Hursandchilik", "Hayrat", "Faxr", "G'urur", "Qiziqish", "Sog'inch", "Orzu", "Havas", "Samimiyat", "Qo'rquv", "Vahima", "Xavotirlanish", "Tashvish", "Iztirob", "Alam", "G'am", "Hasrat", "Yolg'izlik", "Jahldorlik", "G'azab", "Nafrat", "Hasad", "Achinish", "Afsuslanish", "Uyat", "Xijolat", "Ishonchsizlik", "Motam", "Qayg'u", "Hayajon", "O'kinch", "Xafalik", "G'araz", "Umidsizlik", "Shubha", "Iztirob", "Vijdon"]
        produxtalar = ["Go'sht", "Baliq", "Yog'", "Saryog'", "Un", "Non", "Makaron", "Guruch", "Mosh", "Noxat", "Loviya", "Tuxum", "Sut", "Qatiq", "Qaymoq", "Tvorog", "Pishloq", "Kolbasa", "Sosiska", "Qand", "Shakar", "Asal", "Choy", "Qahva", "Tuz", "Murch", "Zira", "Kashnich", "Ukrop", "Sirke", "Ketchup", "Mayonez"]
        movies = ["Titanik", "Avatar", "Terminator", "Rambo", "Rokki", "Gladiator", "Spartak", "Jasur yurak", "Matritsa", "Yulduzlararo", "GarriPotter", "Uzuklarhukmdori", "Xobbit", "O'rgimchakodam", "Supermen", "Betmen", "Temirodam", "Qasoskorlar", "QoraPantera", "Forsaj", "Transformatorlar", "Yuradavri", "KingKong", "Godzilla", "Qirolsher", "Uydayolg'iz", "Tarzan", "Alovuddin", "Muzlikdavri", "Shrek", "Madagaskar", "KungFuPanda", "Muzyurak", "TomvaJerri", "Pokémon", "Kalmaro'yini", "Qamoqdanqochish", "Taxtlaro'yini", "Mahalladaduvduvgap", "Abdullajon", "Shumbola"]
        diniy = ["Alloh", "Quron", "Hadis", "Islom", "Iymon", "Musulmon", "Ummat", "Duo", "Namoz", "Ro'za", "Haj", "Zakot", "Sadaqa", "Halol", "Harom", "Qibla", "Masjid", "Azon", "Ibodat", "Sajda", "Ruku", "Qiyom", "Takbir", "Tasbeh", "Tahorat", "G'usl", "Tayammum", "Imom", "Muazzin", "Jamoat", "Vitr", "Sunnat", "Farz", "Nafl", "Tarovih", "Janoza", "Sura", "Oyat", "Juz", "Tajvid", "Qiroat", "Tafsir", "Tazkiya", "Zikr", "Tasavvuf", "Tarbiya", "Shirk", "Kufr", "Munofiq", "Taqvo", "Sabr", "Shukr", "Adolat", "Tavba", "Payg'ambar", "Sahoba", "Ramazon", "Hayit", "Hijrat", "Inshaalloh", "Alhamdulillah", "Subhanalloh", "Lailahaillalloh", "Astagfirulloh", "Jannat", "Do'zax", "Mahshar", "Sirat", "Qazo", "Qadar"] # 70 
        zvaniya = ["Askar", "Kichikserjant", "Serjant", "Kattaserjant", "KichikLeytenant", "Leytenant", "KattaLeytenant", "Kapitan", "Mayyor", "Podpolkovnik", "Polkovnik", "Generalmayor", "GeneralLeytenant", "GeneralPolkovnik", "General"]
        inson_haraktirlari = ["Mehribon", "Sadoqatli", "Halol", "Adolatli", "Sabrli", "Shukrli", "Ishchan", "Mehnatkash", "Jasur", "Oqko'ngil", "Samimiy", "Tashabbuskor", "Sahiy", "Fidoiy", "Mard", "Muloyim", "Iymonli", "Oqibatli", "G'ururli", "Qadrdon", "O'zgaruvchan", "Topqir", "Tezkor", "Yordamchi", "Masuliyatli", "Qanoatli", "Xushmuomala", "Kamtar", "O'jar", "Maqtanchoq", "Mag'rur", "Ikkiyuzlamachi", "Adolatsiz", "Yolg'onchi", "Xasis", "Ochko'z", "Qo'rqoq", "Dangasa", "Jahldor", "Hasadchi", "Beparvo", "Qo'pol", "Nozik", "Oqil", "Tarbiyali", "Odobli", "Ishonchli", "O'ylovchan", "Sergap", "Hayolparast", "Hazilkash", "Xushchaqchaq"]
        games = ["Shaxmat", "Shashka", "Domino", "Narda", "Karta", "Futbol", "Basketbol", "Voleybol", "Tennis", "Badminton", "Bilyard", "Bowling", "PUBG", "Durak", "FIFA", "PES", "ClashofClans", "ClashRoyale", "CandyCrush", "AngryBirds"]
        cities = ["Parij", "London", "Dubai", "Tokio", "Roma", "Istanbul", "Madrid", "Berlin", "Maskva", "Pekin", "Shanxay", "Toshkent", "Samarqand", "Bali", "Antaliya", "Seul", "Bangkok", "Barselona", "LasVegas", "HongKong", "LosAngeles", "Sidney", "Florensiya", "Granada", "Sevilya", "Valensiya", "Bilbao", "Lyon", "Shiraz", "Qohira", "Budapesht", "Colombo", "KualaLumpur", "SanFransisko", "RiodeJaneyro", "Kasablanka", "Marakesh", "SanktPeterburg", "Mexiko"] # 40
        banks = ["Xalq", "Agro", "Mikrokredit", "Aloqa", "Ipoteka", "Turon", "Asaka", "Tenge", "Kapital", "Universal", "Hamkor", "Anor", "Davr", "Uzum", "Savdogar", "OrientFinans", "IpakYo'li", "Garant", "Infin", "Markaziy"]
        football_players = ["Pele", "Maradona", "Zidane", "Ronaldo", "Ronaldinho", "Karlos", "Pirlo", "Beckham", "Raul", "Henry", "DelPiero", "Kaka", "Eto'o", "Drogba", "Shevchenko", "Torres", "Rooney", "Lampard", "Gerrard", "Xavi", "Iniesta", "Casillas", "Puyol", "Neuer", "DaniAlves", "Marcelo", "Pique", "Ramos", "Vidic", "Terry", "Ferdinand", "Nesta", "Cannavaro", "Buffon", "Cristiano", "Messi", "Neymar", "Suarez", "Bale", "Lewandowski", "Benzema", "Ibragimovich", "Mbappe", "Haaland", "DeBruyne", "Modric", "Kroos", "Muller", "Schweinsteiger", "Robben", "Ribery", "O'zil", "Hazard", "Griezmann", "Kane", "Mane", "Salah", "Aubameyang", "Cavani", "Aguero", "DiMaria", "Dybala", "Coutinho", "DavidVilla", "Hierro", "Sanchez", "Navas", "Courtois"]
        jismoniy_harakatlar = ["Yurish", "Yugurish", "O'tirish", "Turish", "Yotish", "Uxlash", "Sakrash", "Ko'tarish", "Tushirish", "Olish", "Berish", "Tutish", "Uzatish", "Qo'yish", "Qochish", "Yiqilish", "Chopish", "Haydash", "Tushish", "Chaynash", "Ichish", "Yeyish", "Kirish", "Chiqish", "Qarash", "Ko'rish", "Eshitish", "Urish", "Qichqirish", "Yumish", "Ochish", "Bo'yash", "Tozalash", "Yuvish"]
        ruxiy_harakatlar = ["O'ylash", "Eslash", "Unutish", "Bilish", "Sezish", "Kulish", "Yig'lash", "Ajablanish", "Ishonish", "Shubhalanish", "O'rganish", "O'qish", "Hisqilish", "Anglash", "Tasdiqlash", "Hayajonlanish", "Faxrlanish", "Qo'rqish", "Tashvishlanish", "Xavotirlanish", "G'azablanish", "Xafabo'lish", "Afsuslanish"]
        matematika = ["Son", "Raqam", "Nol", "Bir", "Ikki", "Uch", "To'rt", "Besh", "Olti", "Yetti", "Sakkiz", "To'qqiz", "O'n", "Yuz", "Ming", "Million", "Milliard", "Juft", "Toq", "Qo'shish", "Ayirish", "Ko'paytirish", "Bo'lish", "Qoldiq", "Foiz", "Daraja", "Kvadrat", "Kub", "IldizOsti", "Yig'indi", "Ayirma", "Kasr", "Musbat", "Manfiy", "NaturalSon", "Butunson", "Ratsionalson", "Irratsionalson", "Radius", "Diametr", "Aylana", "Doira", "Perimetr", "Yuza", "Hajm", "Uchburchak", "To'rtburchak", "To'g'riburchak", "O'tkirburchak", "O'tmasburchak", "Paralel", "Perpendikulyar", "Chiziq", "Koordinata", "Grafik", "Formula", "Misol", "Masala", "Javob", "Tenglama", "Tengsizlik", "Funksiya", "Qiymat", "Logarifm", "Trigonometrik", "Sinus", "Kosinus", "Tangens", "Kotangens", "Pifagor", "Determinant", "Vektor", "Hisoblash", "Proportsiya", "Diagramma", "Faktorial", "Mediana", "Limit", "Integral", "Hosila"] # 80         
        fizika = ["Modda", "Jism", "Zarra", "Atom", "Molekula", "Proton", "Neytron", "Elektron", "Massa", "Hajm", "Zichlik", "Tezlik", "Tezlanish", "Vaqt", "Energiya", "Ish", "Quvvat", "Harakat", "Inersiya", "Kuch", "Tortish kuchi", "Gravitatsiya", "Ishqalanish", "Impuls", "Moment", "Bosim", "Og'irlik", "Arximedkuchi", "Prujina", "Taranglikkuchi", "Blok", "Harorat", "Termometr", "Issiqlik", "Qaynash", "Erish", "Bug'lanish", "Kondensatsiya", "Sublimatsiya", "Kaloriya", "Kelvin", "Tselsiy", "Farengeyt", "Tok", "Kuchlanish", "Qarshilik", "Ampermetr", "Voltmetr", "Galvanometr", "Generator", "Transformator", "Elektromagnit", "Magnitmaydon", "Tokkuchi", "Kondensator", "Induktsiya", "Elektrod", "Elektr", "Dielektrik", "Yoruglik", "Nurlanish", "Refleksiya", "Sinish", "Linza", "Oyna", "Mikroskop", "Teleskop", "Spektr", "Lazer", "Tovush", "Chastota", "Amplituda", "To'lqin", "Uzunlik", "Rezonans", "Vibratsiya", "Akustika", "Infratovush", "Ultratovush", "Termodinamika", "Konveksiya", "Radiatsiya", "Sig'imi", "O'tkazuvchanlik", "Entropiya", "Supero'tkazgich", "Dispersiya", "Interferensiya", "Difraksiya", "Kvant", "Foton", "Yadro", "Alfa", "Beta", "Gamma", "Relativlik", "Qoratuynuk", "Kvars"] # 100
        kimyo = ["Modda", "Element", "Atom", "Molekula", "Proton", "Neytron", "Elektron", "Izotop", "Ion", "Kation", "Anion", "Gaz", "Suyuqlik", "Plazma", "Uglerod", "Vodorod", "Kislorod", "Azot", "Metan", "Etan", "Propan", "Butan", "Natriy", "Kaliy", "Kaltsiy", "Magniy", "Alyuminiy", "Temir", "Mis", "Rux", "Qalay", "Qo'rg'oshin", "Oltin", "Kumush", "Platina", "Xlor", "Ftor", "Brom", "Yod", "Sul'fur", "Fosfor", "Silikon", "Benzol", "Spirt", "Glyukoza", "Suxaroza", "Oqsil", "Uglevod", "Polimer", "Plastik", "Kauchuk", "Teflon", "Aralashma", "Birikma", "Reaksiya", "Reagent", "Mahsulot", "Katalizator", "Yonish", "Neytrallash", "Oksidlanish", "Qaytarilish", "Eritma", "Erituvchi", "Kislota", "Konsentratsiya", "Diffuziya", "Distillatsiya", "Filtratsiya", "Kristallanish", "Bug'lanish", "Kondensatsiya", "Endotermik", "Ekzotermik", "Probirka", "Kolba", "Byureta", "Pipetka", "Termometr", "Laboratoriya"] # 80
        metros = ["Olmazor", "Chilonzor", "MirzoUlug'bek", "Novza", "Milliybog'", "Xalqlardo'stligi", "O'zbekiston", "Kosmonavtlar", "Paxtakor", "Mustaqillikmaydoni", "AmirTemur", "HamidOlimjon", "Pushkin", "BuyukIpakyo'li", "Beruniy", "Tinchlik", "Chorsu", "G'afurG'ulom", "AlisherNavoiy", "Oybek", "Toshkent", "Mashinasozlar", "Do'stlik", "Mingo'rik", "YunusRajabiy", "AbdullaQodiriy", "Minor", "Bodomzor", "Shahriston", "Yunusobod", "Turkiston", "Texnopark", "Yashnobod", "Tuzel", "Olmos", "Rohat", "Yangibozor", "Qo'yliq", "Matonat", "Tolariq", "Qiyot", "Xonobod", "Turon", "Chinor", "Qipchoq"] 
        company = ["Uzcard", "Humo", "Beeline", "Ucell", "Mobiuz", "Uzmobile", "Uztelecom", "Apple", "Samsung", "Huawei", "Nokia", "Sony", "LG", "HP", "Dell", "Asus", "Acer", "Artel", "Akfa", "Google", "Amazon", "Facebook", "Intel", "Nike", "Adidas", "Puma", "Zara", "Gucci", "Prada", "Rolex", "Canon", "Nikon", "Panasonic", "Bosch", "Nestle", "CocaCola", "Pepsi", "McDonalds", "Disney", "Pixar", "Marvel", "Fox", "Starbucks", "Lenovo", "Microsoft", "Epam", "Netflix", "Tesla", "SpaceX", "Toshiba", "Hitachi", "Yandex", "Alibaba"] 
        program = ["Oson", "Click", "Payme", "Paynet", "IMO", "OLX", "Clock", "Word", "Excel", "Zoom", "Gmail", "Google", "Browser", "Telegram", "Messenger", "WhatsApp", "Instagram", "Facebook", "YouTube", "Calendar", "Gallery", "Calculator", "Viber", "Skype", "Shazam", "Netflix", "Chrome", "MXPlayer", "Canva", "Twitter", "WeChat", "MyTaxi", "YandexGo", "GooglePlay", "PlayMarket", "AppStore", "GoogleMaps", "VoiceRecorder", "PowerPoint", "AnyDesk", "CapCut", "ChatGPT", "Telegraph", "Snapchat", "BigoLive", "AliExpress", "Amazon", "ZoodMall", "UzumMarket"] # 50
        programming = ["R", "Go", "PHP", "CSS", "Git", "SQL", "JSON", "XML", "Dart", "Rust", "Ruby", "Java", "Sass", "Less", "HTML", "Nodejs", "Linux", "Swift", "Vue", "jQuery", "Oracle", "MySQL", "Python", "React", "GSAP", "Flask", "Redis", "Vue", "Nextjs", "Nuxtjs", "MongoDB", "Chartjs", "Threejs", "Docker", "GitHub", "GitLab", "aHost", "Heroku", "Netlify", "Vercel", "Railway", "Firebase", "SQLite", "Tailwind", "Angular", "Django", "Spring", "Laravel", "Symfony", "NestJS", "FastAPI", "Expressjs", "Bootstrap", "Postman", "WebStorm", "PhpStorm", "CLion", "Xcode", "VSCode", "Brackets", "Webpack", "Matlab", "Kotlin", "Kalkulyator", "VisualStudio", "PyCharm", "Nextjs", "ObjectiveC", "IntelliJ IDEA", "AndroidStudio", "SublimeText", "CodeBlocks", "DigitalOcean", "JupyterNotebook", "PostgreSQL", "GoogleCloud", "WebSocket"] # 80
        tecnology = ["Soat", "Radio", "GPS", "WiFi", "iOS", "VPN", "iPad", "iPhone", "Dron", "Robot", "Kamera", "Planshet", "Android", "SIMkarta", "Naushnik", "Quloqchin", "Fleshka", "Windows", "Laptop", "Monitor", "Printer", "Skaner", "Server", "Router", "Kompyuter", "Smartfon", "Kalkulyator", "Televizor", "Muzlatgich", "Kirmashina", "Changyutgich", "Mikropech", "Gazplita", "Ventilyator", "Termometr", "Bankomat", "Navigator", "Notebook", "Klaviatura", "Protsessor", "Bluetooth", "Internet", "Zaryadlagich", "PowerBank", "Smartwatch", "Konditsioner", "PlayStation", "Desktop", "Modem"] # 50
        

        name_json = {
            "category": "Ism",
            "word": random.choice(names),
        }

        color_json = {
            "category": "Rang",
            "word": random.choice(colors),
        }

        calendar_json = {
            "category": "Kalendar",
            "word": random.choice(calendar),
        }

        animal_json = {
            "category": "Hayvon",
            "word": random.choice(animals),
        }

        fruit_json = {
            "category": "Meva",
            "word": random.choice(fruit),
        }

        vegetable_json = {
            "category": "Sabzavot",
            "word": random.choice(vegetables),
        }

        ovqat_json = {
            "category": "Ovqat",
            "word": random.choice(ovqatlar),
        }

        oila_va_qarindosh =  {
            "category": "Oila azosi yoki Qarindosh",
            "word": random.choice(oila_va_qarindoshlar),
        }

        sport = {
            "category": "Sport turi",
            "word": random.choice(sports),
        }
        
        maktab_anjom_json = {
            "category": "Maktab anjomi",
            "word": random.choice(maktab_anjomlar),
        }

        job_json = {
            "category": "Kasb",
            "word": random.choice(jobs),
        }

        nature_json = {
            "category": "Tabiat",
            "word": random.choice(names),
        }

        bird_json = {
            "category": "Qush",
            "word": random.choice(birds),
        }

        phone_json = {
            "category": "Telefon",
            "word": random.choice(phones),
        }

        uzb_region_json = {
            "category": "Uzb Shahar-tumanlar",
            "word": random.choice(uzb_regions),
        }

        country_json = {
            "category": "Davlatlar",
            "word": random.choice(countries),
        }

        kiyim_kichak_json = {
            "category": "Kiyim-Kichak",
            "word": random.choice(kiyim_kichaklar),
        }

        oshxona_buyumlar = {
            "category": "Oshxona buyumlar",
            "word": random.choice(oshxona_buyumlar),
        }

        car_json = {
            "category": "Moshina",
            "word": random.choice(cars),
        }

        his_tuygu_json = {
            "category": "His-tuyg'u",
            "word": random.choice(his_tuygular),
        }

        produxta_json = {
            "category": "Produxta",
            "word": random.choice(produxtalar),
        }

        movie_json = {
            "category": "Kino nomi",
            "word": random.choice(movies),
        }

        diniy_json = {
            "category": "Islomiy so'zlar",
            "word": random.choice(diniy),
        }

        zvaniya_json = {
            "category": "Unvon",
            "word": random.choice(zvaniya),
        }

        inson_haraktir_json = {
            "category": "Inson haraktiri",
            "word": random.choice(inson_haraktirlari),
        }

        game_json = {
            "category": "O'yin",
            "word": random.choice(games),
        }

        city_json = {
            "category": "Mashhur Shahar",
            "word": random.choice(cities),
        }

        bank_json = {
            "category": "Bank",
            "word": random.choice(banks),
        }

        football_player_json = {
            "category": "Futbolchi",
            "word": random.choice(football_players),
        }

        jismoniy_harakat_json = {
            "category": "Jismoniy harakatlar",
            "word": random.choice(jismoniy_harakatlar),
        }

        ruxiy_harakat_json = {
            "category": "Ruxiy harakatlar",
            "word": random.choice(ruxiy_harakatlar),
        }

        matematika_json = {
            "category": "Matematika",
            "word": random.choice(matematika),
        }

        fizika_json = {
            "category": "Fizika",
            "word": random.choice(fizika),
        }

        kimyo_json = {
            "category": "Kimyo",
            "word": random.choice(kimyo),
        }

        metro_json = {
            "category": "Metro bekati",
            "word": random.choice(metros),
        }

        company_json = {
            "category": "Kampaniya",
            "word": random.choice(company),
        }

        program_json = {
            "category": "Kerakli Dasturlar",
            "word": random.choice(program),
        }

        programming_json = {
            "category": "Dasturlash",
            "word": random.choice(programming),
        }

        tecnology_json = {
            "category": "Texnologiya",
            "word": random.choice(tecnology),
        }







        return Response(tecnology) 