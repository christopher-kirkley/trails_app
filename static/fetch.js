document.getElementById('add').addEventListener
('click', getText);

function getText(e){

	e.preventDefault();
	// fetch('http://localhost:5000/api/trail')
	// .then(function(res){
	// 	return res.text();
	// })
	// .then(function(data){
	// 	console.log(data);
	// });

	
};
	

document.addEventListener('DOMContentLoaded', () => {
	getJSON();
});

function getJSON() {
	fetch('http://localhost:5000/api/trail', { method: 'GET' })
	.then((res) => res.json())
	.then((data) => {
		data.forEach(function(trail){
			addTrailToList(trail);
		});
			
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
	addTrailToList(json);
	sendHttpRequest('POST', 'http://127.0.0.1:5000/api/trail', json);
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

