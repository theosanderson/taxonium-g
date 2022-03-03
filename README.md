tar -xf /mnt/data/gisaid_data/metadata_tsv.tar.xz --directory /mnt/data/amended_data
python3 reprocess_metadata.py
python3 fix_trimmed_pb.py /mnt/data/gisaid_data/optimised_trimmed.pb /mnt/data/amended_data/fixed.pb
matUtils extract -i /mnt/data/amended_data/fixed.pb --metadata=/mnt/data/amended_data/amended_data.csv -d /mnt/data/amended_data/ -F name2,continent,country,subregion --write-taxodium=taxodium.pb -f wuhCor1.fa -g ncbiGenes.gtf
node server.js --database_dir /mnt/data/amended_data/ --port 8000 --summary_json summary.json