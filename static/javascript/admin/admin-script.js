/// JavaScript
document.addEventListener('DOMContentLoaded', () => {
    const popUp = document.querySelector('.pop-up-message');
    
    if (popUp) {
        const messages = popUp.querySelectorAll('p');
        messages.forEach(msg => {
            const closeBtn = document.createElement('span');
            closeBtn.className = 'close-btn';
            closeBtn.innerHTML = '&times;';
            msg.appendChild(closeBtn);
        });
  
        const timeout = setTimeout(() => {
            popUp.classList.add('slide-out');
        }, 5000);
  
        popUp.addEventListener('click', (e) => {
            if (e.target.classList.contains('close-btn')) {
                clearTimeout(timeout);
                popUp.classList.add('slide-out');
            }
        });
  
        popUp.addEventListener('animationend', (e) => {
            if (e.animationName === 'slideOut') {
                popUp.remove();
            }
        });
    }
  });

function passwordToggle() {
    var passwordField = document.getElementById("password");
    var passwordToggle = document.getElementById("password-eyecon");

    if (passwordField.type === "password") {
        passwordField.type = "text";
        passwordField.placeholder = "Password";
        passwordToggle.src = "../../static/images/icon/eye-open.png";
    } else {
        passwordField.type = "password";
        passwordField.placeholder = "**********";
        passwordToggle.src = "../../static/images/icon/eye-closed.svg";
    }
}

const sidebar = document.getElementById('sidebar-container');
const headerMenu = document.getElementById('header-menu');
const sidebarMenu = document.getElementById('sidebar-menu');

// Universal toggle function
function toggleSidebar() {
    const isVisible = sidebar.style.display === 'flex' || sidebar.style.display === 'block';
    sidebar.style.display = isVisible ? 'none' : 'flex'; // or 'block'
}

// Header menu toggle
headerMenu.addEventListener('click', function(event) {
    toggleSidebar();
    event.stopPropagation();
});

// Sidebar menu toggle
sidebarMenu.addEventListener('click', function(event) {
    toggleSidebar();
    event.stopPropagation();
})

// Close with ESC key
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape' && window.getComputedStyle(sidebar).display !== 'none') {
        sidebar.style.display = 'none';
    }
});
