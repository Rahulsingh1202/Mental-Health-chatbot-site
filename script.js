const chatbox = document.getElementById('chatbox');
const userInput = document.getElementById('userInput');

// Function to send a message
function sendMessage() {
    const message = userInput.value.trim();

    if (message !== "") {
        // Add the user's message to the chatbox
        const userMessage = document.createElement('p');
        userMessage.innerHTML = `<strong>You:</strong> ${message}`;
        chatbox.appendChild(userMessage);

        // Send the message to the backend to get a response
        fetch('/get_response', {
            method: 'POST',
            body: JSON.stringify({ message: message }),
            headers: { 'Content-Type': 'application/json' }
        })
        .then(response => response.json())
        .then(data => {
            const botMessage = document.createElement('p');
            botMessage.innerHTML = `<strong>Bot:</strong> ${data.response}`;
            chatbox.appendChild(botMessage);
            
            // Scroll the chatbox to the bottom
            chatbox.scrollTop = chatbox.scrollHeight;
        });

        // Clear the input field
        userInput.value = "";
    }
}
