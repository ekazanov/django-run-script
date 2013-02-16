django-run-script
==========

# Info #
Author: Evgeny Kazanov
# Introduction #
Sometimes it is very usefull to run python scripts which use Django
ORM. This application allows to do it from command line.

The similar functionality there is in django-extensions, but this
script allows:

1. To write scripts with less coding.
1. To locate scripts anywhere. 

# System requirements #

1. Python (Script was tested with 2.7 and 2.6 versions),
1. Django (Script was tested with 1.4 version)

# Installation #
1. Copy "run_script" directory to applications directory.
1. Add 'run_script' to INSTALLED\_APPS.

# Usage #

	manage.py run_script <script_path/script_name>

# Script sample #

	from your_application.models import  YourModelClass`

	for o in YourModelClass.objects.all():
		try:
			print o.id,
			print o.some_field
		except Exception, e:
			print "an error = ",str(e)


