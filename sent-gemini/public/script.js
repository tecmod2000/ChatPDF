 // Display sentiment result on the webpage
 document.getElementById('sentimentForm').addEventListener('submit', async function (event) {
    event.preventDefault();

    const text = document.getElementById('text').value;

    // Send a POST request to the server
    const response = await fetch('/analyze', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text }),
    });

    // Fetch the Result and display it on the webpage
    const result = await response.text();
    document.getElementById('result').innerText = result;
  });