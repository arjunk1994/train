$(document).ready(function(){

		$("#dis").hide();
		var id=0;
		
		
		$('#b1').click(function(){
			

					id=id+1;
			savemultiple(id);
		}
		)
		
		
		$('#b2').click(function(){
			save();
		})		
		
		$('#b4').click(function()
		{
			$("#dis").show();
			displayMultiply();
		})
		$("#b3").click(function() 
		{
    		deleteMultiply();
		});

		function save()
		{
			if (typeof(Storage) !== "undefined")
			 {
			 	var id=localStorage.length;
				if($('#name').val()!=="" && $('#age').val()!==""){
					localStorage.setItem("Sid",id);
					localStorage.setItem("Fname",$('#fname').val());
					localStorage.setItem("Lname",$('#lname').val());
					localStorage.setItem("Mobile",$('#mobile').val());
					localStorage.setItem("Email",$('#email').val());
					localStorage.setItem("Phone",$('#phone').val());
					localStorage.setItem("Year",$('#year').val());

					alert("Record saved successfully");
				}
			}
			else {
  				$('#s1').html("Sorry, your browser does not support Web Storage...");
			}
		}
		function savemultiple(id)
		{
			if (typeof(Storage) !== "undefined")
			 {
				if($('#name').val()!=="" && $('#age').val()!==""){
					var sid=("Sid",$('#sid').val());
					var fname=$('#fname').val();
					var lname=$('#lname').val();
					var mname=$('#mname').val();
					var mobile=$('#mobile').val();
					var email=$('#email').val();
					var phone=$('#phone').val();
					var pemail=$('#pemail').val();
					var year=$('#year').val();
					
					
					var array=[];
					array.push(sid,fname,lname,mname,mobile,email,phone,pemail,year);
					localStorage.array+=JSON.stringify({"Sid":id,"Fname":fname,"Lname":lname,"Mobile":mobile,"Email":email,"Phone":phone,"Pemail":pemail,"Year":year})
					
					alert("Saved");
				}
			}
			
		}
		function display()
		{

			console.log(localStorage.key(2));
			$('#view').show();	
			if (typeof(Storage) !== "undefined")
			 {

					$('#ssid').val(localStorage.getItem("Sid"));
					$('#sfname').val(localStorage.getItem("Fname"));
					$('#slname').val(localStorage.getItem("Lname"));	
					$('#smobile').val(localStorage.getItem("Mobile"));	
					$('#semail').val(localStorage.getItem("Email"));	
					$('#sphone').val(localStorage.getItem("Phone"));
					$('#syear').val(localStorage.getItem("Year"));	
							
									
			}
		
	}
	function displayMultiply()
	{
		
    	for(let i=0;i<localStorage.length;i++)
			{
				var key=localStorage.key(i);
				var value=localStorage.getItem(key);
				console.log(key+""+value);
				disp.innerHTML+=`${key}: ${value}</br>`;
				// var data +=`${key}: ${value}`;
				// var cata = JSON.parse(data);
				
				
			}
	}
	function deleteMultiply()
	{
		
 
			window.localStorage.clear();
	}

});
