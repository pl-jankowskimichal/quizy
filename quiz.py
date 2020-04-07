zagadki = [
{
    "pytanie":"Kto jest premierem Polski?",
    "odpowiedzi":["Morawiecki","Kaczyński","Duda"],
    "poprawna_odp":"Morawiecki",
},
{
    "pytanie":"Ile złotych piłek dostał Ronaldo?",
    "odpowiedzi":["3","5","8"],
    "poprawna_odp":"5",
},
]
def pobierz_odp(odpowiedzi):
    for odp in odpowiedzi:
        print(odp)
    while True:
        proba=input()
        if proba in odpowiedzi:
            break; # wyjdź z pętli
        else:
            print("Podaj odp z listy:", odpowiedzi)
    return proba
def quiz(zagadki):
    punkty = 0
    maksymalne_punkty = len(zagadki)
    for zagadka in zagadki:
        print(zagadka["pytanie"])
        proba = pobierz_odp(zagadka["odpowiedzi"])
        if proba == zagadka["poprawna_odp"]:
            punkty += 1
    print("Zdobyłeś: ", punkty, "/",maksymalne_punkty, "! Gratulacje!")

quiz(zagadki)
