const hintToggle = document.getElementById("hintToggle");
const hintContainer = document.getElementById('hintContainer');


hintToggle.addEventListener("click", function() {
    if (hintToggle.innerText === "⌄") {
        hintToggle.innerText = "^";
        hintContainer.style.display = 'none';
        hintToggle.style.top = "-5px";
    } else {
        hintToggle.innerText = "⌄";
        hintContainer.style.display = 'flex';
        hintToggle.style.top = "-18px";
    }
});
