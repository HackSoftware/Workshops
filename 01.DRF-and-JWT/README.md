# Django Rest Framework and JWT Authentication

As the headline says, the focus of the workshop is understanding some key concepts about DRF + JWT.

## Agenda

### Serializers

1. Looking at the code of Django Rest Framework
  * `APIView` & `generic.*`
  * `Serializer`, `ReturnDict` and modifying `serializer.data`

### DRF Authentication & Authorization

1. What is authentication / authorization / permissions in Django?
2. Lifecycle of `APIView`. Looking at `rest_framework/views.py`
3. Handling authentication
  * Looking at `rest_framework/authentication.py`
  * Looking at `rest_framework/request.py`
3. Handling permissions
  * Looking at `rest_framework/permissions.py`
4. How everything fits together?
5. Making custom authentication


### JWT

1. What's the idea behind JWT?
2. JWT Authentication backend
3. JWT Views for obtaiking tokens
  * Looking at [DRF JWT Auth](https://github.com/GetBlimp/django-rest-framework-jwt)

## Materials

* [DRF Github](https://github.com/tomchristie/django-rest-framework)
* [JWT Spec](https://jwt.io/)
* [DRF JWT Auth](https://github.com/GetBlimp/django-rest-framework-jwt)
* [DRF Authentication](http://www.django-rest-framework.org/api-guide/authentication/#authentication)

## Problems

* Implement a simple serializer class, similar to that in DRF.
* Implement a custom authentication backend.


## Authentication / Authorization

1. First authentication is made by calling `request.user`
  - This will either fail as an authentication or pass to anonymous user
  - We can add additional permission check for `IsAuthenticated`
