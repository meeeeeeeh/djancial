jQuery(document).ready(function($) {
	
	"use strict";
	


//------- remove class active on body
$("body *").not('.top-area > .setting-area > li > a').on("click", function() {
	$(".top-area > .setting-area > li > div").not('.searched').removeClass('active');
	
 });
	

//--- user setting dropdown on topbar	
$('.user-img').on('click', function() {
	$('.user-setting').toggleClass("active");
});	
	
//--- side message box	
$('.friendz-list > li, .chat-users > li').on('click', function() {
	$('.chat-box').addClass("show");
	return false;
});	
	$('.close-mesage').on('click', function() {
		$('.chat-box').removeClass("show");
		return false;
	});	
	
//------ scrollbar plugin
	if ($.isFunction($.fn.perfectScrollbar)) {
		$('.dropdowns, .twiter-feed, .invition, .followers, .chatting-area, .peoples, #people-list, .chat-list > ul, .message-list, .chat-users, .left-menu').perfectScrollbar();
	}




//progress line for page loader
	$('body').show();
	NProgress.start();
	setTimeout(function() { NProgress.done(); $('.fade').removeClass('out'); }, 2000);
	
//--- bootstrap tooltip	
	$(function () {
	  $('[data-toggle="tooltip"]').tooltip();
	});
	
// Sticky Sidebar & header
	if($(window).width() < 769) {
		jQuery(".sidebar").children().removeClass("stick-widget");
	}

	if ($.isFunction($.fn.stick_in_parent)) {
		$('.stick-widget').stick_in_parent({
			parent: '#page-contents',
			offset_top: 60,
		});

		
		$('.stick').stick_in_parent({
		    parent: 'body',
            offset_top: 0,
		});
		
	}
	
/*--- topbar setting dropdown ---*/	
	$(".we-page-setting").on("click", function() {
	    $(".wesetting-dropdown").toggleClass("active");
	  });	
	  
/*--- topbar toogle setting dropdown ---*/	
$('#nightmode').on('change', function() {
    if ($(this).is(':checked')) {
        // Show popup window
        $(".theme-layout").addClass('black');	
    }
	else {
        $(".theme-layout").removeClass("black");
    }
});



	
//---- responsive header
	
$(function() {

	//	create the menus
	$('#menu').mmenu();
	$('#shoppingbag').mmenu({
		navbar: {
			title: 'General Setting'
		},
		offCanvas: {
			position: 'right'
		}
	});

	//	fire the plugin
	$('.mh-head.first').mhead({
		scroll: {
			hide: 200
		}
		
	});
	$('.mh-head.second').mhead({
		scroll: false
	});

	
});		

//**** Slide Panel Toggle ***//
	  $("span.main-menu").on("click", function(){
	     $(".side-panel").toggleClass('active');
		  $(".theme-layout").toggleClass('active');
		  return false;
	  });

	  $('.theme-layout').on("click",function(){
		  $(this).removeClass('active');
	     $(".side-panel").removeClass('active');
	  });


	
// Responsive nav dropdowns
	$('.offcanvas-menu li.menu-item-has-children > a').on('click', function () {
		$(this).parent().siblings().children('ul').slideUp();
		$(this).parent().siblings().removeClass('active');
		$(this).parent().children('ul').slideToggle();
		$(this).parent().toggleClass('active');
		return false;
	});	
	


});//document ready end





