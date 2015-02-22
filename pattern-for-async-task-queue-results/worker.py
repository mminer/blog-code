import time
import requests
from celery import Celery, Task
from config import NOTIFIER_HOST, NOTIFIER_PORT, RABBITMQ_HOST, RABBITMQ_PORT


class NotifierTask(Task):
    """Task that sends notification on completion."""
    abstract = True

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        url = 'http://{}:{}/notify'.format(NOTIFIER_HOST, NOTIFIER_PORT)
        data = {'clientid': kwargs['clientid'], 'result': retval}
        requests.post(url, data=data)


broker = 'amqp://{}:{}'.format(RABBITMQ_HOST, RABBITMQ_PORT)
app = Celery(__name__, broker=broker)


@app.task(base=NotifierTask)
def mytask(clientid=None):
    """Simulates some slow computation."""
    time.sleep(5)
    return 42
