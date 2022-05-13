sudo docker run --pull always -p 8000:80 -v "/mnt/data/amended_data/gisaid.jsonl.gz:/myfile.jsonl.gz" -e "DATA_FILE=/myfile.jsonl.gz" -e "CONFIG_JSON=config_gisaid.json" theosanderson/taxonium_backend:mast

sudo docker run --pull always -p 3000:80 theosanderson/taxonium_frontend:master