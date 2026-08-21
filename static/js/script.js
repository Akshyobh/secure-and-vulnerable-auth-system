const registerPassword = document.getElementById("registerPassword");
const showRegisterPassword = document.getElementById("showRegisterPassword");

const loginPassword = document.getElementById("loginPassword");
const showLoginPassword = document.getElementById("showLoginPassword");


// ====================
// SHOW / HIDE PASSWORD
// ====================

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


// ====================
// REGISTRATION FIELDS
// ====================

const phone = document.getElementById("phone");
const phoneMessage = document.getElementById("phoneMessage");

const email = document.getElementById("email");
const emailMessage = document.getElementById("emailMessage");

const nameField = document.getElementById("name");
const nameMessage = document.getElementById("nameMessage");

const username = document.getElementById("username");
const usernameMessage = document.getElementById("usernameMessage");

const passwordMessage = document.getElementById("passwordMessage");

const registerSubmit = document.getElementById("registerSubmit");


// ====================
// NAME VALIDATION
// ====================

if (nameField) {

    nameField.addEventListener("input", function () {

        if (/^[A-Za-z ]{2,50}$/.test(nameField.value)) {

            nameMessage.textContent = "✓ Valid name";
            nameMessage.className = "text-success";

            // Enable Email
            email.disabled = false;

        } else {

            nameMessage.textContent =
                "✗ Name should contain only letters";

            nameMessage.className = "text-danger";

            // Disable everything after Name
            email.disabled = true;
            phone.disabled = true;
            username.disabled = true;
            registerPassword.disabled = true;
            showRegisterPassword.disabled = true;

            if (registerSubmit) {
                registerSubmit.disabled = true;
            }

        }

    });

}


// ====================
// EMAIL VALIDATION
// ====================

if (email) {

    email.addEventListener("input", function () {

        const emailValue = email.value;

        if (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailValue)) {

            emailMessage.textContent = "✓ Valid email address";
            emailMessage.className = "text-success";

            // Enable Phone
            phone.disabled = false;

        } else {

            emailMessage.textContent = "✗ Invalid email address";
            emailMessage.className = "text-danger";

            // Disable everything after Email
            phone.disabled = true;
            username.disabled = true;
            registerPassword.disabled = true;
            showRegisterPassword.disabled = true;

            if (registerSubmit) {
                registerSubmit.disabled = true;
            }

        }

    });

}


// ====================
// PHONE VALIDATION
// ====================

if (phone) {

    phone.addEventListener("input", function () {

        const phoneNumber = phone.value;

        if (/^[0-9]{10}$/.test(phoneNumber)) {

            phoneMessage.textContent = "✓ Valid phone number";
            phoneMessage.className = "text-success";

            // Enable Username
            username.disabled = false;

        } else {

            phoneMessage.textContent = "✗ Enter exactly 10 digits";
            phoneMessage.className = "text-danger";

            // Disable everything after Phone
            username.disabled = true;
            registerPassword.disabled = true;
            showRegisterPassword.disabled = true;

            if (registerSubmit) {
                registerSubmit.disabled = true;
            }

        }

    });

}


// ====================
// USERNAME VALIDATION
// ====================

if (username) {

    username.addEventListener("input", function () {

        if (/^[A-Za-z0-9_]{4,20}$/.test(username.value)) {

            usernameMessage.textContent = "✓ Valid username";
            usernameMessage.className = "text-success";

            // Enable Password
            registerPassword.disabled = false;
            showRegisterPassword.disabled = false;

        } else {

            usernameMessage.textContent =
                "✗ Use 4-20 letters, numbers or _";

            usernameMessage.className = "text-danger";

            // Disable Password
            registerPassword.disabled = true;
            showRegisterPassword.disabled = true;

            if (registerSubmit) {
                registerSubmit.disabled = true;
            }

        }

    });

}


// ====================
// PASSWORD VALIDATION
// ====================

if (registerPassword) {

    registerPassword.addEventListener("input", function () {

        const value = registerPassword.value;

        const strong =
            value.length >= 8 &&
            /[A-Z]/.test(value) &&
            /[a-z]/.test(value) &&
            /\d/.test(value) &&
            /[!@#$%^&*(),.?":{}|<>]/.test(value);

        if (strong) {

            passwordMessage.textContent = "✓ Strong password";
            passwordMessage.className = "text-success";

            // Enable Submit
            if (registerSubmit) {
                registerSubmit.disabled = false;
            }

        } else {

            passwordMessage.textContent =
                "✗ Minimum 8 characters with uppercase, lowercase, number and special character";

            passwordMessage.className = "text-danger";

            // Disable Submit
            if (registerSubmit) {
                registerSubmit.disabled = true;
            }

        }

    });

}


// ====================
// LOGIN USERNAME VALIDATION
// ====================

const loginUsername = document.getElementById("loginUsername");

if (loginUsername) {

    loginUsername.addEventListener("input", function () {

        const value = loginUsername.value;

        if (/^[A-Za-z0-9_]{4,20}$/.test(value)) {

            // Valid username → enable password
            loginPassword.disabled = false;
            showLoginPassword.disabled = false;

        } else {

            // Invalid username → disable password
            loginPassword.disabled = true;
            showLoginPassword.disabled = true;

            loginPassword.value = "";
            showLoginPassword.checked = false;
            loginPassword.type = "password";

        }

    });

}