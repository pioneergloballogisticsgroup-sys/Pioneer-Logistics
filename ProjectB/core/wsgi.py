import os
import sys # <--- ADD THIS IMPORT

# ADD THIS BLOCK BELOW THE IMPORTS:
from pathlib import Path
# Set BASE_DIR to the folder containing 'core' and 'website' (the outer ProjectB folder)
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
# END ADDITION

from django.core.wsgi import get_wsgi_application
# IMPORTANT: Use the nested settings path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjectB.core.settings')

application = get_wsgi_application()

