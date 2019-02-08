var inputImage = document.getElementById('upload');
function previewImage(event) {
    event.preventDefault();
    let reader = new FileReader();
    let uploadField = document.getElementById('upload-field')
    let ImageField = document.getElementById("image-field");

    reader.onload = function(){
        if(reader.readyState == 2){
            ImageField.src = reader.result;
            ImageField.style.width = "100%";
            uploadField.style.display = "none";
            let image = reader.result;
        }
    }

    reader.readAsDataURL(event.target.files[0]);
    
    
}

inputImage.addEventListener('change', previewImage);