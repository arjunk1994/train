var ph 

function auto()
{

 ph =setInterval(red1, 6000);
 red1();

}
function red1()
{	
	if (red2.style.fill=="black" && yellow2.style.fill=="black")
	 {
	red2.style.fill="red";
	yellow2.style.fill="black";
	green2.style.fill="black";
	}
	else if (red2.style.fill=="red") 
	{	
		yellow();
	}
	else if (yellow2.style.fill="yellow") 
	{
		green();
	}
}



function green()
{
	red2.style.fill="black";
	yellow2.style.fill="black";
	green2.style.fill="green";

}
function yellow()
{	
	if (yellow2.style.fill=="black") {

		red2.style.fill="black";
		yellow2.style.fill="yellow";
		green2.style.fill="black";
	}
	else{
		yellow2.style.fill="black"
	}
}
function red()
{	
	red2.style.fill="red";
	yellow2.style.fill="black";
	green2.style.fill="black";
}
function blank()
{
	red2.style.fill="black";
	yellow2.style.fill="black";
	green2.style.fill="black";
	clearInterval(ph);
	clearInterval(yu);


	red2.style.fill="black";
	yellow2.style.fill="black";
	green2.style.fill="black";
	
}
function blinkyellow()
{
	
	
	yu=setInterval(yellow, 500);
	
	yellow();

}
function allon()
{
	clearInterval(ph);
	clearInterval(yu);
	red2.style.fill="red";
	yellow2.style.fill="yellow";
	green2.style.fill="green";

}