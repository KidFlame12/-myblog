function add() {
    background_ImgTag = new Image();
    background_ImgTag.onload = uploadbackground;
   background_ImgTag.src = background_image 
}
rover_ImgTag = new Image();
    rover_ImgTag.onload = uploadrover;
   Rover_ImgTag.src = rover_image
function uploadbackground() {
    ctx.drawImage(rover_imgTag, rover_x, rover_y, rover_width, rover_height);
}
   window.addEventListener("keydown",mykeydown);
function mykeydown (e)
{
    keypressed = e.keycode;
    console.log(keypressed);
    if(keypressed == '38')
   {
    up();
    console.log("up");
   }
   if(keypressed == '40');
   {
    down();
    Console.log("down");
}
if(keypressed == '37')
    {
      left();
    console.log("left");
}
if(keypressed == '39')
{
    right();
    console.log("right");
}
}

function up()
{
    if(rover_y >==0)
    {
        rover_y -= 10;
        console.log("when up arrow is pressed =  " + rover_x + rover_y);
        uploadbackground();
        uploadrover();

    }
}