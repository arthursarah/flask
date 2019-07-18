from flask import Flask,render_template,request
import os
 
app = Flask(__name__)

@app.route('/add_todos')
def todo():
    
    return render_template('form.html')
  
@app.route('/add_todo')
def add_todo():
    item=request.args.get('item')
    return item
if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(debug=True, host='0.0.0.0',port=port)
