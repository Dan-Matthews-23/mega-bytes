
const quantitySelect = document.getElementById("quantity");

// Set the maximum quantity you'd like to offer
const maxQuantity = 10;

for (let i = 1; i <= maxQuantity; i++) {
    const option = document.createElement("option");
    option.value = i;
    option.text = i;
    quantitySelect.appendChild(option);
}



/*

// Variables
let order_div = document.getElementById("display_order");
let total_cost = document.getElementById("total_cost");
let orderArray = JSON.parse(localStorage.getItem("orderArray")) || [];
basketTotalElement = document.getElementById("basket-total");
const jsonData = JSON.stringify(orderArray);
document.getElementById('orderData').value = jsonData;
*/

const selectProductBtns = document.querySelectorAll('.open-modal');

// Event Listeners
selectProductBtns.forEach(btn => {
    btn.addEventListener('click', openModal);
});

/*
// Initial call to update everything
updateOrder();
updateSum();


function updateOrder() {
    if (orderArray.length > 0) {
        order_div.innerHTML = orderArray.map((entry, index) => `
            ${entry.product_name} (x ${entry.product_quantity})<br>
            £${entry.price}<br>
            <br>
            <span id="delete_item" data-index="${index}"><i class="btn fa-solid fa-trash fa-xl"></i></span>
            <br><br>
        `).join('');

        const deleteButtons = order_div.querySelectorAll('#delete_item');
        deleteButtons.forEach(button => {
            button.addEventListener('click', () => deleteItem(button.dataset.index));
        });

    } else {
        order_div.innerHTML = "Your basket is empty";

    }
    //updateSum()

}

function updateSum() {
    let totalSum = orderArray.reduce((accumulator, entry) => {
        const itemPrice = parseFloat(entry.price); // Convert price to number

        if (isNaN(itemPrice)) {
            console.error("Failed to convert price to float:", entry);
            return accumulator; // Skip invalid prices
        }
        return accumulator + itemPrice;
    }, 0);

    totalSum = parseFloat(totalSum).toFixed(2);

    total_cost.innerHTML = (`Total: £${totalSum}`);

    if (totalSum) {
        basketTotalElement.innerHTML = (`£${totalSum}`);
    } else {
        basketTotalElement.innerHTML = (`£0.00`);
    }
    //updateOrder()

}


function deleteItem(index) {
    orderArray.splice(index, 1);
    localStorage.setItem("orderArray", JSON.stringify(orderArray));
    updateOrder();
}
*/

