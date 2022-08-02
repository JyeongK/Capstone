#!/bin/bash
source ~/anaconda3/etc/profile.d/conda.sh


conda create -n class python==3.8 -y
conda activate class
pip install --ignore-installed -r requirements_c.txt
conda install -c conda-forge tensorflow==2.9.1 -y
conda deactivate

conda create -n segment python==3.8 -y
conda activate segment
conda install -c nvidia cudatoolkit=11.0 cudnn=8.0.4=cuda11.0_0 -y
pip install --ignore-installed -r requirements.txt
conda deactivate
