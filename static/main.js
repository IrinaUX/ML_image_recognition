

var fileSelect = document.getElementById("file-upload");

fileSelect.addEventListener("change", fileSelectPreviewFile, false);


function fileSelectPreviewFile(e) {
  
  var files = e.target.files || e.dataTransfer.files;
 
  for (var i = 0, f; (f = files[i]); i++) {
    previewFile(f);

  }
}
// Get HTML elements as variables to JavaScript
var imagePreview = document.getElementById("image-preview");
var imageDisplay = document.getElementById("image-display");
var uploadCaption = document.getElementById("upload-caption");
var predResult = document.getElementById("pred-result");
var loader = document.getElementById("loader");

// Button Events

function submitImage() {
  
  console.log("submit");

  if (!imageDisplay.src || !imageDisplay.src.startsWith("data")) {
    window.alert("Please select an image before submit.");
    return;
  }

  loader.classList.remove("hidden");
  imageDisplay.classList.add("loading");

  // call the predict function of the backend
  predictImage(imageDisplay.src);
}

function clearImage() {
  
  fileSelect.value = "";

  
  imagePreview.src = "";
  imageDisplay.src = "";
  predResult.innerHTML = "";

  hide(imagePreview);
  hide(imageDisplay);
  hide(loader);
  hide(predResult);
  show(uploadCaption);

  imageDisplay.classList.remove("loading");
}

function previewFile(file) {
   
  var filereaderinstance = new FileReader();
  filereaderinstance.readAsDataURL(file);
  filereaderinstance.onloadend = () => {
    imagePreview.src = URL.createObjectURL(file);

    show(imagePreview);
    hide(uploadCaption);

    // reset
    predResult.innerHTML = "";
    imageDisplay.classList.remove("loading");

    displayImage(filereaderinstance.result, "image-display");
  };
}

// FETCH
function predictImage(image) {

  fetch("/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(image)
  })
    .then(resp => {
      if (resp.ok)
        resp.json().then(data => {
          displayResult(data);
        });
    })
    .catch(err => {
      console.log("Error occured", err.message);
      window.alert("Something went wrong.");
    });
}

function displayImage(image, id) {

  let display = document.getElementById(id);
  display.src = image;
  show(display);
}

function displayResult(data) {
 
  hide(loader);
  predResult.innerHTML = data.result;
  show(predResult);
}

function hide(el) {
 el.classList.add("hidden");
}

function show(el) {
  el.classList.remove("hidden");
}
