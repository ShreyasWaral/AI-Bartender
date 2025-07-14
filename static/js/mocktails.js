
const mixBtn = document.getElementById("mix-btn");

mixBtn.addEventListener("click", function() {
  mixBtn.classList.add("shaking");
  setTimeout(() => {
    mixBtn.classList.remove("shaking");
  }, 500);
});
