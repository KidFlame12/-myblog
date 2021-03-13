

function getData() {firebase.database().ref("/").on('value', function(snapshot) {document.getElementById("output").innerHTML = "";snapshot.forEach(function(childSnapshot) {childKey  = childSnapshot.key;
       Room_names = childkey;
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
