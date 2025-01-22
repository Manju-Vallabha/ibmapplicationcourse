# Application Setup

This guide will help you set up a virtual environment, activate it, and create a basic Streamlit application.

## 1. Create a Virtual Environment

To isolate dependencies, create a virtual environment.

### For Windows:
```bash
python -m venv venv
```

## 2. Activate the Virtual Environment/.

### For Windows:
```bash
venv\Scripts\activate
```
## 3. Install Dependencies from requirements.txt

If project having a `requirements.txt` file, you can install all the dependencies with one command:

```bash
pip install -r requirements.txt
```

## 4. Run the Streamlit App

terminal -> new terminal -> and enter below command:
Start the Streamlit application with the following command:

```bash
Streamlit run app.py
```
and updated version app run the following command on terminal.

```bash
Streamlit run upp_app.py
```

## Troubleshooting: Script Execution Policy Error on Windows

If you encounter an error while activating the virtual environment, such as:

### Run the following command in PowerShell:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
