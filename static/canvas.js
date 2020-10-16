console.log("CANVAS.JS");

var canvas, ctx, flag = false,
prevX = 0,
currX = 0,
prevY = 0,
currY = 0,
dot_flag = false;

var x = "dark-gray",
y = 2;

var imageDisplay = document.getElementById("image-display");

console.log("Script");

function draw() {
ctx.beginPath();
ctx.moveTo(prevX, prevY);
ctx.lineTo(currX, currY);
ctx.strokeStyle = x;
ctx.lineWidth = y;
ctx.stroke();
ctx.closePath();
}    

function init() {
console.log("Script initialized");
canvas = document.getElementById('can');
console.log(canvas);
ctx = canvas.getContext("2d");
w = canvas.width;
h = canvas.height;

canvas.addEventListener("mousemove", function (e) {
    findxy('move', e)
}, false);
canvas.addEventListener("mousedown", function (e) {
    findxy('down', e)
}, false);
canvas.addEventListener("mouseup", function (e) {
    findxy('up', e)
}, false);
canvas.addEventListener("mouseout", function (e) {
    findxy('out', e)
}, false);
}

function save() {
document.getElementById("img-capture").style.border = "2px solid";
var dataURL = canvas.toDataURL();
document.getElementById("img-capture").src = dataURL;
console.log(dataURL);
document.getElementById("img-capture").style.display = "inline";
}

function findxy(res, e) {
if (res == 'down') {
    prevX = currX;
    prevY = currY;
    currX = e.clientX - canvas.offsetLeft;
    currY = e.clientY - canvas.offsetTop;

    flag = true;
    dot_flag = true;
    if (dot_flag) {
        ctx.beginPath();
        ctx.fillStyle = x;
        ctx.fillRect(currX, currY, 2, 2);
        ctx.closePath();
        dot_flag = false;
    }
}
if (res == 'up' || res == "out") {
    flag = false;
}
if (res == 'move') {
    if (flag) {
        prevX = currX;
        prevY = currY;
        currX = e.clientX - canvas.offsetLeft;
        currY = e.clientY - canvas.offsetTop;
        draw();
    }
}
}

function erase() {
ctx.clearRect(0, 0, w, h);
document.getElementById("img-capture").style.display = "none";
}

function submit(image) {
console.log("submit");
canvas = document.getElementById('can');
console.log(canvas);
var dataURL = canvas.toDataURL();
image = document.getElementById("img-capture");
image.src = dataURL;
console.log(image.src);
console.log(dataURL);
predictImage(image.src);
}

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

init();