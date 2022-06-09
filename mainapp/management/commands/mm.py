from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This command using for call 'makemessages' with flags:\n" "--locale=ru --no-location"

    def handle(self, *args, **options):
        call_command("makemessages", "--locale=ru", "--no-location")
