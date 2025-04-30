const chatForm = document.getElementById('chat-form');
const chatBox = document.getElementById('chat-box');

chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const userInput = document.getElementById('user-input').value.trim();

    if (userInput === '') return;

    // Show user message
    chatBox.innerHTML += `<div class="user"><b>You:</b> ${userInput}</div>`;
    document.getElementById('user-input').value = '';

    // Send user message to backend
    const response = await fetch('/get', {
        method: 'POST',
        body: new URLSearchParams({ 'messageText': userInput }),
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    });

    const data = await response.json();

// Show bot response
if (data.response.includes("<iframe")) {
    chatBox.innerHTML += `<div class="bot">${data.response}</div>`;
} else {
    chatBox.innerHTML += `<div class="bot"><b>LankaTravelMate:</b> ${data.response}</div>`;
}
chatBox.scrollTop = chatBox.scrollHeight;
});
