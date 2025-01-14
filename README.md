# MedicalChatBotGenAI
# create conda  environment after opening repository[new env  Yes for all promps ]
conda create -n bot python=3.10 -y 
# Activate environment
conda activate bot

# Install requirements
pip install -r requirements.txt

# To see list of packages
pip list



conda env list 
conda deactivateDeactivating the environment you wish to delete: conda deactivate
Removing the environment: conda env remove --name <environment-name>>