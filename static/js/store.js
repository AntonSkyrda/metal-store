'use strict';

//Form logic
// Get elements
const form = document.getElementById('contact-form');
const inputFields = document.getElementById('input-fields');
const name = document.getElementById('id_name');
const phoneNumber = document.getElementById('id_phone_number');
const email = document.getElementById('id_email');
const message = document.getElementById('id_message');

// Define placeholders
const inputPlaceHolderForName = 'Імʼя';
const inputPlaceHolderForPhoneNumber = 'Номер телефону';
const inputPlaceHolderForEmail = 'Email';
const inputPlaceHolderForMessage = 'Повідомлення';

// Add placeholder
const addPlaceHolder = function (input, placeHolder) {
    input.setAttribute('placeholder', placeHolder);
}

// Form reset
addPlaceHolder(name, inputPlaceHolderForName);
addPlaceHolder(phoneNumber, inputPlaceHolderForPhoneNumber);
phoneNumber.setAttribute('type', 'tel');
phoneNumber.setAttribute('maxlength', '15');
addPlaceHolder(email, inputPlaceHolderForEmail);
addPlaceHolder(message, inputPlaceHolderForMessage);
name.value = '';
phoneNumber.value = '';
email.value = '';
message.value = '';

// Form validation
const isInvalidInputText = (input) => input === '' || input === null || input.trim() === '';
const isInvalidInputTel = (input) => {
    const clearInput = input.replace(/\D/g, '');
    const clearInputLength = clearInput.length;
    if (!/^\d+$/.test(clearInput)) return true;
    else if (clearInputLength < 10 || clearInputLength > 13) return true;
    return false;
};

// Form print error message
const printErrorMessage = (message) => {
    const error = document.createElement('p');
    error.classList.add('error','alert', 'alert-danger');
    error.setAttribute('id', 'error');
    error.setAttribute('role', 'alert');
    error.innerText = message;
    inputFields.appendChild(error);
}

// Form submitting
form.addEventListener('submit', function (event) {
    event.preventDefault();
    let error = document.getElementById('error');
    let validationStatus = true;
    if (error) {
        error.remove();
        name.style.borderColor = '#f8f9fa';
        phoneNumber.style.borderColor = '#f8f9fa';
        email.style.borderColor = '#f8f9fa';
        message.style.borderColor = '#f8f9fa';
    }
    if (isInvalidInputText(name.value)) {
        printErrorMessage('Введіть Імʼя!');
        name.style.borderColor = 'red';
        validationStatus = false;
    }else if (isInvalidInputText(phoneNumber.value) || isInvalidInputTel(phoneNumber.value)) {
        printErrorMessage('Введіть номер телефону!');
        phoneNumber.style.borderColor = 'red';
        validationStatus = false;
    }else if (isInvalidInputText(email.value) || !email.value.includes('@')) {
        printErrorMessage('Введіть Email!');
        email.style.borderColor = 'red';
        validationStatus = false;
    }else if(isInvalidInputText(message.value)) {
        printErrorMessage('Введіть повідомлення!');
        message.style.borderColor = 'red';
        validationStatus = false;
    }
    if (validationStatus) {
        form.submit();
    }
})
