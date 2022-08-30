This was a version of Taxonium that ran within the GISAID infrastructure. `fix_trimmed_pb.py` fixes the UShER protobuf used within GISAID which has the masked sites literally removed from the reference (with all the other sites therefore shifting position).

sudo docker run --pull always -p 8000:80 -v "/mnt/data/amended_data/gisaid.jsonl.gz:/myfile.jsonl.gz" -e "DATA_FILE=/myfile.jsonl.gz" -e "CONFIG_JSON=config_gisaid.json" theosanderson/taxonium_backend:mast

sudo docker run --pull always -p 3000:80 theosanderson/taxonium_frontend:master
