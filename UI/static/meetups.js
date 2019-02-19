function Meetup() {
    let url = 'https://misocho01-questioner.herokuapp.com/api/v2/meetups/upcoming';

    fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    })

        .then(response => response.json())
        .then((data) => {
            let meetup = data.data[0];
            let meetupHtml = '';
            console.log(meetup[1]);
            let image_url = '';
            for (let i = 0; i < meetup.length; i += 1) {
                console.log(meetup[i]);
                let date = meetup[i].happeningon
                let imageThumbnail = ''
                var splitDate = date.split(' ');
                console.log(splitDate)
                month = splitDate[2];
                date = splitDate[1];
                if (meetup[i].images == null){
                    imageThumbnail = "../images/dafault_image.svg";
                } else {
                    url = 'https://i.imgur.com/'
                    image_url = meetup[i].images.replace(url, '');
                    file = image_url.split('.');
                    fileName = file[0] + 'm';
                    fileExtension = file[1];
                    imageThumbnail = url + fileName +'.'+ fileExtension;
                    console.log(imageThumbnail);
                }

                meetupHtml += ` <div class="card">
                <div class="in-card">
                    <div class="in-card-upper">
                        <div class="in-card-image">
                        <image src="${imageThumbnail}"></image>
                        </div>
                    </div>
                    <div class="lower-container">
                        <div class="in-card-lower">
                            <div class="in-card-date">
                                <div class="month">${month}</div>
                                <div class="date">${date}</div>
                            </div>
                            <div class="in-card-text">
                                <div class="meetup-text">
                                    <div class="meetup-title">
                                        <a href="questions.html">${meetup[i].title}</a>
                                    </div>
                                    <div class="meetup-details">
                                        <p>${meetup[i].happeningon}</p>
                                        <p>${meetup[i].location}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>`;
            }
            document.getElementById('meetups').innerHTML = meetupHtml;
        }

        )
}
window.addEventListener('load', Meetup);