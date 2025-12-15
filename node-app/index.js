const { loadUsers } = require('./usersLoader');
const { submitTransaction } = require('./operations');

const users = loadUsers();

async function simulate() {
    for (let i = 0; i < 100; i++) {
        const user = users[Math.floor(Math.random() * users.length)];
        const ops = ['CONSENT', 'ACCESS', 'RTBF'];
        const op = ops[Math.floor(Math.random() * ops.length)];

        const start = Date.now();
        await submitTransaction(user.user_id, op, user.consent);
        const latency = Date.now() - start;

        console.log(`${op} | user=${user.user_id} | latency=${latency}ms`);
    }
}

simulate();
