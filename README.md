![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=googledrive&logoColor=white)![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)![Kali](https://img.shields.io/badge/Kali-268BEE?style=for-the-badge&logo=kalilinux&logoColor=white)![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)![Google](https://img.shields.io/badge/google-4285F4?style=for-the-badge&logo=google&logoColor=white)![DuckDuckGo](https://img.shields.io/badge/DuckDuckGo-DE5833?style=for-the-badge&logo=DuckDuckGo&logoColor=white)![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)![Windows 11](https://img.shields.io/badge/Windows%2011-%230079d5.svg?style=for-the-badge&logo=Windows%2011&logoColor=white)

[![GitHub](https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/karthikeyanrathinam/)
[![Linkedin](https://img.shields.io/badge/LinkedIn-0A66C2.svg?style=for-the-badge&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/karthikeyanrathinam/)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/@linkagethink)
[![Gmail](https://img.shields.io/badge/Gmail-EA4335.svg?style=for-the-badge&logo=Gmail&logoColor=white)](mailto:karthikeyanr1801@gmail.com)

# **LLama 2 LLM Run Local CPU and Access the LLM via API calling**
This project implements a simple server-client architecture to interact with a language model using HTTP requests.

# Table of Contents
- [What](#what)
- [Overview](#Overview)
- [Installation](#Installation)
- [Usage](#Usage)
- [Server Code](#ServerCode)
- [Client Code](#ClientCode)
- [Contributing](#Contributing)
- [License](#License)

## Overview
This project utilizes a language model to generate responses to user queries. The ```server-script``` handles HTTP requests and uses the language model to generate responses, while the ```client-script``` interacts with the server to retrieve these responses.

## Installation
Requirements:

Python 3.x
Dependencies: ```ctransformers, langchain```

Installation Steps:

Clone this repository.
Install dependencies:
```python
pip install ctransformers langchain
```
## Usage
To use the provided scripts:

#Server Side
Run the server script ```serverScript.py```:

```bash
python serverScript.py
```
The server will start on port 8000.

#Client Side
Use the client script ```clientScript.py``` to interact with the server:

```python
import requests
import json
import logging
```

```python
url = 'http://localhost'  # Replace with your server address if needed
Question = 'Hello, server!'
port = 8000
result = api_calls(url, Question, port)
print(result)
```
## ServerCode
The serverScript.py file includes functionality to handle GET requests and generate model responses:

```python
# Generate model response
model_response=self.model_response(received_question)

# Prepare JSON response
response_data = {'response': f"{model_response}"}
response = json.dumps(response_data).encode('utf-8')
```

## ClientCode

The clientScript.py file makes API calls to the server and handles responses:

```python
response = requests.get(f"{url}:{port}?question={Question}")
```
## Contributing
Contributions to this project are welcome! If you'd like to contribute, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Follow 

[![GitHub](https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/karthikeyanrathinam/)
[![Linkedin](https://img.shields.io/badge/LinkedIn-0A66C2.svg?style=for-the-badge&logo=LinkedIn&logoColor=white)](https://www.linkedin.com/in/karthikeyanrathinam/)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/@linkagethink)
[![Gmail](https://img.shields.io/badge/Gmail-EA4335.svg?style=for-the-badge&logo=Gmail&logoColor=white)](mailto:karthikeyanr1801@gmail.com)
