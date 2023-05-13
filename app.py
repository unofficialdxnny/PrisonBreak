from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def prison_breaks():
    url = 'https://api.publicapis.org/entries'
    response = requests.get(url)
    data = response.json()
    prison_breaks = []
    for entry in data['entries']:
        if 'Prison' in entry['API']:
            prison_break = {}
            prison_break['date'] = entry['Description']
            prison_break['country'] = entry['Link']
            prison_break['prison_name'] = entry['API']
            prison_break['escapees'] = entry['Auth']
            prison_break['details'] = entry['Category']
            prison_breaks.append(prison_break)
    return render_template('prison_breaks.html', prison_breaks=prison_breaks)

if __name__ == '__main__':
    app.run(debug=True)
