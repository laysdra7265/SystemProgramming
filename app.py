import os

from flask import Flask, request, redirect, url_for, \
    render_template, flash, Markup

import processlib.Tools as Tools
from processlib.Parser import Parser
from processlib.Scanner import Scanner

basedir = os.path.abspath(os.path.dirname(__file__))

# configuration
DEBUG = True
SECRET_KEY = 'mkz75asklLd8wdA9'
# create app
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/parse', methods=['POST'])
def add_entry():
    c0_code = request.form['text']
    try:
        flash(c0_code, 'editor')
        parser = Parser(Scanner(c0_code))
        parser_res = Tools.TreeTools.dump_html_code(parser.parsed_tree)
        flash(Markup(parser_res),'output')
    except RuntimeError as e:
        flash(Markup(Tools.dump_to_html(str(e))), 'output')
    finally:
        return redirect(url_for('index'))


if __name__ == '__main__':
    # Remote Debug
    app.run(host='0.0.0.0',port=5000)