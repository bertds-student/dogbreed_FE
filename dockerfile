# frontend/Dockerfile
FROM python:3.9
WORKDIR /code
COPY ./requirements.dev.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./main.py /code/main.py
EXPOSE 8501
CMD ["streamlit", "run", "main.py"]
