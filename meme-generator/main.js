// Selecting elements from the HTML document
const generateMemeBtn = document.querySelector(".meme-generator .generate-meme-btn")
const memeImage = document.querySelector(".meme-generator img");
const memeTitle = document.querySelector(".meme-generator .meme-title");
const memeAuthor = document.querySelector(".meme-generator .meme-author");

// Function to update meme details in the HTML
const updateDetails = (url, title, author) => {
    memeImage.setAttribute("src", url)
    memeTitle.innerHTML = title;
    memeAuthor.innerHTML = `Meme by: ${author}`;
}

// Function to generate a meme by fetching data from an API
const generateMeme = () => {
    fetch("https://meme-api.com/gimme/wholesomememes")
    .then((response) => response.json())
    .then(data => {
        updateDetails(data.url, data.title, data.author)
    });
};

// Event listener to generate a meme when the button is clicked
generateMemeBtn.addEventListener("click", generateMeme);

generateMeme();
