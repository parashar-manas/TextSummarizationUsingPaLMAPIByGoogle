# Text Summarization Usin  PaLM API By Google
This represents a straightforward implementation of article summarization, leveraging Google's PaLM API for text completion and seamlessly integrated with the Streamlit framework.

Key Features:

1. Article Summarization: The project implements article summarization using Google's PaLM (Probabilistic and Lexical Modeling) API text completion, allowing users to generate concise summaries of long articles or text.
2. Adjustable Creativity Level: Users can adjust the "Temperature" parameter to control the creativity level of the summarization process. Higher values lead to more creative summaries, while lower values result in more conservative, factual summaries.
3. Limit on Summary Length: Users can define the maximum length of the article summary by adjusting the "Max Output Tokens" parameter. This feature ensures that the generated summary stays within a specified character limit.
4. Easy API Key Setup: To use the project, users need to visit https://makersuite.google.com/app/home, create a new API Key under Text Prompt, and replace the placeholder "YOUR_API_KEY" in the .env file with their actual API Key.
5. User-Friendly Interface: The project utilizes Streamlit to provide a user-friendly web-based interface for summarizing articles. Users can interact with the app without needing to write code.
6. Step-by-Step Setup Instructions: The project includes clear and concise instructions for setting up the environment. Users are guided through the process of installing the required dependencies using pip install -r requirements.txt.
7. Running the App: Users can run the summarization app by executing streamlit run main.py in their project folder. The app will automatically open in their default web browser, or they can access it at http://127.0.0.1:8501/ if it doesn't open automatically.
8. Custom Use Case Prompt: Users can provide a custom use case prompt along with the article text or URL to tailor the summarization process to their specific needs. For example, they can request summaries with bulleted lists or use case-specific instructions.
9. Summary Display: The generated article summary is displayed in a summary box within the app, making it easy for users to read and analyze.
10. Web Access: The project is deployed online, and users can access it via the provided URL: https://text-summarizer-using-palm-api.onrender.com/.
11. Issue Resolution: Users are encouraged to raise issues in the project's repository if they encounter any problems or face difficulties. The project provides support for issue resolution and improvement.
