
url = "https://raw.githubusercontent.com/W-L/ProblematicSites_SARS-CoV2/master/archived_vcf/problematic_sites_sarsCov2.2021-10-14-11%3A49.vcf"
import urllib.request
import gzip
# iterate over lines
masked_positions = set()
with urllib.request.urlopen(url) as response:
        for line in response:
            line = line.decode('utf-8')

            if line.startswith('#'):
                continue
            # parse line
            print
            fields = line.split('\t')
            chrom = fields[0]
            pos = int(fields[1])
            ref = fields[3]
            alt = fields[4]
            qual = fields[5]
            filt = fields[6]
            if filt=="mask":
                masked_positions.add(pos)

masked_pos_to_real_pos = {}

masked_i = 0
for i in range(max(list(masked_positions))):
    masked_pos_to_real_pos[masked_i] = i
    if i+1 not in masked_positions:
        masked_i+=1


import parsimony_pb2
import sys
import os
tree_file = sys.argv[1]
tree_file_out = sys.argv[2]
tree_file_handle = open(tree_file, 'rb')

data = parsimony_pb2.data()
data.ParseFromString(tree_file_handle.read())
tree_file_handle.close()
import tqdm

for node_mutations in tqdm.tqdm(data.node_mutations):
    for mutation in node_mutations.mutation:
        if mutation.position in masked_pos_to_real_pos:
            mutation.position = masked_pos_to_real_pos[mutation.position]

# Save output
tree_file_handle = open(tree_file_out, 'wb')
tree_file_handle.write(data.SerializeToString())
tree_file_handle.close()