function populateCountries(){


    let dropdown = $('#ld');

    dropdown.empty();
    
    dropdown.append('<option selected="true" disabled>Choose Country</option>');
    dropdown.prop('selectedIndex', 0);
    
    const url = 'http://battuta.medunes.net/api/country/all/?key=0c5882d3537bb027ab201d08bbcde432';
    
    $.getJSON(url, function (data) { 
      $.each(data, function (key, entry) {
        dropdown.append($('<option></option>').attr('value', entry.code).text(entry.name));
      })
    });
}

 
