

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

 