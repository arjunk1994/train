function validate()
  {
    var name = document.getElementById("names"); 
    var email = document.getElementById("emailid");
    var age = document.getElementById("age");
    var mobileno = document.getElementById("mobileno");

    var address= document.getElementById("address");


    if (name.value == "")                                  
    { 
        window.alert("Enter your name."); 
        name.focus(); 
        return false; 
    } 
    if (email.value.indexOf("@", 0) < 0)                 
    { 
        window.alert("Enter a valid e-mail address."); 
        email.focus(); 
        return false; 
    } 
   
    if (email.value.indexOf(".", 0) < 0)                 
    { 
        window.alert("Enter a valid e-mail address."); 
        email.focus(); 
        return false; 
    } 

    if (age.value > 110)                                  
    { 
        window.alert("Enter the valid age."); 
        age.focus(); 
        return false; 
    } 
    if (mobileno.length >= 12 )                                  
    { 
        window.alert("Phone number is not required"); 
        mobileno.focus(); 
        
    } 
     if (address.value == "")                                  
    { 
        window.alert("Enter your Address."); 
        address.focus(); 
        return false; 
    } 


  }