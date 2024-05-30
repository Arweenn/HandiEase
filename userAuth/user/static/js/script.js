document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.querySelector('.form-login');
    const signupForm = document.querySelector('.form-signup');
    const loginMessage = document.getElementById('login-message');
    const signupMessage = document.getElementById('signup-message');

    loginForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const email = document.getElementById('login-email').value;
        const password = document.getElementById('login-password').value;

        if (email && password) {
            // Simulate successful login
            loginMessage.textContent = 'Login successful!';
            loginMessage.style.color = 'green';
        } else {
            loginMessage.textContent = 'Login failed. Please check your credentials.';
            loginMessage.style.color = 'red';
        }
    });

    signupForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const email = document.getElementById('signup-email').value;
        const password = document.getElementById('signup-password').value;
        const passwordConfirm = document.getElementById('signup-password-confirm').value;

        if (email && password && password === passwordConfirm) {
            // Simulate successful signup
            signupMessage.textContent = 'Registration successful!';
            signupMessage.style.color = 'green';
        } else if (password !== passwordConfirm) {
            signupMessage.textContent = 'Passwords do not match.';
            signupMessage.style.color = 'red';
        } else {
            signupMessage.textContent = 'Signup failed. Please check your details.';
            signupMessage.style.color = 'red';
        }
    });
});
