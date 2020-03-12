import os
from flask import Flask, request, render_template, send_from_directory #, url_for, redirect

app = Flask(__name__)

@app.route("/")
def fileFrontPage():
    return render_template('fileform.html')

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'files[]' in request.files:
        file = request.files['files[]']
        if file.filename != '':            
            file.save(os.path.join('/home/shawn/share/upload', file.filename))
    # return redirect(url_for('fileFrontPage'))
    return "File uploaded successfully!"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run()