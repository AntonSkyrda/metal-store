'use strict';

//Form logic
const form = document.getElementById('contact-form');

if (form) {
    // Get elements
    const inputFields = document.getElementById('input-fields');
    const inputs = inputFields.querySelectorAll('input, textarea');
    const [name, phoneNumber, email, message] = inputs;

    const placeholders = ['Імʼя', 'Номер телефону', 'Email', 'Повідомлення'];

    // Add placeholder
    const addPlaceHolder = function (...inputs) {
        for (let i = 0; i < inputs.length; i++) {
            inputs[i].setAttribute('placeholder', placeholders[i]);
        }
    }

    // Form reset
    addPlaceHolder(...inputs);
    phoneNumber.setAttribute('type', 'tel');
    phoneNumber.setAttribute('maxlength', '15');
    inputs.forEach(input => {
        input.value = '';
    });

// Form validation
    const isInvalidInputText = (input) => input === '' || input === null || input.trim() === '';
    const isInvalidInputTel = (input) => {
        const clearInput = input.replace(/\D/g, '');
        const clearInputLength = clearInput.length;
        if (!/^\d+$/.test(clearInput)) return true;
        else if (clearInputLength < 10 || clearInputLength > 13) return true;
        return false;
    };
    const isInvalidInputEmail = (input) => {
        const validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
        console.log(validRegex.test(input));
    }

// Form print error message
    let validationStatus = true;
    const printErrorMessage = (element, message) => {
        const error = document.createElement('p');
        error.classList.add('error', 'alert', 'alert-danger');
        error.setAttribute('id', 'error');
        error.setAttribute('role', 'alert');
        error.innerText = message;
        element.style.borderColor = 'red';
        validationStatus = false;
        inputFields.appendChild(error);
    }

// Form submitting
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        let error = document.getElementById('error');
        if (error) {
            error.remove();
            inputs.forEach(input => {
                input.style.borderColor = '#f8f9fa';
            });
        }
        if (isInvalidInputText(name.value)) {
            printErrorMessage(name, 'Введіть Імʼя!');
        } else if (isInvalidInputText(phoneNumber.value) || isInvalidInputTel(phoneNumber.value)) {
            printErrorMessage(phoneNumber, 'Введіть номер телефону!');
        } else if (isInvalidInputText(email.value) || isInvalidInputEmail(email.value)) {
            printErrorMessage(email, 'Введіть Email!');
        } else if (isInvalidInputText(message.value)) {
            printErrorMessage(message, 'Введіть повідомлення!');
        }
        if (validationStatus) {
            form.submit();
        }
    })
}

// Dropdowns
document.addEventListener('DOMContentLoaded', () => {
    const btnDropdowns = document.querySelectorAll('.btn-dropdown');
    const btnDropends = document.querySelectorAll('.btn-dropend');
    const firstDropdown = () => bootstrap.Dropdown.getOrCreateInstance('#first-dropdown');

    btnDropdowns.forEach(dropdown => {
        dropdown.addEventListener('click', event => {
            firstDropdown().toggle();
        })
    });

    btnDropends.forEach(dropend => {
        dropend.addEventListener('click', event => {
            bootstrap.Dropdown.getOrCreateInstance(dropend.parentNode).toggle();
            dropend.querySelector('.btn-dropend-span').classList.toggle('dropend-active');
        })
    })
})

//Search button

const searchForm = document.getElementById('search-form');
if(searchForm.querySelector('p')) {
    searchForm.querySelector('p').classList.add('me-2');
    searchForm.querySelector('p').querySelector('input').classList.add('form-control');
}

