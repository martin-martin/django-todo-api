# Django Todo API

Using Django REST Framework to build a Todo API.

Based on [this article](https://codeburst.io/building-an-api-with-django-rest-framework-and-class-based-views-75b369b30396)

## TODO

* Currently doesn't serialize the POST data correctly when adding a User (e.g. 'username' requires an `int`)
* Adding Todos results in `ValueError at /todos/
Cannot assign "<django.contrib.auth.models.AnonymousUser object at 0x10e60ba58>": "Todo.user" must be a "User" instance.`
