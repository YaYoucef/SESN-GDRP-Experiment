const BigchainDB = require('bigchaindb-driver');
const { v4: uuidv4 } = require('uuid');
const { conn } = require('./bigchaindbClient');

async function submitTransaction(userId, operationType, payload) {
    const keypair = new BigchainDB.Ed25519Keypair();

    const asset = {
        user_id: userId,
        operation: operationType,
        timestamp: new Date().toISOString()
    };

    const metadata = {
        payload_id: uuidv4(),
        details: payload
    };

    const tx = BigchainDB.Transaction.makeCreateTransaction(
        asset,
        metadata,
        [BigchainDB.Transaction.makeOutput(
            BigchainDB.Transaction.makeEd25519Condition(keypair.publicKey)
        )],
        keypair.publicKey
    );

    const signedTx = BigchainDB.Transaction.signTransaction(tx, keypair.privateKey);
    return conn.postTransactionCommit(signedTx);
}

module.exports = { submitTransaction };
