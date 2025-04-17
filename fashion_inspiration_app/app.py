from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '*************' 

def fetch_images(query):
    url = f'https://pixabay.com/api/?key={API_KEY}&q={query}&image_type=photo&pretty=true'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        images = [item['webformatURL'] for item in data['hits']] 
        return images
    else:
        return []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        color = request.form['color']
        style = request.form['style']
        occasion = request.form['occasion']
        search_query = f"{style} {occasion} fashion outfit {color}"
        images = fetch_images(search_query)

        return render_template('suggestions.html', images=images, suggestions=search_query)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5001)
