
function sendHttpRequest(method, url, data) {
	const promise = new Promise((resolve, reject) => {
		const xhr = new XMLHttpRequest();
		xhr.open(method, url);

		xhr.responseType = 'json';

		if (data) {
			xhr.setRequestHeader('Content-Type', 'application/json');
		};
		
		xhr.onload = () => {
			resolve(xhr.response);
		};

		xhr.send(JSON.stringify(data));
	});
	return promise;
};

function getJSON() {
	sendHttpRequest('GET', 'http://127.0.0.1:5000/api/get_trails').then(responseData => {
		const data = responseData;

		data.forEach((trail) => addTrailToList(trail)); 
		});
};

function addTrailToList(trail) {
	const list = document.querySelector('#trails-table');
	
	const row = document.createElement('tr');

	row.innerHTML = `
		<td>${trail.name}</td>
		<td>${trail.distance}</td>
		<td>${trail.neighborhood}</td>
		<td>${trail.status}</td>
	`;

	list.appendChild(row);

};



document.addEventListener('DOMContentLoaded', getJSON());

