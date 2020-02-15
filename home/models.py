from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=64)
    content = models.TextField()
    parent = models.ForeignKey(
        "self", related_name="children", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.name
