var i = 0;
var feynman = '"It doesn\'t matter how beautiful your theory is, it doesn\'t matter how smart you are. If it doesn\'t agree with experiment, it\'s wrong." (Feynman, 1958)'; /* The text */
var header = "Research. Made. Easy.";
var speed = 110; /* The speed/duration of the effect in milliseconds */

function typeWriter() {
  if (i < header.length) {
    document.getElementById("landing_slogan").innerHTML += header.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}

function search() {
  var query = document.getElementById("search_query").value
  
  location.replace("http://127.0.0.1:8000/search_page/" + query);
}

// Get the input field
var input = document.getElementById("search_query");

// Press search button when user presses enter
input.addEventListener("keyup", function(event) {
  // Number 13 is the "Enter" key on the keyboard
  if (event.keyCode === 13) {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a click
    document.getElementById("go").click();
  }
});

typeWriter();