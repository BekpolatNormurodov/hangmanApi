from rest_framework.views import APIView
from rest_framework.response import Response
import random

class MaqolApi(APIView):
    def get(self, request):

        maqol_1 = [
            {
                "savol": "Kuch - ....",
                "javob": "birlikda"
            },
            {
                "savol": "Faqir kishi ....",
                "javob": "panada"
            },
            {
                "savol": "Erning so'zi ....",
                "javob": "bitta"
            },
            {
                "savol": "Falokat oyoq ....",
                "javob": "ostida"
            },
            {
                "savol": "Kuz — .... fasli.",
                "javob": "hosil"
            }]

        maqol_2 = [
            {
                "savol": "Elchiga .... yo'q.",
                "javob": "o'lim"
            },
            {
                "savol": "Hisobli do'st ....",
                "javob": "ayrilmas"
            },
            {
                "savol": "Ko'p gap .... yuk.",
                "javob": "eshakka"
            },
            {
                "savol": "Mard maydonda ....",
                "javob": "sinalar"
            },
            {
                "savol": "Yaxshi so'z - ....",
                "javob": "sadaqa"
            }]

        maqol_3 = [
            {
                "savol": "....ning tagi rohat",
                "javob": "mehnat"
            },
            {
                "savol": "Nomus o'limdan ....",
                "javob": "kuchli"
            },
            {
                "savol": "Hasad — qalbni ....",
                "javob": "chiritadi"
            },
            {
                "savol": "Til — qalbning ....",
                "javob": "tarjimoni"
            },
            {
                "savol": "Ko'p gap - .... yuk",
                "javob": "eshakka"
            }]

        maqol_4 = [
            {
                "savol": "Andishaning oti ....",
                "javob": "qo'rqoq"
            },
            {
                "savol": "Hur gulning isi ....",
                "javob": "boshqa"
            },
            {
                "savol": "Har kallada har ....",
                "javob": "hayol"
            },
            {
                "savol": "Intilganga tole ....",
                "javob": "yor"
            },
            {
                "savol": "Jahl kelsa, aql ....",
                "javob": "ketar"
            }]

        maqol_5 = [
            {
                "savol": "Mehmon otangdan ....",
                "javob": "ulug'"
            },
            {
                "savol": "Hovli olma, .... ol.",
                "javob": "qo'shni"
            },
            {
                "savol": "Til - insonning ....",
                "javob": "oynasi"
            },
            {
                "savol": "Har kim ekkanini ....",
                "javob": "o'radi"
            },
            {
                "savol": "Har to'kisda bir ....",
                "javob": "ayb"
            }]

        maqol_6 = [
            {
                "savol": "Hunar - hunardan ....",
                "javob": "unar"
            },
            {
                "savol": ".... kishi och qolmas",
                "javob": "hunarli"
            },
            {
                "savol": "Ikki yorti - bir ....",
                "javob": "butun"
            },
            {
                "savol": "It hurar, karvon ....",
                "javob": "o'tar"
            },
            {
                "savol": "Bukrini .... tuzatadi.",
                "javob": "g'or"
            }]

        maqol_7 = [
            {
                "savol": "Danagidan .... shirin.",
                "javob": "mag'izi"
            },
            {
                "savol": "Eru xotin - qo'sh ....",
                "javob": "ho'kiz"
            },
            {
                "savol": ".... olma, qo'shni ol.",
                "javob": "hovli"
            },
            {
                "savol": "Nima eksang shuni ....",
                "javob": "o'rasan"
            },
            {
                "savol": "Hunarli kishi och ....",
                "javob": "qolmas"
            }]

        maqol_8 = [
            {
                "savol": "Farzandning baxti ....",
                "javob": "duo"
            },
            {
                "savol": "Onaning ko‘z nuri ....",
                "javob": "farzand"
            },
            {
                "savol": "Avval o'yla, keyin ....",
                "javob": "so'yla"
            },
            {
                "savol": "Ko'z qo'rqoq, qo'l ....",
                "javob": "botir"
            },
            {
                "savol": "Ish bor yerda .... bor.",
                "javob": "xato"
            }]

        maqol_9 = [
            {
                "savol": "oz so'zla - .... so'zla",
                "javob": "soz"
            },
            {
                "savol": "Do'sting uchun .... yut.",
                "javob": "zahar"
            },
            {
                "savol": "Ering suydi - eling ....",
                "javob": "suydi"
            },
            {
                "savol": "“Hayt” degan tuyaga ....",
                "javob": "mador"
            },
            {
                "savol": ".... bor yerda xato bor.",
                "javob": "ish"
            }]

        maqol_10 = [
            {
                "savol": "Mol achchig'i - jon ....",
                "javob": "achchig'i"
            },
            {
                "savol": ".... rizqning kalitidir.",
                "javob": "mehnat"
            },
            {
                "savol": "Sog‘liq — eng katta ....",
                "javob": "boylik"
            },
            {
                "savol": "Ayol - gul, erkak - ....",
                "javob": "bog'bon"
            },
            {
                "savol": "Janjalli uyda baraka ....",
                "javob": "bo'lmas"
            }]

        maqol_11 = [
            {
                "savol": "Ko'pdan quyon qochib ....",
                "javob": "qutulmas"
            },
            {
                "savol": "Nomi ulug' - suprasi ....",
                "javob": "quruq"
            },
            {
                "savol": "Nafsi g'olib hayitda ....",
                "javob": "o'ladi"
            },
            {
                "savol": "Har xato - yangi bir ....",
                "javob": "saboq"
            },
            {
                "savol": "Yaxshi niyat — yarim ....",
                "javob": "davlat"
            }]

        maqol_12 = [
            {
                "savol": "Buqdan qo'rqqan tezak ....",
                "javob": "yopmaydi"
            },
            {
                "savol": "El og'ziga elak tutib ....",
                "javob": "bo'lmas"
            },
            {
                "savol": "Hazil, hazilning tagi ....",
                "javob": "zil"
            },
            {
                "savol": "Haqiqat egiladi, ammo ....",
                "javob": "sinmaydi"
            },
            {
                "savol": "Ishongan tog'da kiyik ....",
                "javob": "yotmas"
            }]

        maqol_13 = [
            {
                "savol": "Ko'rpangga qarab oyoq ....",
                "javob": "uzat"
            },
            {
                "savol": "O'qish insonni .... qiladi",
                "javob": "inson"
            },
            {
                "savol": "Bir mayizni .... kishi yer.",
                "javob": "qirq"
            },
            {
                "savol": "Egilgan boshni .... kesmas.",
                "javob": "qilich"
            },
            {
                "savol": "Ezgulikning erta kechi ....",
                "javob": "yo'q"
            }]

        maqol_14 = [
            {
                "savol": "Husn to'yda kerak, aql ....",
                "javob": "kunda"
            },
            {
                "savol": "Ko'r ko'rni qorong'uda ....",
                "javob": "topadi"
            },
            {
                "savol": "Mehnat - mehnatni tagi ....",
                "javob": "rohat"
            },
            {
                "savol": "Odobli bola - oilaning ....",
                "javob": "ko'zgusi"
            },
            {
                "savol": ".... qilsang - .... topasan",
                "javob": "hurmat"
            }]

        maqol_15 = [
            {
                "savol": "Yaxshi qo‘shni — yarim ....",
                "javob": "qarindosh"
            },
            {
                "savol": "Aytilgan so'z - otilgan ....",
                "javob": "o'q"
            },
            {
                "savol": "Er yigitning uyalgani - ....",
                "javob": "o'lgani"
            },
            {
                "savol": "Kemaga tushganning joni ....",
                "javob": "bir"
            },
            {
                "savol": ".... bilib  - ustunsiz bina.",
                "javob": "ustozsiz"
            }]

        maqol_16 = [
            {
                "savol": "Birniki mingga, mingniki ....",
                "javob": "olamda"
            },
            {
                "savol": "Do'stsiz boshim - tuzsiz ....",
                "javob": "oshim"
            },
            {
                "savol": "Kamtarga kamol, manmanga ....",
                "javob": "zavol"
            },
            {
                "savol": "Ko'r hassasini bir marta ....",
                "javob": "yo'qotadi"
            },
            {
                "savol": "Non ham non, ushog'i ham ....",
                "javob": "non"
            }]

        maqol_17 = [
            {
                "savol": "Aqilli bosh - ming .... teng.",
                "javob": "qo'lga"
            },
            {
                "savol": ".... onalar oyog'i ostidadur.",
                "javob": "jannat"
            },
            {
                "savol": "Alloh rizqni ....ga bog'lagan",
                "javob": "mehnat"
            },
            {
                "savol": ".... - o'zligingni topishdir.",
                "javob": "baxt"
            },
            {
                "savol": "Sukut bazan eng dono javobdir.",
                "javob": ""
            }]

        maqol_18 = [
            {
                "savol": "Kattaga hurmat - kichikka ....",
                "javob": "izzat"
            },
            {
                "savol": "Do'st - ...., dushman soyadir.",
                "javob": "oyna"
            },
            {
                "savol": "Esingning borida etagingni ....",
                "javob": "yop"
            },
            {
                "savol": "Kambag'al bo'lsang ko'chib ....",
                "javob": "boq"
            },
            {
                "savol": "Kerakli toshning og'irligi ....",
                "javob": "yo'q"
            }]

        maqol_19 = [
            {
                "savol": "Mug'ombir o'z tumshug'idan ....",
                "javob": "ilinar"
            },
            {
                "savol": "Ota-onani sevgan - .... sevadi.",
                "javob": "vatanni"
            },
            {
                "savol": "Har danday amal - .... bog'liq.",
                "javob": "niyatga"
            },
            {
                "savol": "Har bir kun - hayotdan bir ....",
                "javob": "sahifa"
            },
            {
                "savol": "Ayol - uy bekasi, erkak uy ....",
                "javob": "egasi"
            }]

        maqol_20 = [
            {
                "savol": "Aqlli o'zini ayblar, aqlsiz ....",
                "javob": "do'stini"
            },
            {
                "savol": "Do'st boshga boqar, dushman ....",
                "javob": "oyoqqa"
            },
            {
                "savol": "Har qush uyasida ko'rganini ....",
                "javob": "qiladi"
            },
            {
                "savol": "Kim tabib - boshidan o'tgan ....",
                "javob": "tabib"
            },
            {
                "savol": "Obro‘ — insonning ko'rinmas ....",
                "javob": "boyligi"
            }]

        maqol_21 = [
            {
                "savol": "So'zga emas, .... ham quloq sol.",
                "javob": "sukutga"
            },
            {
                "savol": "O'rgatish - ilmni .... qilishdir",
                "javob": "sadaqa"
            },
            {
                "savol": ".... yoshda emas, boshda bo'ladi.",
                "javob": "aql"
            },
            {
                "savol": "Bahor — tabiatning qayta ....dir.",
                "javob": "tirilishi"
            },
            {
                "savol": "Rizqni tor qiladigan narsa — ....",
                "javob": "isrof"
            }]

        maqol_22 = [
            {
                "savol": "Hurmat — insonning eng katta ....",
                "javob": "boyligi"
            },
            {
                "savol": "Chin .... og'ir kuningda bilinadi",
                "javob": "do'st"
            },
            {
                "savol": "Bir kattaning gapiga kir, bir ....",
                "javob": "kichikning"
            },
            {
                "savol": "Birovga choh qazisang, o'zing ....",
                "javob": "tusharsan"
            },
            {
                "savol": "Bulbul chamanni sevar, Odam — ....",
                "javob": "Vatanni"
            }]

        maqol_23 = [
            {
                "savol": "Do'st boshga kulfat tushganda ....",
                "javob": "sinaladi"
            },
            {
                "savol": "Laqmaning kallasi, tarozuning ....",
                "javob": "pallasi"
            },
            {
                "savol": "Dangasa odam tongni .... bog'laydi",
                "javob": "tunga"
            },
            {
                "savol": "Ilm o'rgatishdan oldin .... o'rgat",
                "javob": "odob"
            },
            {
                "savol": "Yaxshi .... - oltin tobutdan afzal",
                "javob": "nom"
            }]

        maqol_24 = [
            {
                "savol": "Kulgu — qalbga eng yaxshi ....dir.",
                "javob": "davo"
            },
            {
                "savol": "Hayotning har kuni - bu yangi ....",
                "javob": "sahifa"
            },
            {
                "savol": "Yaxshi so‘z — yaraga .... bo‘ladi.",
                "javob": "malham"
            },
            {
                "savol": "Afting qiyshiq bo'lsa, oynadan ....",
                "javob": "o'pkalama"
            },
            {
                "savol": "Dushmanning kulgani - siringni ....",
                "javob": "bilgani"
            }]

        maqol_25 = [
            {
                "savol": "Ignadek joydan tuyadek .... kiradi.",
                "javob": "sovuq"
            },
            {
                "savol": "Nodon do'stdan, ziyrak dushman ....",
                "javob": "yaxshi"
            },
            {
                "savol": "Kuz — to‘plagan mehnatning ....dir.",
                "javob": "mevasi"
            },
            {
                "savol": "Ehtiromsiz .... - toshga o'xshaydi.",
                "javob": "yurak"
            },
            {
                "savol": "Kengga keng dunyo, torga .... dunyo.",
                "javob": "tor"
            }]

        maqol_26 = [
            {
                "savol": "Har kimniki o'ziga, oy ko'rinar ....",
                "javob": "ko'ziga"
            },
            {
                "savol": "Aqlsiz boylik — egasiz .... kabidir.",
                "javob": "xazina"
            },
            {
                "savol": "Odob — insonning eng go‘zal ....dir.",
                "javob": "libosi"
            },
            {
                "savol": "Trbiyasiz jamiyat - poydevorsiz ....",
                "javob": "imorat"
            },
            {
                "savol": "Ota-onangni rozi qil - .... rozi qil",
                "javob": "volidangni"
            }]

        maqol_27 = [
            {
                "savol": "Yoz — tabiatning eng go‘zal ....dir.",
                "javob": "ziyofati"
            },
            {
                "savol": "Har bir tukilgan barg - .... sabog'i",
                "javob": ""
            },
            {
                "savol": "Farzandning eng katta tayanchi ....?",
                "javob": "otaona"
            },
            {
                "savol": "Farzand uchun eng qimmat tuyg‘u ....",
                "javob": "mehr"
            },
            {
                "savol": "Ezgu niyat - odamni ....dan saqlaydi",
                "javob": "yomonlik"
            }]

        maqol_28 = [
            {
                "savol": "Har bir .... - yangi bilim sari yo'l",
                "javob": "savol"
            },
            {
                "savol": "Aytar so'zni ayt, aytmas so'zdan ....",
                "javob": "qayt"
            },
            {
                "savol": "Do'st achitib gapirar, dushman — ....",
                "javob": "kuldirib"
            },
            {
                "savol": "Eshakning mehnati halol, go'shti ....",
                "javob": "harom"
            },
            {
                "savol": "Ikki kemaga oyoq qo'ygan .... bo'lur.",
                "javob": "g'arq"
            }]

        maqol_29 = [
            {
                "savol": "Mehrsiz oila — ildizsiz .... kabidir.",
                "javob": "daraxt"
            },
            {
                "savol": "Yaxshilikni .... qil, lekin doimo qil",
                "javob": "yashirin"
            },
            {
                "savol": ".... inson - hayotni chuqur anglaydi.",
                "javob": "sabrli"
            },
            {
                "savol": "Dushmaning bo'lishi seni .... qiladi.",
                "javob": "kuchli"
            },
            {
                "savol": "Yoz — .... uchun eng katta barakadir.",
                "javob": "mehnatkash"
            }]

        maqol_30 = [
            {
                "savol": "Yomon nomdan ko'ra, .... ketgan avzal",
                "javob": "izsiz"
            },
            {
                "savol": "Niyat halol bo'lsa, ... yordam beradi",
                "javob": "Alloh"
            },
            {
                "savol": "Vatansiz odam, ildizsiz .... kabidir.",
                "javob": "daraxt"
            },
            {
                "savol": "Bilim egasi - mol dunyo egasidan ....",
                "javob": "boyroq"
            },
            {
                "savol": "Ayolga bergan .... - o'zinga qaytadi.",
                "javob": "hurmat"
            }]

        maqol_31 = [
            {
                "savol": "Boshinga qilich kelsa ham .... so'zla.",
                "javob": "rost"
            },
            {
                "savol": "Dunyoni suv bossa, to'pig'iga ham ....",
                "javob": "chiqmaydi"
            },
            {
                "savol": "Ish ishtaha ochar, dangasa ishdan ....",
                "javob": "qochar"
            },
            {
                "savol": "Minnatli oshdan, beminnat .... yaxshi.",
                "javob": "musht"
            },
            {
                "savol": ".... — insonning eng katta boyligidir.",
                "javob": "aql"
            }]

        maqol_32 = [
            {
                "savol": ".... odam kam gapirib, ko'p tinglaydi.",
                "javob": "aqlli"
            },
            {
                "savol": "Aql — chiroq, idrok esa uning ....dir.",
                "javob": "yorug‘i"
            },
            {
                "savol": "Vaqt — insonning eng qimmatli ....dir.",
                "javob": "ne’mati"
            },
            {
                "savol": "Farzandning baxti — ota-onasining ....",
                "javob": "duosida"
            },
            {
                "savol": ".... ikki qalb o'rtasidagi ko'prikdir.",
                "javob": "ishonch"
            }]

        maqol_33 = [
            {
                "savol": "Baxtning siri — ko‘ngilning ....dadur.",
                "javob": "pokligi"
            },
            {
                "savol": "Sukut ko'p hollarda eng kuchli ....dir",
                "javob": "javob"
            },
            {
                "savol": "Ko‘ngil — insonning eng nozik ....dir.",
                "javob": "joyi"
            },
            {
                "savol": "Dangasaga ish buyursang, senga aql ....",
                "javob": "o'rgatar"
            },
            {
                "savol": "Darding bo'lsa bo'lsin, .... bo'lmasin.",
                "javob": "qarzing"
            }]

        maqol_34 = [
            {
                "savol": "Ishonmagin do'stingga, somon tiqar ....",
                "javob": "po'stingga"
            },
            {
                "savol": "Kambag'alni tuyaning ustida ham it ....",
                "javob": "qopadi"
            },
            {
                "savol": "Mehmon kelar eshikdan, rizqi kelar ....",
                "javob": "teshikdan"
            },
            {
                "savol": "Qancha ter tuksang, shuncha .... olasan",
                "javob": "hosil"
            },
            {
                "savol": ".... odamga davo ham bo'ladi, balo ham.",
                "javob": ""
            }]

        maqol_35 = [
            {
                "savol": "Farzand tarbiyasida eng muhim qadriyat?",
                "javob": "hurmat"
            },
            {
                "savol": "Vaqtni tanigan odam - .... sari yuradi.",
                "javob": "donolik"
            },
            {
                "savol": "Bir lahzaning qadri, uni .... bilinadi.",
                "javob": "yo'qotganda"
            },
            {
                "savol": "Har daqiqa boylikdir, uni .... o'tqazma",
                "javob": "behuda"
            },
            {
                "savol": ".... ajratgan har bir lahza qadirlidir.",
                "javob": "o'qishga"
            }]

        maqol_36 = [
            {
                "savol": ".... olish - dunyoga va oxiratga foyda.",
                "javob": ""
            },
            {
                "savol": ".... tez o'tadi, qadrini bilgan yutadi.",
                "javob": "yoshlik"
            },
            {
                "savol": "Xiyonat — yurakdagi eng chuqur ....dir.",
                "javob": "yaradir"
            },
            {
                "savol": "Birgina yaxshilik yuzlab ....ni yopadi.",
                "javob": "yomonlik"
            },
            {
                "savol": "Farzand bilan davlatning erta-kechi ....",
                "javob": "yo'q"
            }]

        maqol_37 = [
            {
                "savol": "Sabrli bo'lish - o'zingni .... bilishdir",
                "javob": "boshqara"
            },
            {
                "savol": "....ni saqlash qiyin, yo‘qotish esa oson",
                "javob": "obro'"
            },
            {
                "savol": "Baxtni ...., shunda u seni tark etmaydi.",
                "javob": "qadrla"
            },
            {
                "savol": "Boylik vaqtincha, ammo yaxshi nom — ....",
                "javob": "abadiy"
            },
            {
                "savol": "Halol kasb — rizqning eng katta ....dir.",
                "javob": "manbai"
            }]

        maqol_38 = [
            {
                "savol": "Farzand — ota-onaning eng katta ....dir.",
                "javob": "sinovi"
            },
            {
                "savol": "Yolg‘on — ishonchning eng katta ....dir.",
                "javob": "dushmani"
            },
            {
                "savol": "Yaxshi do'st - ...., yomon do'st - sinov",
                "javob": "taqdir"
            },
            {
                "savol": "Yaxshilik — qalbning eng go‘zal ....dir.",
                "javob": "ziynati"
            },
            {
                "savol": "Arpa ekkan arpa o'rar, bug'doy ekkan ....",
                "javob": "bug'doy"
            }]

        maqol_39 = [
            {
                "savol": "Bolaga ishga buyur, orqasidan o'zing ....",
                "javob": "yugur"
            },
            {
                "savol": "Nimani hor qilsang, shunga .... bo'lasan.",
                "javob": "zor"
            },
            {
                "savol": "Taom lazzati tuzida, odam lazzati ....da.",
                "javob": "tili"
            },
            {
                "savol": "Odob bilan aytilgan tanbeh, .... aylanadi",
                "javob": "darsga"
            },
            {
                "savol": ".... yomg‘iri — tabiatning ko‘z yoshidir.",
                "javob": "bahor"
            }]

        maqol_40 = [
            {
                "savol": "Ovqat tanani boqadi, halollik esa ....ni.",
                "javob": "ruh"
            },
            {
                "savol": "Baxtli bo'lmoq uchun .... tozalash kerak.",
                "javob": "qalbni"
            },
            {
                "savol": "Do'st tanlash ...., uni yuqotish xatodir.",
                "javob": "taqdir"
            },
            {
                "savol": "O'rganish - umr bo'yi davom etadigan ....",
                "javob": "yo'l"
            },
            {
                "savol": "Er-xotinning urushi - doka ro'molning ....",
                "javob": "qurishi"
            }]

        maqol_41 = [
            {
                "savol": "Har kimniki o'ziga, .... ko'rinar ko'ziga.",
                "javob": "oy"
            },
            {
                "savol": "Kasalini yashirsang, istimasi .... qiladi.",
                "javob": "oshkor"
            },
            {
                "savol": "Laylakning ketishiga boqma, kelishiga ....",
                "javob": "boq"
            },
            {
                "savol": "Oltin olma, duo ol — duo oltindan ham ....",
                "javob": "afzal"
            },
            {
                "savol": "Ona qizi uchun eng muhim .... hisoblanadi.",
                "javob": "ustoz"
            }]

        maqol_42 = [
            {
                "savol": "Dangasa o'zini, mehnatkash boshqasini ....",
                "javob": "boqadi"
            },
            {
                "savol": "Sabr daraxtining mevasi doim .... bo‘ladi.",
                "javob": "shirin"
            },
            {
                "savol": "Xiyonat — qalbda og'riq beradigan ....dir.",
                "javob": "zahar"
            },
            {
                "savol": ".... - Allohga bo'lgan ishonchning belgisi",
                "javob": "sabr"
            },
            {
                "savol": "Sabr — ilmning ham, iymonning ham ....dir.",
                "javob": "ustuni"
            }]

        maqol_43 = [
            {
                "savol": "Og'ir kunlar sabrni sinaydi, sabr esa ....",
                "javob": "imonni"
            },
            {
                "savol": "Yozda qilingan mehnat, qishda .... beradi.",
                "javob": "rohat"
            },
            {
                "savol": "Rizqni kengaytiradigan kalit — bu ....dir.",
                "javob": "halollik"
            },
            {
                "savol": "Baxtni topish uchun avvalo uni .... kerak.",
                "javob": ""
            },
            {
                "savol": ".... — donishmandning eng katta qurolidir.",
                "javob": "sukut"
            }]

        maqol_44 = [
            {
                "savol": "vaqtni bekorga sarflama - u sening ....dir",
                "javob": "hayoting"
            },
            {
                "savol": "Onaning duosi — oilaning eng katta ....dir.",
                "javob": "qalqoni"
            },
            {
                "savol": "Rizqni oz yoki ko'pligi emas, .... muhimdir",
                "javob": "barakasi"
            },
            {
                "savol": "Baxt — orzularning emas, shukrning ....dir.",
                "javob": "mevasi"
            },
            {
                "savol": "Erkak ayolni qadrlasa, oilasi .... bo‘ladi.",
                "javob": "mustahkam"
            }]

        maqol_45 = [
            {
                "savol": "Ishonch — har qanday munosabatning ....dir.",
                "javob": "ustuni"
            },
            {
                "savol": "O‘rgatgan ustoz, farzandga ikkinchi ....dir",
                "javob": "ota"
            },
            {
                "savol": ".... ko'rsatgan yo'l - eng to'g'ri yo'ldir.",
                "javob": "ustoz"
            },
            {
                "savol": "O'rgatgan bilan bahs qilma - tingla va ....",
                "javob": "angla"
            },
            {
                "savol": "Birovga o'lim tilaguncha, o'zinga .... tila.",
                "javob": "umr"
            }]

        maqol_46 = [
            {
                "savol": "Do'st so'zini tashlama, tashlab boshing ....",
                "javob": "qashlama"
            },
            {
                "savol": "Gul o'ssa - yerning ko'rki, qiz o'ssa — ....",
                "javob": "yurtning"
            },
            {
                "savol": "Halol mehnatning noni, oltindan ham ....dir.",
                "javob": "qimmat"
            },
            {
                "savol": ".... — qorong‘ilikdagi eng yorqin yulduzdir.",
                "javob": "umid"
            },
            {
                "savol": ".... - o'zini sevmagan odamning ko'zgusidir.",
                "javob": "hasad"
            }]

        maqol_47 = [
            {
                "savol": "Bir kun tuz ichgan joyinga qirq kun .... ber.",
                "javob": "salom"
            },
            {
                "savol": "Devor tagida gapirma, devorning ham .... bor.",
                "javob": "qulog'i"
            },
            {
                "savol": "Dushmanga joningni bersang ham, siringni ....",
                "javob": "berma"
            },
            {
                "savol": "Oila — insonning dunyodagi eng katta ....dir.",
                "javob": "qal'asi"
            },
            {
                "savol": "Ilm eshikni ochadi, amal esa uni .... qiladi.",
                "javob": "mustahkam"
            }]

        maqol_48 = [
            {
                "savol": "Elakka chiqqan xotinning ellik og'iz .... bor.",
                "javob": "gapi"
            },
            {
                "savol": "Ming marta eshitgandan, bir marta ko'rgan ....",
                "javob": "yaxshi"
            },
            {
                "savol": "Farzand tarbiyasi - .... emas, umurlik mehnat.",
                "javob": "yillik"
            },
            {
                "savol": "O‘ylamay gapirgan, oxirida o‘ylab .... qiladi.",
                "javob": "pushaymon"
            },
            {
                "savol": "Ota-onaning rozi bo‘lishi — Allohning ....dir.",
                "javob": "roziligi"
            }]

        maqol_49 = [
            {
                "savol": "Har .... bir haqiqatni ochadi - kim kimligini.",
                "javob": "xiyonat"
            },
            {
                "savol": "Rizqni ko‘p qiladigan narsa — ota-onaning ....",
                "javob": "duosi"
            },
            {
                "savol": "Do'st bo'lishdan oldin, .... bo'lishni o'rgan.",
                "javob": "do'st"
            },
            {
                "savol": ".... qilgan odamning yuzida doim nur porlaydi.",
                "javob": "yaxshilik"
            },
            {
                "savol": "O'rgatish - yurakdan yurakka .... o'tqazishdir",
                "javob": "nur"
            }]

        maqol_50 = [
            {
                "savol": "Maqtanganning uyiga bor, kerilganning .... bor.",
                "javob": "to'yi"
            },
            {
                "savol": ".... — baxt eshigini ochadigan yagona kalitdir.",
                "javob": "mehnat"
            },
            {
                "savol": "Til yarasi — qilich yarasidan ham .... bo‘ladi.",
                "javob": "og‘ir"
            },
            {
                "savol": "Janjalni bosadigan eng katta kuch — bu ....dir.",
                "javob": "sukut"
            },
            {
                "savol": "Bahsda g'olib bo'lish - ba'zan .... ayrilishdir",
                "javob": "do'stdan"
            }]

        maqol_51 = [
            {
                "savol": "Savdoda halollik — foydaning eng katta ....dir.",
                "javob": "garovi"
            },
            {
                "savol": "Yolg‘on savdo — qisqa foyda, ammo uzoq ....dir.",
                "javob": "zarar"
            },
            {
                "savol": "Do‘stlik — ikki tanada yashovchi bitta ....dir.",
                "javob": "qalb"
            },
            {
                "savol": "Erkakning kuchi mehnatda, ayolning kuchi ....da",
                "javob": "tarbiya"
            },
            {
                "savol": "Yaxshi insonning soyasi ham odamga .... beradi.",
                "javob": "orom"
            }]

        maqol_52 = [
            {
                "savol": "Arpaning doni bo'lguncha, bug'doyning .... bo'l.",
                "javob": "somoni"
            },
            {
                "savol": "Ish bilganga bir tanga, gap bilganga .... tanga.",
                "javob": "ming"
            },
            {
                "savol": "Joyimiz tor bo'lsa ham, ko'nglimiz .... bo'lsin.",
                "javob": "keng"
            },
            {
                "savol": "Kambag'al don topmaydi, don topsa .... topmaydi.",
                "javob": "idish"
            },
            {
                "savol": "Boylik bezagi — oltin, insonning bezagi esa ....",
                "javob": "odob"
            }]

        maqol_53 = [
            {
                "savol": ".... topishdan avval, .... bo'lishni o'rgan.",
                "javob": "do'st"
            },
            {
                "savol": "Onaning duosi — farzand uchun eng katta ....dir.",
                "javob": "qalqon"
            },
            {
                "savol": "Qish — tabiatning sokin, ammo eng og‘ir ....dir.",
                "javob": "sinovi"
            },
            {
                "savol": "Til — insonning o‘zini oshkor qiladigan ....dir.",
                "javob": "oyna"
            },
            {
                "savol": "Kasb — ota merosi emas, har kimning o‘z ....dir.",
                "javob": "mehnati"
            }]

        maqol_54 = [
            {
                "savol": "Do‘stni boylikda emas, qiyinchilikda .... kerak.",
                "javob": "sinash"
            },
            {
                "savol": "Ayol erining soyasi, erkak esa ayolning ....dir.",
                "javob": "tayanchi"
            },
            {
                "savol": "Yoshlikda olingan bilim, .... o'yilgan naqshdir.",
                "javob": "toshga"
            },
            {
                "savol": "Yaxshilik qilgan qo‘l hech qachon .... qolmaydi.",
                "javob": "bo‘sh"
            },
            {
                "savol": ".... qilgan odam, oxirida o‘ziga ham .... qiladi.",
                "javob": "xiyonat"
            }]

        maqol_55 = [
            {
                "savol": "Yaxshi taqdir — sovg‘a, yomon taqdir esa ....dir.",
                "javob": "saboq"
            },
            {
                "savol": "Yaxshi niyatli odamning yo‘li doimo .... bo‘ladi.",
                "javob": "ochiq"
            },
            {
                "savol": "Haddan oshgan ...., oxirida ko‘z yoshga aylanadi.",
                "javob": "kulgu"
            },
            {
                "savol": "Farzand tarbiyasi — millatning eng katta ....dir.",
                "javob": "kelajagi"
            },
            {
                "savol": ".... — qadrini faqat undan uzoqlashganda bilasan.",
                "javob": "vatan"
            }]

        maqol_56 = [
            {
                "savol": "Ishonchni tiklash, uni yo‘qotishdan ko'ra ....dir",
                "javob": "qiyin"
            },
            {
                "savol": "Yaxshilik qilgan odam oxirida faqat .... yig‘adi.",
                "javob": "baxtdan"
            },
            {
                "savol": "Ignachining ming urgani, temirchining .... urgani.",
                "javob": "bir"
            },
            {
                "savol": "Oila — jamiyatning eng kichik, ammo eng buyuk ....",
                "javob": "maktabi"
            },
            {
                "savol": ".... bilan yengilmas dushmanni ham yengish mumkin.",
                "javob": "aql"
            }]

        maqol_57 = [
            {
                "savol": "Farzand tarbiyasi — ota-onaning eng buyuk ....dir.",
                "javob": "merosi"
            },
            {
                "savol": "Og‘ir kunning yorug‘i hamisha .... ortidan keladi.",
                "javob": "sabr"
            },
            {
                "savol": ".... — baxt eshigini ochadigan eng katta kalitdir.",
                "javob": "sabr"
            },
            {
                "savol": "Sabr — Allohning bandaga bergan eng buyuk ....dir.",
                "javob": "sovg‘asi"
            },
            {
                "savol": "Obro‘ — pul bilan emas, faqat .... bilan topiladi.",
                "javob": "amal"
            }]

        maqol_58 = [
            {
                "savol": "Halol rizq oz bo‘lsa ham, uning .... ko‘p bo‘ladi.",
                "javob": "barakasi"
            },
            {
                "savol": "Rizqsiz odam yo‘q, ammo har bir rizqning .... bor.",
                "javob": "hisobi"
            },
            {
                "savol": "Erkak — oilaning suyanchi, ayol esa uning ....dir.",
                "javob": "qalbi"
            },
            {
                "savol": "Har xiyonat - bir saboq, har ishonch - bir ....dir",
                "javob": "sinov"
            },
            {
                "savol": "Dangasaning ishi bitmas, yoz kelsa ham .... bitmas.",
                "javob": "qishi"
            }]

        maqol_59 = [
            {
                "savol": "Oilada hurmat yuq bo'lsa, .... ham uzoq yashamaydi.",
                "javob": "muhabbat"
            },
            {
                "savol": "Kuzda yig‘ilmagan ...., qishda qashshoqlik bo‘ladi.",
                "javob": "hosil"
            },
            {
                "savol": "Rizqning lazzati — halollikda, barakasi esa ....da.",
                "javob": "shukr"
            },
            {
                "savol": "Boylik qo‘ldan ketadi, baxt esa qalbda .... qoladi.",
                "javob": "abadiy"
            },
            {
                "savol": "Hurmat - qalblarni birlashtiradi, ... esa ajratadi.",
                "javob": "kibr"
            }]

        maqol_60 = [
            {
                "savol": "Ilmsiz kuch — ko‘r odamning qo‘lidagi .... kabidir.",
                "javob": "qurol"
            },
            {
                "savol": "Ayolning ko‘z yoshlari — erkakning haqiqiy ....dir.",
                "javob": "imtihoni"
            },
            {
                "savol": "Xiyonat — muhabbatni o‘ldiradi, do‘stlikni esa ....",
                "javob": "parchalaydi"
            },
            {
                "savol": "Xiyonat qilgan qalb hech qachon chin .... topmaydi.",
                "javob": "baxt"
            },
            {
                "savol": "Dangasaga ish buyursang, otangdan ortiq .... qiladi.",
                "javob": "nasihat"
            }]

        maqol_61 = [
            {
                "savol": "Ishonch — qalbni birlashtiradigan eng katta ....dir.",
                "javob": "ko‘prik"
            },
            {
                "savol": "Janjalning ildizi — jahlda, mevasi esa .... bo‘ladi.",
                "javob": "pushaymon"
            },
            {
                "savol": "Janjal chiqsa, eshikdan birinchi .... chiqib ketadi.",
                "javob": "aql"
            },
            {
                "savol": "Ko‘ngilni ko‘targan odam, aslida qalbni .... qiladi.",
                "javob": "nurli"
            },
            {
                "savol": "Pul cho'ntakda bo'lsa xizmatkor, yurakda bo'lsa ....",
                "javob": "xoin"
            }]

        maqol_62 = [
            {
                "savol": "Do‘st seni ko‘taradi, dushman esa seni .... istaydi.",
                "javob": "yiqitishni"
            },
            {
                "savol": ".... yillar davomida quriladi, bir lahzada buziladi.",
                "javob": "ishonch"
            },
            {
                "savol": "Yomonlik urug'i tez unadi, lekin mevasi .... bo'ladi",
                "javob": "achchiq"
            },
            {
                "savol": "Yaxshilikning ildizi — halollik, mevasi esa ....dir.",
                "javob": "baxt"
            },
            {
                "savol": "Arqog'ini ko'rib bo'zini ol, ....ni ko'rib qizini ol.",
                "javob": "onasini"
            }]

        maqol_63 = [
            {
                "savol": "Dehqon bo'lsang shudgor qil, mulla bo'lsang .... qil.",
                "javob": "takror"
            },
            {
                "savol": "Har yerni qilma orzu, har yerda ham bordir toshu ....",
                "javob": "torozu"
            },
            {
                "savol": "Idroksiz inson — ko‘zi ochiq, ammo .... ko‘r odamdir.",
                "javob": "qalban"
            },
            {
                "savol": "Vaqtni behuda ketqazma, u hayotdan qirqilgan bir ....",
                "javob": "bo'lakdir"
            },
            {
                "savol": "Tarbiya — oltin emas, ammo undan qimmatliroq ....dir.",
                "javob": "boylik"
            }]

        maqol_64 = [
            {
                "savol": "Shukr qilingan rizq oz bo‘lsa ham, .... ko‘p bo‘ladi.",
                "javob": "barakasi"
            },
            {
                "savol": "Sabr daraxti achchiq, ammo uning mevasi .... bo‘ladi.",
                "javob": "shirin"
            },
            {
                "savol": "Ovqatni shirin qiladigan narsa — .... va halollikdir.",
                "javob": "mehnat"
            },
            {
                "savol": "Ko‘ngilni og‘ritish oson, lekin uni tuzatish ....dir.",
                "javob": "qiyin"
            },
            {
                "savol": "Erkakning sharafi — halollikda, ayolning sharafi ....",
                "javob": "iffatda"
            }]

        maqol_65 = [
            {
                "savol": "Do'stim deb siringni aytma, do'stingning ham .... bor.",
                "javob": "do'sti"
            },
            {
                "savol": "Mehnat — insonning qo‘lida qurol, qalbida esa ....dir.",
                "javob": "umid"
            },
            {
                "savol": "Haqiqat — quyosh kabi, uni hech qachon .... bo‘lmaydi.",
                "javob": "yopib"
            },
            {
                "savol": "Yoshlikdagi dangasalik, qarilikdagi eng og‘ir ....dir.",
                "javob": "pushaymon"
            },
            {
                "savol": "Hayot — nafas olishda emas, balki  bilan yashashdadur.",
                "javob": "maqsad"
            }]

        maqol_66 = [
            {
                "savol": "Kimki o‘z aqliga tayanmasa, boshqalarning .... bo‘ladi.",
                "javob": "quli"
            },
            {
                "savol": "Kimki boshqaga ilm o‘rgatsa, uning savobi .... bo‘ladi.",
                "javob": "abadiy"
            },
            {
                "savol": "Onaning ko‘z yoshlari — farzand uchun eng katta ....dir.",
                "javob": "la’nat"
            },
            {
                "savol": "Ota gapidan - yo'l topiladi, ona .... - baraka topiladi.",
                "javob": "duosidan"
            },
            {
                "savol": "Xiyonat — dushmanlikdan ham xavfli, chunki u ichdan ....",
                "javob": "yemiradi"
            }]

        maqol_67 = [
            {
                "savol": "Sabr bilan to‘kilgan ko‘z yosh, oxirida ....ga aylanadi.",
                "javob": "quvonch"
            },
            {
                "savol": "Hasad qilgan odam, o‘zgani emas, avvalo o‘zini ....laydi",
                "javob": "azob"
            },
            {
                "savol": "Ovqatning lazzati — tuzda, hayotning lazzati esa ....da.",
                "javob": "shukr"
            },
            {
                "savol": ".... har doim yoningda, faqat uni ko'ra bilishing kerak.",
                "javob": "baxt"
            },
            {
                "savol": "Janjal — kichik uchqundan chiqib, katta ....ga aylanadi.",
                "javob": "olov"
            }]

        maqol_68 = [
            {
                "savol": "Boylik ko‘paygan sayin, insonning .... ham ko'p bo‘ladi.",
                "javob": "sinovi"
            },
            {
                "savol": "Kim ilmni amal qilmasa, u faqat yuk ortgan .... kabidir.",
                "javob": "eshak"
            },
            {
                "savol": "Hayot seni sinaydi, ammo sinov ortida doim bir .... bor.",
                "javob": "hikmat"
            },
            {
                "savol": "O‘rgatish — yodlatish emas, balki qalbga .... solishdir.",
                "javob": "nur"
            },
            {
                "savol": "Taqdirni qabul qilmagan odam doimiy .... ichida yashaydi.",
                "javob": "azob"
            }]

        maqol_69 = [
            {
                "savol": "Yoshlik — daraxtning gullashi, qarilik esa uning ....dir.",
                "javob": "mevasi"
            },
            {
                "savol": "Ishonchni mustahkam qiladigan narsa — halollik va ....dir.",
                "javob": "rostgo'ylik"
            },
            {
                "savol": "Hurmat — qalblarni birlashtiradigan eng mustahkam ....dir.",
                "javob": "ip"
            },
            {
                "savol": "Yoshlik .... bilan, qarilik ularni tushunish bilan o'tadi.",
                "javob": "xatolar"
            },
            {
                "savol": "Chin muhabbat - ishonch bilan yashaydi, .... bilan o'ladi.",
                "javob": "shubha"
            }]

        maqol_70 = [
            {
                "savol": "Boylik tugaydi, kuch susayadi, ammo yaxshi nom .... qoladi.",
                "javob": "abadiy"
            },
            {
                "savol": "Halol ovqat — tan uchun oziq, harom ovqat .... uchun zahar.",
                "javob": "qalb"
            },
            {
                "savol": "Oilada muhabbat bo‘lsa, qashshoqlik ham .... kabi ko‘rinadi.",
                "javob": "boylik"
            },
            {
                "savol": "Ota-onasiga xizmat qilmagan farzand, kun kelib .... bo‘ladi.",
                "javob": "xor"
            },
            {
                "savol": "Ko‘ngil — oynaga o‘xshaydi, bir sinib qolsa, .... bo‘lmaydi.",
                "javob": "butun"
            }]

        maqol_71 = [
            {
                "savol": "Yoshlikda o‘rganmagan ilm, qarilikda eng og‘ir .... bo‘ladi.",
                "javob": "hasrat"
            },
            {
                "savol": "Ota-onasini e’zozlagan farzand, ertaga o‘zi ham .... ko‘radi.",
                "javob": "ehtirom"
            },
            {
                "savol": "Hasad — yomonlikning urug‘i, uning mevasi doimo .... bo‘ladi.",
                "javob": "achchiq"
            },
            {
                "savol": "Rizq — Allohning in’omi, uni kengaytiradigan narsa — ....dir.",
                "javob": "shukr"
            },
            {
                "savol": "Baxtli odam — boriga shukur qilsa, baxtsiz odam .... izlaydi.",
                "javob": "kamchilik"
            }]

        maqol_72 = [
            {
                "savol": ".... saqlagan odam, hech qachon so‘zidan pushaymon bo‘lmaydi.",
                "javob": "sukut"
            },
            {
                "savol": "Boylikning haqiqati — halollikda, yolg‘on boylik esa ....dir.",
                "javob": "baloga"
            },
            {
                "savol": "Ilm — insonning eng katta boyligi, uni hech kim .... olmaydi.",
                "javob": "o‘g‘irlay"
            },
            {
                "savol": "Katta arava qayoqdan yursa, kichik arava ham o'sha yoqdan ....",
                "javob": "yuradi"
            },
            {
                "savol": "Bolaga bergan tarbiya — dunyoga qoldirilgan eng katta ....dir.",
                "javob": "xotira"
            }]

        maqol_73 = [
            {
                "savol": "Rizq — odamni boqadi, ammo uni topish uchun .... qilish kerak.",
                "javob": "mehnat"
            },
            {
                "savol": "Har bir ishning o'z vaqti bor, erta qilinsa xato, kechiksa ....",
                "javob": "zarar"
            },
            {
                "savol": "Do‘stlikning ildizi — ishonch, dushmanlikning ildizi — ....dir.",
                "javob": "hasad"
            },
            {
                "savol": "Do‘stlikning ildizi — ishonch, muhabbatning ildizi esa ....dir.",
                "javob": "sadoqat"
            },
            {
                "savol": "Xiyonatning izlari — ko‘rinmaydi, ammo qalbdagi .... yo'qolmaydi.",
                "javob": "og‘riq"
            }]

        maqol_74 = [
            {
                "savol": "Yoshlik — imkoniyat davri, qarilik esa qilgan ishlarning ....dir.",
                "javob": "hisobi"
            },
            {
                "savol": ".... — yoshlikning soyasi, yoshlikning qadri esa ....da bilinadi.",
                "javob": "qarilik"
            },
            {
                "savol": "Hayot — manzilgacha bo'lgan notekis yo'l, asl manzil esa ....dir.",
                "javob": "oxirat"
            },
            {
                "savol": "Farzandiga otaning mehri ketmoncha bo'lsa, onaning mehri .... bor.",
                "javob": "osmoncha"
            },
            {
                "savol": "Xatolar — hayotning yozuvi, tajriba esa uning eng to‘g‘ri ....dir.",
                "javob": "izohi"
            }]

        maqol_75 = [
            {
                "savol": "Tajriba — o‘qituvchi, ammo uning kitobi faqat .... bilan yoziladi.",
                "javob": "umr"
            },
            {
                "savol": "Chin do‘st — ko‘zingdagi quvonchni emas, yuragingdagi .... sezadi.",
                "javob": "og‘riqni"
            },
            {
                "savol": "Haqiqiy o‘rgatish — til bilan emas, eng avvalo .... bilan bo‘ladi.",
                "javob": "amal"
            },
            {
                "savol": "Birovni ustidan .... zinhor, sening ham ustingdan kuladiganlar bor.",
                "javob": "kulmagin"
            },
            {
                "savol": "Baxtli bo‘lish — boshqalarga .... ulashishni ham o‘z ichiga qiladi.",
                "javob": "baxt"
            }]

        maqol_76 = [
            {
                "savol": ".... — yozilgan kitob, ammo uni qanday o‘qish insonning o'z qo‘lida.",
                "javob": "taqdir"
            },
            {
                "savol": "Tajriba — eng qimmat ustoz, lekin uning darslari odatda .... bo‘ladi.",
                "javob": "og‘riqli"
            },
            {
                "savol": "Ishonch — suvga o‘xshaydi, agar to‘kilib ketsa, uni qayta .... qiyin.",
                "javob": "yig‘ish"
            },
            {
                "savol": "Baxt — ko‘p narsaga ega bo‘lishda emas, bor narsaga .... qilishdadir.",
                "javob": "shukr"
            },
            {
                "savol": ".... — insonni ulug‘ qilmaydi, balki uning asl qiyofasini ko‘rsatadi.",
                "javob": "boylik"
            }]

        maqol_77 = [
            {
                "savol": "Yaxshi gap bilan .... inidan chiqarar, yomon gap bilan qilich qinidan",
                "javob": "ilon"
            },
            {
                "savol": "Yoshlik — kuch-quvvat, qarilik esa hayotdan olingan eng katta ....dir.",
                "javob": "hikmat"
            },
            {
                "savol": "Kim mehnatning achchiq terini to‘ksa, oxirida uning .... shirin bo‘ladi.",
                "javob": "mevasi"
            },
            {
                "savol": "Boylikni oshiradigan narsa — halollik, kamaytiradigan narsa esa ....dir.",
                "javob": "isrof"
            },
            {
                "savol": "Ko‘p bilgan emas, bilganini to‘g‘ri ishlata olgan odam .... hisoblanadi.",
                "javob": "dono"
            }]

        maqol_78 = [
            {
                "savol": "Hayot yo‘li tekis emas, ammo sabr qilgan odam har qanday ....ni yengadi.",
                "javob": "to‘siq"
            },
            {
                "savol": "Oila mustahkamligi — uy devorida emas, qalblardagi .... bilan o‘lchanadi.",
                "javob": "mehr"
            },
            {
                "savol": "Har bir lahza — inson qo‘lidan chiqib ketayotgan ....ning bir bo'lagidir.",
                "javob": "umur"
            },
            {
                "savol": "Sadoqatni asragan qalb — yuksaladi, xiyonat qilgan qalb esa .... bo‘ladi.",
                "javob": "halok"
            },
            {
                "savol": "Erkak sabr qilsa — oilani asraydi, ayol sabr qilsa — butun ....ni asraydi.",
                "javob": "nasl"
            }]

        maqol_79 = [
            {
                "savol": "Ota-ona duosidan mahrum bo‘lgan farzand, hayotda hech qachon .... topmaydi.",
                "javob": "baraka"
            },
            {
                "savol": "Taqdir — qalbni sinaydi, ammo uni sabr bilan qabul qilgan odam .... topadi.",
                "javob": "baxt"
            },
            {
                "savol": "Dushmaning qilgan zarbasidan ko‘ra, do‘stning xiyonati ko‘proq .... beradi.",
                "javob": "og‘riq"
            },
            {
                "savol": "Tajriba — insonning boyligi, uni hech qachon .... bilan sotib olib bo‘lmaydi.",
                "javob": "pul"
            },
            {
                "savol": "Mehnatsiz yashashni istagan inson — hayotning eng achchiq .... kutgan insondir.",
                "javob": "yolg'onini"
            }]

        maqol_80 = [
            {
                "savol": "Mehnatkash odamning qo‘li charchaydi, ammo uning qalbi hech qachon .... sezmaydi",
                "javob": "charchoq"
            },
            {
                "savol": "Dangasa odam orzular haqida gapiradi, mehnatkash odam esa ularni .... chiqaradi.",
                "javob": "ro‘yobga"
            },
            {
                "savol": "Qarilik — yoshlikning oynasi, yoshlik qanday o‘tsa, qarilik shunday .... beradi.",
                "javob": "javob"
            },
            {
                "savol": "Yo‘qotilgan boylik qaytadi, yo‘qotilgan sog‘liq tiklanadi, ammo yo‘qotilgan .... qaytmaydi.",
                "javob": "vaqt"
            },
            {
                "savol": ".... — insonning eng sodiq hamrohi, ammo uni qadrlamagan odamning eng katta dushmani bo‘ladi.",
                "javob": "vaqt"
            }]

        maqol_81 = [
            {
                "savol": "Yaxshi niyatga yo'lning o'zi ham ....",
                "javob": "ochiladi"
            },
            {
                "savol": "O'ylab qilingan ish — yarmi .... ishdir.",
                "javob": "bajarilgan"
            },
            {
                "savol": "Tilni tiygan — dushmanni ....",
                "javob": "uyaltirar"
            },
            {
                "savol": "Oqibatli ishning mevasi — ....",
                "javob": "baraka"
            },
            {
                "savol": "Donishmand so'zni yuzga chizmaydi, .... chizadi.",
                "javob": "qalbga"
            }]

        maqol_82 = [
            {
                "savol": "...ni qadrlagan — hayotni qadrlaydi.",
                "javob": "vaqt"
            },
            {
                "savol": "Quyosh botar, ammo .... botmaydi.",
                "javob": "umid"
            },
            {
                "savol": "Tajribasiz jasorat — ....ga eltadi",
                "javob": "xato"
            },
            {
                "savol": ".... terning hidi — eng shirin hid",
                "javob": "halol"
            },
            {
                "savol": "Aql toshga balo erur, g‘azab ....",
                "javob": "boshga"
            }]
                 
        maqol_83 = [
            {
                "savol": "....dan chiqgan so'z, yurakka yetib borar.",
                "javob": "yurak"
            },
            {
                "savol": "Kichik qadamlar katta ....ga yetaklar",
                "javob": "yo‘l"
            },
            {
                "savol": "Bir kelgan .... — ikki bor eshik qoqmaydi.",
                "javob": "imkon"
            },
            {
                "savol": "Taqdir eshikni yopsa, duo ....ni ochur",
                "javob": "deraza"
            },
            {
                "savol": "Barakani ochadigan kalit — ....",
                "javob": "shukr"
            }]

        maqol_84 = [
            {
                "savol": "Mehnat yo‘l, ilm — ....",
                "javob": "chiroq"
            },
            {
                "savol": "Ustoz ko‘rsatgan yo‘l — ....ga aylanar.",
                "javob": "yo‘ldosh"
            },
            {
                "savol": "Boshlanmagan ish — eng katta ....",
                "javob": "to‘siq"
            },
            {
                "savol": "Oqil hato qilgach, undan ....",
                "javob": "saboq oladi"
            },
            {
                "savol": "Mehr bilan berilgan .... — ikki karra to‘yimli.",
                "javob": "luqma"
            }]

        maqol_85 = [
            {
                "savol": ".... insonni pastga qulatadi.",
                "javob": "kibr"
            },
            {
                "savol": "Yaxshi so‘z — eshik, yomon so‘z — ....",
                "javob": "devor"
            },
            {
                "savol": "Do‘stlikni saqlaydigan qo‘riqchi — ....",
                "javob": "ishonch"
            },
            {
                "savol": "Bir urug‘ — o‘n .... beradi",
                "javob": "meva"
            },
            {
                "savol": "Sabr — ko‘rinmasa ham, ammo ....",
                "javob": "seziladi"
            }]

        maqol_86 = [
            {
                "savol": ".... — buyuklikning ildizi.",
                "javob": "kamtarlik"
            },
            {
                "savol": "Yaxshi .... — ertaning eng yaxshi sarmoyasi.",
                "javob": "niyat"
            },
            {
                "savol": "....ni boshqara olmaysan, lekin u seni boshqaradi.",
                "javob": "vaqt"
            },
            {
                "savol": "Shoshma-shoshma, tez yurib ....",
                "javob": "adashma"
            },
            {
                "savol": ".... oynasini tirnagan — ko‘z yoshidir.",
                "javob": "ko‘ngil"
            }]

        maqol_87 = [
            {
                "savol": "Oq yo‘lda iz qoldirgan — .... qoldirgan",
                "javob": "nom"
            },
            {
                "savol": ".... niyat — qanotsiz qush.",
                "javob": "rejasiz"
            },
            {
                "savol": "Kunduzda qilingan .... — kechada yoritadi.",
                "javob": "ezgulik"
            },
            {
                "savol": "Donolik savoldan boshlanadi, jaholat — .... qilishdan.",
                "javob": "xulosa"
            },
            {
                "savol": "Sinov kelmasa, sabr ham .... bo'lar.",
                "javob": "uyquda"
            }]

        maqol_88 = [
            {
                "savol": "Birovning yutug‘idan hasad — ....ni qisqartiradi.",
                "javob": "umr"
            },
            {
                "savol": "pok .... — kir ishni ham tozalaydi.",
                "javob": "niyat"
            },
            {
                "savol": "Qalbdagi bog‘ni sug‘oradigan suv — ....",
                "javob": "mehr"
            },
            {
                "savol": "Hikmat — baland ovoz emas, chuqur ....",
                "javob": "tinchlik"
            },
            {
                "savol": "Ko‘p narsani bilgan dono emas, bilganini .... qilgan odam dono.",
                "javob": "amal"
            }]

        maqol_89 = [
            {
                "savol": "G‘iybat — o‘z qalbingdagi ....",
                "javob": "chang"
            },
            {
                "savol": ".... uyg'ongan joydan yo‘l boshlanadi.",
                "javob": "umid"
            },
            {
                "savol": "Sening narxing — so‘zlaringda emas, ....da",
                "javob": "ishlaring"
            },
            {
                "savol": "Bo‘sh .... baland jaranglaydi.",
                "javob": "idish"
            },
            {
                "savol": "Rizqning eni — mehnatda, bo‘yi — ....da",
                "javob": "shukr"
            }]

        maqol_90 = [
            {
                "savol": "Og‘ir so‘zni yut — yengil .... toparsan.",
                "javob": "uyqu"
            },
            {
                "savol": "Haq yo‘lidagi qo‘rquv — soya, irodang — ....",
                "javob": "quyosh"
            },
            {
                "savol": "Imkonni kutgan — o‘tdi, uni yaratgan — ....",
                "javob": "yutdi"
            },
            {
                "savol": "Yaxshi fikr — mehmon, uni uyda tutib turuvchi — ....",
                "javob": "amal"
            },
            {
                "savol": "Yomon odatni yengish — yovni yengishdan ....",
                "javob": "qiyin"
            }]

        maqol_91 = [
            {
                "savol": "Ko‘ngilga yo‘l — quloqdan, aqilga — ....dan.",
                "javob": "sukut"
            },
            {
                "savol": "Maqsad ko‘r bo‘lsa, mehnat — ....",
                "javob": "charchoq"
            },
            {
                "savol": "Chiroq moysiz yonmas, do‘stlik — ....siz.",
                "javob": "ishonch"
            },
            {
                "savol": "Tiling qisqa bo‘lsin, ....ing — uzun.",
                "javob": "qo‘l"
            },
            {
                "savol": "Ezgulik ko‘chatini ertalab ek — kechga .... bo‘ladi.",
                "javob": "soya"
            }]

        maqol_92 = [
            {
                "savol": "O‘zingni yenggan — ming .... yengar",
                "javob": "yovni"
            },
            {
                "savol": "O‘tmishdan saboq ol — ammo unga ....",
                "javob": "ko‘chma"
            },
            {
                "savol": "Qadrini bilmagan — oltinni ham .... bilar",
                "javob": "tosh"
            },
            {
                "savol": "Yaxshi soat — ishni, yomon soat — ....ni ko‘paytirar",
                "javob": "bahona"
            },
            {
                "savol": "....dagi qulfni kalit emas, shirin so'z ochadi.",
                "javob": "qalb"
            }]

        maqol_93 = [
            {
                "savol": "Ishonch — ko‘prik, yolg‘on — ....",
                "javob": "chuqurlik"
            },
            {
                "savol": "Bir qarich adolat — yuz ....ga teng",
                "javob": "nasihat"
            },
            {
                "savol": "Ko‘ngilni sindirish — .... buzishdan og‘ir",
                "javob": "uy"
            },
            {
                "savol": "Kechagi xato — bugungi ....",
                "javob": "ustoz"
            },
            {
                "savol": "Oqil do‘st, bu senga ....dir",
                "javob": "oyna"
            }]

        maqol_94 = [
            {
                "savol": "Odam kiyimdan emas, ....dan bezak topar",
                "javob": "odob"
            },
            {
                "savol": "Qadamni sekin ol — .... tinchiydi",
                "javob": "chang"
            },
            {
                "savol": "Hayot sahifasini qalaming bilan emas, .... bilan yoz",
                "javob": "amal"
            },
            {
                "savol": "Mehnat qo‘li qattiq — ammo .... yumshoq",
                "javob": "noni"
            },
            {
                "savol": "Bahona qidirgan — .... yo‘qotar.",
                "javob": "yo‘l"
            }]

        maqol_95 = [
            {
                "savol": "Gurung ko‘p joyda .... bo‘g‘iladi.",
                "javob": "haqiqat"
            },
            {
                "savol": "Yaxshi fikr — mehmon, uni ushlab qoluvchi — ....",
                "javob": "intizom"
            },
            {
                "savol": "Sabr — kalit, duo — ....",
                "javob": "eshik"
            },
            {
                "savol": "Manzil yaqin bo‘lsa ham, .... uzoq bo‘lsa yetib bormaysan",
                "javob": "niyat"
            },
            {
                "savol": ".... kosadan ichilgan suv — saroy choyidan totli",
                "javob": "kamtar"
            }]

        maqol_96 = [
            {
                "savol": "Qalb daryo bo‘lsa, til — ....",
                "javob": "ariq"
            },
            {
                "savol": "Vaqt yo‘lovchi emas, u — ....",
                "javob": "poyezd"
            },
            {
                "savol": "Uyalish — pardadir, vijdon — ....",
                "javob": "bino"
            },
            {
                "savol": "Yaxshi qo‘shni — devordan balandroq ....",
                "javob": "qo‘riq"
            },
            {
                "savol": "To‘g‘ri chiziq — eng qisqa yo‘l, halol so‘z — eng qisqa ....",
                "javob": "isbot"
            }]

        maqol_97 = [
            {
                "savol": "Ilmning dushmani — manmanlik bo'lsa, do‘sti — ....",
                "javob": "savol"
            },
            {
                "savol": "Orttirilgan jin do‘st — topilgan ....",
                "javob": "xazinadir"
            },
            {
                "savol": "Yaxshi fikr — bahor shamoli, yomon fikr — .... bo‘roni.",
                "javob": "qor"
            },
            {
                "savol": "So‘zning shifosi bor, ammo u ham .... aytilsa.",
                "javob": "vaqtida"
            },
            {
                "savol": "Haqiqat kechiksa ham, oxirida ....",
                "javob": "yutadi"
            }]

        maqol_98 = [
            {
                "savol": "Qalbdagi qorong‘ulikni yoritadigan chiroq — ....",
                "javob": "ilm"
            },
            {
                "savol": "Bir don urug‘dan butun bir .... boshlanadi",
                "javob": "bog‘"
            },
            {
                "savol": "Do‘st yuzida tabassum, dushman yuzida .... bo‘ladi",
                "javob": "maska"
            },
            {
                "savol": "Sabrli yurak — tog‘dan ham ....",
                "javob": "mustahkam"
            },
            {
                "savol": ".... bilan aytilgan so‘z — muzlagan qalbni ham eritadi.",
                "javob": "mehr"
            }]

        maqol_99 = [
            {
                "savol": "....ni qanot qilmagan odam — ucholmaydi.",
                "javob": "orzu"
            },
            {
                "savol": "To‘g‘rilik — odam uchun eng katta ....",
                "javob": "zirh"
            },
            {
                "savol": "Ko‘z yoshini yashirish mumkin, ammo qalbdagi ....ni yashirib bo‘lmaydi",
                "javob": "og‘riq"
            },
            {
                "savol": "Tilni tiyish — oltindan ham qimmatli ....",
                "javob": "fazilat"
            },
            {
                "savol": "Insonning buyukligi boylikda emas, balki ....",
                "javob": "odobida"
            }]

        maqol_100 = [
            {
                "savol": "Adolatli hukm — mingta ....dan kuchli",
                "javob": "qurol"
            },
            {
                "savol": "Hayotning eng katta sabog‘i — ....ni qadrlash",
                "javob": "vaqt"
            },
            {
                "savol": "....ni yo‘qotgan — qo‘lida qurol bo‘lsa ham yengiladi.",
                "javob": "umid"
            },
            {
                "savol": "Odamning haqiqiy boyligi — qalbida saqlangan ....",
                "javob": "nur"
            },
            {
                "savol": "Donolik — so‘zning uzunligida emas, ....",
                "javob": "ma’nosida"
            }
        ]


        lvl_1 = random.choice(maqol_1)
        lvl_2 = random.choice(maqol_2)
        lvl_3 = random.choice(maqol_3)
        lvl_4 = random.choice(maqol_4)
        lvl_5 = random.choice(maqol_5)
        lvl_6 = random.choice(maqol_6)
        lvl_7 = random.choice(maqol_7)
        lvl_8 = random.choice(maqol_8)
        lvl_9 = random.choice(maqol_9)
        lvl_10 = random.choice(maqol_10)
        lvl_11 = random.choice(maqol_11)
        lvl_12 = random.choice(maqol_12)
        lvl_13 = random.choice(maqol_13)
        lvl_14 = random.choice(maqol_14)
        lvl_15 = random.choice(maqol_15)
        lvl_16 = random.choice(maqol_16)
        lvl_17 = random.choice(maqol_17)
        lvl_18 = random.choice(maqol_18)
        lvl_19 = random.choice(maqol_19)
        lvl_20 = random.choice(maqol_20)
        lvl_21 = random.choice(maqol_21)
        lvl_22 = random.choice(maqol_22)
        lvl_23 = random.choice(maqol_23)
        lvl_24 = random.choice(maqol_24)
        lvl_25 = random.choice(maqol_25)
        lvl_26 = random.choice(maqol_26)
        lvl_27 = random.choice(maqol_27)
        lvl_28 = random.choice(maqol_28)
        lvl_29 = random.choice(maqol_29)
        lvl_30 = random.choice(maqol_30)
        lvl_31 = random.choice(maqol_31)
        lvl_32 = random.choice(maqol_32)
        lvl_33 = random.choice(maqol_33)
        lvl_34 = random.choice(maqol_34)
        lvl_35 = random.choice(maqol_35)
        lvl_36 = random.choice(maqol_36)
        lvl_37 = random.choice(maqol_37)
        lvl_38 = random.choice(maqol_38)
        lvl_39 = random.choice(maqol_39)
        lvl_40 = random.choice(maqol_40)
        lvl_41 = random.choice(maqol_41)
        lvl_42 = random.choice(maqol_42)
        lvl_43 = random.choice(maqol_43)
        lvl_44 = random.choice(maqol_44)
        lvl_45 = random.choice(maqol_45)
        lvl_46 = random.choice(maqol_46)
        lvl_47 = random.choice(maqol_47)
        lvl_48 = random.choice(maqol_48)
        lvl_49 = random.choice(maqol_49)
        lvl_50 = random.choice(maqol_50)
        lvl_51 = random.choice(maqol_51)
        lvl_52 = random.choice(maqol_52)
        lvl_53 = random.choice(maqol_53)
        lvl_54 = random.choice(maqol_54)
        lvl_55 = random.choice(maqol_55)
        lvl_56 = random.choice(maqol_56)
        lvl_57 = random.choice(maqol_57)
        lvl_58 = random.choice(maqol_58)
        lvl_59 = random.choice(maqol_59)
        lvl_60 = random.choice(maqol_60)
        lvl_61 = random.choice(maqol_61)
        lvl_62 = random.choice(maqol_62)
        lvl_63 = random.choice(maqol_63)
        lvl_64 = random.choice(maqol_64)
        lvl_65 = random.choice(maqol_65)
        lvl_66 = random.choice(maqol_66)
        lvl_67 = random.choice(maqol_67)
        lvl_68 = random.choice(maqol_68)
        lvl_69 = random.choice(maqol_69)
        lvl_70 = random.choice(maqol_70)
        lvl_71 = random.choice(maqol_71)
        lvl_72 = random.choice(maqol_72)
        lvl_73 = random.choice(maqol_73)
        lvl_74 = random.choice(maqol_74)
        lvl_75 = random.choice(maqol_75)
        lvl_76 = random.choice(maqol_76)
        lvl_77 = random.choice(maqol_77)
        lvl_78 = random.choice(maqol_78)
        lvl_79 = random.choice(maqol_79)
        lvl_80 = random.choice(maqol_80)
        lvl_81 = random.choice(maqol_81)
        lvl_82 = random.choice(maqol_82)
        lvl_83 = random.choice(maqol_83)
        lvl_84 = random.choice(maqol_84)
        lvl_85 = random.choice(maqol_85)
        lvl_86 = random.choice(maqol_86)
        lvl_87 = random.choice(maqol_87)
        lvl_88 = random.choice(maqol_88)
        lvl_89 = random.choice(maqol_89)
        lvl_90 = random.choice(maqol_90)
        lvl_91 = random.choice(maqol_91)
        lvl_92 = random.choice(maqol_92)
        lvl_93 = random.choice(maqol_93)
        lvl_94 = random.choice(maqol_94)
        lvl_95 = random.choice(maqol_95)
        lvl_96 = random.choice(maqol_96)
        lvl_97 = random.choice(maqol_97)
        lvl_98 = random.choice(maqol_98)
        lvl_99 = random.choice(maqol_99)
        lvl_100 = random.choice(maqol_100)


        return Response(tecnology)