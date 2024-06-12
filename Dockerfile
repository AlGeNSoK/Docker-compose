FROM python

WORKDIR /application

COPY ./stocks_products /application

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000
