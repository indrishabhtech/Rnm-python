document.addEventListener("DOMContentLoaded", function() {
    const seeNewImageButton = document.getElementById("see-new-image");
    const toyImageElement = document.getElementById("toy-image");

    seeNewImageButton.addEventListener("click", function() {
        fetchToyImage();
    });

    async function fetchToyImage() {
        const url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly";

        const options = {
            method: 'GET',
            headers: {
                "X-RapidAPI-Key": "076439c01cmsh83529df627792f6p1742d3jsnfb2e4eed7953",
                "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
            }
        };

        try {
            const response = await fetch(url, options);
            const data = await response.json();
            if (data.success) {
                toyImageElement.src = data.url;
            } else {
                console.error("Failed to fetch Wether location image.");
            }
        } catch (error) {
            console.error("Error fetching toy image:", error);
        }
    }

    // Fetch initial toy image
    fetchToyImage();
});
