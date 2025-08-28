from rest_framework.views import APIView
from rest_framework.response import Response
import random


class CrosswordAPI(APIView):
    def get(self, request):
lvl_1 = {
    "question": "U to'xtamasdan yuradi, ammo ",
    "answer": "vaqt"
}

lvl_2 = {
    "question": "Har bir odamda bor, lekin hech kim bir xil emas. Bu nima?",
    "answer": "mijoz"
}

lvl_3 = {
    "question": "Bor kuchingni sarflab, u senga kuch beradi. Bu nima?",
    "answer": "sport"
}

lvl_4 = {
    "question": "Senda bo‘lishi yaxshi, ko‘pchilik undan mahrum. Bu nima?",
    "answer": "aqil"
}

lvl_5 = {
    "question": "Yengil, og‘ir emas, ammo hammani bosib o‘tadi. Bu nima?",
    "answer": "fikr"
}

lvl_6 = {
    "question": "Uchmasang yetolmaysan, lekin qanoting yo‘q. Bu nima?",
    "answer": "orzu"
}

lvl_7 = {
    "question": "U qancha ko‘p bo‘lsa, shuncha kam ko‘rinadi. Bu nima?",
    "answer": "bilim"
}

lvl_8 = {
    "question": "Bo‘linmasin deyilgan, ammo ko‘p joyda bo‘linadi. Bu nima?",
    "answer": "nol"
}

lvl_9 = {
    "question": "Odamni gapirtiradi, lekin o‘zi jim. Bu nima?",
    "answer": "savol"
}

lvl_10 = {
    "question": "Sen uni topsang, yo‘qoladi. Bu nima?",
    "answer": "yoqotish"
}

lvl_11 = {
    "question": "U ko‘p narsa aytadi, lekin faqat kuzatuvchi. Bu nima?",
    "answer": "statistika"
}

lvl_12 = {
    "question": "Har kuni o‘zgaradi, lekin hech kim uni boshqara olmaydi. Bu nima?",
    "answer": "ob-havo"
}

lvl_13 = {
    "question": "Har bir kompyuterda bor, lekin yurak emas. Bu nima?",
    "answer": "protsessor"
}

lvl_14 = {
    "question": "Uch harfli so‘z, ammo millionlarni boshqaradi. Bu nima?",
    "answer": "pul"
}

lvl_15 = {
    "question": "Ko‘rib bo‘lmaydi, ammo tushuniladi. Bu nima?",
    "answer": "hissiyot"
}

lvl_16 = {
    "question": "Teskari o‘qilsa ham o‘zgaramaydi. Bu qanday so‘z?",
    "answer": "level"
}

lvl_17 = {
    "question": "Eng baland narsa emas, ammo hamma unga chiqishga harakat qiladi. Bu nima?",
    "answer": "marta"
}

lvl_18 = {
    "question": "O‘qish bilan ko‘p bo‘ladi, yozish bilan kam. Bu nima?",
    "answer": "suhbat"
}

lvl_19 = {
    "question": "Har kuni gapiriladi, ammo faqat jimlikda eshitiladi. Bu nima?",
    "answer": "fikr"
}

lvl_20 = {
    "question": "Qanchalik bo‘lishsang, shunchalik ko‘payadi. Bu nima?",
    "answer": "ilm"
}

        return Response(name) 