# Django Rest Framework and JWT Authentication

As the headline says, the focus of the workshop is understanding some key concepts about DRF + JWT.

## Agenda

1. Looking at the code of Django Rest Framework
  * `APIView` & `generic.*`
  * `Serializer`, `ReturnDict` and modifying `serializer.data`
2. Understanding concepts for authentication and authorization
  * How does DRF handle authentication and authorization?
3. API authentication & JWT
  * What's the need for JWT?
  * Looking at [DRF JWT Auth](https://github.com/GetBlimp/django-rest-framework-jwt)

## Materials

* [DRF Github](https://github.com/tomchristie/django-rest-framework)
* [JWT Spec](https://jwt.io/)
* [DRF JWT Auth](https://github.com/GetBlimp/django-rest-framework-jwt)
* [DRF Authentication](http://www.django-rest-framework.org/api-guide/authentication/#authentication)

## Problems

* Implement a simple serializer class, similar to that in DRF.


## Authentication / Authorization

1. First authentication is made by calling `request.user`
  - This will either fail as an authentication or pass to anonymous user
  - We can add additional permission check for `IsAuthenticated`
