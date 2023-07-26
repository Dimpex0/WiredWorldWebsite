const input = document.getElementById('search-input')
const list = document.getElementById('search-list')
const PRODUCTS_API_URL = 'http://127.0.0.1:8000/products-api/'

let products = []

fetch(PRODUCTS_API_URL)
    .then(res => res.json())
    .then(data => {
        console.log(data)
        data.forEach(product => {
            products.push(product)
        })
    })

input.oninput = () => {
    list.innerHTML = ''
    let inputWords = input.value.split(' ')
    inputWords.forEach(word => {
        if (word === '') {
            const index = inputWords.indexOf(word)
            inputWords.splice(index, 1)
        }
    })
    products.forEach(product => {
        inputWords.every(word => {
            if (product.title.toLowerCase().includes(word.trim().toLowerCase()) && input.value !== '') {
                let li = document.createElement('li')

                let a = document.createElement('a')
                a.href = 'details/' + product.id + '/'
                li.appendChild(a)

                let img = document.createElement('img')
                img.src = '/media/' + product.image.split('/media/')[1]
                a.appendChild(img)

                let p = document.createElement('p')
                p.textContent = product.title
                a.appendChild(p)

                let price_p = document.createElement('p')
                price_p.textContent = `${product.price} BGN`
                price_p.classList.add('list-price')
                a.appendChild(price_p)

                list.appendChild(li)
                return false;
            }
            return true;
        })
    })
}
