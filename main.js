song = "";

function setup() {
    canvas = createCanvas(600, 500)
    canvas.center();


    video = createCanvas(VIDEO);
    video.hide();

    poseNet = ml5.poseNet(video, modelLoaded);
    poseNet.on('pose', gotPoses);
}

function draw() {
   image(video, 0, 0, 600, 500); 
}

song = ""; 
leftWristX = 0;
leftWristY = 0;
rightWristX = 0;
rightWristY = 0;
function preload()
{
    song = loadSound("music.mp3") 
}

function play() {
   song.play;
   song.setvolume(1);
   song.rate(1); 
}

function modelLoaded() {
    console.log('PoseNet is Initiliazed');
}

function gotPoses(results)
{
    if(results.length > 0)
    {
        console.log(results)
         leftWristX = results[0].pose.leftWrist.x
        leftWristX = results[0].pose.leftWrist.y
        console.log("leftWristX = " + leftWristX + "leftWristY = " + leftWristY);


        leftWristX = results[0].pose.rightWrist.x
        leftWristX = results[0].pose.rightWrist.y
        console.log("rightWristX = " + rightWristX + "rightWristY = " + rightWristY);
    }
}