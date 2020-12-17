from flask import Flask, render_template, request, jsonify, make_response, json
from pusher import pusher

app = Flask(__name__)

pusher = pusher_client = pusher.Pusher( #definuje jaký pusher používáme
  app_id='1124121',
  key='f98348521f3f514f3091',
  secret='c732fe64eec3ac0897d6',
  cluster='eu',   
  ssl=True
)

name = ''

@app.route('/') #výchozí url je index -> zadání jména
def index():
  return render_template('index.html')

@app.route('/opponent') #přesměruje 
def play():
  global name
  name = request.args.get('username')
  return render_template('opponent.html')

@app.route("/pusher/auth", methods=['POST']) #get custom data z pusheru
def pusher_authentication():
  auth = pusher.authenticate(
    channel=request.form['channel_name'],
    socket_id=request.form['socket_id'],
    custom_data={
      u'user_id': name,
      u'user_info': {
        u'role': u'player'
      }
    }
  )
  return json.dumps(auth)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

name = ''
