FROM python:3.6-stretch
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5005
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
