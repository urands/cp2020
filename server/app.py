from shared import app
from image import render_image
from flask import Response, render_template, send_from_directory, request

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('static/images', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory('static/fonts', path)

@app.route('/')
def index():
    start = request.args.get('start','2020-01-01')
    stop = request.args.get('stop', '2020-11-27')
    temp = request.args.get('temp', default='')
    invest = request.args.get('invest', default='')
    apart = request.args.get('apart', default='')
    return render_template('index.html', start = start, stop = stop, temp=temp, invest = invest, apart=apart)

@app.route('/p2')
def index2():
    start = request.args.get('start','2012-01-01')
    stop = request.args.get('stop', '2020-11-27')
    temp = request.args.get('temp', default='')
    invest = request.args.get('invest', default='')
    apart = request.args.get('apart', default='')
    return render_template('index2.html', start = start, stop = stop, temp=temp, invest = invest, apart=apart)

@app.route('/p3')
def index3():
    start = request.args.get('start','2020-01-01')
    stop = request.args.get('stop', '2020-11-27')
    temp = request.args.get('temp', default='')
    invest = request.args.get('invest', default='')
    apart = request.args.get('apart', default='')
    return render_template('index3.html', start = start, stop = stop, temp=temp, invest = invest, apart=apart)

@app.route('/plot.png')
def plot():
    output = render_image()
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)

