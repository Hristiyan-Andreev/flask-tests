from flask import render_template, Flask, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__)
app.secret_key = 'example'

class OurForm(FlaskForm):
    foo = StringField('foo')

@app.route('/')
def index():
	form = OurForm()
	return render_template('multipleajax.html', form=form)
	#return render_template('ajax.html', form=form)

@app.route('/form/', methods=['post'])
def form1():
	form = OurForm()
	if form.validate_on_submit():
		return jsonify(data={'message': 'hello {}'.format(form.foo.data)})
	return jsonify(data=form.errors)

	
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')