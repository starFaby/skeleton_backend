from app import createApp
PORT = 8000
DEBUG = True
app = createApp()

@app.errorhandler(404)
def noFound(error):
    return "Not Found"

@app.route('/')
def index():
    return "backend"


if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG)