
# End-to-end-Medical-Chatbot-Generative-AI


# How to run?
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n medibot python=3.10 -y
```

```bash
conda activate medibot
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Pinecone & openai credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# run the following command to store embeddings to pinecone
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:

- Python
- LangChain
- Flask
- GPT
- Pinecone
## 3. Create ECR repo  to store/save docker image
-Save uri: 913524949784.dkr.ecr.eu-north-1.amazonaws.com/medicalchatbot
## 5.Open EC2 and Install Docker in EC2 Mahine:

  sudo apt-get upgrade -y
  
  sudo apt-get upgrade
  
 #required

  curl -fsSL https://get.docker.com -o get-docket.sh
  
  sudo sh get-docker.sh
  
  sudo usermod -aG docker ubuntu
  
  -- doker version
  
  newgrp doker
  
  # 6. Configure EC2 as self -hosted runner 
  setting>actions>runner>new self hosted runner>choose os>then run command  one by one -->OS -Linux ->follow the commnads shown in Github

  #7. Set up github secret

  -AWS_ACCESS_KEY_ID
  -AWS_SECRET_ACCESS_KEY
  -AWS_DEFAULT_REQION
  -ECR_REPO
  -PINECONE_API_KEY
  -OPENAI_API_KEY


