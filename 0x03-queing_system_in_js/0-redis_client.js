import { createClient } from "redis";

const clinet = createClient();

clinet.on('connect', () => {
    console.log('Redis client connected to the server');
});

clinet.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});
