document.addEventListener('DOMContentLoaded', (event) => {
    const links = document.querySelectorAll('#linkContainer a');

    // Fonction pour obtenir l'URL de base sans les paramètres de pagination
    function getBaseUrl(url) {
        const urlObj = new URL(url);
        const basePath = urlObj.pathname + (urlObj.search.split('&page=')[0] || '');
        return basePath;
    }

    // Fonction pour mettre à jour les classes 'selected' en fonction de l'URL actuelle
    function updateSelectedLink() {
        // Obtenir le chemin de l'URL actuelle sans les paramètres de pagination
        const currentPath = getBaseUrl(window.location.href);

        // Parcourir chaque lien pour ajouter/enlever la classe 'selected'
        links.forEach(link => {
            // Obtenir le chemin du lien sans les paramètres de pagination
            const linkPath = getBaseUrl(link.href);

            // Comparer le chemin de l'URL du lien avec le chemin de l'URL actuelle
            if (linkPath === currentPath) {
                link.classList.add('selected');
            } else {
                link.classList.remove('selected');
            }

            // Condition spéciale pour la rubrique "Tout"
            if (link.href === window.location.origin + '/' && window.location.pathname === '/' && !window.location.search.includes('q=')) {
                link.classList.add('selected');
            }
        });
    }

    // Mettre à jour les classes 'selected' lors du chargement initial de la page
    updateSelectedLink();

    // Ajouter un événement 'click' à chaque lien pour naviguer correctement
    links.forEach(link => {
        link.addEventListener('click', function(event) {
            // Ne pas ajouter ou retirer de classes ici pour éviter le clignotement
            // La mise à jour des classes se fera uniquement lors du chargement de la nouvelle page
        });
    });
});


const moveToTopButton = document.querySelector("#move-to-top-button");

// 
window.addEventListener("scroll", () => {
  let scrollPosition = window.scrollY || document.documentElement.scrollTop;

  if (scrollPosition > 250) {
    moveToTopButton.style.bottom = "50px";
  } else {
    moveToTopButton.style.bottom = "-50px";
  }
});

// Scroll smoothly to the top of the page when the button is clicked
moveToTopButton.addEventListener("click", (onclick) => {
  onclick.preventDefault();

  window.scrollTo({
    top: 0,
    behavior: "smooth"
  });
});
