# Python-Flask-Project

An API of superhero movies built in Python and Flask, using a SQL database with PeeWee models with full CRUD.

---

## API Endpoints

|   Description    |   Endpoints   | Operators |
| :--------------: | :-----------: | :-------: |
| List all movies  |   `/movie`    |   `GET`   |
| Find movie by id | `/movie/<id>` |   `GET`   |
| Add a new movie  |   `/movie`    |  `POST`   |
|  Update a movie  | `/movie/<id>` |   `PUT`   |
|  Delete a movie  | `/movie/<id>` | `DELETE`  |


## CRUD in action

---

### GET

![alt text](./IMAGES/GET.png "GET ON POSTMAN")

![alt text](./IMAGES/GETBYID.png "GET BY ID")

---

### UPDATES

![alt text](./IMAGES/UPDATE.png "UPDATING A MOVIE")

![alt text](./IMAGES/GETAFTERUPDATE.png "GET AFTER UPDATING")

---

### DELETING

![alt text](./IMAGES/DELETE.png "DELETING A MOVIE")

![alt text](./IMAGES/GETAFTERDELETE.png "GET AFTER DELETING")
