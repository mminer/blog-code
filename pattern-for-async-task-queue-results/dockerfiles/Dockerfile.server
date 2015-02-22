FROM python:3.4-onbuild
EXPOSE 5000
CMD ["gunicorn", "--bind=0.0.0.0:5000", "server:app"]
