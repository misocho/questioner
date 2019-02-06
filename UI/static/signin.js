// Sign in user
var signIn = document.getElementById('signin-btn');
function login(event) {
    event.preventDefault();
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    fetch('https://misocho01-questioner.herokuapp.com/api/v2/auth/signin', {

        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    })
        .then((resp) => resp.json())
        .then((data) => {
            if (data.status == 200) {
                localStorage.setItem('token', data.token);
                window.location.href = '../templates/index.html';
            } else {
                window.alert(data.error);
            }
        })
        .catch((error) => console.error(error))
}
signIn.addEventListener('click', login);