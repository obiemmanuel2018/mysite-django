function changeColor(current) {

    // if (current == "whatsapp") {

    //     icons.style.background = 'linear-gradient(#ffff,#25d366)'

    // } else if (current == "instagram") {

    //     icons.style.background = 'linear-gradient(#FEDA77 2%,#F58529,#DD2A7B,#8134AF,#515BD4)'

    // } else if (current == "facebook") {

    //     icons.style.background = 'linear-gradient(#4267B2,#ffff)'
    // } 
    if (current == "gmail") {
        icons.style.background = 'linear-gradient(#EEEEEE, #B23121)'
    } else if (current == '') {
        icons.style.background = "white";

    }
}


function scrollDown() {
    window.scroll(0, 500);
}

function scrolling() {

    if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {

        document.getElementById('main').style.overflow = 'scroll'


    } else {

        document.getElementById('main').style.overflow = 'hidden'

    }



}