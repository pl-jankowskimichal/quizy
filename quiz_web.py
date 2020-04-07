# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, flash

app = Flask(__name__)

app.config.update(dict(SECRET_KEY="secretkey"))


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

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        punkty = 0
        odpowiedzi = request.form
        for wskaznik, odp in odpowiedzi.items():
            if odp == zagadki[int(wskaznik)]['poprawna_odp']:
                punkty += 1
        flash('Liczba poprawnych odpowiedzi, to: {0}'.format(punkty))
        return redirect(url_for('index'))

    return render_template("index.html", zagadki=zagadki)

if __name__ == "__main__":
    app.run(debug=True)
