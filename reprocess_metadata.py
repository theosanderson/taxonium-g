import json
from collections import OrderedDict
import pandas as pd

infile = "/mnt/data/amended_data/metadata.tsv"
columns = OrderedDict()
columns['Accession ID'] = 'strain'
columns['Virus name'] = 'name2'
columns['Collection date'] = 'date'
columns['Pango lineage'] = 'pangolin_lineage'
columns['Location'] = 'location'

print("Starting")
data = pd.read_csv(infile, sep='\t', usecols=columns.keys())
print("Read in data")
data = data.rename(columns=columns)
# Split location into continent, country, and subregion
split =  data['location'].str.split(' +\\/ +', expand=True)
print("Split")
data['continent'] = split[0]
data['country'] = split[1]
data['subregion'] = split[2]
# drop location
data = data.drop('location', axis=1)
print("Writing to file...")

data['genbank_accession'] = "?"
data.to_csv('/mnt/data/amended_data/amended_data.csv', index=False)

