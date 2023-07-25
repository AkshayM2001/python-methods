const hamburger = document.querySelector(".hamburger");
const navmenu = document.querySelector(".nav-menu");

hamburger.addEventListener("click", () =>{
    hamburger.classList.toggle("active");
    navmenu.classList.toggle("active");
})


// NAVBAR ENDED

// LOGIN PAGE SWITCH METHOD

let color = ["#222f3e", "#f368e0", "#ee5253", "#0abde3", "#10ac84", "#5f27cd"];

let i = 0;
document.querySelector(".button").addEventListener("click",
function(){
    i= i < color.length ? ++i : 0;
    document.querySelector(".log-back").style.background = color[i]
    
});


// RELOD NOTIFICATION

// window.addEventListener('beforeunload', function(e) {
//     e.preventDefault();
//     e.returnValue = '';
// });


// ENDED RELOD NOTIFICATION


// SEE PASSWORD CHANGING PASS TO TEXT 

// const check = document.querySelector(".check");
// const pass = document.querySelector(".bu2");

// check.onclick = togglePassword;

// function togglePassword(){
// if (check.checked) pass.type = "text";
// else pass.type = "password";
// }