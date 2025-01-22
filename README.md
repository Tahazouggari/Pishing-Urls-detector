# Pishing-Urls-detector
A Phishing URLs Detector using Machine Learning is a system designed to identify and classify URLs as either legitimate or malicious (phishing). 


## How to Run?

- Clone or download [python-phishing-url-detection](https://github.com/Tahazouggari/Pishing-Urls-detector.git) 

`git clone https://github.com/Tahazouggari/Pishing-Urls-detector.git`


- Create a virtual environment.
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

Open http://127.0.0.1:5000 in your browser.
