
	function zai() {
		var na= document.getElementById("name").value;
	    var email= document.getElementById("emai").value;
	    var mna= document.getElementById("mname").value;
	    var sa= document.getElementById("State").value;
	    var clas= document.getElementById("cls").value;
	    var age= document.getElementById("Age").value;
	    var ads= document.getElementById("Address").value;
	    var gen= document.getElementById("Gender").value;
	    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
        if(email.value.match(mailformat))
{        				    
		 if (email&&mna&&sa&&cls&&Age&&ads&&na&&gen) {
		    	alert(" Registeration in sucessfull")
			}
			 }
	 
	
		
		

	if (true) {	
	if (!na) {
		document.getElementById("lopp1").innerHTML ="! Enter name"	
		 
	}
	if (!fna){
		document.getElementById("lopp2").innerHTML ="! Enter email"
		
	}
    if (!mna){
		document.getElementById("lopp3").innerHTML ="! Enter mobile number"
		
	}
	if (!sa){
		document.getElementById("lopp5").innerHTML ="! Enter State"
		
		
	}
	if (!cls){
		document.getElementById("lopp6").innerHTML ="! Enter class"
		
		
	}
	if (!age){
		document.getElementById("lopp7").innerHTML ="! Enter age"
		

	}
	if (!ads){
		document.getElementById("lopp8").innerHTML ="! Enter Address"
		

	}
	if (!gen){
		document.getElementById("lopp4").innerHTML ="! choose Gender"
		

	}
	 if(email.value.match(mailformat))
{ 
	
	}
	else{

	}	
	
}
