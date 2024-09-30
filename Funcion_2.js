var electro ={};
var text = {};
if(msg.payload==1){
    electro.payload = true;
    text.payload ="REGANDO..."
}
if(msg.payload==0){
    electro.payload = false;
    text.payload = "Valvula fechada..."
}
return [electro,text];