from flask import Flask, render_template, request,redirect
import os
 
items =[]
app = Flask(__name__)
 
@app.route('/foo/<name>')
def foo(name):
    return render_template('form.html', to=name,items=items)

    

@app.route('/add_todo')
def add_todo():
    item =request.args.get('item')
    items.append(item)
    return redirect("/foo/sarah", code=302)



if __name__ == '__main__':
    port=os.environ.get('PORT', 5000)
    app.run(debug=True, host='0.0.0.0', port=port)
