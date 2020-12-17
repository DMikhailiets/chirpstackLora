**Chirpstack API:**

**_How to deploy:_**

* `cd chirpstack-docker`

* `docker-compose up -d`
* `cd ../`
* `python -m virtualenv venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* `python3 manage.py runserver`

Or, you can run it with **_gunicorn_** for production.