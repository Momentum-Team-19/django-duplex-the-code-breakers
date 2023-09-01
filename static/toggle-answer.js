const promptBox = document.getElementById('promptBox');
const answerBox = document.getElementById('answerBox');

promptBox.addEventListener("click", function() {
    if (answerBox.style.display === "none") {
        answerBox.style.display = "flex";
    } else {
        answerBox.style.display = 'none';
    }
});
