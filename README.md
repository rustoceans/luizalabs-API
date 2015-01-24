# LuizaLabs API

This app is a test for selection process at Luiza Labs.

# Mission
The purpose was to create a API with default RESTful coming some datas of Facebook from a FACEBOOK ID. With FACEBOOK ID it's possible get some datas as follows:
```json
{
  "id": "1",
  "first_name": "test",
  "gender": "male",
  "last_name": "test",
  "locale": "pt_BR",
  "name": "test",
  "username": "test"
}
```

The API get a FACEBOOK ID and from her, we save all elements above and provides:

```json
{
  "username": "test",
  "name": "test",
  "facebook_id": "123",
  "gender": "male",
}
```

# Install Command Line
First, to continue this installation tutorial you need install some dependencies. If you have all installed, ignore it.

In your shell, run:
```sh
~$ sudo apt-get install python-setuptools python-dev build-essential
~$ sudo easy_install pip
~$ sudo pip install virtualenv
```

All right, we are ready! :smirk:

_____
Make the download of luizalabs-alexsander.tar.gz tarball file.

To run, extract all files of tarball file with:
```sh
~$ tar -xzf luizalabs-alexsander.tar.gz
```
Or, right click on the luizalabs-test.tar.gz file and select the extract here option from the drop-down menu, and it will be extracted on the same folder as the compressed file.

Create a new folder to create a virtual machine.
```sh
~$ mkdir luizalabs-alexsander && cd luizalabs-alexsander && virtualenv vm && cd vm
```

Copy and paste the project to current folder /vm/:
```sh
~/luizalabs/vm$ cp -a ~/alexsander/. ~/luizalabs-alexsander/vm/
```
Activate the virtual machine:
```sh
~/luizalabs/vm$ source bin/activate
```
Install all requirements:
```sh
~/luizalabs/vm$ pip install -r requirements.txt
```
Synchronize your database:
```sh
~/luizalabs/vm$ python manage.py syncdb
```

And run it!
```sh
~/luizalabs/vm$ python manage.py runserver
```

Example
-------

You can see this examples for get the respective responses.

Insert data:
```vim
$ curl -X POST -F facebook_id=[Facebook ID] http://localhost:8000/api/person/
/* Status code response: 201 */
```

List data(s):
```vim
$ curl http://localhost:8000/api/person/
/* Status code response: 200 */
```

Response data:
```json
{
  "count": 16,
  "next": "http://localhost:8000/api/person/&page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "username": "username",
      "name": "name",
      "facebook_id": "number",
      "gender": "male"
    }
  ]
}
```

List with limit data:
```vim
$ curl http://localhost:8000/api/person/?limit=1
/* Status code response: 200 */
```

Or list for page, so on:
```vim
$ curl http://localhost:8000/api/person/?page=1
/* Status code response: 200 */
```

Delete data:
```vim
$ curl -X DELETE http://localhost:8000/api/person/[Facebook ID]/
/* Status code response: 204 */
```

**See You!**


## License

Copyright (C) 2015 Alexsander Falcucci

MIT.
