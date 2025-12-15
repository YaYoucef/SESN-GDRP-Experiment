const BigchainDB = require('bigchaindb-driver');
const API_PATH = 'http://bigchaindb1:9984/api/v1/';

const conn = new BigchainDB.Connection(API_PATH);

module.exports = { conn };
