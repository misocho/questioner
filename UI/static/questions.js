function GetMeetupId() {
    var url = window.location.href;
    var meetupid = url.split('=')[1];
    return meetupid;
}

function GetMeetup() {
    let meetup_id = GetMeetupId();
    console.log(meetup_id);
    let url = `https://misocho01-questioner.herokuapp.com/api/v2/meetups/${meetup_id}`;
    fetch(url, {
        methods: GetMeetup,
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then(response => response.json())
    .then((data) => {
        console.log(data);
    })
}

window.addEventListener('load', GetMeetup);