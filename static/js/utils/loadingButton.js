export function loadingButton(buttonId, loadingText) {
    const button = document.getElementById(buttonId);
    if (button) {
        button.style.cursor = "progress";
        button.innerHTML = loadingText;
        button.disabled = true;
    }
}

export function resetButton(buttonId, defaultText) {
    const button = document.getElementById(buttonId);
    if (button) {
        button.style.cursor = "default";
        button.innerHTML = defaultText;
        button.disabled = false;
    }
}