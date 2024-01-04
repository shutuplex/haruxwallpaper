from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "On message Haru"

images = [
  "https://telegra.ph//file/77cdd70b8e5257f362db1.jpg",
  "https://telegra.ph//file/d61fee11d1493b2f044c6.jpg",
  "https://telegra.ph//file/373783e44da189c586c2b.jpg",
  "https://telegra.ph//file/2a468cdccfc932d8e9378.jpg",
  "https://telegra.ph//file/19b203615171543da0002.jpg",
  "https://telegra.ph//file/54f2930cd345de8f20578.jpg",
  "https://telegra.ph//file/429d58fa92ccf9ee27da1.jpg",
  "https://telegra.ph//file/39b4f28097a0e6dc6e21c.jpg"
    
]

@app.route('/random_image', methods=['GET'])
def random_image():
    return jsonify({'image_url': random.choice(images)})

if __name__ == '__main__':
    app.run(debug=True)
