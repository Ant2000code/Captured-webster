
    
    function openNav() {
      document.getElementById("mySidebar").style.width = "250px";
      document.getElementById("main").style.marginLeft = "250px";
    }
    
    function closeNav() {
      document.getElementById("mySidebar").style.width = "0";
      document.getElementById("main").style.marginLeft= "0";
    }
    function accAns()
    {
      if(taken=='on')
      alert("hello");
    }
    $(document).ready(function(){
    $(".saveques").on('click',function(){
      
        var quesid=$(this).data('answer');
        //Ajax request
        $.ajax({
          url:"/check",
          type:"post",
          data:{
            
            ques_id:quesid,
            csrfmiddlewaretoken:"{{csrf_token}}"
            
          },
          dataType:'json',
          beforeSend:function(){
            $(".saveques").addClass('disabled').text('saving...');
            
          },
          success:function(res){
            console.log(res);

             if(res.save==1){

             alert("Your question has been saved successfully! You can work on it in the working section!");  
             $(".saveques").text('Saved!Check your working section.');
             
              
            }
            if(res.save==0){
              alert("Sorry this question has been expired you are not allowed to access it now!"); 
              $(".saveques").text('Expired');
            }
            if(res.save==2){
              alert("You are already working on a question! Only one question can be worked upon at one time!"); 
              $(".saveques").removeClass('disabled').text('Accept and Save').css("font-weight","bold");
            }
            
          }

      
        });
    });
    
  });


    