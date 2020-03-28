
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
	sendHttpRequest('GET', 'http://127.0.0.1:5000/api/trail').then(responseData => {
		const data = responseData;

		data.forEach((trail) => addTrailToList(trail)); 
		});
};

function sendJSON() {
	let name = document.querySelector('#name').value;
	let distance = document.querySelector('#distance').value;
	let neighborhood = document.querySelector('#neighborhood').value;
	let trail_status = document.querySelector('#trail-status').value;
	let json = {'name': name,
				'neighborhood': neighborhood,
				'distance': 3,
				'status': false,
				}
	console.log(json);
	sendHttpRequest('POST', 'http://127.0.0.1:5000/api/trail', json);
};

function deleteTrail(trail_id) {
	sendHttpRequest('DELETE', `http://127.0.0.1:5000/api/trail/${trail_id}`).then(responseData => {
		const data = responseData;
		console.log(data);
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
		<td><button type="button" name="delete" class="btn btn-primary btn-sm" id=${trail.id}>Delete</button></td>
	`;

	list.appendChild(row);

};


document.addEventListener('DOMContentLoaded', getJSON());

document.querySelector('#trails-table').addEventListener('click', function(e) {
	if(e.target.name == 'delete'){
		trail_id = e.target.id;
		deleteTrail(trail_id);
	};
});

document.querySelector('#add').addEventListener('click', (e) => { 
	e.preventDefault();
	sendJSON();
});


