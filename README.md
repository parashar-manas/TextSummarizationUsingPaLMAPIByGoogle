# Text Summarization Using PaLM API by Google

## Overview  
This solution enables streamlined, generative text summarization through a lightweight Streamlit interface integrated with Google’s PaLM API. The platform supports configurable model parameters, real-time inference, and a clean operational workflow suited for research acceleration, editorial pipelines, and content-intelligence use cases.

## Key Features  
- Interactive summarization interface with rich text input  
- Adjustable temperature for controlling generation creativity  
- Configurable maximum output tokens for summary length management  
- Model selection for flexible API utilization  
- Modular code separation between UI and generation logic  
- Secure API key handling via environment variables  

## Dataset Requirement  
This application does not require a dataset. Users directly input raw text or article content into the interface for summarization. Only an active **Google Generative AI API key** is needed for inference.

## Workflow Architecture  
1. Load environment variables and initialize PaLM API credentials.  
2. Render Streamlit UI components for text input, parameter controls, and model selection.  
3. Capture user input and configuration settings.  
4. Execute summarization through the PaLM text-generation endpoint.  
5. Display generated summaries dynamically in the Streamlit interface.  
6. Handle errors, empty inputs, or invalid configurations gracefully.  

## Installation  

### 1. Clone the repository  
```bash
git clone <your-repo-url>
cd <project-folder>
