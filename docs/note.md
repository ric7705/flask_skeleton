# note

## DB
put db connection string in the following file
/config/dev.py
/config/prod.py

### init DB

```
python manage.py
```

## run

local dev:
```
export FLASK_ENV=development
export FLASK_APP=mysite
flask run
```

production:
```
export FLASK_ENV=development
export FLASK_APP=mysite
flask run
```

supervisor:

```
gunicorn -b0.0.0.0:80 "mysite:create_app()
```
