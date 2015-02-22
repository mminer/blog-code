FROM python:3.4-onbuild

# Create new user to keep Celery from complaining about being run as root.
RUN groupadd -r celery && useradd -r -g celery celery
USER celery

CMD ["celery", "-A", "worker:app", "worker", "--loglevel=INFO"]
