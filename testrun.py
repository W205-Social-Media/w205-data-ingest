import ConfigParser
import requests
import json
from pprint import pprint
import io
import FacebookDataIngestSource

import psycopg2
import sys

term = str(sys.argv)

data = FacebookDataIngestSource(term)

pprint(data)