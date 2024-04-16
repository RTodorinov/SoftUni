function attachEvents() {
    const baseURL = 'http://localhost:3030/jsonstore/games/';
    const loadButton = document.getElementById('load-games');
    const addButton = document.getElementById('add-game');
    const editButton = document.getElementById('edit-game');
    const gamesList = document.getElementById('games-list');

    loadButton.addEventListener('click', loadGames);
    addButton.addEventListener('click', addGame);
    editButton.addEventListener('click', editGame);

    async function loadGames() {
        try {
            const response = await fetch(baseURL);
            const data = await response.json();

            gamesList.innerHTML = '';
            for (const game of Object.values(data)) {
                const gameDiv = createGameDiv(game);
                gamesList.appendChild(gameDiv);
            }
            // Deactivate edit button
            editButton.disabled = true;
        } catch (error) {
            console.error('Error loading games:', error);
        }
    }

    async function addGame() {
        try {
            const gameName = document.getElementById('g-name').value;
            const gameType = document.getElementById('type').value;
            const maxPlayers = document.getElementById('players').value;

            const newGame = {
                name: gameName,
                type: gameType,
                players: maxPlayers
            };

            await fetch(baseURL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(newGame)
            });

            // Clear input fields
            document.getElementById('g-name').value = '';
            document.getElementById('type').value = '';
            document.getElementById('players').value = '';

            loadGames();
        } catch (error) {
            console.error('Error adding game:', error);
        }
    }

    async function editGame() {
        try {
            const gameId = document.querySelector('.selected').dataset.id;
            const gameName = document.getElementById('g-name').value;
            const gameType = document.getElementById('type').value;
            const maxPlayers = document.getElementById('players').value;

            const editedGame = {
                name: gameName,
                type: gameType,
                players: maxPlayers
            };

            await fetch(baseURL + gameId, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(editedGame)
            });

            // Clear input fields
            document.getElementById('g-name').value = '';
            document.getElementById('type').value = '';
            document.getElementById('players').value = '';

            // Deactivate edit button
            editButton.disabled = true;

            loadGames();
        } catch (error) {
            console.error('Error editing game:', error);
        }
    }

    function createGameDiv(game) {
        const gameDiv = document.createElement('div');
        gameDiv.classList.add('board-game');
        gameDiv.dataset.id = game._id;

        const contentDiv = document.createElement('div');
        contentDiv.classList.add('content');

        const namePara = document.createElement('p');
        namePara.textContent = game.name;
        contentDiv.appendChild(namePara);

        const typePara = document.createElement('p');
        typePara.textContent = game.type;
        contentDiv.appendChild(typePara);

        const playersPara = document.createElement('p');
        playersPara.textContent = game.players;
        contentDiv.appendChild(playersPara);

        const buttonsContainer = document.createElement('div');
        buttonsContainer.classList.add('buttons-container');

        const changeButton = document.createElement('button');
        changeButton.classList.add('change-btn');
        changeButton.textContent = 'Change';
        changeButton.addEventListener('click', populateForm);
        buttonsContainer.appendChild(changeButton);

        const deleteButton = document.createElement('button');
        deleteButton.classList.add('delete-btn');
        deleteButton.textContent = 'Delete';
        deleteButton.addEventListener('click', deleteGame);
        buttonsContainer.appendChild(deleteButton);

        gameDiv.appendChild(contentDiv);
        gameDiv.appendChild(buttonsContainer);

        return gameDiv;
    }

    function populateForm(event) {
        const gameDiv = event.target.closest('.board-game');
        const gameId = gameDiv.dataset.id;
        const gameName = gameDiv.querySelector('.content p:nth-child(1)').textContent;
        const gameType = gameDiv.querySelector('.content p:nth-child(3)').textContent;
        const maxPlayers = gameDiv.querySelector('.content p:nth-child(2)').textContent;

        document.getElementById('g-name').value = gameName;
        document.getElementById('type').value = gameType;
        document.getElementById('players').value = maxPlayers;

        // Activate edit button
        editButton.disabled = false;

        // Highlight selected game
        const selectedGame = document.querySelector('.selected');
        if (selectedGame) {
            selectedGame.classList.remove('selected');
        }
        gameDiv.classList.add('selected');
    }

    async function deleteGame(event) {
        try {
            const gameDiv = event.target.closest('.board-game');
            const gameId = gameDiv.dataset.id;

            await fetch(baseURL + gameId, {
                method: 'DELETE'
            });

            gameDiv.remove();
        } catch (error) {
            console.error('Error deleting game:', error);
        }
    }
}

attachEvents();
