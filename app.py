from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
	a = random.randint(1,4)
	return "Number: " + str(a)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
