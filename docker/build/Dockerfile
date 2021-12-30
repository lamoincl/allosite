FROM python:3.8-alpine
WORKDIR /usr/src/app/
COPY entrypoint.sh /usr/src/app/
WORKDIR /app
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
