# official Python image as the base image
FROM python:3.8-slim

# referencing docker compose (find wiki) #
ENV PORT ${PORT}

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8060

# run dash application
CMD ["python3", "main.py"]