FROM python

ENV PYTHONUNBUFFRED 1
ENV DJANGO_SETTINGS_MODULE "todoapp.settings"

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]