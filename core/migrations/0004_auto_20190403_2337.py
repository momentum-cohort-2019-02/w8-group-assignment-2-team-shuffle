# Generated by Django 2.2 on 2019-04-04 03:37

from django.db import migrations
from django.conf import settings
import os.path
import csv
from django.core.files import File
from django.template.defaultfilters import slugify

def import_initial_cards(apps, schema_editor):
    """
    Read a CSV file full of posts and insert them into the database.
    """
    Deck = apps.get_model('core', 'Deck')
    Card = apps.get_model('core', 'Card')

    Card.objects.all().delete()
    datapath = os.path.join(settings.BASE_DIR, 'core/database')
    datafile = os.path.join(datapath, 'card_data.csv')

    with open(datafile) as file:
        reader = csv.DictReader(file) 
        for row in reader:
            #set Deck_site_name so that you can only add posts that haven't been added
            question = row['question']

            if Card.objects.filter(question=question).count():
                return
            #if the title isn't there, make new deck
            deck = Deck.objects.filter(title=row['decks'])
            card = Card(
                question=row['question'],
                answer=row['answer'],
                url=row['url'],
            )
       
            card.save()
            card.decks.set(deck)
            card.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190403_1644'),
    ]

    operations = [
        migrations.RunPython(import_initial_cards),
    ]
