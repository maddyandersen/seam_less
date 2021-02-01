#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/seam_less/")
sys.path.append("/var/www/seam_less/seam_less/")

from seam_less import app as application
application.secret_key = 'Add your secret key'
