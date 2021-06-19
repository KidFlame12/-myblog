


function take_snapshot(){
    save('myFilterimage.png');
}




function preload() {
   }


function setup()  {
    canvas = CreateCanvas(640, 480);
    canvas.position(110, 250);
    video = createCapture(VIDEO);
    video.size(300,300)
    video.hide();


    poseNet = ml5.poseNet(video,modelloaded);
    poseNet.on('pose', gotPoses);
tint_color = "";
}


function draw()  {
    image(video, 0, 0, 640, 480);
    tint(tint_color);
}

function take_snapshot(){
    save('student_name.png');
}

function filter_tint()
{
    tint_color = document.getElementById("color_name").value;
}

function draw() {
    image(video, 0, 0,300, 300);
}
function modelloaded()