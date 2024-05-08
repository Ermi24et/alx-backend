const kue = require('kue');
const que = kue.createQueue();

const jobInfo = {
    phoneNumber: '06766733',
    message: 'This is the code to verify your account',
};

const queName = 'push_notification_code';

const job = que.create(queName, jobInfo).save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
    console.log('Notification job completed');
});

job.on('failed', () => {
    console.log('Notification job failed');
})