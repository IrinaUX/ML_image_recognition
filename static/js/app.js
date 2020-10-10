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
//  // Select the image
//  const img = document.querySelector('#my-image');
//  img.addEventListener('load', function (event) {
//     const dataUrl = getDataUrl(event.currentTarget);
//     console.log(dataUrl);
//  });

//  function upload() {
//      var fileinput = document.getElementById("finput");
//      var filename = fileinput.nodeValue;
//      alert("Chose " + filename)
//  }

function readFile() {
  
  if (this.files) {
      
    var FR = new FileReader();
    
    FR.addEventListener("load", function(e) {
      document.getElementById("img").src       = e.target.result;
      document.getElementById("b64").innerHTML = e.target.result;
      console.log("Add event listener")
    }); 
      
      FR.readAsDataURL( this.files[0] );
    }
  }
  
  document.getElementById("inp").addEventListener("change", readFile);


