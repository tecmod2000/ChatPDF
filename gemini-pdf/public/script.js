document.getElementById('pdfForm').addEventListener('submit', async function (event) {
  event.preventDefault();

  const fileInput = document.getElementById('file');
  const file = fileInput.files[0];
  const formData = new FormData();
  formData.append('file', file);

  // Send a POST request to the server
  const response = await fetch('/analyze', {
      method: 'POST',
      body: formData,
  });

  // Fetch the Result and display it on the webpage
  const result = await response.text();
  document.getElementById('result').innerText = result;
});