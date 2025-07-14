// static/js/script.js

const shakeBtn = document.getElementById("shake-btn");

shakeBtn.addEventListener("click", function() {
  shakeBtn.classList.add("shaking");
  setTimeout(() => {
    shakeBtn.classList.remove("shaking");
  }, 500);
});
