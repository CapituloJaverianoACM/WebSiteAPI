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
