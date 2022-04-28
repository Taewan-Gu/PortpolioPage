FROM python:3.8
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 3006
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3006"]