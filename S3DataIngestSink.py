import boto
import datetime
import uuid

class S3DataIngestSink
  """Output data to S3"""

  def __init__(self, config):
    self.config = config
    aws_access_key_id = self.config['aws_access_key_id']
    aws_secret_access_key = self.config['aws_secret_access_key']
    aws_bucket = 'shoot2top'

    conn = boto.connect_s3(aws_access_key_id, aws_secret_access_key)
    
    self.bucket = conn.get_bucket(aws_bucket, validate = True)

    now = datetime.datetime.now().isoformat()

    unique = str(uuid.uuid4())

    self.folder = now + '-' + unique


  def write(self, source):

    self.record_index = 0
    self.file_index = 0

    self.batch_size = 5

    self.batch = [ ]

    for item in source:
      self.record_index = record_index + 1
      self.batch.append(item)

      if self.record_index >= self.batch_size:
        self.flush()

  def flush(self):

    filename = str(self.file_index).zfill(7)
    key_name = self.folder + '/' + filename
    key = self.bucket.new_key(key_name)
    key.set_contents.from_string('\n'.join(self.batch))

    self.file_index = self.file_index + 1

    self.batch = [ ]
    self.record_index = 0
    

    

    