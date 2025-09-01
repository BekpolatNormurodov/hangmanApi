from rest_framework.views import APIView
from rest_framework.response import Response
import random


class Viktoriya(APIView):
    def get(self, request):

        quiz_1 = {
            "question": "Yerning sun'iy yo'ldoshi?",
            "answer": "Oy",
            "variant": ["Venera", "Oy", "Quyosh", "Mars"]
        }
        quiz_2 = {
            "question": "Osmonga eng yaqin yulduz?",
            "answer": "Quyosh",
            "variant": ["Proksima", "Sirius", "Quyosh", "Vega"]
        }
        quiz_3 = {
            "question": "Eng baland tog' cho'qqisi?",
            "answer": "Everest",
            "variant": ["Kilimanjaro", "Elbrus", "Everest", "K2"]
        }
        quiz_4 = {
            "question": "Eng katta cho'l?",
            "answer": "Saxara",
            "variant": ["Karakum", "Saxara", "Atakama", "Qizilqum"]
        }
        quiz_5 = {
            "question": "Eng katta okean?",
            "answer": "Tinch",
            "variant": ["Hind", "Tinch", "Atlantika", "Shimoliy Muz"]
        }
        quiz_6 = {
            "question": "Eng uzun daryo?",
            "answer": "Nil",
            "variant": ["Amazonka", "Yanszi", "Nil", "Mississippi"]
        }
        quiz_7 = {
            "question": "O'zbekistonning eng katta daryosi?",
            "answer": "Amudaryo",
            "variant": ["Amudaryo", "Zarafshon", "Chirchiq", "Sirdaryo"]
        }
        quiz_8 = {
            "question": "O'zbekistonning milliy taomi?",
            "answer": "Plov",
            "variant": ["Lag'mon", "Manti", "Somsa", "Plov"]
        }
        quiz_9 = {
            "question": "Eng tez quruqlik hayvoni?",
            "answer": "Gepard",
            "variant": ["Ot", "Gepard", "Bo'ri", "Sher"]
        }
        quiz_10 = {
            "question": "Qushlarning eng kichigi?",
            "answer": "Kolibri",
            "variant": ["Kolibri", "Bulbul", "Qaldirg'och", "To'tiqush"]
        }
        quiz_11 = {
            "question": "Eng yirik sutemizuvchi?",
            "answer": "Kit",
            "variant": ["Fil", "Kit", "Begemot", "Kashalot"]
        }
        quiz_12 = {
            "question": "Xona haroratida suyuq metall?",
            "answer": "Simob",
            "variant": ["Simob", "Mis", "Qo'rg'oshin", "Oltin"]
        }
        quiz_13 = {
            "question": "Yerning ichki markaziy qismi?",
            "answer": "Yadro",
            "variant": ["Qobiq", "Mantiya", "Yadro", "Litosfera"]
        }
        quiz_14 = {
            "question": "O'zbekiston ramzidagi afsonaviy qush?",
            "answer": "Humo",
            "variant": ["Lochin", "Burgut", "Humo", "Qarg'a"]
        }
        quiz_15 = {
            "question": "Piramidalar mamlakati?",
            "answer": "Misr",
            "variant": ["Xitoy", "Iroq", "Misr", "Yunoniston"]
        }
        quiz_16 = {
            "question": "Futbol vatani?",
            "answer": "Angliya",
            "variant": ["Angliya", "Braziliya", "Ispaniya", "Italiya"]
        }
        quiz_17 = {
            "question": "Olimpiya o'yinlari vatani?",
            "answer": "Yunoniston",
            "variant": ["Xitoy", "Rim", "Yunoniston", "Fransiya"]
        }
        quiz_18 = {
            "question": "Shaxmat vatani?",
            "answer": "Hindiston",
            "variant": ["Eron", "Xitoy", "Rossiya", "Hindiston"]
        }
        quiz_19 = {
            "question": "Telefon ixtirochisi familiyasi?",
            "answer": "Bell",
            "variant": ["Marconi", "Edison", "Tesla", "Bell"]
        }
        quiz_20 = {
            "question": "Kimyoviy jadval muallifi?",
            "answer": "Mendeleyev",
            "variant": ["Dalton", "Lavoazye", "Mendeleyev", "Bor"]
        }
        quiz_21 = {
            "question": "Nisbiylik nazariyasi muallifi?",
            "answer": "Eynshtayn",
            "variant": ["Eynshtayn", "Bor", "Nyuton", "Planck"]
        }
        quiz_22 = {
            "question": "Gravitatsiya qonuni muallifi?",
            "answer": "Nyuton",
            "variant": ["Galiley", "Kepler", "Eynshtayn", "Nyuton"]
        }
        quiz_23 = {
            "question": "Zoologiya peshvosi?",
            "answer": "Aristotel",
            "variant": ["Aristotel", "Gippokrat", "Platon", "Darvin"]
        }
        quiz_24 = {
            "question": "Quyosh tizimidagi eng katta sayyora?",
            "answer": "Yupiter",
            "variant": ["Saturn", "Yupiter", "Uran", "Neptun"]
        }
        quiz_25 = {
            "question": "Halqalari bilan mashhur sayyora?",
            "answer": "Saturn",
            "variant": ["Saturn", "Yupiter", "Uran", "Neptun"]
        }
        quiz_26 = {
            "question": "Qizil sayyora nomi?",
            "answer": "Mars",
            "variant": ["Mars", "Venera", "Pluton", "Merkuriy"]
        }
        quiz_27 = {
            "question": "Quyoshga eng yaqin sayyora?",
            "answer": "Merkuriy",
            "variant": ["Yer", "Mars", "Merkuriy", "Venera"]
        }
        quiz_28 = {
            "question": "Oy yuzasidagi qoramtir tekislik?",
            "answer": "Dengiz",
            "variant": ["Dengiz", "Plato", "Qit'a", "Krater"]
        }
        quiz_29 = {
            "question": "Juda zich yulduz qoldig'i?",
            "answer": "Neytron",
            "variant": ["Oq mitti", "Neytron", "Qora tuynuk", "Qizil ulkan"]
        }
        quiz_30 = {
            "question": "Yulduz portlashi hodisasi?",
            "answer": "Supernova",
            "variant": ["Komet", "Supernova", "Aurore", "Kuar"]
        }
        quiz_31 = {
            "question": "Quyoshdan keyingi yaqin yulduz?",
            "answer": "Proksima",
            "variant": ["Sirius", "Alpha Centauri A", "Betelgeyze", "Proksima"]
        }
        quiz_32 = {
            "question": "Eng chuqur ko'l?",
            "answer": "Baykal",
            "variant": ["Aral", "Tanganika", "Baykal", "Kaspiy"]
        }
        quiz_33 = {
            "question": "Eng katta orol?",
            "answer": "Grenlandiya",
            "variant": ["Grenlandiya", "Yangi Gvineya", "Borneo", "Madagaskar"]
        }
        quiz_34 = {
            "question": "Shimoliy qutb okeani nomi?",
            "answer": "Arktika",
            "variant": ["Antarktika", "Arktika", "Tinch", "Atlantika"]
        }
        quiz_35 = {
            "question": "Janubiy qutb materigi?",
            "answer": "Antarktida",
            "variant": ["Janubiy Amerika", "Antarktida", "Avstraliya", "Afrika"]
        }
        quiz_36 = {
            "question": "Yevropa va Osiyoni ajratuvchi tog'?",
            "answer": "Ural",
            "variant": ["Kavkaz", "Qorabog'", "Ural", "Tyan-Shan"]
        }
        quiz_37 = {
            "question": "O'zbekiston qadimiy shahri?",
            "answer": "Buxoro",
            "variant": ["Namangan", "Buxoro", "Guliston", "Nukus"]
        }
        quiz_38 = {
            "question": "Samarqanddagi mashhur majmua?",
            "answer": "Registon",
            "variant": ["Registon", "Hazrati Imom", "Ichanqala", "Shohi Zinda"]
        }
        quiz_39 = {
            "question": "Xivadagi qadimiy hudud?",
            "answer": "Ichanqala",
            "variant": ["Chor Minor", "Registon", "Ark", "Ichanqala"]
        }
        quiz_40 = {
            "question": "Xorazmdagi qadimiy qal'alar?",
            "answer": "Ellikqala",
            "variant": ["Ellikqala", "Ayazqala", "Topraqqala", "Qoyqirilganqala"]
        }
        quiz_41 = {
            "question": "O'zbekistonning g'arbiy cho'li?",
            "answer": "Qizilqum",
            "variant": ["Qizilqum", "Atakama", "Karakum", "Saxara"]
        }
        quiz_42 = {
            "question": "O'zbekistonning eng katta ko'li?",
            "answer": "Aral",
            "variant": ["Sudochye", "Aydarko'l", "Aral", "Qorako'l"]
        }
        quiz_43 = {
            "question": "Ovqatni parchalaydigan oqsil?",
            "answer": "Ferment",
            "variant": ["Antitanacha", "Hemoglobin", "Gormon", "Ferment"]
        }
        quiz_44 = {
            "question": "Nafas olish uchun zarur gaz?",
            "answer": "Kislorod",
            "variant": ["Karbonat angidrid", "Azot", "Kislorod", "Geliy"]
        }
        quiz_45 = {
            "question": "Suyak mustahkam elementi?",
            "answer": "Kalsiy",
            "variant": ["Kaliy", "Fosfor", "Kalsiy", "Natriy"]
        }
        quiz_46 = {
            "question": "Inson tanasidagi eng katta organ?",
            "answer": "Teri",
            "variant": ["Jigar", "Teri", "Yurak", "O'pka"]
        }
        quiz_47 = {
            "question": "Eng uzun odam suyagi?",
            "answer": "Son",
            "variant": ["Tizza suyagi", "O'mrov", "Son", "Bilak"]
        }
        quiz_48 = {
            "question": "Eng kuchli odam mushagi?",
            "answer": "Til",
            "variant": ["Biceps", "Yurak", "Boldir", "Til"]
        }
        quiz_49 = {
            "question": "Insonning asosiy qon aylantiruvchi a'zosi?",
            "answer": "Yurak",
            "variant": ["Miya", "Yurak", "O'pka", "Jigar"]
        }
        quiz_50 = {
            "question": "Islomning oxirgi payg'ambari?",
            "answer": "Muhammad",
            "variant": ["Muhammad", "Musho", "Ibrohim", "Iso"]
        }
        quiz_51 = {
            "question": "Makka markazidagi muqaddas inshoot?",
            "answer": "Kaaba",
            "variant": ["Hira g'ori", "Kaaba", "Masjid al-Aqso", "Masjid an-Nabaviy"]
        }
        quiz_52 = {
            "question": "Musulmon ibodat yo'nalishi?",
            "answer": "Qibla",
            "variant": ["Sajda", "Tavof", "Rukoo'", "Qibla"]
        }
        quiz_53 = {
            "question": "Islomning asosiy kitobi?",
            "answer": "Qur'on",
            "variant": ["Qur'on", "Zabur", "Tavrot", "Injil"]
        }
        quiz_54 = {
            "question": "Xristianlik markaziy shaxsi?",
            "answer": "Iso",
            "variant": ["Yahyo", "Muso", "Ibrohim", "Iso"]
        }
        quiz_55 = {
            "question": "Budda tug'ilgan mamlakat?",
            "answer": "Hindiston",
            "variant": ["Nepal", "Yaponiya", "Hindiston", "Xitoy"]
        }
        quiz_56 = {
            "question": "Sharq tabobati allomasi?",
            "answer": "Ibnsino",
            "variant": ["Razi", "Beruniy", "Ibnsino", "Forobiy"]
        }
        quiz_57 = {
            "question": "Mashhur temuriy astronom?",
            "answer": "Ulug'bek",
            "variant": ["Beruniy", "Ali Qushchi", "Navoiy", "Ulug'bek"]
        }
        quiz_58 = {
            "question": "Xamsa muallifi shoir?",
            "answer": "Navoiy",
            "variant": ["Navoiy", "Jomiy", "Bobur", "Fuzuliy"]
        }
        quiz_59 = {
            "question": "Hamlet muallifi?",
            "answer": "Shekspir",
            "variant": ["Shekspir", "Chexov", "Pushkin", "Servantes"]
        }
        quiz_60 = {
            "question": "Don Kixot muallifi?",
            "answer": "Servantes",
            "variant": ["Balzak", "Servantes", "Shekspir", "Dante"]
        }
        quiz_61 = {
            "question": "Mona Liza muallifi?",
            "answer": "Leonardo",
            "variant": ["Rafael", "Donatello", "Mikelanjelo", "Leonardo"]
        }
        quiz_62 = {
            "question": "Layli va Majnun muallifi?",
            "answer": "Nizomiy",
            "variant": ["Jomiy", "Navoiy", "Nizomiy", "Fuzuliy"]
        }
        quiz_63 = {
            "question": "Kosmosga chiqqan birinchi odam?",
            "answer": "Gagarin",
            "variant": ["Armstrong", "Titov", "Tereshkova", "Gagarin"]
        }
        quiz_64 = {
            "question": "Oyga qadam qo'ygan birinchi inson?",
            "answer": "Armstrong",
            "variant": ["Armstrong", "Aldrin", "Kollins", "Gagarin"]
        }
        quiz_65 = {
            "question": "Dunyoni aylanib chiqqan sayyoh?",
            "answer": "Magellan",
            "variant": ["Kolumb", "Magellan", "Kuk", "Vasko da Gama"]
        }
        quiz_66 = {
            "question": "Eng mashhur minorasi?",
            "answer": "Eyfel",
            "variant": ["Eyfel", "Qal'a minorasi", "Shamol minorasi", "Piza"]
        }
        quiz_67 = {
            "question": "Eng mashhur haykal?",
            "answer": "Ozodlik",
            "variant": ["Ozodlik", "Buyuk Sfenks", "Dovud", "Yaxshi niyat"]
        }
        quiz_68 = {
            "question": "Eng mashhur teatr?",
            "answer": "Bolshoy",
            "variant": ["La Skala", "Kovent Garden", "Metropoliten", "Bolshoy"]
        }
        quiz_69 = {
            "question": "Eng mashhur kino markazi?",
            "answer": "Gollivud",
            "variant": ["Pinewood", "Bollywood", "Mosfilm", "Gollivud"]
        }
        quiz_70 = {
            "question": "Eng mashhur multfilm markazi?",
            "answer": "Disney",
            "variant": ["Disney", "Illumination", "DreamWorks", "Pixar"]
        }
        quiz_71 = {
            "question": "Eng baland bino?",
            "answer": "Burj",
            "variant": ["Shanghai Tower", "Abraj Al-Bayt", "One World Trade", "Burj"]
        }
        quiz_72 = {
            "question": "Eng katta masjid?",
            "answer": "Harom",
            "variant": ["Masjid an-Nabaviy", "Al-Azhar", "Al-Aqso", "Harom"]
        }
        quiz_73 = {
            "question": "Uzbekistondagi eng katta stadion?",
            "answer": "Bunyodkor",
            "variant": ["Paxtakor", "Jar", "Bunyodkor", "Markaziy"]
        }
        quiz_74 = {
            "question": "Eng mashhur simfoniya bastakori?",
            "answer": "Betxoven",
            "variant": ["Betxoven", "Chaykovskiy", "Motsart", "Bax"]
        }
        quiz_75 = {
            "question": "Eng mashhur italyan rassomi?",
            "answer": "Leonardo",
            "variant": ["Leonardo", "Bottichelli", "Karavaggio", "Rafael"]
        }
        quiz_76 = {
            "question": "Eng mashhur ispan rassomi?",
            "answer": "Pikasso",
            "variant": ["Dali", "Goya", "Velaskes", "Pikasso"]
        }
        quiz_77 = {
            "question": "Mashhur yunon matematik?",
            "answer": "Pifagor",
            "variant": ["Pifagor", "Arximed", "Tales", "Evklid"]
        }
        quiz_78 = {
            "question": "Mashhur ixtirochi chiroq?",
            "answer": "Edison",
            "variant": ["Bell", "Volta", "Edison", "Tesla"]
        }
        quiz_79 = {
            "question": "Eng mashhur futbol klubi?",
            "answer": "Real",
            "variant": ["Bavariya", "Real", "Barselona", "Liverpul"]
        }
        quiz_80 = {
            "question": "Eng mashhur futbolchi?",
            "answer": "Ranoldo",
            "variant": ["Pele", "Ranoldo", "Maradona", "Messi"]
        }
        quiz_81 = {
            "question": "Eng mashhur basketbolchi?",
            "answer": "Jordan",
            "variant": ["LeBron", "Bryant", "O'Neal", "Jordan"]
        }
        quiz_82 = {
            "question": "Eng mashhur bokschi?",
            "answer": "Ali",
            "variant": ["Holyfield", "Mayweather", "Ali", "Tyson"]
        }
        quiz_83 = {
            "question": "Eng mashhur tennischi?",
            "answer": "Federer",
            "variant": ["Federer", "Djokovich", "Sampras", "Nadal"]
        }
        quiz_84 = {
            "question": "Eng mashhur shaxmatchi?",
            "answer": "Kasparov",
            "variant": ["Karpov", "Fisher", "Kasparov", "Carlsen"]
        }
        quiz_85 = {
            "question": "Eng mashhur kino aktyor?",
            "answer": "Chaplin",
            "variant": ["Hanks", "Chaplin", "Pitt", "De Niro"]
        }
        quiz_86 = {
            "question": "Eng mashhur amerikalik kino aktyori?",
            "answer": "DiCaprio",
            "variant": ["Tom Cruise", "DiCaprio", "Johnny Depp", "Brad Pitt"]
        }
        quiz_87 = {
            "question": "Eng mashhur hind kino aktyori?",
            "answer": "Shoxruxxon",
            "variant": ["Salmonxon", "Shoxruxxon", "Amitabh", "Amirxon"]
        }
        quiz_88 = {
            "question": "Eng mashhur xitoy kino aktyori?",
            "answer": "JekiChan",
            "variant": ["Endi Lau", "JekiChan", "Jet Li", "Donni Yen"]
        }
        quiz_89 = {
            "question": "Eng mashhur turk sultoni?",
            "answer": "Suleyman",
            "variant": ["Osmon G'oziy", "Suleyman", "Selim I", "Mehmed II"]
        }
        quiz_90 = {
            "question": "Eng mashhur mo'g'ul sarkardasi?",
            "answer": "Chingiz",
            "variant": ["Batu", "Subutoy", "Teymur", "Chingiz"]
        }
        quiz_91 = {
            "question": "Eng mashhur rim sarkardasi?",
            "answer": "Sezar",
            "variant": ["Sezar", "Avgust", "Traian", "Neron"]
        }
        quiz_92 = {
            "question": "Eng mashhur yunon sarkardasi?",
            "answer": "Aleksandr",
            "variant": ["Afina", "Aleksandr", "Perikl", "Leonid"]
        }
        quiz_93 = {
            "question": "Eng mashhur ingliz qirolichasi?",
            "answer": "Yelizaveta",
            "variant": ["Anna", "Yelizaveta", "Viktoriya", "Merigold"]
        }
        quiz_94 = {
            "question": "Eng mashhur fransuz imperatori?",
            "answer": "Napoleon",
            "variant": ["Lyudovik XIV", "Napoleon", "Sharl De Goll", "Filipp"]
        }
        quiz_95 = {
            "question": "Eng mashhur rus imperatori?",
            "answer": "Pyotr",
            "variant": ["Nikolay", "Pavel", "Pyotr", "Ivan IV"]
        }
        quiz_96 = {
            "question": "Eng mashhur rus shoiri?",
            "answer": "Pushkin",
            "variant": ["Yesenin", "Lermontov", "Mayakovskiy", "Pushkin"]
        }
        quiz_97 = {
            "question": "Eng mashhur turkiy shoir?",
            "answer": "Yassaviy",
            "variant": ["Sakkokiy", "Yassaviy", "Mashrab", "Alisher"]
        }
        quiz_98 = {
            "question": "Eng mashhur uyg'ur shoiri?",
            "answer": "Lutfiy",
            "variant": ["Amiriy", "Sakkokiy", "Atayi", "Lutfiy"]
        }
        quiz_99 = {
            "question": "Eng mashhur o'zbek shoiri?",
            "answer": "Navoiy",
            "variant": ["Cho'lpon", "Furqat", "Bobur", "Navoiy"]
        }
        quiz_100 = {
            "question": "Eng mashhur xitoy faylasufi?",
            "answer": "Konfutsiy",
            "variant": ["Konfutsiy", "Men-Szi", "Lao Sz", "Sun Szi"]
        }

        
        quizzes = [quiz_1, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10, quiz_11, quiz_12, quiz_13, quiz_14, quiz_15, quiz_16, quiz_17, quiz_18, quiz_19, quiz_20, quiz_21, quiz_22, quiz_23, quiz_24, quiz_25, quiz_26, quiz_27, quiz_28, quiz_29, quiz_30, quiz_31, quiz_32, quiz_33, quiz_34, quiz_35, quiz_36, quiz_37, quiz_38, quiz_39, quiz_40, quiz_41, quiz_42, quiz_43, quiz_44, quiz_45, quiz_46, quiz_47, quiz_48, quiz_49, quiz_50, quiz_51, quiz_52, quiz_53, quiz_54, quiz_55, quiz_56, quiz_57, quiz_58, quiz_59, quiz_60, quiz_61, quiz_62, quiz_63, quiz_64, quiz_65, quiz_66, quiz_67, quiz_68, quiz_69, quiz_70, quiz_71, quiz_72, quiz_73, quiz_74, quiz_75, quiz_76, quiz_77, quiz_78, quiz_79, quiz_80, quiz_81, quiz_82, quiz_83, quiz_84, quiz_85, quiz_86, quiz_87, quiz_88, quiz_89, quiz_90, quiz_91, quiz_92, quiz_93, quiz_94, quiz_95, quiz_96, quiz_97, quiz_98, quiz_99, quiz_100]




        
        return Response(name) 
