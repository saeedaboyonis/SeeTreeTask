FROM python:3.8.5
COPY templates /templates/
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY main.py .
EXPOSE 5000
CMD python main.py
