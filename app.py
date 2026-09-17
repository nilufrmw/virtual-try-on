import os
from flask import Flask, request, render_template, send_file
from gradio_client import Client, handle_file

app = Flask(__name__)
client = Client("yisol/IDM-VTON", token="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")

os.makedirs('uploads', exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tryon', methods=['POST'])
def tryon():
    person = request.files['person']
    garment = request.files['garment']

    person_path = 'uploads/person.png'
    garment_path = 'uploads/garment.png'

    person.save(person_path)
    garment.save(garment_path)

    result = client.predict(
        dict={"background": handle_file(person_path), "layers": [], "composite": None},
        garm_img=handle_file(garment_path),
        garment_des="garment",
        is_checked=True,
        is_checked_crop=False,
        denoise_steps=30,
        seed=42,
        api_name="/tryon"
    )

    return send_file(result[0], mimetype='image/png')

app.run(debug=True, port=5000)
