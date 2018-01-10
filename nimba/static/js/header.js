var head = document.querySelector("#head") ;
var headY = head.getBoundingClientRect().height;
var header = document.querySelector(".header") ; 


window.addEventListener("scroll"  , function () {
	var scrollY = window.scrollY ;

	if (scrollY > headY) {
		if (!header.classList.contains("fixable")) {
			header.classList.add("fixable") ;
		}
	}else if (scrollY == 0 && header.classList.contains("fixable")) {
		header.classList.remove("fixable")
	}
})