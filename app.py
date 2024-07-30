from flask import Flask, render_template, jsonify

app = Flask(__name__)

EVENTS = [
    {
        'id': 1,
        'title': 'selection middle',
        'location': 'Zuppa',
        'date': '2025-07-24'
    },
    {
        'id': 2,
        'title': 'selection long',
        'location': 'Zuppa',
        'date': '2025-07-25'
    },
    {
        'id': 3,
        'title': 'ROB',
        'location': 'Szentes',
        #'date': '2025-09-20'
    }
]


@app.route("/")
def hello_world():
    #return "<p>Hello, World!</p>"
    return render_template('home.html', events=EVENTS)


@app.route("/api/events")
def list_events():
    return jsonify(EVENTS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
