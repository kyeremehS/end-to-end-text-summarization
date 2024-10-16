# end-to-end-text-summarization

## workflows
1. Update config.yaml
2. Update params.yaml
3. update entity
4. update the configuration manager in src config
5. update the components
6. update the pipeline
7. update the main.py
8. update the app.py


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/kyeremehS/end-to-end-text-summarization
```

### STEP 01- Create a new conda environment after opening the repository

```bash
conda create -n summary python=3.8 -y
```

```bash
conda activate summary
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# run the following command
python app.py
```

```bash
open up you local host and port
```



# AWS CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

  #with specifc access

  1. EC2 access: It is virtual machine

  2. ECR: Elastic Container registry to save your docker image in aws

  #Description: About the deployment

  1. Build docker image of the source code

  2. Push your docker image to ECR

  3. Launch the EC2

  4. Pull your image from ECR into EC2

  5. Launch your docker image into EC2

  #Policy:

  1. AmazonEC2ContainerRegistryFullAccess

  2. AmazonEC2FullAccess

  ## 3. Create ECR repo to store/save docker image
  - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/catdog

  ## 4. Create EC2 machine (Ubuntu)

  ## 5. Open EC2 and Install docker in EC2 Machine

    #optimal

    sudo apt-get update -y

    sudo apt-get upgrade

    #required 

