document.addEventListener('DOMContentLoaded', function() {
    const loginButton = document.getElementById('loginButton');
    loginButton.addEventListener('click', function() {
        window.location.href = '/login'; // Replace with your actual login URL path
    });
});
let text = document.getElementById("text");
let leaf = document.getElementById("leaf");
let hill4 = document.getElementById("hill4");
let hill5 = document.getElementById("hill5");
let tree = document.getElementById("tree");

window.addEventListener("scroll", () => {
    let scrollValue = window.scrollY;

    text.style.marginTop = scrollValue * 2 + "px";
    leaf.style.marginBottom = scrollValue * 1.5 + "px";
    leaf.style.marginLeft = scrollValue * 1.5 + "px";
    hill4.style.marginRight = scrollValue * 1.5 + "px";
    hill5.style.marginLeft = scrollValue * 1.5 + "px";
    tree.style.marginTop = scrollValue * 1.5 + "px";
})
