FROM python:3.10
# crear un directorio de trabajo
WORKDIR /servidor
COPY servidor.py .
EXPOSE 5000
#  instala la dependencias necesarias
RUN pip install flask
# ejecutar al app
CMD [ "python2", "servidor.py" ]