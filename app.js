function getDataUrl(img) {
    // Create canvas
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    // Set width and height
    canvas.width = img.width;
    canvas.height = img.height;
    // Draw the image
    ctx.drawImage(img, 0, 0);
    return canvas.toDataURL('https://testbucketirina.s3.eu-west-2.amazonaws.com/ml-image/img_cat_real.jpeg');
 }
 // Select the image
 const img = document.querySelector('#my-image');
 img.addEventListener('load', function (event) {
    const dataUrl = getDataUrl(event.currentTarget);
    console.log(dataUrl);
 });

 function upload() {
     var fileinput = document.getElementById("finput");
     var filename = fileinput.nodeValue;
     alert("Chose " + filename)
 }


 / Import the plugins
const Uppy = require('@uppy/core')
const XHRUpload = require('@uppy/xhr-upload')
const Dashboard = require('@uppy/dashboard')

// And their styles (for UI plugins)
// With webpack and `style-loader`, you can require them like this:
require('@uppy/core/dist/style.css')
require('@uppy/dashboard/dist/style.css')

const uppy = new Uppy()
  .use(Dashboard, {
    trigger: '#select-files'
  })
  .use(XHRUpload, { endpoint: 'https://api2.transloadit.com' })

uppy.on('complete', (result) => {
  console.log('Upload complete! We’ve uploaded these files:', result.successful)
})



