// Ajouter les écouteurs d'événements après que le DOM a été chargé
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.add-to-reading-list').forEach(button => {
        button.addEventListener('click', addToReadingList);
    });

    document.querySelectorAll('.remove-from-reading-list').forEach(button => {
        button.addEventListener('click', removeFromReadingList);
    });

    function addToReadingList(event) {
        var articleElement = event.target.closest('li');
        var articleTitle = articleElement.dataset.articleTitle;

        $.ajax({
            type: "POST",
            url: addToReadingListUrl,
            data: {
                csrfmiddlewaretoken: csrfToken,
                article_title: articleTitle,
            },
            success: function(response) {
                alert(response.message);
                if (response.status === 'success') {
                    // Ajoute l'article à la liste de lecture dans l'interface
                    var readingList = document.getElementById('reading-list');
                    var noArticlesMessage = document.getElementById('no-articles-message');

                    // Retire le message "Aucun article dans votre liste de lecture" si présent
                    if (noArticlesMessage) {
                        noArticlesMessage.remove();
                    }

                    var newListItem = document.createElement('li');
                    newListItem.setAttribute('data-article-title', articleTitle);
                    newListItem.innerHTML = articleTitle + ' <button class="remove-from-reading-list">Retirer</button>';
                    readingList.appendChild(newListItem);

                    // Ajoute l'écouteur d'événement pour le bouton de retrait
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
                article_title: articleTitle,
            },
            success: function(response) {
                alert(response.message);
                if (response.status === 'success') {
                    articleElement.remove();

                    // Si la liste est vide, affiche le message "Aucun article dans votre liste de lecture"
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
});
