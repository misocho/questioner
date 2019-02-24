function GetMeetupId() {
    var url = window.location.href;
    var meetupid = url.split('=')[1];
    return meetupid;
}

function GetMeetup() {
    let meetup_id = GetMeetupId();
    let url = `https://misocho01-questioner.herokuapp.com/api/v2/meetups/${meetup_id}`;
    fetch(url, {
        methods: GetMeetup,
        headers: {
            'Content-Type': 'application/json'
        },
    })
        .then(response => response.json())
        .then((data) => {
            let meetup = data.data;
            let meetup_title = meetup.title;
            let image_url = '';
            let date = meetup.happeningon;
            let imageThumbnail = '';
            let splitDate = date.split(' ');
            let month = splitDate[2];
            date = splitDate[1];
            console.log(date);
            if (meetup.images == null) {
                imageThumbnail = `../images/no-image.png`;
            } else {
                url = 'https://i.imgur.com/'
                image_url = meetup.images.replace(url, '');
                file = image_url.split('.');
                fileName = file[0] + 'l';
                fileExtension = file[1];
                imageThumbnail = url + fileName + '.' + fileExtension;

            }
            let image_div = document.getElementById('side-image');
            image_div.style.backgroundImage = `url(${imageThumbnail})`;
            let meetup_details = `<div id="meetup-content">
            <div id="meetup-date">
                <div class="month">${month}</div>
                <div class="date">${date}</div>
            </div>
            <div id="more-meetup-details">
                <div id="meetup-title">
                   ${meetup_title}
                </div>
                <div id="meetup-by">
                    by <span id="host-name">Strathmore GDG</span>
                </div>
            </div>
            <div id="attending">
                <div class="button">
                    <input class="btn" type="button" name="" value="Schedule">
                </div>
            </div>
        </div>`

        document.getElementById('meetup-details').innerHTML = meetup_details;
        })
}

window.addEventListener('load', GetMeetup);