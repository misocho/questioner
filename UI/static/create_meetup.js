// Create meetup
var createMeetup = document.getElementById('submit-btn');
function create(event) {
    event.preventDefault();
    let title = document.getElementById('title').value;
    let organizer = document.getElementById('organizer').value;
    let location = document.getElementById('location').value;
    let date = document.getElementById('date').value;
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
            if (data.status !== 200){
                console.log(data.error)
            }
        })
}

createMeetup.addEventListener('click', create)