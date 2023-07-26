const listElements = document.querySelectorAll('.helptext li')
const emailInput = document.getElementById('id_email')
const passwordInput = document.getElementById('id_password1')

passwordInput.oninput = () => {
    // Checks if password has been typed in
    if (passwordInput.value.trim() === '') {
        listElements[0].classList.remove(...listElements[0].classList)
        listElements[1].classList.remove(...listElements[1].classList)
        listElements[2].classList.remove(...listElements[2].classList)
        listElements[3].classList.remove(...listElements[3].classList)
    }
    // Checks if password is similar to email
    if (!emailInput.value.toLowerCase().includes(passwordInput.value.toLowerCase())) {
        listElements[0].classList.add('passed')
    } else {
        listElements[0].classList.remove(...listElements[0].classList)
    }
    // Checks length of the password
    if (passwordInput.value.length >= 8) {
        listElements[1].classList.add('passed')
    } else {
        listElements[1].classList.remove(...listElements[1].classList)
    }
    // Checks the complexity of the password
    let chars_count = {
    'uppercase': 0,
    'lowercase': 0,
    'numbers': 0
    }
    for (const char of passwordInput.value) {
        if (char === char.toUpperCase() && isNaN(char)) {
            chars_count['uppercase'] += 1
            console.log('uppercase')
        }
        if (char === char.toLowerCase() && isNaN(char)) {
            chars_count['lowercase'] += 1
            console.log('lowercase')
        }
        if (!isNaN(char)) {
            chars_count['numbers'] += 1
            console.log('number')
        }
        console.log(`Uppercase - ${chars_count['uppercase']}, Lowercase - ${chars_count['lowercase']}, Numbers - ${chars_count['numbers']}`)
        if (chars_count['uppercase'] >= 1 && chars_count['lowercase'] >= 1 && chars_count['numbers'] >= 1) {
            listElements[2].classList.add('passed')
            console.log(true)
        } else {
            listElements[2].classList.remove(...listElements[2].classList)
            console.log(false)
        }
    }
    // Checks of password contains letters
    for (const char in passwordInput.value) {
        if (!isNaN(parseInt(char))) {
            listElements[3].classList.add('passed')
            break;
        } else {
            listElements[3].classList.remove(...listElements[3].classList)
        }
    }
}
