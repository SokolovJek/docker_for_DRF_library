from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = get_user_model()
        user.objects.create_superuser(username='django',
                                      email='django@mail.ru',
                                      password='geekshop',
                                      first_name='jek',
                                      last_name='sokolov'
                                      )
