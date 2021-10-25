FROM amancevice/pandas:1.3.4-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
COPY tweets.jsonl tweets.jsonl
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]