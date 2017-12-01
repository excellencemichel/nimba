      $(function(){
        // var varia = $(".description").css("color", "red");
        // console.log(varia);

        $("img").mouseover(function(){

          // if($(this).attr(title)=="") return false;

        // var bulletext = ($(this).next().text()) ;
        var bulle = $(this).next() ;

        bulle.append($(this).attr("title"));

        $(this).attr("title","");


        var posTop = $(this).offset().top-$(this).width() +17;
        var posLeft = $(this).offset().left-$(this).width()/2-bulle.width()/2;

        // console.log(posTop);
        // console.log(bulle.html());

        bulle.css({
          top:posTop,
          left:posLeft,
          opacity:0

        });


        bulle.animate({
          top:posTop,
          opacity:0.99

        });


    });



     $("img").mouseout(function(){

        var bulle = $(this).next() ;

        $(this).attr("title", bulle.text());
        // bulle.animate(
        // {
        //   top:bulle.offset().top+10,
        //   opacity:0
        // },500, "linear");
        bulle.html("");
        





    });

      });