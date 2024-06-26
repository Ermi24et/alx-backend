function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) throw Error('Jobs is not an array');

    const queName = 'push_notification_code_3';

    jobs.forEach((jobFormat) => {
        const job = queue.create(queName, jobFormat);

        job.save((err) => {
            if (!err) console.log(`Notification job created: ${job.id}`);
        });

        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
        });

        job.on('failed', (error) => {
            console.log(`Notification job ${job.id} failed: ${error}`);
        });

        job.on('progress', (progress) => {
            console.log(`Notification job ${job.id} ${progress}% complete`);
        });
    });
}

export default createPushNotificationsJobs;
