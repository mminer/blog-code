from urllib.parse import urlparse
from flask import Flask, render_template, request
from config import NOTIFIER_PORT
from worker import mytask


app = Flask(__name__, template_folder='.')


@app.route('/')
def index():
    hostname = urlparse(request.url).hostname
    notifier_url = 'http://{}:{}'.format(hostname, NOTIFIER_PORT)
    return render_template('index.html', notifier_url=notifier_url)


@app.route('/runtask', methods=['POST'])
def runtask():
    clientid = request.form.get('clientid')
    mytask.delay(clientid=clientid)
    return 'running task...', 202
