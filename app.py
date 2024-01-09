from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tropical')
def index():
    return render_template('tropical.html')

@app.route('/cold')
def index():
    return render_template('cold.html')

@app.route('/flowers')
def index():
    return render_template('flowers.html')
    
@app.route('/calculator')
def index():
    return render_template('calculator.html')

@app.route('/about')
def index():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()