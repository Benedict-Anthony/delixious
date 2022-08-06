const searchItem = document.getElementById("search-item");
const searchBtn = document.getElementById("search-btn")

const cartBtn = document.getElementById("cart-btn");
const cartItems = document.getElementById("cart-items");
const cartItemsBar = document.getElementById("cart-items-bar");
const checkoutOutBtn = document.getElementById("checkout-btn")

const menuBtn = document.getElementById("menu-btn");
const menuBar = document.getElementById("menu-bar")

const User = document.getElementById("login-btn")

const accordions = document.querySelectorAll(".accordion")

const cartItemList = document.querySelectorAll(".cartItem");
const checkoutOutItems = document.getElementById("check-out-items-list");

const totalAmout = document.getElementById("total")
const price = document.getElementsByClassName("span-price")

const notLoginUser = document.getElementById("not-login-form")
const form = document.getElementById("form")
const warning = document.getElementById("warning")
const submit = document.getElementById("submit")
const makePaymentProcess = document.getElementById("make-payment")


// navbar togglers
function toggler(toggleBtn, toggleItem) {
    toggleBtn.addEventListener("click", () => {
        toggleItem.classList.toggle("hidden")
    })
}

function scrollRemoveBars() {
    searchItem.classList.add("hidden")
    cartItemsBar.classList.add("hidden")
    menuBar.classList.add("hidden") 
}

toggler(searchBtn, searchItem)
toggler(cartBtn, cartItemsBar)
toggler(menuBtn, menuBar)
window.addEventListener("scroll", scrollRemoveBars )


accordions.forEach((accordion) => {
    
    openAccordion(accordion)
})

function openAccordion(item) {
    const accordionToggler = item.querySelector(".accordion-toggler")
    accordionToggler.addEventListener("click", (e) => {
        accordionContent = item.querySelector
            (".accordion-content")
        
        accordionContent.classList.toggle("close")
    })
}

// cart functionalities

// Ajax cookie for csrf tokrn
function getToken(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getToken('csrftoken')
// const storedItems =  getItems()
const cartUpdateFunc = async (storedItems, customerInfo) => {
    const res = await fetch("/update-cart/", {
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken
        },
        method: "POST",
        body: JSON.stringify({"storedItems": storedItems, "customerInfo":customerInfo})
        
    })
    const data = await res.json()
    console.log(data)
    localStorage.removeItem("store")
    window.location.href = `/check-out-sessions/${data}`
}



// CART COUNT
function updateCart() {
    storedItems = getItems()
    cartCount = storedItems ? storedItems.length : null
   return cartCount
}


cartItemList.forEach((item) => {
    updateBtn =item.querySelector(".update-btn")
    action = updateBtn.getAttribute("data-action")
    
    updateBtn.addEventListener("click", (e) => {
        dataID = e.target.getAttribute("data-id")
        action = e.target.getAttribute("data-action")
        productName = e.target.getAttribute("data-name")
        productPrice = e.target.getAttribute("data-price")
        action = e.target.getAttribute("data-action")
        productImage= e.target.getAttribute("data-image")
        collectCartDetails(dataID, productName, productPrice, productImage)
        cartBtn.firstElementChild.innerHTML = updateCart()
        // storeCartItems()
        

    })
})

cartBtn.firstElementChild.innerHTML = updateCart()

let store =[]
function collectCartDetails(id, name, price, imageUrl) {
    const seletedItems = {
        id: id,
        name: name,
        quantity: 1,
        price: price ,
        imageUrl: imageUrl,
    }
    
    store = [...store, seletedItems]

    localStorage.setItem("store", JSON.stringify(store)) 

}


function getItems() {
    storedItems = JSON.parse(localStorage.getItem("store"))
    return storedItems
}

function storeCartItems() {
    try {
        storedItems = getItems()
        if (storedItems.length > 0) {
            checkoutOutBtn.classList.remove("hidden")
            storedItems.map((item) => {
            displayCartItems(item)
            })
        }
    }
    catch {
        cartItems.innerHTML = `<h4 class="text-black text-center text-xl py-3 md:text-3xl">Your cart is empty.</h4>`
    }
 
}
storeCartItems()
 
cartBtn.addEventListener("click", function () {
        cartItems.innerHTML = ''    
        storeCartItems()
})

function displayCartItems(item) {
    const div = document.createElement("div")
    result = `
     <div class="flex justify-between items-center mt-4">   
        <div class="w-20">
            <img src=${item.imageUrl} class="w-full rounded-full" alt="">
        </div>

        <div class="">
            <h2 class="text-xl">${item.name}</h2>
        </div>
        <div class="">
            <p class="text-orange text-sm">N${item.price}</p>
        </div>
    </div>
    `
    div.innerHTML = result;
    cartItems.appendChild(div)

}



// CHECK OUT PAGE
function checkout() {
    try {
        storedItem = getItems()
        storedItem.forEach((item) => {
            displayCheckOutItems(item)
            
        })
        // for (i = 0; i < storedItem.length; i++){
        //     displayCheckOutItems(storedItem[i])
        // }

    } catch {
        // console.log("not found")
    }
}

