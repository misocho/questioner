var postQuestion = document.getElementById('post-button');

function DisplayPostButton(event) {
    let title = document.getElementById('title-textarea').value;
    let body = document.getElementById('description-textarea').value;

    if (title.length & body.length){
        postQuestion.style.display = 'block';
    }

    else{
        postQuestion.style.display = 'none';
    }
}



function PostQuestion(event) {
    event.preventDefault()
    let title = document.getElementById('title-textarea').value;
    let body = document.getElementById('description-textarea').value;
    let meetupId = GetMeetupId();

    fetch('https://misocho01-questioner.herokuapp.com/api/v2/questions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `${localStorage.getItem('token')}`
        },
        body: JSON.stringify({
            title: title,
            body: body,
            meetup_id: meetupId
        })
    })
        .then((resp) => resp.json())
        .then((data) => {
            if (data.status !== 201) {
                console.log(data.error);
            }
            else {
                console.log(data);
                location.reload();
            }
        })
} 
window.addEventListener('keyup', DisplayPostButton);
postQuestion.addEventListener('click', PostQuestion);