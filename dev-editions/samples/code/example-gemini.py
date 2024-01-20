
import google.generativeai as genai

genai.configure(api_key="AIzaSyAoHCCffIlLIOzHtHE2N5lKJTAV5QG_s7U")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

input = input("Insert a question")
prompt_parts = [
  f"{input}",
]

response = model.generate_content(prompt_parts)
try:
  print(response.text)
except ValueError:
  try:
    print(response.parts, "FEED")
  except ValueError:
    print(response.prompt_feedback, "FEED2")
