const fs = require('fs');

function loadUsers(path = '/data/users.json') {
    const raw = fs.readFileSync(path);
    return JSON.parse(raw);
}

module.exports = { loadUsers };
