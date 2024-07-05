document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.add-to-reading-list').forEach(button => {
        button.addEventListener('click', addToReadingList);
    });

    document.querySelectorAll('.remove-from-reading-list').forEach(button => {
        button.addEventListener('click', removeFromReadingList);
    });
});

function addToReadingList(event) {
    var articleElement = event.target.closest('li');
    var articleTitle = articleElement.dataset.articleTitle;
    var articleLink = articleElement.dataset.articleLink;  // Ajouter le lien de l'article

    $.ajax({
        type: "POST",
        url: addToReadingListUrl,
        data: {
            csrfmiddlewaretoken: csrfToken,
            article_title: articleTitle,
            article_link: articleLink  // Passer le lien de l'article
        },
        success: function(response) {
            alert(response.message);
            if (response.status === 'success') {
                var readingList = document.getElementById('reading-list');
                var noArticlesMessage = document.getElementById('no-articles-message');

                if (noArticlesMessage) {
                    noArticlesMessage.remove();
                }

                var newListItem = document.createElement('li');
                newListItem.setAttribute('data-article-title', articleTitle);
                newListItem.setAttribute('data-article-link', articleLink);  // Ajouter l'attribut de lien de l'article
                newListItem.innerHTML = `<a href="${articleLink}" target="_blank" class="article-title">${articleTitle}</a> <button class="remove-from-reading-list">Retirer</button>`;
                readingList.appendChild(newListItem);

                newListItem.querySelector('.remove-from-reading-list').addEventListener('click', removeFromReadingList);
            }
        },
        error: function(xhr, status, error) {
            console.error(xhr.responseText);
        }
    });
}

function removeFromReadingList(event) {
    var articleElement = event.target.closest('li');
    var articleTitle = articleElement.dataset.articleTitle;

    $.ajax({
        type: "POST",
        url: removeFromReadingListUrl,
        data: {
            csrfmiddlewaretoken: csrfToken,
            article_title: articleTitle
        },
        success: function(response) {
            alert(response.message);
            if (response.status === 'success') {
                articleElement.remove();

                var readingList = document.getElementById('reading-list');
                if (readingList.children.length === 0) {
                    var noArticlesMessage = document.createElement('li');
                    noArticlesMessage.id = 'no-articles-message';
                    noArticlesMessage.textContent = 'Aucun article dans votre liste de lecture.';
                    readingList.appendChild(noArticlesMessage);
                }
            }
        },
        error: function(xhr, status, error) {
            console.error(xhr.responseText);
        }
    });
}

// Fonction pour vérifier si un article est déjà dans la liste de lecture
function checkReadingList() {
    var readingListItems = document.querySelectorAll('#reading-list li');
    var addButtons = document.querySelectorAll('.add-to-reading-list');

    readingListItems.forEach(function(item) {
        var articleTitle = item.dataset.articleTitle;
        addButtons.forEach(function(button) {
            if (button.dataset.articleTitle === articleTitle) {
                button.style.display = 'none'; // Masquer le bouton d'ajout si l'article est déjà dans la liste
            }
        });
    });
}

document.addEventListener('DOMContentLoaded', function() {
    checkReadingList(); // Vérifier au chargement de la page

    // Ajouter un événement pour vérifier également après chaque ajout d'article (en supposant que vous avez une fonction qui gère l'ajout d'articles)
    document.querySelectorAll('.add-to-reading-list').forEach(button => {
        button.addEventListener('click', function(event) {
            // Code pour ajouter l'article à la liste de lecture
            addToReadingList(event);

            // Après l'ajout, vérifier à nouveau
            checkReadingList();
        });
    });
});