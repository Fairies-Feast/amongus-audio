Flask = __import__("flask").Flask
render_template = __import__("flask").render_template

app = Flask('app')
playAudio = False


@app.route('/')
def hello_world():
  return render_template('play.html')


@app.route('/status')
def getStatus():
  return str(playAudio)
@app.route("/toggle")
def toggleAudio():
  global playAudio
  playAudio = not playAudio
  return "OK"

app.run(host='0.0.0.0', port=8080)
