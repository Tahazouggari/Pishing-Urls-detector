# Pishing-Urls-detector
A Phishing URLs Detector using Machine Learning is a system designed to identify and classify URLs as either legitimate or malicious (phishing). The primary goal is to protect users from fraudulent websites that aim to steal sensitive information such as passwords, credit card details, or personal data.
## environement and packages needed to run the code 
        Pandas : sudo apt install python3-pandas
        Flask
        sklearn : pip install scikit-learn

## How to Run?

- Clone or download [python-phishing-url-detection](https://github.com/sannjayy/python-phishing-url-detection) 

`git clone git@github.com:sannjayy/python-phishing-url-detection.git`


- Create a virtual environment
```bash
python -m venv zenv
source zenv/Scripts/activate # Windows
source zenv/bin/activate # Mac
```


- Install basic requirements
```bash
pip install -r requirements.txt

# OR INITIAL INSTALLATION 
pip install --upgrade pip
pip install --upgrade setuptools

pip install pandas whois httpx
pip install pycaret # It will take sometime.
```
## How to Run?

- Clone or download [python-phishing-url-detection](https://github.com/Tahazouggari/Pishing-Urls-detector.git) 

`git clone https://github.com/Tahazouggari/Pishing-Urls-detector.git`


- Create a virtual environment
```bash
python -m venv zenv
source zenv/Scripts/activate # Windows
source zenv/bin/activate # Mac
```


- Install basic requirements
```bash

pip install pandas whois httpx
pip install pycaret # It will take sometime.
```

## Command to Run the Application

Run the following command in your terminal:

```bash
python main.py 


# OUTPUT: {'prediction_label': 0, 'prediction_score': 68.39} 

# 0 = False | 1 True
```

### To Run GUI

```bash
pip install flask

python app.py
```

Open http://127.0.0.1:5000 in your browser!
