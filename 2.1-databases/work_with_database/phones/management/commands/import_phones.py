import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

            for phone in phones:
                self.stdout.write(str(phone.keys()), ending="")
                # TODO: Добавьте сохранение модели
                phone_db = Phone(id=phone['id'],name=phone['name'],image=phone['image'],price=phone['price'],release_date=phone['release_date'],lte_exists=phone['lte_exists'],slug=slugify(phone['name']))
                phone_db.save()
                #'id';'name';'image';'price';'release_date';'lte_exists'
            