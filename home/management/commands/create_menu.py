from django.core.management.base import BaseCommand
from home import models


class Command(BaseCommand):
    help = "Creates some sample menu items"

    def handle(self, *args, **kwargs):
        top = models.MenuItem(name="Top Level", content="Test")
        top.save()

        sub1 = models.MenuItem(name="Sub Menu Item 1", content="1", parent=top)
        sub1.save()

        sub2 = models.MenuItem(name="Sub Menu Item 2", content="2", parent=top)
        sub2.save()

        sub3 = models.MenuItem(name="Sub Menu Item 3", content="3", parent=top)
        sub3.save()

        supersub_1 = models.MenuItem(name="Super Sub 1", content="1", parent=sub1)
        supersub_1.save()

        supersub_2 = models.MenuItem(name="Super Sub 2", content="1", parent=sub1)
        supersub_2.save()

        self.stdout.write("Finished creating menu items")
