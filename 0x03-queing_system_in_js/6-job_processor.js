const kue = require('kue');
const que = kue.createQueue();

function sendNotification(phoneNumber, message) {
    console.log(
        `Sending notification to ${phoneNumber}, with message: ${message}`
    );
}

const queName = 'push_notification_code';

que.process(queName, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message);
    done();
});
