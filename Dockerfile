FROM python:3.8.1-slim
EXPOSE 8000
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENV PYTHONPATH /app
CMD ["uvicorn","--host","0.0.0.0","--port","8000","MLOps_Week3.main:app"]