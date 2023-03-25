To make a method an API method, we need to use `@app.route()`
<pre>@app.route('/getStudent', methods=['GET','POST'])</pre>
<br/>
The html file should come under <code>template</code> folder.
To call the html file from the method, we need to use
<pre>render_template('index.html')</pre>
To send any information to the html file, we need to use <code>name</code> attribute.
<pre>render_template('homepage.html',username="Ahamed")</pre>
In html file, we use to use this <code>username</code> with double curly braces
<pre>Hello {{username}}!</pre>
To get to know the current API method whether GET, POST, PUT, DELETE, we need to use:
<pre>if request.method == 'POST':</pre>