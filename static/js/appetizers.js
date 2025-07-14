const form = document.querySelector("form");
form.addEventListener("submit", () => {
  form.classList.add("shaking");
  setTimeout(() => {
    form.classList.remove("shaking");
  }, 500);
});
