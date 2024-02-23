# Use an official Python runtime as a parent image
FROM python:3.12.1-alpine

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required for Pipenv and compilation of specific Python packages
RUN apk add --no-cache --virtual .build-deps gcc libc-dev make libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev \
    && apk add --no-cache jpeg-dev zlib-dev postgresql-dev gcc python3-dev musl-dev    

# Install pipenv
RUN pip install --upgrade pip && \
    pip install pipenv

# Copy the Pipfile and Pipfile.lock into the container at /app
COPY Pipfile Pipfile.lock /app/

# Install project dependencies
RUN pipenv install --deploy --ignore-pipfile && \
    apk --purge del .build-deps

# Copy the rest of your application code
COPY . /app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Command to run the application
CMD ["pipenv", "run", "gunicorn", "isorrylol.wsgi:application", "--bind", "0.0.0.0:8000"]
