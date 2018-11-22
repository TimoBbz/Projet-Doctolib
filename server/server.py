import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template


UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['rb'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


name = ""
first_name = ""


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global name
    global first_name
    if request.method == 'POST':
        name = request.form['name']
        first_name = request.form['firstname']
        file = request.files['file']
        print("file : ", file.filename)
        if file and allowed_file(file.filename):
            filename = name+first_name+".rb"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("file saved")
            return redirect(url_for('upload_test_file'))
    return render_template('index.html', titre="Submit")


@app.route('/almostdone', methods=['GET', 'POST'])
def upload_test_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = name+first_name+"Test.rb"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("test file saved")
            return redirect(url_for('uploaded_file'))
    return render_template('test.html', titre="Submit")


@app.route('/done')
def uploaded_file():
    return render_template('graph.html', titre='Results')


if __name__ == '__main__':
    app.run(debug=True)
