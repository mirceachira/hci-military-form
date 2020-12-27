# hci-military-form
University project for HCI class - Military survery form

### How to setup this project

You need python 3

If you use WSL (or any linux):
```
source env3/bin/activate

```

After activating the virtual env, install Django in it ( pip3 install Django )

### How to run this project to make sure that it works

In the project folder:
```
You have to create a superuser to log into admin
python manage.py createsuperuser


python manage.py runserver
```

Now go to http://localhost:8000/admin and you should see the admin page.

### Things left to do / improve

Translating stuff and adding instructions:
* Chestionar in loc de survey
* Raspunsuri in loc de ce ii acolo in admin
* Explicatii in romana la campuri
* Tradus toata interfata django admin (exista niste configuratii)

De facut frumos:
* retusat templat-urile
* retusat interfata de admin (titlu, logo, etc.)

De fixat / imbunatatit:
* Mai multe tipuri de intrebari
* *validari* - momentan nu validam varsta ci doar validam numere intregi (vezi pr Andreea unde a implementat asta inainte https://github.com/mirceachira/hci-military-form/pull/1 )
