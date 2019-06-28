
	function zai() {
		var na= document.myform.name.value;
	    var email= document.myform.emai.value;
	    var mna= document.myform.mname.value;
	    var sa= document.myform.State.value;
	    var clas= document.myform.cls.value;
	    var age= document.myform.Age.value;
	    var ads= document.myform.Address.value;
	    var gen= document.myform.Gender.value;
		
		
	if (true) {
		    	alert(" Registeration in sucessfull")
			}	

	
	if (!na) {
		document.getElementById("lopp1").innerHTML ="! Enter name"	
		 
	}else if (!fna){
		document.getElementById("lopp2").innerHTML ="! Enter email"
		
	}
    else if (!mna){
		document.getElementById("lopp3").innerHTML ="! Enter mobile number"
		
	}
	else if (!sa){
		document.getElementById("lopp5").innerHTML ="! Enter State"
		
		
	}
	else if (!cls){
		document.getElementById("lopp6").innerHTML ="! Enter class"
		
		
	}
	else if (!age){
		document.getElementById("lopp7").innerHTML ="! Enter age"
		

	}
	else if (!ads){
		document.getElementById("lopp8").innerHTML ="! Enter Address"
		

	}
	else if (!gen){
		document.getElementById("lopp4").innerHTML ="! choose Gender"
		

	}else
			 }
	 