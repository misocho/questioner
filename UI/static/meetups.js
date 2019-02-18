function Meetup() {
    let url = 'https://misocho01-questioner.herokuapp.com/api/v2/meetups';
    let title = document.getElementById('title');
    let organizer = document.getElementById('organizer');
    let location = document.getElementById('location');
    let date = document.getElementById('date');
    let time = document.getElementById('time');

    fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    })

        .then(response => response.json())
        .then((data) => {
            console.log(data);
        }

        )
}

window.addEventListener('load', Meetup);