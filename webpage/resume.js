function sendToEmail() {
let email = document.querySelector('contactEmail')
let phoneNumber = document.querySelector('contactNumber')
let body = "Email: " + email + "Phone Number: " + phoneNumber
window.open('mailto:jordankraudeTP@gmail.com?subject=subject&body='+email + '' + phoneNumber);
}

document.querySelector('submit').addEventListener('click', sendToEmail)
