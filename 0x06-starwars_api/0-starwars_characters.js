#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
	const filmId = process.argv[2];
	request(`${API_URL}/films/${filmId}/`, (err, _, body) => {
		if (err) {
			console.error(err);
			return;
		}

		const charactersURL = JSON.parse(body).characters;
		const charactersName = charactersURL.map(url =>
			new Promise((resolve, reject) => {
				request(url, (promiseErr, __, charactersReqBody) => {
					if (promiseErr) {
						reject(promiseErr);
						return;
					}
					resolve(JSON.parse(charactersReqBody).name);
				});
			})
		);

		Promise.all(charactersName)
			.then(names => console.log(names.join('\n')))
			.catch(allErr => console.error(allErr));
	});
}
