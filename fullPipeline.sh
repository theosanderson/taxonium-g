#! /bin/bash
source /home/ubuntu/miniconda3/bin/activate base
cd /mnt/data/taxonium-g 
source pipeline1.sh
source pipeline2.sh
source pipeline3.sh