let L = 9;
let M = L;

// First part of the diamond (top half)
while (M >= 1) {
    let leadingSpaces = Math.floor((L - M) / 2);
    let string = " ".repeat(leadingSpaces);

    for (let i = 0; i < M; i++) {
        string += "* ";
    }

    console.log(string.trim());
    M -= 2;
}

// Second part of the diamond (bottom half)
M = 1;

while (M <= L) {
    let leadingSpaces = Math.floor((L - M) / 2);
    let string = " ".repeat(leadingSpaces);

    for (let i = 0; i < M; i++) {
        string += "* ";
    }

    console.log(string.trim());
    M += 2;
}
