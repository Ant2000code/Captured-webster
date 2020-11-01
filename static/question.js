
 /*validation*/
  function validate(){
      var ques =document.getElementById("question");
      if(ques.value.trim()=="")
      {
        alert("Blank Question");
        return false;
      }

      alert("Question has been Submitted");
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