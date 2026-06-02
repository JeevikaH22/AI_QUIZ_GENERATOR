# AI Quiz Generator

A lightweight generative AI web application that automatically creates customized quizes based on a user-specified topic, number of questions, and difficulty level. 

## Features
* **Customizable Quizzes:** Generate questions dynamically by providing any topic.
* **Difficulty Scaling:** Supports multiple difficulty tiers to match user proficiency.
* **Flexible Question Count:** Choose exactly how many questions you want to generate.
* **Clean UI:** Simple, intuitive frontend templates for seamless user interaction.

## Project Structure
```
├── templates/
│   └── (HTML frontend templates)
├── app.py
├── .env
└── README.md
```

Install following dependencies-
pip install flask google-generativeai python-dotenv

CREATE .env file and add following content-
GEMINI_API_KEY=your_actual_api_key_here

Run the application using the command-
python app.py
