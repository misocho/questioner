var createMeetup = document.getElementById('submit-btn');


function changeDateFormat(inputDate) {  // expects Y-m-d
    var splitDate = inputDate.split('-');
    if (splitDate.count == 0) {
        return null;
    }

    var year = splitDate[0];
    var month = splitDate[1];
    var day = splitDate[2];

    return month + '-' + day + '-' + year;
}

var inputImage = document.getElementById('upload');
function previewImage(event) {
    event.preventDefault();
    let reader = new FileReader();
    let uploadField = document.getElementById('upload-field')
    let ImageField = document.getElementById("image-field");
    let imageContainer = document.getElementById("img-container");


    reader.onload = function () {
        if (reader.readyState == 2) {
            ImageField.src = reader.result;
            ImageField.style.width = "100%";
            uploadField.style.display = "none";
            ImageField.style.height = "276px";
            imageContainer.style.display = "contents";
        }
    }

    reader.readAsDataURL(event.target.files[0]);


}

inputImage.addEventListener('change', previewImage);

var save = document.getElementById('save-btn');
function uploadImgur(event) {
    event.preventDefault();
    let image = document.getElementById('image-field').src;
    var strImage = image.replace(/^data:image\/[a-z]+;base64,/, "");
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
            var image_url;
            image_url = data.data.link;
            console.log(image_url)

            // Create meetup
            function create(event) {
                event.preventDefault();
                let title = document.getElementById('title').value;
                let organizer = document.getElementById('organizer').value;
                let location = document.getElementById('location').value;
                let date = changeDateFormat(document.getElementById('date').value);
                let time = document.getElementById('time').value;
                fetch('https://misocho01-questioner.herokuapp.com/api/v2/meetups', {

                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `${localStorage.getItem('token')}`
                    },
                    body: JSON.stringify({
                        title: title,
                        organizer: organizer,
                        location: location,
                        happeningOn: date + " " + time
                    })
                })
                    .then((resp) => resp.json())
                    .then((data) => {
                        if (data.status !== 201) {
                            console.log(data.error)
                        }
                        else {
                            console.log(data.message)
                            let meetup_id = data.data[0].id;
                            let image = document.getElementById("image-field").src;
                            const type = "." + image.split(';')[0].split('/')[1];

                            fetch(`https://misocho01-questioner.herokuapp.com/api/v2/meetups/${meetup_id}/img`, {
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json',
                                    'Authorization': `${localStorage.getItem('token')}`
                                },
                                body: JSON.stringify({
                                    image: image_url
                                })
                            }).then((resp) => resp.json())
                                .then((data) => {
                                    if (data.status !== 201) {
                                        console.log(data.error)
                                    }
                                    else {
                                        console.log(data)
                                    }
                                })
                        }
                    })
            }

            createMeetup.addEventListener('click', create)

        })
}
save.addEventListener('click', uploadImgur);
