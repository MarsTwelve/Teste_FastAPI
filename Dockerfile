FROM python:3.10
WORKDIR /FastAPI
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "FastAPI:app", "--host", "0.0.0.0", "--port", "8080"]