function setupAIPromptButton() {
    const generateBtn = document.createElement("button");
    generateBtn.id = "ai-prompt-generate-btn";
    generateBtn.className = "lg secondary gradio-button";
    generateBtn.textContent = "✨ Auto Prompt";
    generateBtn.style.marginLeft = "10px";
    generateBtn.onclick = async () => {
        const promptTextarea = gradioApp().querySelector("#txt2img_prompt textarea, #img2img_prompt textarea");
        const apiKey = await getApiKeyFromUI();
        if (!apiKey) return;
        
        promptTextarea.value = "Generating... (check console for errors)";
        const response = await fetch("/ai_prompt/generate", {
            method: "POST",
            body: JSON.stringify({
                prompt: promptTextarea.value,
                api_key: apiKey
            })
        });
        const data = await response.json();
        promptTextarea.value = data.prompt || "Error: Check API key";
    };

    gradioApp().querySelector("#txt2img_prompt, #img2img_prompt").appendChild(generateBtn);
}

onUiUpdate(setupAIPromptButton);
