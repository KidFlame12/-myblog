
//ADD YOUR FIREBASE LINKS HERE

function getData() {firebase.database().ref("/").on('value', function(snapshot) {document.getElementById("output").innerHTML = "";snapshot.forEach(function(childSnapshot) {childKey  = childSnapshot.key;
       Room_names = childKey;
      //Start code
      function adduser() {

            user_name = document.getElementById("user_name").value;
        
            localStorage.setItem("user_name", user_name);
        
            window.location = "kwitter_room.html";
        }
function addroom()  
{
      Room_name = document.getElementById("Room_name").value;
      firebase.database().ref("/").child(Room_names)
}      
      //End code
      });});}
getData();
 function send() {
     msg = document.getElementById("msg").value;
     firebase.database().ref(Room_name).push({
           name:user_name,
           message:msg,
           like:0
     });

     document.getElementById("msg").value= "";
 }
                    
 
 function getData(){
firebase.database().ref("/"+room_name).on('value',function(snapshot) {
      document.getElementById("output")
})
 }