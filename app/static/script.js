async function uploadFile(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const response = await fetch('/gerar-bo', {
        method: 'POST',
        body: formData
    });
    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.style.display = 'none';
    a.href = url;
    a.download = 'boletim.md';
    document.body.appendChild(a);
    a.click();
    window.URL.revokeObjectURL(url);
}