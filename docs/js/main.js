
(function ($) {
    "use strict";
	
	new WOW().init();
	
	jQuery(document).ready(function($){	
	
	// one page nav
	$('#nav').onePageNav({
	    currentClass: 'current',
	    changeHash: true,
	    scrollSpeed: 1500,
	    scrollThreshold: 0.5,
	    filter: ':not(.external)',
	    easing: 'swing',
	    begin: function() {
	        //I get fired when the animation is starting
	    },
	    end: function() {
	        //I get fired when the animation is ending
	    },
	    scrollChange: function(jQuerycurrentListItem) {
	        //I get fired when you enter a section and I pass the list item of the section
	    }
	});	
	

	//  main slider
	var mainSlider = $('#main_slider');
	
	/*----- main slider -----*/
	mainSlider.nivoSlider({
		directionNav: true,
		animSpeed: 500,
		slices: 18,
		pauseTime: 50000000,
		pauseOnHover: false,
		controlNav: true,
		prevText: '<i class="fa fa-angle-left nivo-prev-icon"></i>',
		nextText: '<i class="fa fa-angle-right nivo-next-icon"></i>'
	});	

	// Owl Carousel for Team	
	var teamCarousel = $('.team_carousel');
    teamCarousel.owlCarousel({
        loop:false,
        autoplay:false,
        dots:false,
		margin:30,
        responsive:{
            0:{
                items:1
            },
            400:{
                items:1
            },
            600:{
                items:2
            },
            992:{
                items:4
            }
        }
    });			
	
	// Owl Carousel for Testimonials	
	var testiCarousel = $('.testimonials_carousel');
    testiCarousel.owlCarousel({
        loop:false,
        autoplay:false,
        dots:false,
        responsive:{
            0:{
                items:1
            },
            400:{
                items:1
            },
            600:{
                items:1
            },
            992:{
                items:1
            }
        }
    });		

  // Owl Carousel for Services	
	var serCarousel = $('.service_carousel');
    serCarousel.owlCarousel({
        loop:false,
        autoplay:false,
        dots:false,
		margin:30,
        responsive:{
            0:{
                items:1
            },
            400:{
                items:1
            },
            600:{
                items:2
            },
            992:{
                items:4
            }
        }
    });  
	
	// Owl Carousel for Clients	
	var clientCarousel = $('.clients_carousel');
    clientCarousel.owlCarousel({
        loop:false,
        autoplay:false,
        dots:false,
		margin:30,
        responsive:{
            0:{
                items:3
            },
            400:{
                items:4
            },
            600:{
                items:5
            },
            992:{
                items:6
            }
        }
    });	
	
	// Owl Carousel for Related Portfolioss	
	var relatedCarousel = $('.related_port_carousel');
    relatedCarousel.owlCarousel({
        loop:false,
        autoplay:false,
        dots:false,
		margin:30,
        responsive:{
            0:{
                items:1
            },
            400:{
                items:2
            },
            600:{
                items:3
            },
            992:{
                items:4
            }
        }
    });
	
  });		
  
  
		
		
    // jQuery MixItUp
    $('.work_all_item').mixItUp();
	
	    // jQuery Lightbox
    $('.lightbox').venobox({
        numeratio: true,
        infinigall: true
    });

	$(window).on("load", function() {
		 parallaxInit();
	});	
	/*=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
		Parallax
	-=-=-=-=-=-=-=-=-=--=-=-=-=-=-*/
	function parallaxInit() {
		"use strict";
		$(".parallax1").parallax("50%", 0.3);
		$(".parallax2").parallax("50%", 0.3);
		$(".parallax3").parallax("50%", 0.3);
		$(".parallax4").parallax("50%", 0.3);
	}

	/*=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
		Skill charts
	-=-=-=-=-=-=-=-=-=--=-=-=-=-=-*/          
	$('.chart-item').appear(function () {
		$('.chart-three').easyPieChart({
			easing: 'easeOutBounce',
			trackColor: 'rgba(0,0,0,0.1)',
			barColor: "#2558AA",
			lineCap: "round",
			size: "210",
			scaleColor: false,
			lineWidth: 10,
			animate: 2000,
			onStep: function (from, to, percent) {
				$(this.el).find('.percent').text(Math.round(percent));
			}
		});
	});
/*---------------------
 statistics-counter
--------------------- */	
    $('.statistics-counter').counterUp({
        delay: 50,
        time: 3000
    });	
		
    /*-----------------------------
    Loader activation here. 
    -------------------------------*/
    $("#fakeloader").fakeLoader({
        timeToHide:1500, 
        zIndex:999999, 
        spinner:"spinner1",   //Options: 'spinner1', 'spinner2', 'spinner3', 'spinner4', 'spinner5', 'spinner6', 'spinner7' 
        bgColor:"#ffffff"
    });	
	/*----------------------------------------------------*/
	/*	ScrollUp
	/*----------------------------------------------------*/

	$.scrollUp({
		scrollText: '<i class="fa fa-angle-up"></i>',
		easingType: 'linear',
		scrollSpeed: 900,
		animation: 'fade'
	});		
})(jQuery);