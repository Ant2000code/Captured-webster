

  function validate()
  {
    var ques =document.getElementById("answer");
    if(ques.value.trim()=="")
    {
      alert("Blank Answer");
      return false;
    }

    alert("Answer has been Submitted");
    return true;
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