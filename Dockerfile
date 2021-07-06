FROM python:3

COPY simple_http_server.py .
COPY start_simple_http_server.sh .
COPY ssl ./ssl
CMD [ "sh", "./start_simple_http_server.sh" ]
