PIECES = {
    '': '', 'wp': "♙", 'bp':"♟",
};
FILE = 'abcdefgh';
let selected = null;
let availableSquares = [];
let greensq = null;


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
            square.classList.add("square");
            const isLight = (i + j) % 2 === 0;

            if (isLight) {
                square.classList.add("light");
            } else {
                square.classList.add("dark");
            }

            square.innerText = PIECES[cell] || '';
            
            square.onclick = () => {
                handleClick(i, j).then(data => {
                    console.log("Is there any greens data?:", data);
                    data.forEach((note) => {
                        availableSquares.push(toBoardNotation(note));   
                    });
                console.log("available squares to higlight:", availableSquares)
                availableSquares.forEach((square) => {
                    let i = square[0];
                    let j = square[1];
                    const targetSquare = container.children[i].children[j];
                    targetSquare.classList.add("available")
                availableSquares = []
                });                    
                });
                square.classList.add("selected");
            };

            rowDiv.appendChild(square);
        });

        container.appendChild(rowDiv);
    });


};


function toChessNotation(i, j) {
    let file = String.fromCharCode(97 + j);
    let rank = 8 - i;
    return file + rank;
}

function toBoardNotation(notation) {
    let i = -(parseInt(notation[1]) - 8);
    let j = FILE.indexOf(notation[0]);
    return [i, j];
}


async function handleClick(i, j) {
    if (!selected) {
        selected = [i, j];
        const greens = await legalSquares(toChessNotation(i, j));
        console.log("legalMoves produces greens:", greens)
        return greens;
    }

    const start = toChessNotation(selected[0], selected[1]);
    const end = toChessNotation(i, j);
    
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
    return ["a1"];
}


async function legalSquares(selected_square) {
    const res = await fetch("/legal", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            sq: selected_square
        })
    });
    const availableMoves = await res.json();
    console.log("AvailableMoves:", availableMoves);
    return availableMoves;
};

async function greens(i ,j) {
    const greens = await handleClick(i, j);
    return greens;
};

fetchBoard();