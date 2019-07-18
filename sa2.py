from flask import Flask,render_template,request
 
app = Flask(__name__)

@app.route('/add_todos')
def todo():
    
    return render_template('form.html')
  
@app.route('/add_todo')
def add_todo():
    item=request.args.get('item')
    return item
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')