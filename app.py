from flask import Flask, render_template, request, redirect, url_for, session
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array,load_img
from PIL import Image
import numpy as np
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-default")

UPLOAD_FOLDER = os.path.join('static', 'forms', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


model3 = load_model("model222_poultry_r50.h5")
CLASS_NAMES = ['Coccidiosis', 'Healthy', 'New Castle Disease', 'Salmonella']

USERS = {
    "admin": ["nikhilsrimanth@gmail.com","password123"]
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        passwd = request.form['password']
        if uname in USERS and USERS[uname][1] == passwd:
            session['user'] = uname
            return redirect(url_for('index'))
        return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')
@app.route("/signup",methods=['POST'])
def signup():
    a = request.form['username']
    b = request.form['email']
    c = request.form['password']
    USERS[a] = [b,c]
    return redirect(url_for("index"))


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'user' not in session:
        return redirect(url_for('login'))

    if 'file' not in request.files or request.files['file'].filename == '':
        return render_template('index.html', result="No file selected", show_predict=True)

    file = request.files['file']
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    img = load_img(file_path,target_size=(224, 224))
    x = img_to_array(img)
    img_array = np.expand_dims(x, axis=0)


    predictions3 = model3.predict(img_array,verbose=0)

    print(predictions3)
    predicted_index3 = np.argmax(predictions3)
    
    predicted_label3 = CLASS_NAMES[predicted_index3]

    confidence3 = predictions3[0][predicted_index3]*100
    file_url = url_for('static', filename=f'forms/uploads/{filename}')

    return render_template('index.html',
                           result=predicted_label3,
                           confidence=confidence3,
                           image_url=file_url,
                           show_predict=True)


if __name__ == '__main__':
    app.run(debug=True)
