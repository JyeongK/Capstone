source ~/anaconda3/etc/profile.d/conda.sh

USER=$(whoami)

cd /home/${USER}

wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
sh Anaconda3-2022.05-Linux-x86_64.sh
rm Anaconda3-2022.05-Linux-x86_64.sh

exec bash
conda deactivate

conda update conda -y
conda update anaconda -y
conda update --all -y

conda info --env
