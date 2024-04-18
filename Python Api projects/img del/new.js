const url = 'https://toys-new-image.p.rapidapi.com/?type=bat';
const options = {
	method: 'GET',
	headers: {
		// Here paste your api key.
		// i am using js fetch method so make sure if you change function that should be js according
	}
};

try {
	const response = await fetch(url, options);
	const result = await response.text();
	console.log(result);
} catch (error) {
	console.error(error);
}