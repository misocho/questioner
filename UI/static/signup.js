// Create a new user
var signUp = document.getElementById('signup-btn');
function register(event){
    let firstname = document.getElementById('firstname')
    let lastname = document.getElementById('lastname')
    let othername = document.getElementById('othername')
    let email = document.getElementById('email')
    let phoneNumber = document.getElementById('phonenumber')
    let username = document.getElementById('username')
    let password = document.getElementById('password')
    fetch('https://misocho01-questioner.herokuapp.com/api/v2/auth/signup', {
        method:'POST',
        headers: {
            'Accept': 'application/json',
            'Content-type': 'aoolication/json'
        },
        body: JSON.stringify({
            firstname: firstname,
            lastname: lastname,
            email: email,
            phoneNumber: phoneNumber,
            username: username,
            password: password
        })
    })
    .then((resp) => resp.json())
    .then((data) => {
        if (data.status == 200){
            window.location.href = 'index.html'
            window.alert(data.data)
        }else{
            window.alert(data.error);
        }
    })
    .catch((error) => console.error(error))
}
documentTitle = document.querySelector('title').innerHTML;
if (documentTitle == "Questioner" ){
    signUp.addEventListener('click', register);
}