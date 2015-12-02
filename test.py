import DataIngest

config = file('.w205-data-ingest.cfg')

print config

run = DataIngest(config)

run
