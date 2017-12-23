$("body").prognroll({
	height: 2,
	color: "#0D91CF"
});

if(scrollPage) {
	$.scrollify({
		section : ".acm-section, .acm-maincover",
		interstitialSection : ".footer",
		easing: "easeOutExpo",
		scrollSpeed: 600,
		scrollbars: true,
		standardScrollElements: "",
		setHeights: false,
		touchScroll:false
	});
}

$('.acm-awards').owlCarousel({
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

$('#navbarTrigger').on('click', function() {
	var nav = $(this).attr('target');
	$(nav).slideToggle();
});
