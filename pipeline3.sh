wget -qN https://raw.githubusercontent.com/theosanderson/taxonium/master/taxoniumtools/test_data/hu1.gb
usher_to_taxonium --input /mnt/data/amended_data/sheared.pb --output /mnt/data/amended_data/gisaid_temp.jsonl.gz --metadata /mnt/data/amended_data/amended_data.csv --genbank hu1.gb --columns name2,date,pangolin_lineage,continent,country,subregion --chronumental --chronumental_steps=300 --chronumental_reference_node=EPI_ISL_402124
mv /mnt/data/amended_data/gisaid_temp.jsonl.gz mv /mnt/data/amended_data/gisaid.jsonl.gz
microk8s kubectl rollout restart deploy