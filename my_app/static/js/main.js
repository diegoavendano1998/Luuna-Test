$(document).ready(function(){
    let $btns=$('.project-area .button-group button');

    // Sort galeria proyectos
    $btns.click(function(e){
        $('.project-area .button-group button').removeClass('active');
        e.target.classList.add('active');
        let selector=$(e.target).attr('data-filter');
        $('.project-area .grid').isotope({
            filter: selector
        });
        return false;
    })

    // Alinear galeria projectos
    // $('.project-area .button-group #btn1').trigger('click');

    // Popup galeria proyectos
    $('.project-area .grid .test-popup-link').magnificPopup({
        type: 'image',
        gallery:{enabled:true}
      });


    // Carrusel clientes (0-544 cliente1, 544 < ... Cliente2)
      $('.site-main .client-area .owl-carousel').owlCarousel({
          loop:true,
          autoplay:true,
          dots:true,
          responsive:{
              0:{
                  items:1
              },
              544:{
                  items:2
              }
          }
      })

    //   Sticky navbar
    let nav_offset_top = $('.header-area').height()+50;

    function navbarFixed(){
        if($('.header-area').lenght){
            $(window).scroll(function(){
                let scroll = $(window).scrollTop();
                if(scroll >= nav_offset_top){
                    $('.header-area .main-menu').addClass('navbar-fixed');
                } else {
                    $('.header-area .main-menu').removeClass('navbar-fixed');
                }
            })
        }
    }


    navbarFixed();
});