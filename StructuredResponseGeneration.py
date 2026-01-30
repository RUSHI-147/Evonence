#Use the Gemini API to generate a response in JSON format for the query: 
#"List 3 benefits of Python for data science." Handle cases where the response isn’t valid JSON

import google.generativeai as genai
import json
genai.configure(api_key="GEMINI_API_KEY")
def get_python_benefits_json():
    model = genai.GenerativeModel("gemini-pro")
    prompt = """
    List 3 benefits of Python for data science.
    Respond ONLY in valid JSON using this format:
    {
      "benefits": ["benefit1", "benefit2", "benefit3"]
    }
    """
    response = model.generate_content(prompt)
    raw_text = response.text.strip()
    try:
        parsed_response = json.loads(raw_text)
        return parsed_response
    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON received from Gemini",
            "raw_response": raw_text
        }
