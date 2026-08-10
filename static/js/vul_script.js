const registerPassword =document.getElementById("registerPassword");
const showRegisterPassword =document.getElementById("showRegisterPassword");
const loginPassword =document.getElementById("loginPassword");
const showLoginPassword =document.getElementById("showLoginPassword");
if (showRegisterPassword) {
    showRegisterPassword.addEventListener("change", function () {
        if (showRegisterPassword.checked) {
            registerPassword.type = "text";
        } else {
            registerPassword.type = "password";
        }
    });
}
if (showLoginPassword) {
    showLoginPassword.addEventListener("change", function () {
        if (showLoginPassword.checked) {
            loginPassword.type = "text";
        } else {
            loginPassword.type = "password";
        }
    });
}
