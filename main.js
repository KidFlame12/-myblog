player1_name = localStorage.getItem("player1_name"); 
player2_name = localStorage.getItem("player2_name"); 
player1_score = 0;
player2_score = 0;
document.getElementById("player1_name").innerHTML = player1_name + " : ";
 function send() {
     get_word = document.getElementById("word").value;
     word = get_word
 }