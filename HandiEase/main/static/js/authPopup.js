document.addEventListener('DOMContentLoaded', function () {
    var authPopup = document.getElementById('authPopup');
    var openAuthPopup = document.getElementById('openAuthPopup');
    var close = document.getElementsByClassName('close')[0];
    var loginForm = document.getElementById('loginForm');
    var registerForm = document.getElementById('registerForm');
    var logoutButton = document.getElementById('logoutButton');
    loginForm.action = '/login/';
    registerForm.action = '/register/';


    if (openAuthPopup) {
        openAuthPopup.onclick = function () {
            authPopup.style.display = 'block';
        }
    }

    if (close) {
        close.onclick = function () {
            authPopup.style.display = 'none';
        }
    }

    window.onclick = function (event) {
        if (event.target == authPopup) {
            authPopup.style.display = 'none';
        }
    }

    function handleRegFormSubmit(event, form, redirectUrl) {
        event.preventDefault();
        var formData = new FormData(form);
        const form_data = new URLSearchParams();
        for (const [key, value] of formData.entries()) {
            form_data.append(key, value);
        };
        console.log(form.action)
        fetch(form.action, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                // 'X-CSRFToken': getCookie('csrftoken'),
            },
            body: form_data,
        }).then(async response => {
            try {
                var variable = await response.json();
                return (variable);
            } catch (e) {
                throw new Error('La réponse du serveur n\'est pas un JSON valide ' + e);
            }
        }).then(data => {
            if (data.success) {
                window.location.href = redirectUrl; // Redirection après succès
            } else {
                alert(data.message);
            }
        }).catch(error => {
            console.error('Erreur:', error);
            alert(error.message || 'Une erreur est survenue. Veuillez réessayer.');
        });
    }

    function handleLogFormSubmit(event, form, redirectUrl) {
        event.preventDefault();
        var formData = new FormData(form);
        const form_data = new URLSearchParams();
        for (const [key, value] of formData.entries()) {
            form_data.append(key, value);
        };
        console.log(form.action)
        fetch(form.action, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                // 'X-CSRFToken': getCookie('csrftoken'),
            },
            body: form_data,
        }).then(async response => {
            try {
                var variable = await response.json();
                return (variable);
            } catch (e) {
                throw new Error('La réponse du serveur n\'est pas un JSON valide ' + e);
            }
        }).then(data => {
            if (data.success) {
                window.location.reload(); // Redirection après succès
            } else {
                alert(data.message);
            }
        }).catch(error => {
            console.error('Erreur:', error);
            alert(error.message || 'Une erreur est survenue. Veuillez réessayer.');
        });
    }

    if (loginForm) {
        loginForm.onsubmit = function (event) {
            handleLogFormSubmit(event, loginForm, '/');
        }
    }

    if (registerForm) {
        registerForm.onsubmit = function (event) {
            handleRegFormSubmit(event, registerForm, '/');
        }
    }

    if (logoutButton) {
        logoutButton.addEventListener('click', function () {
            fetch('/logout/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    // 'X-CSRFToken': '{{ csrf_token }}'
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.reload();
                } else {
                    alert(data.error);
                }
            })
        });
    }
});
