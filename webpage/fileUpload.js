const input = document.getElementById('fileUploader');
const link = document.getElementById('link');
let objectURL;

input.addEventListener('change', function () {
  if (objectURL) {
    // revoke the old object url to avoid using more memory than needed
    URL.revokeObjectURL(objectURL);  
  }

  const file = this.files[0];
  objectURL = URL.createObjectURL(file);

  link.download = file.name;
  link.href = objectURL;
});