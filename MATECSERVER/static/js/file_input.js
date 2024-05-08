const fileInput = document.getElementById('fileInput');
const fileNameInput = document.getElementById('fileName');

fileInput.addEventListener('change', function () {
    if (this.files && this.files[0]) {
        const file = this.files[0];
        fileNameInput.value = `This is "${file.name}" of "Yo Mama"`; // Set read-only file name

        const reader = new FileReader();
        reader.onload = function (e) {
            document.getElementById('').setAttribute('src', e.target.result);
        };
        reader.readAsDataURL(file);
    } else {
        fileNameInput.value = ''; // Clear file name if no file selected
        document.getElementById('').setAttribute('src', ''); // Clear preview if no file selected
    }
});