// home.js

document.addEventListener("DOMContentLoaded", () => {
  const spiritsBtn = document.getElementById("spirits-btn");
  const mocktailsBtn = document.getElementById("mocktails-btn");
  const appetizersBtn = document.getElementById("appetizers-btn");

  if (spiritsBtn) {
    spiritsBtn.addEventListener("click", () => {
      // You could add fancy effects here too
      window.location.href = "/cocktails";
    });
  }

  if (mocktailsBtn) {
    mocktailsBtn.addEventListener("click", () => {
      window.location.href = "/mocktails";
    });
  }

  if (appetizersBtn) {
    appetizersBtn.addEventListener("click", () => {
      window.location.href = "/appetizers";
    });
  }
});
