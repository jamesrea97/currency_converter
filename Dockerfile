FROM python:3.9

COPY ./src .

RUN pip install --no-cache-dir -r dependencies/development.txt

CMD [ "python", "main.py" ]