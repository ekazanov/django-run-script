import os
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Test script running software"
    
    def handle(self, *args, **options):
        scr_name = args[0]
        fd = open(scr_name)
        try:
            script_text = fd.read( )
        finally:
            fd.close( )
            
        exec(script_text)
