""" README https://docs.djangoproject.com/en/dev/howto/custom-management-commands/ """

from django.core.management.base import BaseCommand, CommandError
from apps.core.classes.add_dummy_content import AddDummyContent


class Command(BaseCommand):
    help = 'Create or Update Dummy content'

    def handle(self, *args, **options):
        add_dummy_content = AddDummyContent()
        add_dummy_content.addContent()

        self.stdout.write(self.style.SUCCESS('Dummy content Created'))
        # self.stdout.write(self.style.ERROR('Error message'))