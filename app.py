from flask import Flask, request, render_template
from PIL import Image
from array import array

from inference import get_Prediction
import io
app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html', value='hi')
    if request.method == 'POST':
        text = request.form['text']
        processed_text = text.upper()
        print(processed_text)
        sequence = get_Prediction(processed_text)
        print(sequence)
        return render_template('result.html',  Sequence=sequence,)

if __name__ == '__main__':
    app.run(debug=True)