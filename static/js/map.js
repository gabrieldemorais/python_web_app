  var tbl = document.createElement("table");
  var leftDiv = document.getElementById("sidebar");
  for (var i = 0; i < locations.length; i++) {     
      var row = document.createElement("tr"); 
      var rowHeader = document.createElement("tr"); 

      if(i == 0)
      {  
        var cell1 = document.createElement("th");           
        var cell2 = document.createElement("th");
        var cell3 = document.createElement("th");
        var text1 = document.createTextNode('Dispositivo');
        var text2 = document.createTextNode('Conexão');
        var text3 = document.createTextNode('Status');

        cell1.appendChild(text1);
        cell2.appendChild(text2);
        cell3.appendChild(text3);
        rowHeader.appendChild(cell1);            
        rowHeader.appendChild(cell2);
        rowHeader.appendChild(cell3);
        tbl.appendChild(rowHeader);
      }  

      for (var j = 0; j < 3; j++) {  
          a = document.createElement('a');
          a.id = 'link'+i;
          a.href =  '#';            
          a.innerHTML = "XBee_"+i;
          var cellText1 = document.createTextNode("XBee_"+i);
          if(locations[i][2] == 'disconnected')
          {
            var cellText2 = document.createTextNode("desconectado");
            var cellText3 = document.createTextNode("--");
          }
          else
          {
            var cellText2 = document.createTextNode("conectado");
            if(locations[i][4] == 'lower')
            {
              if(locations[i][2] <= locations[i][3])
              {
                var cellText3 = document.createElement('b');
                cellText3.style.color = '#ff4d4d';
                var tn = document.createTextNode('alerta');
                cellText3.appendChild(tn);                
              }
              else
              {
                var cellText3 = document.createTextNode("ok"); 
              }
            }
            else 
            {
              if(locations[i][2] >= locations[i][3])
              {
                var cellText3 = document.createElement('b');
                cellText3.style.color = '#ff4d4d';
                var tn = document.createTextNode('alerta');
                cellText3.appendChild(tn);
              }
              else
              {
                var cellText3 = document.createTextNode("ok"); 
              } 
            }
          }          

          var cell = document.createElement("td");  
          if(j==0)                  
            cell.appendChild(a);
          else if(j == 1)
            cell.appendChild(cellText2);
          else
            cell.appendChild(cellText3);
          row.appendChild(cell);
      }
      tbl.appendChild(row);
  }
  leftDiv.appendChild(tbl);
  
  var c;
  
  function initMap() {
    
    
    var map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: 40.785091, lng: -73.968285},
      zoom: 8
    });

    for (i = 0; i < locations.length; i++) {  

      var info_content = 'Potenciometro: ' + locations[i][2]; 

      marker = new google.maps.Marker({
        position: new google.maps.LatLng(locations[i][0], locations[i][1]),
        map: map
      });

      var infowindow = new google.maps.InfoWindow();

      google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
          infowindow.setContent('Potenciometro: ' + locations[i][2]);
          infowindow.open(map, marker);
        }
      })(marker, i));

      c = document.getElementById('link'+i);      

      

      google.maps.event.addDomListener(c, 'click', (function(marker, i) {
        return function() {
          infowindow.setContent('Potenciometro: ' + locations[i][2]);
          infowindow.open(map, marker);         
        }
      })(marker, i));
    }
  }