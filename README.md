
# note-taking Django API

This is a backend django API for note-taking app.





## Overview
A note is having a title, body and tags. Each note can have multiple tags attched to it.

The api has the functionalities for users to:

    1) add, edit and delete their notes
    2) filter their notes by tag name
    3) search the note content by keywords

For using the api, follow the below steps:

    1) Clone the repository -->           git clone https://github.com/saloni027/backend-coding-challenge.git
    2) Create virtual env and install the requirements.txt -->   python3 -m venv venv | pip install -r requirements.txt
    3) Do the migrations -->               python manage.py migrate | python manage.py makemigrations 
    4) Run the server -->                 python manage.py runserver
    
The api requires authentication for any operation by the User.
## API Reference

#### Register as a new User and get the token.

```http
  POST account/register/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | username |
| `password` | `string` | password  |
| `password2` | `string` | confirm password |

#### if you are a registered person, you can login with this endpoint and get the token.

```http
  POST /account/login/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | username |
| `password` | `string` | password  |

#### if you are logged in, you can logout with below endpoint. It will require a token.

```http
  POST /account/logout/ 
```

#### Get the list of notes. Make sure to add the token in the Headers.

```http
  GET /notes
```

#### Get a single note. Make sure to add the token in the Headers.

```http
  GET /notes/<id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of note to fetch |

#### Post notes. Make sure to add the token in the Headers.

```http
  POST notes/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `title` | `string` | title of note |
| `body` | `string` | body of note  |
| `tags` | `list` | list of dictionaries containing tag_titles |

#### Modify notes. Make sure to add the token in the Headers.

```http
  PUT notes/<id>
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `title` | `string` | title of note |
| `body` | `string` | body of note  |
| `tags` | `list` | list of dictionaries containing tag_titles |

#### Delete notes. Make sure to add the token in the Headers.

```http
  DELETE notes/<id>
```

TODO: Add feature to make Notes public or private.
Public notes can be viewed without authentication, however they cannot be modified






