<div align=center>
    <img src="./recipe-finder.jpg" alt="Recipe Finder" width="30%" height="30%" />
    <hr>
</div>

# Recipe Finder with GenAI Backend

This is the backend of the Recipe Finder application, developed using Python, Google Gemini, the Google AI Developer Kit (ADK), and FastAPI. Its primary goal is to provide intelligent recipe and drink recommendations based on user input.

## ✨ Features

- **Multilingual Support:** Translate user inputs and agent responses into the desired language.
- **Context-Aware Recipe Search:** Find relevant recipes based on available ingredients, dietary restrictions, and culinary preferences.
- **Detailed Recipe Steps:** Get step-by-step instructions for chosen recipes, including estimated cooking times.
- **Perfect Drink Pairings:** Receive tailored drink recommendations to complement your selected dish.

## 💭 How it works

The project integrates with Google Gemini and orchestrates interactions through four specialized agents:

1.  **Translator Agent:** Responsible for translating all user-facing texts and agent responses into the specified language, ensuring a seamless multilingual experience.
2.  **Search Agent:** Utilizes `google_search` to intelligently find and filter recipes based on the user's provided ingredients, dietary restrictions, and culinary type, returning up to 5 relevant options.
3.  **Recipe Agent:** Given a chosen recipe from the search results, this agent uses `google_search` to retrieve and present the complete step-by-step cooking instructions, along with an estimated preparation time.
4.  **Drink Agent:** Acts as a sommelier, leveraging `google_search` to suggest up to 3 perfect drink pairings that complement the flavors of the selected recipe.

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.9+
- `pip` (Python package installer)
- A Google Gemini API Key (obtainable from [Google AI Studio](https://aistudio.google.com/))

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/giupiombo/recipe-finder-backend.git
    cd recipe-finder-backend
    ```

2.  **Create and activate a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # For Windows: .\venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your Google API Key:**
    Create a file named `.env` in the root directory of your project (where `main.py` is located) and add your Google Gemini API Key:
    ```dotenv
    GOOGLE_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY_HERE"
    ```
    **Important:** Replace `"YOUR_ACTUAL_GEMINI_API_KEY_HERE"` with your actual API key. Do not commit this file to public repositories.

### Running the API

1.  **Start the FastAPI server:**

    ```bash
    uvicorn main:app --reload
    ```

    The `--reload` flag will automatically restart the server on code changes.

2.  **Access the API documentation:**
    Open your web browser and navigate to `http://localhost:8000/docs#/`. Here, you will find the interactive OpenAPI (Swagger UI) documentation, allowing you to test each API endpoint directly.
