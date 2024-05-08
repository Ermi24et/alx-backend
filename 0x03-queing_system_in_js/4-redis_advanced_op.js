import { createClient } from "redis";
const redis = require('redis');

const client = createClient();

client.connect();

client.on('error', (error) => console.error(`Redis client not connected to the server: ${error.message}`));
client.on('connect', () => console.log('Redis connected to the server'));

const key = 'HolbertonSchools';
const states = ['Portland', 'Seatle', 'New York', 'Bogota', 'Cali', 'Paris'];
const val = [50, 80, 20, 20, 40, 2];

states.forEach((k, i) => {
  client.hSet(key, k, val[i], redis.print);
});

client.hGetAll(key, (err, value) => {
  console.log(value);
});
