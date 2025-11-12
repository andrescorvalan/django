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

RUN mkdir /scripts
COPY runserver.sh /scripts/runserver.sh
RUN chmod +x /scripts/runserver.sh

CMD ["/scripts/runserver.sh"]