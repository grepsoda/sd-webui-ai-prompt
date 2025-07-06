import os
import requests
import gradio as gr
from modules import scripts

class AIPromptGenerator(scripts.Script):
    def title(self):
        return "AI Prompt Generator"

    def ui(self, is_img2img):
        # Add API key input & style dropdown
        api_key = gr.Textbox(label="Enter AI API Key")
        style = gr.Dropdown(
            choices=["MidJourney", "Photorealistic", "Anime", "Fantasy"],
            label="Prompt Style"
        )
        return [api_key, style]

    def run(self, p, api_key, style):
        # Call Gemini/OpenAI API
        prompt = self.generate_prompt(p.prompt, api_key, style)
        p.prompt = prompt  # Override the input prompt
        return p

    def generate_prompt(self, input_text, api_key, style):
        # Example: Gemini API call
        if "google" in api_key:  # Detect if it's a Gemini key
            response = requests.post(
                "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent",
                json={"contents": [{"parts": [{"text": f"Generate a {style}-style SD prompt: {input_text}"}]}],
                params={"key": api_key}
            )
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        # Add OpenAI/Claude support here...
