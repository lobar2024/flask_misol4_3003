from flask import Flask, render_template

app = Flask(__name__)

@app.route('/length')
def length_page():
    text = "Hello"
    return render_template('length.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)
