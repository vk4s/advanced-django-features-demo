from django.core.management.base import BaseCommand, CommandError

from biolinks.models import BioLink
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Prints all the available biolinks"

    def add_arguments(self, parser):
        # optional argument (remove -- to make positional argument)
        parser.add_argument("--user-emails", nargs="+", type=str)

    def handle(self, *args, **options):
        biolinks = []
        if 'user_emails' in options and options["user_emails"] is not None:
            for user_email in options["user_emails"]:
                try:
                    user = get_user_model().objects.get(email=user_email)
                    biolinks = BioLink.objects.filter(owner_id=user.id)
                except BioLink.DoesNotExist:
                    raise CommandError('Poll "%s" does not exist' % user_email)
        else:
            biolinks = BioLink.objects.all()

        for biolink in biolinks:
            self.stdout.write(self.style.SUCCESS(biolink.link))
