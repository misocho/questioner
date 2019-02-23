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
        let meetupHtml = '';
        let image_url = '';
        let date = meetup.happeningon;
        let imageThumbnail = '';
        let  splitDate = date.split(' ');
        let meetup_id = meetup.id;
        let month = splitDate[2];
        date = splitDate[1];
        console.log(date);
    })
}

window.addEventListener('load', GetMeetup);