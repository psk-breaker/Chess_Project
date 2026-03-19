async function fetchBoard() {
    const res = await fetch('/board');
    const board = await res.json();
    renderBoard(board);
}

function renderBoard(board) {
    const container = document.getElementById('board');
    container.innerHTML = '';

    board.forEach((row, i) => {
        const rowDiv = document.createElement('div');
        rowDiv.className = 'row';

        row.forEach((cell, j) => {
            const square = document.createElement('div');
            square.className = 'square';
            square.innerText = cell || '';
            square.onclick = () => handleClick(i, j);

            rowDiv.appendChild(square);
        });

        container.appendChild(rowDiv);
    });
}

function toChessNotation(i, j) {
    const file = String.fromCharCode(97 + j);
    const rank = 8 - i;
    return file + rank;
}

let selected = null;

async function handleClick(i, j) {
    if (!selected) {
        selected = [i, j];
        return;
    }

    const start = toChessNotation(selected[0], selected[1]);
    const end = toChessNotation(i, j);
    console.log("Move:", start, end);

    const res = await fetch("/move", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            start: start,
            end: end
        })
    });

    selected = null;
    fetchBoard();
}

fetchBoard();