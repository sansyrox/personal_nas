import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = '/Users/ssanskar/Desktop/server_interface/server-back-end'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# how check if the subsequence exits in a file or check no dots in the file
ALLOWED_EXTENSIONS = ['.txt', '.pdf', '.png', '.jpg', '.jpeg', '.gif', '.zip', '.rar', '.7zip', '.dir']

# def allowedfiles()

@app.route('/')
def return_main():
	return "Hello World"


@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		if 'file' not in request.files:
			resp = {"Upload UnSuccessfull":"No file Present"}
			resp = jsonify(resp)
			resp.status_code = 400
			return resp
		file = request.files['file']
			# if user does not select file, browser also
			# submit a empty part without filename

		if file.filename == '':
			resp = {"Upload UnSuccessfull":"File Name not clear"}
			resp = jsonify(resp)
			resp.status_code = 400
			return resp
		f = request.files['file']
		file_name =secure_filename(f.filename)
		# check if file is allowed or not
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
		resp = {"Upload Successfull":f.filename}
		resp = jsonify(resp)
		resp.status_code = 200
		return resp

if __name__ == '__main__':
    app.run(debug=False,port=5000,host= '0.0.0.0')

