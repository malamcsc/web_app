from flask import Flask
#from waitress import serve

app = Flask(__name__)

@app.route('/')
def main():
  return 'Hello world Test app for github action'

# if __name__ == "__main__":
#     app.run(app, host="0.0.0.0", port=8080)