function displayCheckOutItems(item) {
    const div = document.createElement("div")
    result = `
    <div class="relative flex items-cart justify-between items-center bg-gray-200 mt-4 py-1 px-3 item">
            <div class="w-20">
                <img class="w-full rounded-full" src="${item.imageUrl}" alt="">
            </div>
            <h3 class="text-black font-semibold text-xl">${item.name}</h3>

            <div class="flex items-center justify-between md:space-x-8 flex-col md:flex-row">
                <div class="flex items-center justify-center space-x-3">
                    <div class="fas fa-minus text-orange"></div>
                    <p class="quantity">${item.quantity}</p>
                    <div class="fas fa-plus text-orange"></div>
                </div>
                <div class="text-black price">N<span class="span-price">${item.price * item.quantity}</span></div>
                <div class="fas fa-trash mt-5 md:mt-0 right-0 text-orange"></div>

                <p class="product-price hidden">${item.price}</p>
            </div>
    </div>
    `
    div.innerHTML = result

    checkoutOutItems.appendChild(div)
}

checkout()



// increase cart count
for (i = 0; i < getItems().length;i++){
    const plus = document.getElementsByClassName("fa-plus")[i]
    const quantity = document.getElementsByClassName("quantity")[i]
    const price = document.getElementsByClassName("price")[i]
    const productPrice = document.getElementsByClassName("product-price")[i]
    const productID = getItems()[i].id
    const item = getItems()[i]
    plus.addEventListener("click", function () {
         quantity.textContent =parseFloat(quantity.textContent)  +1
         price.textContent ="N" + parseFloat(quantity.textContent) *  parseFloat(productPrice.textContent)
        increase(productID)
        // totalAmout.textContent = calcTotal()

    })
}


// decrease cart count
for (i = 0; i < getItems().length;i++){
    const plus = document.getElementsByClassName("fa-minus")[i]
    const productID = getItems()[i].id
    const item = getItems()[i]
    const quantity = document.getElementsByClassName("quantity")[i]
    const price = document.getElementsByClassName("price")[i]
    const productPrice = document.getElementsByClassName("product-price")[i]
    plus.addEventListener("click", function () {
        if (parseFloat(quantity.textContent) == 1) {
            quantity.textContent = 1
        } else {
            quantity.textContent =parseFloat(quantity.textContent)  -1
        }
        price.textContent ="N" + parseFloat(quantity.textContent) *  parseFloat(productPrice.textContent)
        decrease(productID)
    })
}

// removing item from cart
for (i = 0; i < getItems().length;i++){
    const remove = document.getElementsByClassName("fa-trash")[i]
    const productID = getItems()[i].id
    const item = document.getElementsByClassName("item")[i]
    remove.addEventListener("click", function () {
       item.classList.add("hidden")
        filterItem(productID)
        cartBtn.firstElementChild.innerHTML = updateCart()
        
    })
}

// function to actually increase
function increase(id) {
    storedItems = getItems()
    update = storedItems.map((item) => (
        item.id ===id ? {...item, quantity:item.quantity+1} : item
    ))

    localStorage.setItem("store", JSON.stringify(update)) 

}

// function to actually decrease
function decrease(id) {
    storedItems = getItems()
    update = storedItems.map((item) => (
        item.id ===id ? {...item, quantity:item.quantity-1} : item
    ))
    localStorage.setItem("store", JSON.stringify(update)) 
}

function filterItem(id) {
    const storedItems = getItems()

   const update = storedItems.filter((item) =>(
        item.id !== id
   ))
    localStorage.setItem("store", JSON.stringify(update))
}



if (user !== "AnonymousUser") {
    notLoginUser.classList.add("hidden")
}

form.addEventListener("submit", (e) => {
    e.preventDefault()
    storedItems = getItems()
    if (user !== "AnonymousUser") {
        if (form.state.value === '' || form.city.value === '' || form.street.value === '' || form.description.value === '') {
            formValidation()
        } else {
            
           const customerInfo = loggedInUser()

            cartUpdateFunc(storedItems, customerInfo )
            form.reset()

            console.log("loged in user, sent to backend succesfully")
            form.reset()
            hideForm()
        }

    } else {
        if (form.firstname.value === '' || form.lastname.value === '' || form.email.value === '' || form.contact.value === '' || form.state.value === '' || form.city.value === '' || form.street.value === '' || form.description.value === '') {
            formValidation()
        } else {
            const customerInfo = notLoggedInUser()
            cartUpdateFunc(storedItems, customerInfo )
            form.reset()
            hideForm()

        }
    }
})

function formValidation() {
    warning.classList.remove("hidden")
    form.classList.add("bg-red-800")

    setTimeout(() => {
        warning.classList.add("hidden")
        form.classList.remove("bg-red-800")
    }, 3000)
}

function notLoggedInUser() {
    const info = {
        firstName: form.firstname.value,
        lastName: form.lastname.value,
        email: form.email.value,
        contact: form.contact.value,
        state: form.state.value,
        city: form.city.value,
        town: form.town.value,
        street: form.street.value,
        description:form.description.value
        
    }

    return info
}

function loggedInUser() {
    const info = {
        state: form.state.value,
        city: form.city.value,
        town: form.town.value,
        street: form.street.value,
        description:form.description.value
    }

    return info
}

function hideForm() {
    form.classList.add("hidden")
    makePaymentProcess.classList.remove("hidden")
} 
