FROM python:3.12-bookworm

# AÑADIR 'sqlite3' aquí para que el binario esté disponible
RUN apt-get update && \ 
    apt-get install -y \
    python3-dev \
    libgdal-dev \
    graphviz \
    graphviz-dev \
    sqlite3

WORKDIR /usr/src/app

RUN pip install --upgrade pip && pip install --upgrade setuptools

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
