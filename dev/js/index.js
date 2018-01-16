//import owlCarousel from 'owl.carousel';
import $ from 'jquery';
import './libs/prognroll';
import scrollify from 'jquery-scrollify';
import './libs/owl.carousel.min.js';
import alertify from 'alertifyjs';
import getFormData from 'get-form-data';

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

$('.acm-modal_close').on('click', function() {
	var target = $(this).attr('target');
	$(target).fadeOut();
	$('body').css('overflow', 'auto');
});

$('.acm-modal').on('click', function(e) {
	if($(e.target).is('.acm-modal')) {
		var trigger = $(this).children('.acm-modal_close');
		trigger.click();
	}
});

$('.acm-modal_trigger').on('click', function() {
	var target = $(this).attr('target');
	$(target).fadeIn();
	$('body').css('overflow', 'hidden');
});

$('.acm-awards, .acm-teams, .modal_carousel').owlCarousel({
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

document.sendQuestionEmail = () => {
	const form = document.getElementById("questionform");
	const data = getFormData(form);
	$.ajax({
		type: "POST",
		url: "/sendQuestionEmail/",
		data: data,
		success: function(response) {
			console.log(response);
			alertify.success(response.state);
		}
	});
}

document.sendJoinForm = () => {
	const form = document.getElementById("joinform");
	const data = getFormData(form);
	$.ajax({
		type: "POST",
		url: "/sendJoinForm/",
		data: data,
		success: function(response) {
			console.log(response);
			alertify.success(response.state);
		}
	});
}

alertify.defaults.notifier.position = "bottom-left";
