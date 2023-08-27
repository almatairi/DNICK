// Example using vanilla JavaScript
const buyButtons = document.querySelectorAll('.buy-button');

buyButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Perform action when button is clicked, such as adding to cart
        console.log("Added to cart!");
    });
});
