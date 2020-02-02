FROM python:3

WORKDIR /app

COPY Pipfile* ./
RUN pip3 install --no-cache-dir pipenv && \
    pipenv install --system --deploy --clear

COPY . .

CMD [ "python3", "./app.py" ]