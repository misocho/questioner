function changeDateFormat(inputDate){  // expects Y-m-d
    var splitDate = inputDate.split('-');
    if(splitDate.count == 0){
        return null;
    }

    var year = splitDate[0];
    var month = splitDate[1];
    var day = splitDate[2]; 

    return month + '-' + day + '-' + year;
}


// Create meetup
var createMeetup = document.getElementById('submit-btn');
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
            }
        })
    var happeningOn2 = date + " " + time;
    console.log(happeningOn2);
}

createMeetup.addEventListener('click', create)
