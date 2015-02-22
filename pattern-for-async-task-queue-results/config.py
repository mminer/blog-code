import os

DEBUG = True

NOTIFIER_HOST = os.environ.get('NOTIFIER_PORT_3000_TCP_ADDR', 'localhost')
NOTIFIER_PORT = int(os.environ.get('NOTIFIER_PORT_3000_TCP_PORT', 3000))

RABBITMQ_HOST = os.environ.get('RABBITMQ_PORT_5672_TCP_ADDR', 'localhost')
RABBITMQ_PORT = int(os.environ.get('RABBITMQ_PORT_5672_TCP_HOST', 5672))
