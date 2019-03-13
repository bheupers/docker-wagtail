# Docker Wagtail starter



Simple container to run wagtail.
- Python 3
- Wagtail:latest

### Usage

Clone this repo. If you have a wagtail project already, clone into the repo root eg ```./mysite```

If you are starting a new site:

Start the containers

``` docker-compose up -d```

SSH to the web container

``` docker exec -it [web container name] /bin/bash ```

Create app with wagtail@

``` wagtail start mysite```

Then proceed as per the wagtail docs:

##### Create the database
By default, this would create an SQLite database file within the project directory.

```python manage.py migrate```

##### Create an admin user #####

```python manage.py createsuperuser```

##### Run the development server

```python manage.py runserver 0.0.0.0:8000```

Your site is now accessible at 0.0.0.0:8000 (or watever ip your docker is set to), with the admin backend available at http://localhost:8000/admin/.

[Read more on the wagtail docs](http://docs.wagtail.io/en/v1.13.1/)

*you may need to run ```   sudo chown -R $USER:$USER . ``` if you create a wagtail project from within docker

##### Deploy on heroku with Docker

Install heroku command-line utility.

* heroku login
* heroku create

This will create a app with name : app_name
* cd  mysite

We will use the docker file in mysite directory
* heroku container:push web --app=[app_name]
* heroku container:release web --app=[app_name]
* heroku open --app=[app_name]

This is only for demo usage. It will use the SQLite3 database that was present when pushed. 
After every restart it will use that database version again.
