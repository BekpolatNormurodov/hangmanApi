# from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from .serializers import Hangmanserializer
# from api.models import Hangman
from rest_framework.views import APIView
from rest_framework.response import Response


# class HangmanApiView(ListAPIView):
#     queryset = Hangman.objects.all()
#     serializer_class = Hangmanserializer

# class HangmanApiCreate(ListCreateAPIView):
#     queryset = Hangman.objects.all()
#     serializer_class = Hangmanserializer

# class HangmanApiUpdate(RetrieveUpdateDestroyAPIView):
#     queryset = Hangman.objects.all()
#     serializer_class = Hangmanserializer

class HangmanApiView(APIView):
    def get(self, request):
        tecnology = ["Internet", "Kompyuter", "Klaviatura", "Monitor", "WiFi", "Printer", "Ekran", "Bluetooth", "Protsessor", "Kamera"]
        programming = ["Python", "Java", "C++", "JavaScript", "Dart", "Swift", "Go", "Kotlin", "Ruby", "PHP"]
        cities = ["Paris", "London", "Tokyo", "New York", "Rome", "Dubai", "Berlin", "Moscow", "Istanbul", "Seoul"]
        uzb_regions = ["Toshkent", "Namangan", "Samarqand", "Andijon", "Farg'ona", "Buxoro", "Xorazm", "Termiz", "Nukus", "Qarshi"]
        fruit = ["Olma", "Banan", "Uzum", "Anor", "Nok", "Gilos", "Shaftoli", "Apelsin", "Mandarin", "Kivi"]
        vegetables = ["Piyoz", "Sabzi", "Kartoshka", "Bodring", "Pamidor", "Qovoq", "Lavlagi", "Sarimsoq", "Brokkoli", "Baqlajon"]
        fans = ["Atom", "Molekula", "Energiya", "Zarratcha", "DNK", "Magnit", "Issiqlik", "Kuch", "Og'irlik", "Tezlik"]
        games = ["Shaxmat", "Dama", "Monopoliya", "Pubg", "Fortnite", "Ludo", "Mario", "Tetris", "Pacman", "Scrabble"]
        movies = ["Titanic", "Avatar", "Inception", "Joker", "Matrix", "Gladiator", "Frozen", "Interstellar", "Dangal", "Coco"]
        musics = ["Perfect", "Despacito", "Hello", "Roar", "SenKetma", "DemaDema", "Sayyod", "ShifoTopaman", "Levitating", "Shallow"]
        sports = ["Futbol", "Basketbol", "Tennis", "Boks", "Ronaldo", "Messi", "Neymar", "Federer", "Jordan", "Mbappe"]
        jobs = ["Shifokor", "Muallim", "Haydovchi", "Advokat", "Injener", "Dasturchi", "Tikuvchi", "Politsiyachi", "Quruvchi", "Oshpaz"]
        animals = ["Arslon", "Yo'lbars", "It", "Mushuk", "Fil", "Maymun", "Ayiq", "Tulki", "Bo'ri", "Quyon"]
        nature = ["Gul", "Tog'", "Daryo", "O'rmon", "Barg", "Qor", "Shamol", "Yomg'ir", "Quyosh", "Tabiat"]
        travel = ["Parij", "Dubay", "Istanbul", "Toshkent", "Maldiv", "Rim", "Seul", "London", "Tokio", "Samarqand"]
        books = ["Alkimyogar", "Zarra", "HarryPotter", "Ertaklar", "ShumBola", "Ufq", "Qorako'z", "Mehr", "Nodira", "Xamsa"]
        historiy = ["AmirTemur", "Napoleon", "Cleopatra", "Ulug'bek", "Bobur", "Lincoln", "Sezar", "So'g'diyon", "Urganch", "Afrosiyob"]
        cars = ["Malibu", "Nexia", "Cobalt", "Tesla", "BMW", "Mercedes", "Audi", "Ferrari", "Lada", "Chevrolet"]
        calendar = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba", "Yanvar", "Mart", "Dekabr"]
        colors = ["Qizil", "Ko'k", "Yashil", "Sariq", "Oq", "Qora", "To'q sariq", "Moviy", "Binafsha", "Pushti"]
        names = ["Jasur", "Diyor", "Zaynab", "Laylo", "Kamol", "Nodira", "Muhammad", "Aziz", "Dilshod", "Malika"]
        human_body = ["Bosh", "Qo'l", "Oyoq", "Yurak", "Ko'z", "Quloq", "Burni", "Tizza", "Barmoq", "Bel"]

        return Response(tecnology) 