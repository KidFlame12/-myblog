Webcam.set({
    width:350,
    height:300,
    image_format : 'png',
    png_quality:90
    });
    
    
    camera = document.getElementById("camera");
    
    
    Webcam.attach( '#camera' );
    
    
    function take_snapshot()
    {
        Webcam.snap(function(data_uri)  {
        document.log
        })
    }
    function gotResults(error, results) {
        if(error) {
            console.error(error);
        } else {
            console.log(results)
            document.getElementById("result_sign_name").innerHTML = results[0].label;
            document.getElementById("result_sign_name2").innerHTML = results[1].label;
        } if(results[0].label == "peace")
        {
            document.getElementById("update_sign").innerHTML = "U+270C";
        }
        if(results[0].label == "ok")
        {
            document.getElementById("update_sign").innerHTML = "U+1F44C";
        }
        if(results[0].label == "thumbs up")
        {
            document.getElementById("update_sign").innerHTML = "U+1F44D;";
        }
   
        if(results[1].label == "peace")
        {
            document.getElementById("update_sign").innerHTML = "U+270C";
        }
        if(results[1].label == "ok")
        {
            document.getElementById("update_sign").innerHTML = "U+1F44C";
        }
        if(results[1].label == "thumbs up")
        {
            document.getElementById("update_sign").innerHTML = "U+1F44D";
        }
    }