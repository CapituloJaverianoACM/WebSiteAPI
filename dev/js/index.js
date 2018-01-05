//import owlCarousel from 'owl.carousel';
import $ from 'jquery';
import './libs/prognroll';
import scrollify from 'jquery-scrollify';
import './libs/owl.carousel.min.js';

$("body").prognroll({
	height: 2,
	color: "#0D91CF"
});

if(scrollPage) {
	$.scrollify({
		section : ".acm-full-section, .acm-maincover",
		interstitialSection : ".footer",
		easing: "easeOutExpo",
		scrollSpeed: 600,
		scrollbars: true,
		standardScrollElements: "",
		setHeights: false,
		touchScroll:false
	});
}

$('#navbarTrigger').on('click', function() {
	var nav = $(this).attr('target');
	$(nav).slideToggle();
});

$('.acm-modal').hide();

$('.acm-modal_close').on('click', function() {
	var target = $(this).attr('target');
	$(target).fadeOut();
});

$('.acm-modal_trigger').on('click', function() {
	var target = $(this).attr('target');
	$(target).fadeIn();
});

$('.acm-awards, .acm-teams, .acm-modal_carousel .acm-modal_content').owlCarousel({
	loop: true,
	responsive:{
		0: {
			items: 1
		},
		600: {
			items: 2
		},
		1000: {
			items: 3
		},
		1200: {
			items: 4
		},
		1500: {
			items: 5
		}
	}
})

$('.acm-activities').owlCarousel({
	loop: true,
	items: 1,
	autoplay: true,
	autoplayHoverPause: true
})
