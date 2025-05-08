function passwordToggle() {
    var passwordField = document.getElementById("password");
    var passwordToggle = document.getElementById("password-eyecon");

    if (passwordField.type === "password") {
        passwordField.type = "text";
        passwordField.placeholder = "Password";
        passwordToggle.src = "../static/images/icon/eye-open.png";
    } else {
        passwordField.type = "password";
        passwordField.placeholder = "**********";
        passwordToggle.src = "../static/images/icon/eye-closed.svg";
    }
}

function confirmPasswordToggle() {
    var passwordField = document.getElementById("confirm-password");
    var passwordToggle = document.getElementById("confirm-password-eyecon");

    if (passwordField.type === "password") {
        passwordField.type = "text";
        passwordField.placeholder = "Confirm Password";
        passwordToggle.src = "../static/images/icon/eye-open.png";
    } else {
        passwordField.type = "password";
        passwordField.placeholder = "**********";
        passwordToggle.src = "../static/images/icon/eye-closed.svg";
    }
}
