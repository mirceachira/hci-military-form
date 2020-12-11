# hci-military-form
University project for HCI class - Military survery form

### How to setup this project

You need python 3

If you use WSL (or any linux):
```
source env3/bin/activate

After activating the virtual env, install Django in it ( pip3 install Django )
```

### How to run this project to make sure that it works

In the project folder:
```
You have to create a superuser to log into admin
python manage.py createsuperuser


python manage.py runserver
```

Now go to http://localhost:8000/admin and you should see the admin page.
