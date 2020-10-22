function openNav() {
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
  }
  
  function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
  }

  function myFunction(){
      

      alert("Answer has been Submitted");

  }
  var doc = new jsPDF(); 
  var specialElementHandlers = { 
  '#editor': function (element, renderer) { 
  return true; 
  } 
  };
  $("#submit").click(function () { 
  doc.fromHTML($("#content").html(), 15, 15, { 
  'width': 190, 
  'elementHandlers': specialElementHandlers 
  }); 
  doc.save('sample-page.pdf'); 
  });