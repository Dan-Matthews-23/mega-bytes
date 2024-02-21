
https://www.geeksforgeeks.org/how-to-modify-an-objects-property-in-an-array-of-objects-in-javascript/#approach-1-using-arraymap-method


//localStorage.removeItem("selectedItem");
//localStorage.removeItem("orderArray");


const order_div = document.getElementById("display_order");
let orderArray = JSON.parse(localStorage.getItem("orderArray")) || [];
orderArray = orderArray.map(item => ({
    ...item,
    product_price: parseFloat(item.product_price).toFixed(2),
    original_price: parseFloat(item.original_price).toFixed(2)

}));
updateOrderDisplay();

function updateOrderDisplay() {
    if (orderArray.length > 0) {
        order_div.innerHTML = orderArray.map((entry, index) => `
            ${entry.product_name} (x ${entry.product_quantity})<br>
            &pound;${entry.product_price}<br>
            <br>
            <span id="delete_item" data-index="${index}"><i class="btn fa-solid fa-trash fa-xl"></i></span>
            <br><br>
        `).join('');

        // Add event listeners for delete buttons
        const deleteButtons = order_div.querySelectorAll('#delete_item');
        deleteButtons.forEach(button => {
            button.addEventListener('click', () => deleteItem(button.dataset.index));
        });

    } else {
        order_div.innerHTML = "Your basket is empty";
    }
}

// Function to delete an item
function deleteItem(index) {
    orderArray.splice(index, 1);
    localStorage.setItem("orderArray", JSON.stringify(orderArray));
    updateOrderDisplay();
}

// Open modal buttons
const selectProductBtns = document.querySelectorAll('.open-modal');
selectProductBtns.forEach(btn => {
    btn.addEventListener('click', openModal);
});

// Modal Logic
function openModal(event) {

    const modal = document.getElementById("modal-div");
    const quantityDiv = document.getElementById('quantity-div');

    const confirmBtn = document.querySelector('.select-product-btn');

    // Find the existing product in orderArray or create a new one
    const existingItem = orderArray.find(i => i.product_id === event.target.dataset.productId);
    let selectedItem;
    if (existingItem) {
        selectedItem = { ...existingItem }; // Create a copy
    } else {
        selectedItem = {
            product_id: event.target.dataset.productId,
            product_name: event.target.dataset.productName,
            product_price: parseFloat(event.target.dataset.productPrice),
            original_price: parseFloat(event.target.dataset.productPrice),
            product_quantity: 1
        };
    }
    console.log("selectedItem in openModal:", selectedItem);

    quantityDiv.innerHTML = selectedItem.product_quantity;

    modal.classList.add("show");

    const increaseBtn = document.getElementById('increase-quantity');
    const decreaseBtn = document.getElementById('decrease-quantity');
    increaseBtn.addEventListener('click', () => updateQuantity(selectedItem, true));
    decreaseBtn.addEventListener('click', () => updateQuantity(selectedItem, false));

    confirmBtn.addEventListener('click', () => confirmAndClose(selectedItem));

    // Close modal
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

function updateQuantity(selectedItem, isIncrease) {
    if (selectedItem) {
        //console.log("selectedItem before update:", selectedItem) // Check its state here
        if (isIncrease) {
            selectedItem.product_quantity++;
            //console.log(`The new quantity for the product with ID of ${selectedItem.product_id} is ${selectedItem.product_quantity}`);
        } else {
            selectedItem.product_quantity = Math.max(selectedItem.product_quantity - 1, 1);
            console.log(`The new quantity for the product with ID of ${selectedItem.product_id} is ${selectedItem.product_quantity}`);
        }
        // Calculate using the original price
        selectedItem.product_price = (selectedItem.product_quantity * selectedItem.original_price).toFixed(2);
        document.getElementById('quantity-div').innerHTML = selectedItem.product_quantity;
        console.log(`The new quantity for the product with ID of ${selectedItem.product_id} is ${selectedItem.product_quantity}`);
    }
}

// Confirm order and close modal function
function confirmAndClose(selectedItem) {
    // Find the index of the item to update in orderArray
    const existingIndex = orderArray.findIndex(i => i.product_id === selectedItem.product_id);

    if (existingIndex !== -1) {
        orderArray[existingIndex] = { ...selectedItem }; // Create a new copy
    } else {
        orderArray.push(selectedItem);
    }

    localStorage.setItem("orderArray", JSON.stringify(orderArray));
    selectedItem = [];
    updateOrderDisplay();


    document.getElementById("modal-div").classList.remove("show");
    document.getElementById("modal-div").classList.add("hide");
}

