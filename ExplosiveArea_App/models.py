from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
import os

# Create your models here.

def images_path(instance, filename):
    return 'img/{0}'.format(filename)
def videos_path(instance, filename):
    return 'video/{0}'.format(filename)


class Excercise (models.Model):
    ATHLETIC_FOR_ATHLETICS  = 'athletes'
    ATHLETIC_FOR_OLYMPICS   = 'olympics'
    GYM                     = 'gym'
    BASKETBALL_PLANNER      = 'basketball_planner'
    BASKETBALL_EXCERCISES   = 'basketball_excercises'
    BASKETBALL_MOVES        = 'basketball_moves'
    BASKETBALL_DEFENCE      = 'basketball_defence'

    sections = {
        ATHLETIC_FOR_ATHLETICS  : 'אתלטיקה לספורטאים',
        ATHLETIC_FOR_OLYMPICS   : 'אתלטיקה אולימפית',
        GYM                     : 'חדר כושר',
        BASKETBALL_PLANNER      : 'לוח שבועי',
        BASKETBALL_EXCERCISES   : 'אימונים',
        BASKETBALL_MOVES        : 'מהלכים',
        BASKETBALL_DEFENCE      : 'הגנה'
    }
    
    SECTION_CHOICES = [
        (ATHLETIC_FOR_ATHLETICS, sections[ATHLETIC_FOR_ATHLETICS]),
        (ATHLETIC_FOR_OLYMPICS, sections[ATHLETIC_FOR_OLYMPICS]),
        (GYM, sections[GYM]),
        (BASKETBALL_EXCERCISES, sections[BASKETBALL_EXCERCISES]),
        (BASKETBALL_MOVES, sections[BASKETBALL_MOVES]),
        (BASKETBALL_DEFENCE, sections[BASKETBALL_DEFENCE]),
        (BASKETBALL_PLANNER, sections[BASKETBALL_PLANNER]),
    ]

    title           = models.CharField(max_length=100)
    intendedFor     = models.CharField(max_length=100, blank=True, null=True)
    description     = models.CharField(max_length=200, blank=True, null=True)
    instructions    = RichTextField(blank=True, null=True)
    section         = models.CharField(max_length=30, choices=SECTION_CHOICES)
    image           = models.ImageField(upload_to=images_path, blank=True, null=True)
    video           = models.FileField(upload_to=videos_path, blank=True, null=True)
    