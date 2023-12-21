const express = require('express');
const app = express();
const fs = require('fs');

app.get('/', (req, res) => {
    var message = "<h2> Category: FOREN - PWN 💀 (CLOSED)</h2><br>"
    message += "Hello CTF Player, Welcome to the CTF Challenge. <br>"
    message += "This is a FOPWN challenge. <br>"
    message += "You need to exploit the binary to get the flag. <br>"
    message += "But before that you need to find the binnary file, its hidden somewhere inside the file <br>"
    message += "You can download file <a href='/download'>here</a>. <br>"
    message += "This is a limited time challenge. <br>"
    message += "This website will be closed after 1 hour but the services might still up.<br>"
    message += "Good Luck ok !<br>"
    res.send(message);
});

app.get('/download', (req, res) => {
    res.send('you can\'t download the file because the chall was ended')
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

