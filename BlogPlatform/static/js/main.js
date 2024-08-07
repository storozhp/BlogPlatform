document.addEventListener("DOMContentLoaded", function () {
  const flashMessages = document.querySelectorAll(".flash");
  flashMessages.forEach(function (message) {
    setTimeout(function () {
      message.style.transition = "opacity 0.5s ease-out";
      message.style.opacity = "0";
      setTimeout(function () {
        message.remove();
      }, 500);
    }, 2500); // 20000 milliseconds = 20 seconds
  });
});
