'use strict';

let form = document.querySelector('.contactForm');
let inputs = form.querySelectorAll('input,textarea');
$.each(inputs, function(index, element) {
    let input = $(element);
    let label = $("label[for=" + input.attr("id") + "]");

    input.focus(function () {
        label.hide();
        label.addClass('hidden');
        console.log(`hidden + ${input.id}`);
    });

    input.blur(function(){
        if(!input.val()) { label.show(); }
    }); //end of blur()
});