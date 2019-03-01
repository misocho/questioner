let upvote = document.getElementById('upvote-btn');
let downvote = document.getElementById('downvote-btn');

function UpVote(question_id) {
    let url = `https://misocho01-questioner.herokuapp.com/api/v2/questions/${question_id}/upvote`;
    fetch(url, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `${localStorage.getItem('token')}`
        },
    })
    .then(response => response.json())
    .then((data) => {
        if (data.status !== 200){
            console.log(data.error);
        }
        else{
            console.log(data);
            location.reload();
        }
    })
}

function DownVote(question_id) {
    let url = `https://misocho01-questioner.herokuapp.com/api/v2/questions/${question_id}/downvote`;
    fetch(url, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `${localStorage.getItem('token')}`
        },
    })
    .then(response => response.json())
    .then((data) => {
        if (data.status !== 200){
            console.log(data.error);
        }
        else{
            console.log(data);
            location.reload();
        }
    })
}