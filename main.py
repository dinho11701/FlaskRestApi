from flask import Flask

# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



app = Flask(__name__)

#@app.route('/')
#def index():
#    return "Hello World hohoho!"

if __name__ == '__main__':
    app.run(debug=True)
    print("hellos")

