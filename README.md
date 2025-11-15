# Article Summarization App  

A Streamlit-Powered Interface for Generative AI Text Summaries
This project delivers an interactive and lightweight article-summarization platform built on **Google Generative AI (PaLM)** and **Streamlit**. The application enables users to input raw text or article content and generate concise, high-quality summaries with configurable parameters. The design philosophy emphasizes modularity, operational clarity, and seamless user experience.

---

## Overview  

The application provides a streamlined interface for:

- Dynamic article summarization  
- Parameter tuning (temperature and token limits)  
- Model selection  
- Real-time generative output using PaLM API  

This enables high-leverage use cases such as research acceleration, content distillation, and editorial workflows.

---

## Technology Stack  

| Component | Purpose |
|----------|---------|
| **Streamlit** | Front-end UI and app runtime |
| **Google Generative AI (PaLM)** | Text-generation engine |
| **python-dotenv** | Secure environment variable management |
| **dotenv + OS** | API key provisioning |
| **Python 3.x** | Primary execution environment |

---

## Features  

- **Interactive summarization UI** with text-area input  
- **Temperature tuning** to adjust creativity  
- **Configurable maximum output tokens** for concise or detailed summaries  
- **Model selection dropdown** for flexible API usage  
- **Clean function architecture** separating UI and generation logic  
- **Secure API key handling** through environment variables  

---

## Installation & Setup  

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <project-folder>
