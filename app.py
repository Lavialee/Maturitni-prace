    <span class="hljs-keyword">from</span> flask <span class="hljs-keyword">import</span> Flask, render_template, request, jsonify, make_response, json
    <span class="hljs-keyword">from</span> pusher <span class="hljs-keyword">import</span> pusher

    app = Flask(__name__)

    pusher = pusher_client = pusher.Pusher(
      app_id=<span class="hljs-string">'1124121'</span>,
      key=<span class="hljs-string">'f98348521f3f514f3091'</span>,
      secret=<span class="hljs-string">'c732fe64eec3ac0897d6'</span>,
      cluster=<span class="hljs-string">'eu'</span>,
      ssl=<span class="hljs-keyword">True</span>
    )

    name = <span class="hljs-string">''</span>

<span class="hljs-meta">    @app.route('/')</span> #definuje základní doménu
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">index</span><span class="hljs-params">()</span>:</span>
      <span class="hljs-keyword">return</span> render_template(<span class="hljs-string">'index.html'</span>)

<span class="hljs-meta">    @app.route('/play')</span> #definuje doménu /play
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">play</span><span class="hljs-params">()</span>:</span>
      <span class="hljs-keyword">global</span> name
      name = request.args.get(<span class="hljs-string">'username'</span>) 
      <span class="hljs-keyword">return</span> render_template(<span class="hljs-string">'play.html'</span>)

<span class="hljs-meta">    @app.route("/pusher/auth", methods=['POST'])</span> #autorizuje pusher
    <span class="hljs-function"><span class="hljs-keyword">def</span> <span class="hljs-title">pusher_authentication</span><span class="hljs-params">()</span>:</span>
      auth = pusher.authenticate(
        channel=request.form[<span class="hljs-string">'channel_name'</span>],
        socket_id=request.form[<span class="hljs-string">'socket_id'</span>],
        custom_data={
          <span class="hljs-string">u'user_id'</span>: name,
          <span class="hljs-string">u'user_info'</span>: {
            <span class="hljs-string">u'role'</span>: <span class="hljs-string">u'player'</span>
          }
        }
      )
      <span class="hljs-keyword">return</span> json.dumps(auth)

    <span class="hljs-keyword">if</span> __name__ == <span class="hljs-string">'__main__'</span>:
        app.run(host=<span class="hljs-string">'0.0.0.0'</span>, port=<span class="hljs-number">5000</span>, debug=<span class="hljs-keyword">True</span>)

    name = <span class="hljs-string">''</span>
