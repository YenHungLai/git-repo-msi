// FIXME: cannot access external network bc no billing info was set.
const functions = require('firebase-functions');
const admin = require('firebase-admin');
const axios = require('axios');

require('dotenv').config();

admin.initializeApp();

const settings = { timestampsInSnapshots: true };
admin.firestore().settings(settings);

const db = admin.firestore();

const config = {
	channelAccessToken: process.env.CHANNEL_ACCESS_TOKEN,
	channelSecret: process.env.CHANNEL_SECRET
};

exports.linebot = functions.firestore
	.document('orders/{orderId}')
	.onWrite((change, context) => {
		let observer = db.collection('orders').onSnapshot(querySnapshot => {
			let orderInfo;
			querySnapshot.docChanges.forEach(change => {
				if (change.type === 'added') {
					console.log('New order: ', change.doc.data());
					orderInfo = { type: 'New Order', data: change.doc.data() };
				}
				if (change.type === 'modified') {
					console.log('Modified order: ', change.doc.data());
					orderInfo = {
						type: 'Modified Order',
						data: change.doc.data()
					};
				}
				if (change.type === 'removed') {
					console.log('Removed order: ', change.doc.data());
					orderInfo = {
						type: 'Removed Order',
						data: change.doc.data()
					};
				}
			});

			// To me
			axios
				.post('https://api.line.me/v2/bot/message/push', null, {
					headers: {
						'Content-Type': 'application/json',
						Authorization:
							'Bearer ' + process.env.CHANNEL_ACCESS_TOKEN
					},
					data: {
						to: 'U2047b86d40d88cf8814ad5e0cb5fed27',
						messages: [
							{
								type: 'text',
								text: JSON.stringify(
									orderInfo,
									null,
									2
								).substring(0, 2000)
							}
						]
					}
				})
				.then(() => {
					console.log('Message sent successfully');
				})
				.catch(err => {
					console.error(err.response.data);
				});
			// To Allen
			axios
				.post('https://api.line.me/v2/bot/message/push', null, {
					headers: {
						'Content-Type': 'application/json',
						Authorization:
							'Bearer ' + process.env.CHANNEL_ACCESS_TOKEN
					},
					data: {
						to: 'Ubd6d3afcb7c1f5fe7a42793f8180427a',
						messages: [
							{
								type: 'text',
								text: JSON.stringify(
									orderInfo,
									null,
									2
								).substring(0, 2000)
							}
						]
					}
				})
				.then(() => console.log('Message sent successfully'))
				.catch(err => console.error(err.response.data));
        });
        
        return 1;
	});