function openModal(event) {
    const modal = document.getElementById("modal-div");
    //document.getElementById('quantity-div').innerHTML = 1;
    const confirmBtn = document.querySelector('.select-product-btn');
    modal.classList.add("show");
    //const decreaseBtn = document.getElementById('decrease-quantity');
    //decreaseBtn.addEventListener('click', () => updateQuantity(false));
    confirmBtn.addEventListener('click', () => confirmAndClose());

    window.onclick = function (event) {
        if (event.target == modal) {
            modal.classList.remove("show");
            modal.classList.add("hide");
        }
    }
    document.querySelector('.close').onclick = function () {
        modal.classList.remove("show");
        modal.classList.add("hide");
    }
}
/*
const openModalButtons = document.querySelectorAll('.open-modal');
openModalButtons.forEach(modalBtn => {
    modalBtn.addEventListener('click', function (event) {

        const productIdFromBtn = modalBtn.value;
        const productNameFromBtn = this.dataset.productName;
        const productPriceFromBtn = this.dataset.productPrice;
        const foundProduct = orderArray.find(item => item.product_id === productIdFromBtn);
        if (foundProduct) {
            product_id = productIdFromBtn;
            product_name = foundProduct.product_name;            
            const resetQuantity = orderArray.findIndex(a => a.product_id == product_id);
            orderArray[resetQuantity].product_quantity = 1
            default_price = (foundProduct.default_price * orderArray[resetQuantity].product_quantity)
            document.getElementById('quantity-div').innerHTML = orderArray[resetQuantity].product_quantity;
            console.log(orderArray[resetQuantity].product_quantity)
            msg = "Product was found";
        } else {
            document.getElementById('quantity-div').innerHTML = 1;
            product_id = productIdFromBtn;
            product_name = productNameFromBtn;
            default_price = productPriceFromBtn
            default_product_quantity = 1
            msg = "Product was NOT found";
            insertNewProduct = {
                product_id: product_id,
                product_name: product_name,
                default_price: (default_price * default_product_quantity),
                product_quantity: default_product_quantity,
                price: 0.00,
            };
            orderArray.push(insertNewProduct);
            localStorage.setItem("orderArray", JSON.stringify(orderArray));
        }
        const increaseBtn = document.getElementById('increase-quantity');
        const decreaseBtn = document.getElementById('decrease-quantity');
        increaseBtn.addEventListener('click', () => increaseQuantity(product_id, product_name, default_price));
        decreaseBtn.addEventListener('click', () => decreaseQuantity(product_id, product_name, default_price));
    });
    updateOrder();
});

function increaseQuantity(product_id, default_price) {
    if (product_id) {
        product_id = product_id;
    }
    if (default_price) {
        default_price = default_price;
    }
    const pullOrderArrayIndex = orderArray.findIndex(a => a.product_id == product_id);
    if (pullOrderArrayIndex !== -1) {
        if (!isNaN(orderArray[pullOrderArrayIndex].product_quantity)) {
            if ((orderArray[pullOrderArrayIndex].product_quantity) > 0) {
                orderArray[pullOrderArrayIndex].product_quantity += 1;
                document.getElementById('quantity-div').innerHTML = orderArray[pullOrderArrayIndex].product_quantity;
            } else {
                orderArray[pullOrderArrayIndex].product_quantity = 1;
                document.getElementById('quantity-div').innerHTML = orderArray[pullOrderArrayIndex].product_quantity;
            }                
        } else {
            orderArray[pullOrderArrayIndex].product_quantity = 1;
            document.getElementById('quantity-div').innerHTML = orderArray[pullOrderArrayIndex].product_quantity;
        }

        document.getElementById('quantity-div').innerHTML = orderArray[pullOrderArrayIndex].product_quantity;
        orderArray[pullOrderArrayIndex].price = orderArray[pullOrderArrayIndex].default_price * orderArray[pullOrderArrayIndex].product_quantity;
        orderArray[pullOrderArrayIndex].price = orderArray[pullOrderArrayIndex].price.toFixed(2);
        localStorage.setItem("orderArray", JSON.stringify(orderArray));
    } else {
        console.log("Product not found in the order array");
    }
    updateOrder()
}

function decreaseQuantity(product_id, default_price) {
    if (product_id) {
        product_id = product_id;
    }
    if (default_price) {
        default_price = default_price;
    }
    const pullOrderArrayIndex = orderArray.findIndex(a => a.product_id == product_id);
    if (pullOrderArrayIndex !== -1) {
        if (!isNaN(orderArray[pullOrderArrayIndex].product_quantity)) {
            if (orderArray[pullOrderArrayIndex].product_quantity < 1) {
                orderArray[pullOrderArrayIndex].product_quantity = 1
            } else {
                orderArray[pullOrderArrayIndex].product_quantity -= 1;
            }
        } else {
            orderArray[pullOrderArrayIndex].product_quantity = 1;
        }

        document.getElementById('quantity-div').innerHTML = orderArray[pullOrderArrayIndex].product_quantity;
        orderArray[pullOrderArrayIndex].price = orderArray[pullOrderArrayIndex].default_price * orderArray[pullOrderArrayIndex].product_quantity;
        orderArray[pullOrderArrayIndex].price = orderArray[pullOrderArrayIndex].price.toFixed(2);
        localStorage.setItem("orderArray", JSON.stringify(orderArray));
    } else {
        console.log("Product not found in the order array");
    }
    updateOrder()
}

function confirmAndClose(product_id) {
    document.getElementById("modal-div").classList.remove("show");
    document.getElementById("modal-div").classList.add("hide");
    updateOrder()
}
*/