const fileUploader = document.getElementById('fileUploader');
const progress = document.getElementById('progress');
const reader = new FileReader();

fileUploader.addEventListener('change', (event) => {
  const files = event.target.files;
  const file = files[0]
  reader.readAsDataURL(file);
  console.log('files', files);

reader.addEventListener('progress', (event) => {
  if (event.loaded && event.total) {
    const percent = (event.loaded / event.total) * 100;
    progress.value = percent;
    document.getElementById('progress-label').innerHTML = Math.round(percent) + '%';
      
      if (percent === 100) {
        let msg = `<span style="color:green;">File <u><b>${file.name}</b></u> has been uploaded successfully.</span>`;
        feedback.innerHTML = msg;
      }
  }
})

  for (const file of files) {
    const name = file.name;
    const type = file.type ? file.type : 'NA';
    const size = file.size;
    const lastModified = file.lastModified;
    console.log({file, name, type, size, lastModified});
  
  const feedback = document.getElementById('feedback');
  const msg = `File ${files.length} file(s) uploaded successfully!;
  <br/>
              File Size: ${size} 
  <br/>
              File type: ${type} 
  <br/>
              File Last Modified: ${new Date(lastModified)}`;
    feedback.innerHTML = msg;
  }
});