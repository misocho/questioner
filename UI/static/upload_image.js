var inputImage = document.getElementById('upload');
function previewImage(event) {
    event.preventDefault();
    let reader = new FileReader();
    let uploadField = document.getElementById('upload-field')
    let ImageField = document.getElementById("image-field");
    let imageContainer = document.getElementById("img-container");
    

    reader.onload = function(){
        if(reader.readyState == 2){
            ImageField.src = reader.result;
            ImageField.style.width = "100%";
            uploadField.style.display = "none";
            ImageField.style.height = "276px";
            imageContainer.style.display = "contents";
        }
        console.log(reader.result)
    }

    reader.readAsDataURL(event.target.files[0]);
    
    
}

inputImage.addEventListener('change', previewImage);

var save = document.getElementById('save-btn');
function uploadImgur(event) {
    event.preventDefault();
    let image = document.getElementById('image-field').src;
    var strImage = image.replace(/^data:image\/[a-z]+;base64,/, "");
    var image_url;
    data = new FormData();
    data.append("image", strImage);
    fetch('https://api.imgur.com/3/image', {
        method: 'POST',
        headers: {
            'Authorization': 'Client-ID 6c78ded85463291'
        },
        body: data
    }).then((resp) => resp.json())
        .then((data) => {
            image_url = data.data.link;
        })
}
save.addEventListener('click', uploadImgur);