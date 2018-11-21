import os
from flask import Flask, request, redirect, url_for,send_from_directory, render_template


UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['rb'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file'))
    return render_template('index.html', titre="Submit")
@app.route('/done')
def uploaded_file():
    return render_template('results.html', titre='Results')


if __name__ == '__main__':
    app.run(debug=True)

