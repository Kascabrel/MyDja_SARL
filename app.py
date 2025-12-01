from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Home page route"""
    return render_template('index.html', title='MyDja SARL')

@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html', title='About Us')

if __name__ == '__main__':
    app.run(debug=True)
