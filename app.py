import os
import requests
import gradio as gr
from modules import scripts

class AIPromptGenerator(scripts.Script):
    def title(self):
        return "AI Prompt Generator"

    def ui(self, is_img2img):
        with gr.Group():
            with gr.Accordion("🔮 AI Prompt Generator", open=False):
                api_key = gr.Textbox(
                    label="Enter AI API Key (Gemini/OpenAI)",
                    placeholder="sk-... or AIza...",
                    type="password"
                )
                style = gr.Dropdown(
                    label="Prompt Style",
                    choices=["MidJourney", "Photorealistic", "Anime", "Fantasy"],
                    value="MidJourney"
                )
                strength = gr.Slider(
                    label="Creativity Strength",
                    minimum=0.1, maximum=1.0, step=0.1, value=0.7
                )
        return [api_key, style, strength]

    def run(self, p, api_key, style, strength):
        if not api_key:
            raise gr.Error("⚠️ Please enter an API key!")
        
        p.prompt = self.generate_prompt(p.prompt, api_key, style, strength)
        return p

    def generate_prompt(self, input_text, api_key, style, strength):
        # Apply style template (e.g., MidJourney-style)
        prompt = self.apply_style(input_text, style)
        
        # Call AI API (Gemini example)
        if api_key.startswith("AIza"):
            response = requests.post(
                "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent",
                json={
                    "contents": [{
                        "parts": [{
                            "text": f"Improve this Stable Diffusion prompt with {style}-style details (creativity: {strength}): {prompt}"
                        }]
                    }]
                },
                params={"key": api_key}
            )
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        
        # Add OpenAI/Claude support here...
        return prompt

    def apply_style(self, prompt, style):
        styles = {
            "MidJourney": f"cinematic masterpiece, {prompt}, ultra-detailed, 8K, dramatic lighting, unreal engine 5",
            "Photorealistic": f"professional photo of {prompt}, 85mm f/1.8, shallow depth of field, bokeh, kodak portra 400",
            "Anime": f"anime artwork, {prompt}, vibrant colors, studio ghibli style, makoto shinkai",
            "Fantasy": f"fantasy art, {prompt}, intricate details, greg rutkowski, artstation trending"
        }
        return styles.get(style, prompt)
