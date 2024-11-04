button = document.getElementById("btn-user");
userMenu = document.getElementById("user-menu");
button.addEventListener("click", (e) => {
  e.stopPropagation();
  if (userMenu.style.display === "none" || userMenu.style.display === "") {
    userMenu.style.display = "block";
  } else {
    userMenu.style.display = "none";
  }
});
window.addEventListener("click", (event) => {
  if (event.target !== button && !userMenu.contains(event.target)) {
    userMenu.style.display = "none";
  }
});

const messages = document.getElementById("messages");
setTimeout(function () {
  messages.style.display = "none";
}, 3000);
