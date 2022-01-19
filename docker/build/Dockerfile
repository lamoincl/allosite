FROM python:3.8-alpine
RUN apk add -U tzdata && cp /usr/share/zoneinfo/Europe/Paris /etc/localtime
WORKDIR /usr/src/app/
COPY entrypoint.sh /usr/src/app/
WORKDIR /app
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
CMD ["gunicorn", "--bind", "-w", "3", "0.0.0.0:5000", "app:app"]
