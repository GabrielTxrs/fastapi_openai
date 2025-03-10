async function uploadFile(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const response = await fetch('/gerar-bo', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    window.open(result.url, '_blank');
}