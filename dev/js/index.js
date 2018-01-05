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

$('.acm-awards, .acm-teams').owlCarousel({
	loop:false,
	responsive:{
		0: {
			items: 1
		},
		900: {
			items: 2
		},
		1200: {
			items: 3
		}
	}
})

$('.acm-activities').owlCarousel({
	loop: true,
	items: 1,
	autoplay: true,
	autoplayHoverPause: true
})
