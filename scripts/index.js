 var count = 0;
  var colours = ['#749FDD', '#98d3e6', '#46ced8', '#62eaba', '#aceaa4', '#907DF0', '#C2A9DB', '#4984C4', '#00AB97'];

  function addRectangle() {
    var circle = Math.floor(Math.random()*2);
//    alert(circle);
    var random_colour = colours[Math.floor(Math.random()*colours.length)];
    $('#square_parent').append('<div class="rectangle" style="background-color: '+random_colour+'; ' +
                               'border-radius: '+ 50*circle +'%;"></div>');
    count++;
  }