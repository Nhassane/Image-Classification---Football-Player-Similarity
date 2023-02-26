from flask import Flask, request, jsonify, render_template, make_response
import util
import json

app = Flask (__name__)

@app.route('/classify_image', methods =['POST', 'GET'])
def classify_image():
    if request.method == 'POST':
        request_data = request.form
        image_data = request_data.get('image_data')
        response = util.classify_image(image_base64_data=image_data)
        response = make_response(json.dumps(response))
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200
    else:
        return render_template('index.html')
     
if __name__ == '__main__':
    util.load_saved_artifacts()
    app.run(port=5000, debug=True)
       