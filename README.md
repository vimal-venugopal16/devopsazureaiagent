# Azure AI Agent Web App

A FastAPI-based web app using Azure OpenAI and LangChain.

## Setup

1. Create an Azure OpenAI resource and deploy a model (GPT-4/GPT-3.5).
2. Fill in `.env` with your Azure credentials.

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the API server

```bash
uvicorn app:app --reload
```

## API

POST /ask

```json
{
  "message": "What is 3 * 9?"
}
```
