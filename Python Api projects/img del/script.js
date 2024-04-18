document.addEventListener("DOMContentLoaded", function() {
    const seeNewImageButton = document.getElementById("see-new-image");
    const toyImageElement = document.getElementById("toy-image");

    seeNewImageButton.addEventListener("click", function() {
        fetchToyImage();
    });

    async function fetchToyImage() {
        const url = "https://toys-new-image.p.rapidapi.com/?type=bat";

        const options = {
            method: 'GET',
            headers: {
                
            }
        };

        try {
            const response = await fetch(url, options);
            const data = await response.json();
            if (data.success) {
                toyImageElement.src = data.url;
            } else {
                console.error("Failed to fetch toy image.");
            }
        } catch (error) {
            console.error("Error fetching toy image:", error);
        }
    }

    // Fetch initial toy image
    fetchToyImage();
});
