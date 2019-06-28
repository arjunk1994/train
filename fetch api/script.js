// var result =document.getElementById("result");
// var cont=document.getElementById("content")
// var btn= document.getElementById("btn");
// btn.addEventListener("click",function(){
// var ourrequest = new XMLHttpRequest ();
// ourrequest.open('GET','http://services.groupkt.com/country/get/all')
// ourrequest.onload = function(){
// 	var ourdata	= JSON.parse(ourrequest.responseText);
// 	var more1 = ourdata[0];
// 	// var more2 = more1[1];

// 	console.log(more1);
// 	renderHTML(ourdata)

// };
// ourrequest.send();
// function(Data){
// 	result.insertAdjacentHTML('beforeend','htmlstring')



// };

var cont=document.getElementById("content")
var btn= document.getElementById("btn");
btn.addEventListener("click",function(){
var ourRequest=new XMLHttpRequest();
ourRequest.open('GET',"http://battuta.medunes.net/api/country/all/?key=0c5882d3537bb027ab201d08bbcde432");
ourRequest.onload=function(){
var ourData=JSON.parse(ourRequest.responseText);
renterHTML(ourData);
};
ourRequest.send();
});
function renterHTML(data){
var htmlstring='';
for(i=0;i<data.length;i++){
htmlstring+="<p> name  :"+data[i].name+"<br> code  :"+data[i].code+".</p>";
}
cont.insertAdjacentHTML('beforeend',htmlstring);
}
