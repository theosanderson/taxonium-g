tar -xf /mnt/data/gisaid_data/metadata_tsv.tar.xz --directory /mnt/data/amended_data
python3 reprocess_metadata.py
python3 fix_trimmed_pb.py /mnt/data/gisaid_data/optimised_trimmed.pb /mnt/data/amended_data/fixed.pb