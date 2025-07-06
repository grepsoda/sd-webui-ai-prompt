function addAutoPromptButton() {
    const promptBox = document.querySelector("#txt2img_prompt textarea");
    const button = document.createElement("button");
    button.textContent = "✨ Auto Prompt";
    button.onclick = () => {
        const apiKey = prompt("Enter your AI API key:");
        const style = prompt("Style (MidJourney/Photorealistic/etc):");
        generateAIPrompt(apiKey, style).then(prompt => {
            promptBox.value = prompt;
        });
    };
    promptBox.parentNode.appendChild(button);
}

onUiUpdate(() => addAutoPromptButton());
