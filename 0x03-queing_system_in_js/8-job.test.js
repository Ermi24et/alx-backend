import createPushNotificationJobs from './8-job';
import kue from 'kue';
import { expect } from 'chai';

const que = kue.createQueue();

const jobs = [
    {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
    },
    {
        phoneNumber: '4153118782',
        message: 'This is the code 4321 to verify your account',
    },
];

describe('createPushNotificationsJobs', () => {
    before(function () {
        que.testMode.enter();
    });

    afterEach(function () {
        que.testMode.clear();
    });

    after(function () {
        que.testMode.exit();
    });

    it('display a error message if jobs is not an array passing Number', () => {
        expect(() => {
            createPushNotificationJobs(2, que);
        }).to.throw('Jobs is not an array');
    });

    it('display a error message if jobs is not an array passing Object', () => {
        expect(() => {
            createPushNotificationJobs({}, que);
        }).to.throw('Jobs is not an array');
    });

    it('display a error message if jobs is not an array passing String', () => {
        expect(() => {
            createPushNotificationJobs('Hello', que);
        }).to.throw('Jobs is not an array');
    });

    it('should NOT display a error message if jobs is an array with empty array', () => {
        const res = createPushNotificationJobs([], que);
        expect(res).to.equal(undefined);
    });

    it('create two new jobs to the queue', () => {
        createPushNotificationJobs(jobs, que);
        expect(que.testMode.jobs.length).to.equal(2);
        expect(que.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(que.testMode.jobs[0].data).to.eql({
            phoneNumber: '4153518780',
            message: 'This is the code 1234 to verify your account',
        });
        expect(que.testMode.jobs[1].type).to.equal('push_notification_code_3');
        expect(que.testMode.jobs[1].data).to.eql({
            phoneNumber: '4153118782',
            message: 'This is the code 4321 to verify your account',
        });
    });
});
