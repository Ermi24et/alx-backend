import { createClient } from "redis";

const subscriber = createClient();

subscriber.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
});

const holb = 'holberton school channel';

subscriber.subscribe(holb);

subscriber.on('message', (channel, message) => {
    if (channel === holb) console.log(message);

    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe(holb);
        subscriber.quit();
    }
});
