$(function (){
    var $ords= $('#ords')
    $.ajax({
        type: 'GET',
        url: 'https://jsonplaceholder.typicode.com/posts',
        success : function(ords){
            $.each(ords ,function(i , ord){
                $ords.append('<li>userId:'+ord.userId+' ID :'+ord.id+' Title:'+ord.title+ 'Body :' +ord.body+'</li>');
            });
           
        }

    });
});