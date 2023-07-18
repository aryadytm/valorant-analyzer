# AI Career Consultant 🧑‍💼

This app serves as an AI Career Consultant that provides advice based on the user's uploaded CV or portfolio. The app is built using Streamlit and leverages the GPT-3.5-turbo model from OpenAI.

## Tech Used

- Python 3.9
- Streamlit
- Docker
- OpenAI API (GPT3.5)
- LangChain

## Quick Start

First, rename the `.env.example` to `.env` then replace the API keys.

```bash
pip install -r requirements.txt
streamlit run main.py --server.address 0.0.0.0  --server.port 7860
```

## Usage

1. Upload your CV or portfolio file by clicking on the "Upload your CV or Portfolio here" button. Supported file formats are PDF, DOCX, and DOC.
2. Once the file is uploaded, you can ask questions to the AI Career Consultant based on your CV or portfolio. Enter your question in the text area provided.
3. Click on the "Ask Now" button to get the AI's response. The AI will analyze your CV or portfolio and provide advice based on the question asked.
4. The AI's response will be displayed below the question.
