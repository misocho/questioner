function DeleteMeetup(meetup_id) {
    let url = `https://misocho01-questioner.herokuapp.com/api/v2/meetups/${meetup_id}`;

    fetch(url, {
        method: 'DELETE',
        headers: {
            'Content-type': 'application/json',
            'Authorization': `${localStorage.getItem('token')}`
        }
    }).then((resp) => resp.json())
        .then((data) => {
            if (data.status !== 200) {
                console.log(data.error)
            }
            else {
                console.log(data.message);
                location.reload();
            }
        })

}