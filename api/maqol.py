from rest_framework.views import APIView
from rest_framework.response import Response
import random

# 100ta level buladi va har bir levelda 5tadan savol buladi
class MaqolApi(APIView):
    def get(self, request):

        # 40ta
        maqol_1 = [
            {
                "savol": "Aytar so'zni ayt, aytmas so'zdan ....",
                "javob": "qayt"
            },
            {
                "savol": "Aytilgan so'z - otilgan ....",
                "javob": "o'q"
            },
            {
                "savol": "Andishaning oti ....",
                "javob": "qo'rqoq"
            },
            {
                "savol": "Arpa ekkan arpa o'rar, bug'doy ekkan ....",
                "javob": "bug'doy"
            },
            {
                "savol": "Arpaning doni bo'lguncha, bug'doyning .... bo'l.",
                "javob": "somoni"
            },
            {
                "savol": "Arqog'ini ko'rib bo'zini ol, ....ni ko'rib qizini ol.",
                "javob": "onasini"
            },
            {
                "savol": "Afting qiyshiq bo'lsa, oynadan ....",
                "javob": "o'pkalama"
            },
            {
                "savol": "Aqlli o'zini ayblar, aqlsiz ....",
                "javob": "do'stini"
            },
            {
                "savol": "Avval o'yla, keyin ....",
                "javob": "so'yla"
            },
            {
                "savol": "Bir kattaning gapiga kir, bir ....",
                "javob": "kichikning"
            },
            {
                "savol": "Bir kun tuz ichgan joyinga qirq kun .... ber.",
                "javob": "salom"
            },
            {
                "savol": "Birovni ustidan .... zinhor, sening ham ustingdan kuladiganlar bor.",
                "javob": "kulmagin"
            },
            {
                "savol": "Birovga choh qazisang, o'zing ....",
                "javob": "tusharsan"
            },
            {
                "savol": "Birovga o'lim tilaguncha, o'zinga .... tila.",
                "javob": "umr"
            },
            {
                "savol": "Bolaga ishga buyur, orqasidan o'zing ....",
                "javob": "yugur"
            },
            {
                "savol": "Boshinga qilich kelsa ham .... so'zla.",
                "javob": "rost"
            },
            {
                "savol": "Buqdan qo'rqqan tezak ....",
                "javob": "yopmaydi"
            },
            {
                "savol": "Bukrini .... tuzatadi.",
                "javob": "g'or"
            },
            {
                "savol": "Bir mayizni .... kishi yer.",
                "javob": "qirq"
            },
            {
                "savol": "Birniki mingga, mingniki ....",
                "javob": "olamda"
            },
            {
                "savol": "Bulbul chamanni sevar, Odam — ....",
                "javob": "Vatanni"
            },
            {
                "savol": "Dangasaga ish buyursang, otangdan ortiq .... qiladi.",
                "javob": "nasihat"
            },
            {
                "savol": "Dangasaga ish buyursang, senga aql ....",
                "javob": "o'rgatar"
            },
            {
                "savol": "Dangasaning ishi bitmas, yoz kelsa ham .... bitmas.",
                "javob": "qishi"
            },
            {
                "savol": "Danagidan .... shirin.",
                "javob": "mag'izi"
            },
            {
                "savol": "Darding bo'lsa bo'lsin, .... bo'lmasin.",
                "javob": "qarzing"
            },
            {
                "savol": "Devor tagida gapirma, devorning ham .... bor.",
                "javob": "qulog'i"
            },
            {
                "savol": "Dehqon bo'lsang shudgor qil, mulla bo'lsang .... qil.",
                "javob": "takror"
            },
            {
                "savol": "Dunyoni suv bossa, to'pig'iga ham ....",
                "javob": "chiqmaydi"
            },
            {
                "savol": "Dushmanga joningni bersang ham, siringni ....",
                "javob": "berma"
            },
            {
                "savol": "Dushmanning kulgani - siringni ....",
                "javob": "bilgani"
            },
            {
                "savol": "Do'st achitib gapirar, dushman — ....",
                "javob": "kuldirib"
            },
            {
                "savol": "Do'st boshga boqar, dushman ....",
                "javob": "oyoqqa"
            },
            {
                "savol": "Do'st boshga kulfat tushganda ....",
                "javob": "sinaladi"
            },
            {
                "savol": "Do'st so'zini tashlama, tashlab boshing ....",
                "javob": "qashlama"
            },
            {
                "savol": "Do'stim deb siringni aytma, do'stingning ham .... bor.",
                "javob": "do'sti"
            },
            {
                "savol": "Do'sting uchun .... yut.",
                "javob": "zahar"
            },
            {
                "savol": "Do'stsiz boshim - tuzsiz ....",
                "javob": "oshim"
            },
            {
                "savol": "Egilgan boshni .... kesmas.",
                "javob": "qilich"
            },
            {
                "savol": "Ezgulikning erta kechi ....",
                "javob": "yo'q"
            }
        ]

        maqol_2 = [
            {
                "savol": "El og'ziga elak tutib ....",
                "javob": "bo'lmas"
            },
            {
                "savol": "Elakka chiqqan xotinning ellik og'iz .... bor.",
                "javob": "gapi"
            },
            {
                "savol": "Elchiga .... yo'q.",
                "javob": "o'lim"
            },
            {
                "savol": "Er yigitning uyalgani - ....",
                "javob": "o'lgani"
            },
            {
                "savol": "Er-xotinning urushi - doka ro'molning ....",
                "javob": "qurishi"
            },
            {
                "savol": "Ering suydi - eling ....",
                "javob": "suydi"
            },
            {
                "savol": "Erning so'zi ....",
                "javob": "bitta"
            },
            {
                "savol": "Eru xotin - qo'sh ....",
                "javob": "ho'kiz"
            },
            {
                "savol": "Esingning borida etagingni ....",
                "javob": "yop"
            },
            {
                "savol": "Eshakning mehnati halol, go'shti ....",
                "javob": "harom"
            },
            {
                "savol": "Falokat oyoq ....",
                "javob": "ostida"
            },
            {
                "savol": "Farzand bilan davlatning erta-kechi ....",
                "javob": "yo'q"
            },
            {
                "savol": "Farzandiga otaning mehri ketmoncha bo'lsa, onaning mehri .... bor.",
                "javob": "osmoncha"
            },
            {
                "savol": "Faqir kishi ....",
                "javob": "panada"
            },
            {
                "savol": "Gul o'ssa - yerning ko'rki, qiz o'ssa — ....",
                "javob": "yurtning"
            },
            {
                "savol": "Har qush uyasida ko'rganini ....",
                "javob": "qiladi"
            },
            {
                "savol": "“Hayt” degan tuyaga ....",
                "javob": "mador"
            },
            {
                "savol": "Hazil, hazilning tagi ....",
                "javob": "zil"
            },
            {
                "savol": "Hur gulning isi ....",
                "javob": "boshqa"
            },
            {
                "savol": "Har yerni qilma orzu, har yerda ham bordir toshu ....",
                "javob": "torozu"
            },
            {
                "savol": "Har kallada har ....",
                "javob": "hayol"
            },
            {
                "savol": "Har kim ekkanini ....",
                "javob": "o'radi"
            },
            {
                "savol": "Har kimniki o'ziga, .... ko'rinar ko'ziga.",
                "javob": "oy"
            },
            {
                "savol": "Har to'kisda bir ....",
                "javob": "ayb"
            },
            {
                "savol": "Haqiqat egiladi, ammo ....",
                "javob": "sinmaydi"
            },
            {
                "savol": "Hisobli do'st ....",
                "javob": "ayrilmas"
            },
            {
                "savol": ".... olma, qo'shni ol.",
                "javob": "hovli"
            },
            {
                "savol": "Hunar - hunardan ....",
                "javob": "unar"
            },
            {
                "savol": ".... kishi och qolmas",
                "javob": "hunarli"
            },
            {
                "savol": "Husn to'yda kerak, aql ....",
                "javob": "kunda"
            },
            {
                "savol": "Ignadek joydan tuyadek .... kiradi.",
                "javob": "sovuq"
            },
            {
                "savol": "Ignachining ming urgani, temirchining .... urgani.",
                "javob": "bir"
            },
            {
                "savol": "Ikki yorti - bir ....",
                "javob": "butun"
            },
            {
                "savol": "Ikki kemaga oyoq qo'ygan .... bo'lur.",
                "javob": "g'arq"
            },
            {
                "savol": "Intilganga tole ....",
                "javob": "yor"
            },
            {
                "savol": "It hurar, karvon ....",
                "javob": "o'tar"
            },
            {
                "savol": "Ish bilganga bir tanga, gap bilganga .... tanga.",
                "javob": "ming"
            },
            {
                "savol": ".... bor yerda xato bor.",
                "javob": "ish"
            },
            {
                "savol": "Ish ishtaha ochar, dangasa ishdan ....",
                "javob": "qochar"
            },
            {
                "savol": "Ishongan tog'da kiyik ....",
                "javob": "yotmas"
            }
        ]

        maqol_3 = [
            {
                "savol": "Ishonmagin do'stingga, somon tiqar ....",
                "javob": "po'stingga"
            },
            {
                "savol": "Janjalli uyda baraka ....",
                "javob": "bo'lmas"
            },
            {
                "savol": "Jahl kelsa, aql ....",
                "javob": "ketar"
            },
            {
                "savol": "Joyimiz tor bo'lsa ham, ko'nglimiz .... bo'lsin.",
                "javob": "keng"
            },
            {
                "savol": "Kambag'al bo'lsang ko'chib ....",
                "javob": "boq"
            },
            {
                "savol": "Kambag'alni tuyaning ustida ham it ....",
                "javob": "qopadi"
            },
            {
                "savol": "Kamtarga kamol, manmanga ....",
                "javob": "zavol"
            },
            {
                "savol": "Kasalini yashirsang, istimasi .... qiladi.",
                "javob": "oshkor"
            },
            {
                "savol": "Katta arava qayoqdan yursa, kichik arava ham o'sha yoqdan ....",
                "javob": "yuradi"
            },
            {
                "savol": "Kemaga tushganning joni ....",
                "javob": "bir"
            },
            {
                "savol": "Ko'p gap .... yuk.",
                "javob": "eshakka"
            },
            {
                "savol": "Ko'pdan quyon qochib ....",
                "javob": "qutulmas"
            },
            {
                "savol": "Ko'r ko'rni qorong'uda ....",
                "javob": "topadi"
            },
            {
                "savol": "Ko'r hassasini bir marta ....",
                "javob": "yo'qotadi"
            },
            {
                "savol": "Ko'rpangga qarab oyoq ....",
                "javob": "uzat"
            },
            {
                "savol": "Kengga keng dunyo, torga .... dunyo.",
                "javob": "tor"
            },
            {
                "savol": "Kerakli toshning og'irligi ....",
                "javob": "yo'q"
            },
            {
                "savol": "Kim tabib - boshidan o'tgan ....",
                "javob": "tabib"
            },
            {
                "savol": "Kuch - ....",
                "javob": "birlikda"
            },
            {
                "savol": "Ko'z qo'rqoq, qo'l ....",
                "javob": "botir"
            },
            {
                "savol": "Kambag'al don topmaydi, don topsa .... topmaydi.",
                "javob": "idish"
            },
            {
                "savol": "Laylakning ketishiga boqma, kelishiga ....",
                "javob": "boq"
            },
            {
                "savol": "Laqmaning kallasi, tarozuning ....",
                "javob": "pallasi"
            },
            {
                "savol": "Mard maydonda ....",
                "javob": "sinalar"
            },
            {
                "savol": "Maqtanganning uyiga bor, kerilganning .... bor.",
                "javob": "to'yi"
            },
            {
                "savol": "Mehmon kelar eshikdan, rizqi kelar ....",
                "javob": "teshikdan"
            },
            {
                "savol": "Mehmon otangdan ....",
                "javob": "ulug'"
            },
            {
                "savol": "....ning tagi rohat",
                "javob": "mehnat"
            },
            {
                "savol": "Ming marta eshitgandan, bir marta ko'rgan ....",
                "javob": "yaxshi"
            },
            {
                "savol": "Minnatli oshdan, beminnat .... yaxshi.",
                "javob": "musht"
            },
            {
                "savol": "Mol achchig'i - jon ....",
                "javob": "achchig'i"
            },
            {
                "savol": "Mug'ombir o'z tumshug'idan ....",
                "javob": "ilinar"
            },
            {
                "savol": "Nima eksang shuni ....",
                "javob": "o'rasan"
            },
            {
                "savol": "Nodon do'stdan, ziyrak dushman ....",
                "javob": "yaxshi"
            },
            {
                "savol": "Nomi ulug' - suprasi ....",
                "javob": "quruq"
            },
            {
                "savol": "Nomus o'limdan ....",
                "javob": "kuchli"
            },
            {
                "savol": "Non ham non, ushog'i ham ....",
                "javob": "non"
            },
            {
                "savol": "Nafsi g'olib hayitda ....",
                "javob": "o'ladi"
            },
            {
                "savol": "Nimani hor qilsang, shunga .... bo'lasan.",
                "javob": "zor"
            },
            {
                "savol": "Taom lazzati tuzida, odam lazzati ....da.",
                "javob": "tili"
            }
        ]

        maqol_4 = [
            {
                "savol": "Oltin olma, duo ol — duo oltindan ham ....",
                "javob": "afzal"
            },
            {
                "savol": "Har kimniki o'ziga, oy ko'rinar ....",
                "javob": "ko'ziga"
            },
            {
                "savol": "Hovli olma, .... ol.",
                "javob": "qo'shni"
            },
            {
                "savol": "Hunarli kishi och ....",
                "javob": "qolmas"
            },
            {
                "savol": "Ish bor yerda .... bor.",
                "javob": "xato"
            },
            {
                "savol": "Oila mustahkamligi — uy devorida emas, qalblardagi .... bilan o‘lchanadi.",
                "javob": "mehr"
            },
            {
                "savol": "Mehrsiz oila — ildizsiz .... kabidir.",
                "javob": "daraxt"
            },
            {
                "savol": "Ota-onasini e’zozlagan farzand, ertaga o‘zi ham .... ko‘radi.",
                "javob": "ehtirom"
            },
            {
                "savol": "Onaning duosi — oilaning eng katta ....dir.",
                "javob": "qalqoni"
            },
            {
                "savol": "Oila — insonning dunyodagi eng katta ....dir.",
                "javob": "qal'asi"
            },
            {
                "savol": "Oilada hurmat yuq bo'lsa, .... ham uzoq yashamaydi.",
                "javob": "muhabbat"
            },
            {
                "savol": "Oila — jamiyatning eng kichik, ammo eng buyuk ....",
                "javob": "maktabi"
            },
            {
                "savol": "Oilada muhabbat bo‘lsa, qashshoqlik ham .... kabi ko‘rinadi.",
                "javob": "boylik"
            },
            {
                "savol": "Ona qizi uchun eng muhim .... hisoblanadi.",
                "javob": "ustoz"
            },
            {
                "savol": "Farzand tarbiyasi - .... emas, umurlik mehnat.",
                "javob": "yillik"
            },
            {
                "savol": ".... — insonning eng katta boyligidir.",
                "javob": "aql"
            },
            {
                "savol": ".... odam kam gapirib, ko'p tinglaydi.",
                "javob": "aqlli"
            },
            {
                "savol": "Aqlsiz boylik — egasiz .... kabidir.",
                "javob": "xazina"
            },
            {
                "savol": "Idroksiz inson — ko‘zi ochiq, ammo .... ko‘r odamdir.",
                "javob": "qalban"
            },
            {
                "savol": ".... yoshda emas, boshda bo'ladi.",
                "javob": "aql"
            },
            {
                "savol": "O‘ylamay gapirgan, oxirida o‘ylab .... qiladi.",
                "javob": "pushaymon"
            },
            {
                "savol": "Aql — chiroq, idrok esa uning ....dir.",
                "javob": "yorug‘i"
            },
            {
                "savol": "Kimki o‘z aqliga tayanmasa, boshqalarning .... bo‘ladi.",
                "javob": "quli"
            },
            {
                "savol": "Aqilli bosh - ming .... teng.",
                "javob": "qo'lga"
            },
            {
                "savol": ".... bilan yengilmas dushmanni ham yengish mumkin.",
                "javob": "aql"
            },
            {
                "savol": "Mehnat — insonning qo‘lida qurol, qalbida esa ....dir.",
                "javob": "umid"
            },
            {
                "savol": "Kim mehnatning achchiq terini to‘ksa, oxirida uning .... shirin bo‘ladi.",
                "javob": "mevasi"
            },
            {
                "savol": "Mehnat - mehnatni tagi ....",
                "javob": "rohat"
            },
            {
                "savol": "Dangasa odam tongni .... bog'laydi",
                "javob": "tunga"
            },
            {
                "savol": "Qancha ter tuksang, shuncha .... olasan",
                "javob": "hosil"
            },
            {
                "savol": "Mehnatsiz yashashni istagan inson — hayotning eng achchiq .... kutgan insondir.",
                "javob": "yolg'onini"
            },
            {
                "savol": "Mehnatkash odamning qo‘li charchaydi, ammo uning qalbi hech qachon .... sezmaydi",
                "javob": "charchoq"
            },
            {
                "savol": "Dangasa odam orzular haqida gapiradi, mehnatkash odam esa ularni .... chiqaradi.",
                "javob": "ro‘yobga"
            },
            {
                "savol": ".... — baxt eshigini ochadigan yagona kalitdir.",
                "javob": "mehnat"
            },
            {
                "savol": "Dangasa o'zini, mehnatkash boshqasini ....",
                "javob": "boqadi"
            },
            {
                "savol": "Yo‘qotilgan boylik qaytadi, yo‘qotilgan sog‘liq tiklanadi, ammo yo‘qotilgan .... qaytmaydi.",
                "javob": "vaqt"
            },
            {
                "savol": ".... — insonning eng sodiq hamrohi, ammo uni qadrlamagan odamning eng katta dushmani bo‘ladi.",
                "javob": "vaqt"
            },
            {
                "savol": "Vaqtni behuda ketqazma, u hayotdan qirqilgan bir ....",
                "javob": "bo'lakdir"
            },
            {
                "savol": "Har bir lahza — inson qo‘lidan chiqib ketayotgan ....ning bir bo'lagidir.",
                "javob": "umur"
            },
            {
                "savol": "Har bir ishning o'z vaqti bor, erta qilinsa xato, kechiksa ....",
                "javob": "zarar"
            }
        ]

        maqol_5 = [
            {
                "savol": "Tajriba — eng qimmat ustoz, lekin uning darslari odatda .... bo‘ladi.",
                "javob": "og‘riqli"
            },
            {
                "savol": "Xatolar — hayotning yozuvi, tajriba esa uning eng to‘g‘ri ....dir.",
                "javob": "izohi"
            },
            {
                "savol": "Tajriba — insonning boyligi, uni hech qachon .... bilan sotib olib bo‘lmaydi.",
                "javob": "pul"
            },
            {
                "savol": "Har xato - yangi bir ....",
                "javob": "saboq"
            },
            {
                "savol": "Tajriba — o‘qituvchi, ammo uning kitobi faqat .... bilan yoziladi.",
                "javob": "umr"
            },
            {
                "savol": "Odob — insonning eng go‘zal ....dir.",
                "javob": "libosi"
            },
            {
                "savol": "Boylik bezagi — oltin, insonning bezagi esa ....",
                "javob": "odob"
            },
            {
                "savol": "Odobli bola - oilaning ....",
                "javob": "ko'zgusi"
            },
            {
                "savol": "Ilm o'rgatishdan oldin .... o'rgat",
                "javob": "odob"
            },
            {
                "savol": "Trbiyasiz jamiyat - poydevorsiz ....",
                "javob": "imorat"
            },
            {
                "savol": "Farzand tarbiyasi — ota-onaning eng buyuk ....dir.",
                "javob": "merosi"
            },
            {
                "savol": "Bolaga bergan tarbiya — dunyoga qoldirilgan eng katta ....dir.",
                "javob": "xotira"
            },
            {
                "savol": "Tarbiya — oltin emas, ammo undan qimmatliroq ....dir.",
                "javob": "boylik"
            },
            {
                "savol": "Odob bilan aytilgan tanbeh, .... aylanadi",
                "javob": "darsga"
            },
            {
                "savol": ".... qilsang - .... topasan",
                "javob": "hurmat"
            },
            {
                "savol": ".... odamga davo ham bo'ladi, balo ham.",
                "javob": ""
            },
            {
                "savol": "Boylik tugaydi, kuch susayadi, ammo yaxshi nom .... qoladi.",
                "javob": "abadiy"
            },
            {
                "savol": "Sabr daraxtining mevasi doim .... bo‘ladi.",
                "javob": "shirin"
            },
            {
                "savol": "Do‘stni boylikda emas, qiyinchilikda .... kerak.",
                "javob": "sinash"
            },
            {
                "savol": "Vaqt — insonning eng qimmatli ....dir.",
                "javob": "ne’mati"
            },
            {
                "savol": "Halol mehnatning noni, oltindan ham ....dir.",
                "javob": "qimmat"
            },
            {
                "savol": "Yaxshilikni .... qil, lekin doimo qil",
                "javob": "yashirin"
            },
            {
                "savol": "Sukut bazan eng dono javobdir.",
                "javob": ""
            },
            {
                "savol": "Shukr qilingan rizq oz bo‘lsa ham, .... ko‘p bo‘ladi.",
                "javob": "barakasi"
            },
            {
                "savol": ".... — qorong‘ilikdagi eng yorqin yulduzdir.",
                "javob": "umid"
            },
            {
                "savol": "Ota-onangni rozi qil - .... rozi qil",
                "javob": "volidangni"
            },
            {
                "savol": "Onaning duosi — farzand uchun eng katta ....dir.",
                "javob": "qalqon"
            },
            {
                "savol": "Ota-onani sevgan - .... sevadi.",
                "javob": "vatanni"
            },
            {
                "savol": "Farzandning baxti — ota-onasining ....",
                "javob": "duosida"
            },
            {
                "savol": "Ota-onaning rozi bo‘lishi — Allohning ....dir.",
                "javob": "roziligi"
            },
            {
                "savol": "Onaning ko‘z yoshlari — farzand uchun eng katta ....dir.",
                "javob": "la’nat"
            },
            {
                "savol": "Ota-onasiga xizmat qilmagan farzand, kun kelib .... bo‘ladi.",
                "javob": "xor"
            },
            {
                "savol": "Ota-ona duosidan mahrum bo‘lgan farzand, hayotda hech qachon .... topmaydi.",
                "javob": "baraka"
            },
            {
                "savol": ".... onalar oyog'i ostidadur.",
                "javob": "jannat"
            },
            {
                "savol": "Ota gapidan - yo'l topiladi, ona .... - baraka topiladi.",
                "javob": "duosidan"
            },
            {
                "savol": "Ishonch — qalbni birlashtiradigan eng katta ....dir.",
                "javob": "ko‘prik"
            },
            {
                "savol": ".... ikki qalb o'rtasidagi ko'prikdir.",
                "javob": "ishonch"
            },
            {
                "savol": "Ishonch — suvga o‘xshaydi, agar to‘kilib ketsa, uni qayta .... qiyin.",
                "javob": "yig‘ish"
            },
            {
                "savol": "Ishonchni mustahkam qiladigan narsa — halollik va ....dir.",
                "javob": "rostgo'ylik"
            },
            {
                "savol": "Har .... bir haqiqatni ochadi - kim kimligini.",
                "javob": "xiyonat"
            }
        ]

        maqol_6 = [
            {
                "savol": "Xiyonatning izlari — ko‘rinmaydi, ammo qalbdagi .... yo'qolmaydi.",
                "javob": "og‘riq"
            },
            {
                "savol": "Xiyonat — dushmanlikdan ham xavfli, chunki u ichdan ....",
                "javob": "yemiradi"
            },
            {
                "savol": ".... qilgan odam, oxirida o‘ziga ham .... qiladi.",
                "javob": "xiyonat"
            },
            {
                "savol": "Xiyonat — qalbda og'riq beradigan ....dir.",
                "javob": "zahar"
            },
            {
                "savol": "Sadoqatni asragan qalb — yuksaladi, xiyonat qilgan qalb esa .... bo‘ladi.",
                "javob": "halok"
            },
            {
                "savol": "Sabr daraxti achchiq, ammo uning mevasi .... bo‘ladi.",
                "javob": "shirin"
            },
            {
                "savol": ".... inson - hayotni chuqur anglaydi.",
                "javob": "sabrli"
            },
            {
                "savol": "Sabrli bo'lish - o'zingni .... bilishdir",
                "javob": "boshqara"
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
                "savol": ".... - Allohga bo'lgan ishonchning belgisi",
                "javob": "sabr"
            },
            {
                "savol": "Sabr — ilmning ham, iymonning ham ....dir.",
                "javob": "ustuni"
            },
            {
                "savol": "Sabr bilan to‘kilgan ko‘z yosh, oxirida ....ga aylanadi.",
                "javob": "quvonch"
            },
            {
                "savol": "Og'ir kunlar sabrni sinaydi, sabr esa ....",
                "javob": "imonni"
            },
            {
                "savol": "Sabr — Allohning bandaga bergan eng buyuk ....dir.",
                "javob": "sovg‘asi"
            },
            {
                "savol": "Hasad — qalbni ....",
                "javob": "chiritadi"
            },
            {
                "savol": ".... - o'zini sevmagan odamning ko'zgusidir.",
                "javob": "hasad"
            },
            {
                "savol": "Dushmaning bo'lishi seni .... qiladi.",
                "javob": "kuchli"
            },
            {
                "savol": "Hasad — yomonlikning urug‘i, uning mevasi doimo .... bo‘ladi.",
                "javob": "achchiq"
            },
            {
                "savol": "Hasad qilgan odam, o‘zgani emas, avvalo o‘zini ....laydi",
                "javob": "azob"
            },
            {
                "savol": "Qish — tabiatning sokin, ammo eng og‘ir ....dir.",
                "javob": "sinovi"
            },
            {
                "savol": "Yoz — .... uchun eng katta barakadir.",
                "javob": "mehnatkash"
            },
            {
                "savol": "Yoz — tabiatning eng go‘zal ....dir.",
                "javob": "ziyofati"
            },
            {
                "savol": "Kuz — .... fasli.",
                "javob": "hosil"
            },
            {
                "savol": "Kuz — to‘plagan mehnatning ....dir.",
                "javob": "mevasi"
            },
            {
                "savol": "Yozda qilingan mehnat, qishda .... beradi.",
                "javob": "rohat"
            },
            {
                "savol": "Kuzda yig‘ilmagan ...., qishda qashshoqlik bo‘ladi.",
                "javob": "hosil"
            },
            {
                "savol": "Bahor — tabiatning qayta ....dir.",
                "javob": "tirilishi"
            },
            {
                "savol": ".... yomg‘iri — tabiatning ko‘z yoshidir.",
                "javob": "bahor"
            },
            {
                "savol": "Har bir tukilgan barg - .... sabog'i",
                "javob": ""
            },
            {
                "savol": "Obro‘ — pul bilan emas, faqat .... bilan topiladi.",
                "javob": "amal"
            },
            {
                "savol": "Yomon nomdan ko'ra, .... ketgan avzal",
                "javob": "izsiz"
            },
            {
                "savol": "....ni saqlash qiyin, yo‘qotish esa oson",
                "javob": "obro'"
            },
            {
                "savol": "Obro‘ — insonning ko'rinmas ....",
                "javob": "boyligi"
            },
            {
                "savol": "Yaxshi .... - oltin tobutdan afzal",
                "javob": "nom"
            },
            {
                "savol": "Farzandning eng katta tayanchi ....?",
                "javob": "otaona"
            },
            {
                "savol": "Farzandning baxti ....",
                "javob": "duo"
            },
            {
                "savol": "Onaning ko‘z nuri ....",
                "javob": "farzand"
            },
            {
                "savol": "Farzand uchun eng qimmat tuyg‘u ....",
                "javob": "mehr"
            },
            {
                "savol": "Farzand tarbiyasida eng muhim qadriyat?",
                "javob": "hurmat"
            }
        ]

        maqol_7 = [
            {
                "savol": "Ovqatning lazzati — tuzda, hayotning lazzati esa ....da.",
                "javob": "shukr"
            },
            {
                "savol": "Ovqat tanani boqadi, halollik esa ....ni.",
                "javob": "ruh"
            },
            {
                "savol": "Halol ovqat — tan uchun oziq, harom ovqat .... uchun zahar.",
                "javob": "qalb"
            },
            {
                "savol": "Ovqatni shirin qiladigan narsa — .... va halollikdir.",
                "javob": "mehnat"
            },
            {
                "savol": ".... rizqning kalitidir.",
                "javob": "mehnat"
            },
            {
                "savol": "Rizq — Allohning in’omi, uni kengaytiradigan narsa — ....dir.",
                "javob": "shukr"
            },
            {
                "savol": "Rizqni ko‘p qiladigan narsa — ota-onaning ....",
                "javob": "duosi"
            },
            {
                "savol": "Rizqni tor qiladigan narsa — ....",
                "javob": "isrof"
            },
            {
                "savol": "Halol rizq oz bo‘lsa ham, uning .... ko‘p bo‘ladi.",
                "javob": "barakasi"
            },
            {
                "savol": "Rizqning lazzati — halollikda, barakasi esa ....da.",
                "javob": "shukr"
            },
            {
                "savol": "Rizq — odamni boqadi, ammo uni topish uchun .... qilish kerak.",
                "javob": "mehnat"
            },
            {
                "savol": "Rizqsiz odam yo‘q, ammo har bir rizqning .... bor.",
                "javob": "hisobi"
            },
            {
                "savol": "Rizqni oz yoki ko'pligi emas, .... muhimdir",
                "javob": "barakasi"
            },
            {
                "savol": "Alloh rizqni ....ga bog'lagan",
                "javob": "mehnat"
            },
            {
                "savol": "Rizqni kengaytiradigan kalit — bu ....dir.",
                "javob": "halollik"
            },
            {
                "savol": "Baxt — ko‘p narsaga ega bo‘lishda emas, bor narsaga .... qilishdadir.",
                "javob": "shukr"
            },
            {
                "savol": "Baxtli odam — boriga shukur qilsa, baxtsiz odam .... izlaydi.",
                "javob": "kamchilik"
            },
            {
                "savol": "Baxtning siri — ko‘ngilning ....dadur.",
                "javob": "pokligi"
            },
            {
                "savol": "Baxtli bo‘lish — boshqalarga .... ulashishni ham o‘z ichiga qiladi.",
                "javob": "baxt"
            },
            {
                "savol": "Boylik qo‘ldan ketadi, baxt esa qalbda .... qoladi.",
                "javob": "abadiy"
            },
            {
                "savol": "Baxt — orzularning emas, shukrning ....dir.",
                "javob": "mevasi"
            },
            {
                "savol": "Baxtni ...., shunda u seni tark etmaydi.",
                "javob": "qadrla"
            },
            {
                "savol": "Baxtli bo'lmoq uchun .... tozalash kerak.",
                "javob": "qalbni"
            },
            {
                "savol": ".... har doim yoningda, faqat uni ko'ra bilishing kerak.",
                "javob": "baxt"
            },
            {
                "savol": ".... - o'zligingni topishdir.",
                "javob": "baxt"
            },
            {
                "savol": ".... — yozilgan kitob, ammo uni qanday o‘qish insonning o'z qo‘lida.",
                "javob": "taqdir"
            },
            {
                "savol": "Baxtni topish uchun avvalo uni .... kerak.",
                "javob": ""
            },
            {
                "savol": "Taqdirni qabul qilmagan odam doimiy .... ichida yashaydi.",
                "javob": "azob"
            },
            {
                "savol": "Yaxshi taqdir — sovg‘a, yomon taqdir esa ....dir.",
                "javob": "saboq"
            },
            {
                "savol": "Taqdir — qalbni sinaydi, ammo uni sabr bilan qabul qilgan odam .... topadi.",
                "javob": "baxt"
            },
            {
                "savol": "Til - insonning ....",
                "javob": "oynasi"
            },
            {
                "savol": "Til — insonning o‘zini oshkor qiladigan ....dir.",
                "javob": "oyna"
            },
            {
                "savol": "Til yarasi — qilich yarasidan ham .... bo‘ladi.",
                "javob": "og‘ir"
            },
            {
                "savol": "Yaxshi so'z - ....",
                "javob": "sadaqa"
            },
            {
                "savol": "Til — qalbning ....",
                "javob": "tarjimoni"
            },
            {
                "savol": "Janjalning ildizi — jahlda, mevasi esa .... bo‘ladi.",
                "javob": "pushaymon"
            },
            {
                "savol": "Janjalni bosadigan eng katta kuch — bu ....dir.",
                "javob": "sukut"
            },
            {
                "savol": "Janjal chiqsa, eshikdan birinchi .... chiqib ketadi.",
                "javob": "aql"
            },
            {
                "savol": "Janjal — kichik uchqundan chiqib, katta ....ga aylanadi.",
                "javob": "olov"
            },
            {
                "savol": "Bahsda g'olib bo'lish - ba'zan .... ayrilishdir",
                "javob": "do'stdan"
            }
        ]

        maqol_8 = [
            {
                "savol": "Yaxshi niyat — yarim ....",
                "javob": "davlat"
            },
            {
                "savol": "Yaxshi niyatli odamning yo‘li doimo .... bo‘ladi.",
                "javob": "ochiq"
            },
            {
                "savol": "Har danday amal - .... bog'liq.",
                "javob": "niyatga"
            },
            {
                "savol": "Ezgu niyat - odamni ....dan saqlaydi",
                "javob": "yomonlik"
            },
            {
                "savol": "Niyat halol bo'lsa, ... yordam beradi",
                "javob": "Alloh"
            },
            {
                "savol": "Hurmat — insonning eng katta ....",
                "javob": "boyligi"
            },
            {
                "savol": "Hurmat - qalblarni birlashtiradi, ... esa ajratadi.",
                "javob": "kibr"
            },
            {
                "savol": "Hurmat — qalblarni birlashtiradigan eng mustahkam ....dir.",
                "javob": "ip"
            },
            {
                "savol": "Kattaga hurmat - kichikka ....",
                "javob": "izzat"
            },
            {
                "savol": "Ehtiromsiz .... - toshga o'xshaydi.",
                "javob": "yurak"
            },
            {
                "savol": ".... — donishmandning eng katta qurolidir.",
                "javob": "sukut"
            },
            {
                "savol": ".... saqlagan odam, hech qachon so‘zidan pushaymon bo‘lmaydi.",
                "javob": "sukut"
            },
            {
                "savol": "Sukut ko'p hollarda eng kuchli ....dir",
                "javob": "javob"
            },
            {
                "savol": "oz so'zla - .... so'zla",
                "javob": "soz"
            },
            {
                "savol": "Ko'p gap - .... yuk",
                "javob": "eshakka"
            },
            {
                "savol": "Ko‘ngilni og‘ritish oson, lekin uni tuzatish ....dir.",
                "javob": "qiyin"
            },
            {
                "savol": "Ko‘ngil — oynaga o‘xshaydi, bir sinib qolsa, .... bo‘lmaydi.",
                "javob": "butun"
            },
            {
                "savol": "Ko‘ngil — insonning eng nozik ....dir.",
                "javob": "joyi"
            },
            {
                "savol": "Ko‘ngilni ko‘targan odam, aslida qalbni .... qiladi.",
                "javob": "nurli"
            },
            {
                "savol": "So'zga emas, .... ham quloq sol.",
                "javob": "sukutga"
            },
            {
                "savol": ".... — insonni ulug‘ qilmaydi, balki uning asl qiyofasini ko‘rsatadi.",
                "javob": "boylik"
            },
            {
                "savol": "Boylikning haqiqati — halollikda, yolg‘on boylik esa ....dir.",
                "javob": "baloga"
            },
            {
                "savol": "Boylik ko‘paygan sayin, insonning .... ham ko'p bo‘ladi.",
                "javob": "sinovi"
            },
            {
                "savol": "Boylik vaqtincha, ammo yaxshi nom — ....",
                "javob": "abadiy"
            },
            {
                "savol": "Pul cho'ntakda bo'lsa xizmatkor, yurakda bo'lsa ....",
                "javob": "xoin"
            },
            {
                "savol": "Yaxshi qo‘shni — yarim ....",
                "javob": "qarindosh"
            },
            {
                "savol": "Sog‘liq — eng katta ....",
                "javob": "boylik"
            },
            {
                "savol": "Halol kasb — rizqning eng katta ....dir.",
                "javob": "manbai"
            },
            {
                "savol": "Kasb — ota merosi emas, har kimning o‘z ....dir.",
                "javob": "mehnati"
            },
            {
                "savol": "Boylikni oshiradigan narsa — halollik, kamaytiradigan narsa esa ....dir.",
                "javob": "isrof"
            },
            {
                "savol": "Savdoda halollik — foydaning eng katta ....dir.",
                "javob": "garovi"
            },
            {
                "savol": "Yolg‘on savdo — qisqa foyda, ammo uzoq ....dir.",
                "javob": "zarar"
            },
            {
                "savol": "Kulgu — qalbga eng yaxshi ....dir.",
                "javob": "davo"
            },
            {
                "savol": "Haddan oshgan ...., oxirida ko‘z yoshga aylanadi.",
                "javob": "kulgu"
            },
            {
                "savol": "Farzand — ota-onaning eng katta ....dir.",
                "javob": "sinovi"
            },
            {
                "savol": "Farzand tarbiyasi — millatning eng katta ....dir.",
                "javob": "kelajagi"
            },
            {
                "savol": "Vatansiz odam, ildizsiz .... kabidir.",
                "javob": "daraxt"
            },
            {
                "savol": ".... — qadrini faqat undan uzoqlashganda bilasan.",
                "javob": "vatan"
            },
            {
                "savol": "Yolg‘on — ishonchning eng katta ....dir.",
                "javob": "dushmani"
            },
            {
                "savol": "Haqiqat — quyosh kabi, uni hech qachon .... bo‘lmaydi.",
                "javob": "yopib"
            }
        ]

        maqol_9 = [
            {
                "savol": "Vaqtni tanigan odam - .... sari yuradi.",
                "javob": "donolik"
            },
            {
                "savol": "vaqtni bekorga sarflama - u sening ....dir",
                "javob": "hayoting"
            },
            {
                "savol": "Bir lahzaning qadri, uni .... bilinadi.",
                "javob": "yo'qotganda"
            },
            {
                "savol": "Har bir kun - hayotdan bir ....",
                "javob": "sahifa"
            },
            {
                "savol": "Har daqiqa boylikdir, uni .... o'tqazma",
                "javob": "behuda"
            },
            {
                "savol": "Chin do‘st — ko‘zingdagi quvonchni emas, yuragingdagi .... sezadi.",
                "javob": "og‘riqni"
            },
            {
                "savol": "Do'st tanlash ...., uni yuqotish xatodir.",
                "javob": "taqdir"
            },
            {
                "savol": "Do‘stlik — ikki tanada yashovchi bitta ....dir.",
                "javob": "qalb"
            },
            {
                "savol": "Do'st - ...., dushman soyadir.",
                "javob": "oyna"
            },
            {
                "savol": "Do'st bo'lishdan oldin, .... bo'lishni o'rgan.",
                "javob": "do'st"
            },
            {
                "savol": "Do‘stni boylikda emas, qiyinchilikda .... kerak.",
                "javob": "sinash"
            },
            {
                "savol": "Chin .... og'ir kuningda bilinadi",
                "javob": "do'st"
            },
            {
                "savol": "Do‘stlikning ildizi — ishonch, dushmanlikning ildizi — ....dir.",
                "javob": "hasad"
            },
            {
                "savol": "Do‘st seni ko‘taradi, dushman esa seni .... istaydi.",
                "javob": "yiqitishni"
            },
            {
                "savol": "Yaxshi do'st - ...., yomon do'st - sinov",
                "javob": "taqdir"
            },
            {
                "savol": "Ilm — insonning eng katta boyligi, uni hech kim .... olmaydi.",
                "javob": "o‘g‘irlay"
            },
            {
                "savol": "O'qish insonni .... qiladi",
                "javob": "inson"
            },
            {
                "savol": "Har bir .... - yangi bilim sari yo'l",
                "javob": "savol"
            },
            {
                "savol": "Ilmsiz kuch — ko‘r odamning qo‘lidagi .... kabidir.",
                "javob": "qurol"
            },
            {
                "savol": "Kim ilmni amal qilmasa, u faqat yuk ortgan .... kabidir.",
                "javob": "eshak"
            },
            {
                "savol": "Bilim egasi - mol dunyo egasidan ....",
                "javob": "boyroq"
            },
            {
                "savol": "Ilm eshikni ochadi, amal esa uni .... qiladi.",
                "javob": "mustahkam"
            },
            {
                "savol": "Ko‘p bilgan emas, bilganini to‘g‘ri ishlata olgan odam .... hisoblanadi.",
                "javob": "dono"
            },
            {
                "savol": ".... ajratgan har bir lahza qadirlidir.",
                "javob": "o'qishga"
            },
            {
                "savol": ".... olish - dunyoga va oxiratga foyda.",
                "javob": ""
            },
            {
                "savol": "Erkak — oilaning suyanchi, ayol esa uning ....dir.",
                "javob": "qalbi"
            },
            {
                "savol": "Ayol - gul, erkak - ....",
                "javob": "bog'bon"
            },
            {
                "savol": "Erkakning kuchi mehnatda, ayolning kuchi ....da",
                "javob": "tarbiya"
            },
            {
                "savol": "Ayolga bergan .... - o'zinga qaytadi.",
                "javob": "hurmat"
            },
            {
                "savol": "Erkakning sharafi — halollikda, ayolning sharafi ....",
                "javob": "iffatda"
            },
            {
                "savol": "Erkak sabr qilsa — oilani asraydi, ayol sabr qilsa — butun ....ni asraydi.",
                "javob": "nasl"
            },
            {
                "savol": "Ayolning ko‘z yoshlari — erkakning haqiqiy ....dir.",
                "javob": "imtihoni"
            },
            {
                "savol": "Erkak ayolni qadrlasa, oilasi .... bo‘ladi.",
                "javob": "mustahkam"
            },
            {
                "savol": "Ayol erining soyasi, erkak esa ayolning ....dir.",
                "javob": "tayanchi"
            },
            {
                "savol": "Ayol - uy bekasi, erkak uy ....",
                "javob": "egasi"
            },
            {
                "savol": "Yoshlik — daraxtning gullashi, qarilik esa uning ....dir.",
                "javob": "mevasi"
            },
            {
                "savol": "Yoshlikda o‘rganmagan ilm, qarilikda eng og‘ir .... bo‘ladi.",
                "javob": "hasrat"
            },
            {
                "savol": "Yoshlik — imkoniyat davri, qarilik esa qilgan ishlarning ....dir.",
                "javob": "hisobi"
            },
            {
                "savol": "Yoshlik .... bilan, qarilik ularni tushunish bilan o'tadi.",
                "javob": "xatolar"
            },
            {
                "savol": ".... — yoshlikning soyasi, yoshlikning qadri esa ....da bilinadi.",
                "javob": "qarilik"
            }
        ]

        maqol_10 = [
            {
                "savol": "Yoshlikda olingan bilim, .... o'yilgan naqshdir.",
                "javob": "toshga"
            },
            {
                "savol": ".... tez o'tadi, qadrini bilgan yutadi.",
                "javob": "yoshlik"
            },
            {
                "savol": "Yoshlikdagi dangasalik, qarilikdagi eng og‘ir ....dir.",
                "javob": "pushaymon"
            },
            {
                "savol": "Qarilik — yoshlikning oynasi, yoshlik qanday o‘tsa, qarilik shunday .... beradi.",
                "javob": "javob"
            },
            {
                "savol": "Yoshlik — kuch-quvvat, qarilik esa hayotdan olingan eng katta ....dir.",
                "javob": "hikmat"
            },
            {
                "savol": "Hayot — nafas olishda emas, balki  bilan yashashdadur.",
                "javob": "maqsad"
            },
            {
                "savol": "Hayot yo‘li tekis emas, ammo sabr qilgan odam har qanday ....ni yengadi.",
                "javob": "to‘siq"
            },
            {
                "savol": "Hayot seni sinaydi, ammo sinov ortida doim bir .... bor.",
                "javob": "hikmat"
            },
            {
                "savol": "Hayot — manzilgacha bo'lgan notekis yo'l, asl manzil esa ....dir.",
                "javob": "oxirat"
            },
            {
                "savol": "Hayotning har kuni - bu yangi ....",
                "javob": "sahifa"
            },
            {
                "savol": "Ishonch — har qanday munosabatning ....dir.",
                "javob": "ustuni"
            },
            {
                "savol": "Do‘stlikning ildizi — ishonch, muhabbatning ildizi esa ....dir.",
                "javob": "sadoqat"
            },
            {
                "savol": "Chin muhabbat - ishonch bilan yashaydi, .... bilan o'ladi.",
                "javob": "shubha"
            },
            {
                "savol": "Ishonchni tiklash, uni yo‘qotishdan ko'ra ....dir",
                "javob": "qiyin"
            },
            {
                "savol": "Har xiyonat - bir saboq, har ishonch - bir ....dir",
                "javob": "sinov"
            },
            {
                "savol": "Xiyonat — yurakdagi eng chuqur ....dir.",
                "javob": "yaradir"
            },
            {
                "savol": "Dushmaning qilgan zarbasidan ko‘ra, do‘stning xiyonati ko‘proq .... beradi.",
                "javob": "og‘riq"
            },
            {
                "savol": ".... yillar davomida quriladi, bir lahzada buziladi.",
                "javob": "ishonch"
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
                "savol": "Yomonlik urug'i tez unadi, lekin mevasi .... bo'ladi",
                "javob": "achchiq"
            },
            {
                "savol": "Yaxshi gap bilan .... inidan chiqarar, yomon gap bilan qilich qinidan",
                "javob": "ilon"
            },
            {
                "savol": ".... qilgan odamning yuzida doim nur porlaydi.",
                "javob": "yaxshilik"
            },
            {
                "savol": "Yaxshilikning ildizi — halollik, mevasi esa ....dir.",
                "javob": "baxt"
            },
            {
                "savol": "Birgina yaxshilik yuzlab ....ni yopadi.",
                "javob": "yomonlik"
            },
            {
                "savol": "Yaxshi insonning soyasi ham odamga .... beradi.",
                "javob": "orom"
            },
            {
                "savol": "Yaxshilik qilgan qo‘l hech qachon .... qolmaydi.",
                "javob": "bo‘sh"
            },
            {
                "savol": "Yaxshilik — qalbning eng go‘zal ....dir.",
                "javob": "ziynati"
            },
            {
                "savol": "Yaxshi so‘z — yaraga .... bo‘ladi.",
                "javob": "malham"
            },
            {
                "savol": "Yaxshilik qilgan odam oxirida faqat .... yig‘adi.",
                "javob": "baxtdan"
            },
            {
                "savol": "O‘rgatish — yodlatish emas, balki qalbga .... solishdir.",
                "javob": "nur"
            },
            {
                "savol": "O‘rgatgan ustoz, farzandga ikkinchi ....dir",
                "javob": "ota"
            },
            {
                "savol": "Haqiqiy o‘rgatish — til bilan emas, eng avvalo .... bilan bo‘ladi.",
                "javob": "amal"
            },
            {
                "savol": "Kimki boshqaga ilm o‘rgatsa, uning savobi .... bo‘ladi.",
                "javob": "abadiy"
            },
            {
                "savol": "O'rgatish - ilmni .... qilishdir",
                "javob": "sadaqa"
            },
            {
                "savol": "O'rgatish - yurakdan yurakka .... o'tqazishdir",
                "javob": "nur"
            },
            {
                "savol": ".... ko'rsatgan yo'l - eng to'g'ri yo'ldir.",
                "javob": "ustoz"
            },
            {
                "savol": "O'rganish - umr bo'yi davom etadigan ....",
                "javob": "yo'l"
            },
            {
                "savol": ".... bilib  - ustunsiz bina.",
                "javob": "ustozsiz"
            },
            {
                "savol": "O'rgatgan bilan bahs qilma - tingla va ....",
                "javob": "angla"
            }
        ]

           
        lvl_1 = random.choice(maqol_1),
        lvl_2 = random.choice(maqol_2),
        lvl_3 = random.choice(maqol_3),
        lvl_4 = random.choice(maqol_4),
        lvl_5 = random.choice(maqol_5),
        lvl_6 = random.choice(maqol_6),
        lvl_7 = random.choice(maqol_7),
        lvl_8 = random.choice(maqol_8),
        lvl_9 = random.choice(maqol_9),
        lvl_10 = random.choice(maqol_10),


        return Response(tecnology) 