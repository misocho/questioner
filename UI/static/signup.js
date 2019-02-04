// Create a new user
var signUp = document.getElementById('signup-btn');
function register(event) {
    event.preventDefault();
    let firstname = document.getElementById('firstname').value;
    let lastname = document.getElementById('lastname').value;
    let othername = document.getElementById('othername').value;
    let email = document.getElementById('email').value;
    let phoneNumber = document.getElementById('phonenumber').value;
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    fetch('https://misocho01-questioner.herokuapp.com/api/v2/auth/signup', {
        
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            firstname: firstname,
            lastname: lastname,
            othername: othername,
            email: email,
            phoneNumber: phoneNumber,
            username: username,
            password: password
        })
    })
        .then((resp) => resp.json())
        .then((data) => {
            if (data.status == 200) {
                window.location.href = '../templates/index.html'
                window.alert(data.data)
            } else {
                window.alert(data.error);
            }
        })
        .catch((error) => console.error(error))
}
signUp.addEventListener('click', register);