from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return 'Hello world'
 
@app.route('/whereami')
def whereami():
    return 'Ghana!'

@app.route('/whatdidyoueat')
def whatdidyoueat():
    return 'meat pie with drink!'

@app.route('/wherewillyougo')
def wherewillyougo():
    return 'amamoma!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')