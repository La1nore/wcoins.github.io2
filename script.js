const tokenCountElement = document.getElementById('token-count');
const daysElement = document.getElementById('days');
const hoursElement = document.getElementById('hours');
const minutesElement = document.getElementById('minutes');

let tokenCount = 0;
let startTime = new Date();

function updateTimer() {
    const now = new Date();
    const elapsed = now - startTime;
    const minutes = Math.floor(elapsed / (1000 * 60));
    const hours = Math.floor(minutes / 60);
    const days = Math.floor(hours / 24);

    daysElement.innerText = String(days).padStart(2, '0');
    hoursElement.innerText = String(hours % 24).padStart(2, '0');
    minutesElement.innerText = String(minutes % 60).padStart(2, '0');
}

function addToken() {
    tokenCount += 1;
    tokenCountElement.innerText = tokenCount;
}

// Call addToken every minute
setInterval(addToken, 60000);

setInterval(updateTimer, 1000);
updateTimer();
