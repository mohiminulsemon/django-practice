// const loadCategories = () => {
//     fetch('https://fakestoreapi.com/products/categories')
//             .then(res=>res.json())
//             .then(json=>{
//                 const categories = document.getElementById('category-container')
//                 json.forEach(category => {
//                     categories.innerHTML += `<button class="btn btn-primary mx-2" onclick='loadProducts("${category}")'>${category}</button>`
//                 });
//             })

// }

// const loadProducts = (category) => {
//     console.log(category)
// }

// loadCategories()


const loadCategories = () => {
    fetch('https://fakestoreapi.com/products/categories')
        .then(res => res.json())
        .then(json => {
            const categoriesContainer = document.getElementById('category-container');
            json.forEach(category => {
                const button = document.createElement('button');
                button.className = 'btn btn-primary mx-2';
                button.textContent = category;
                button.addEventListener('click', () => loadProducts(category));
                categoriesContainer.appendChild(button);
            });
        });
};

const loadProducts = (category) => {
    console.log(category);
    // Add code to load products based on the selected category
};



const loadAllProducts = () => {
    fetch('https://fakestoreapi.com/products')
            .then(res=>res.json())
            .then(json=>{
                // console.log(json)
                const productsContainer = document.getElementById('products-container')
                json.forEach(product => {
                    productsContainer.innerHTML += `
                    <div class="col my-2">
                        <div class="card" style="width: 20rem; height: 600px;">
                            <img src="${product.image}" class="card-img-top w-100 h-50 mx-auto" alt="${product.title}" style="object-fit: contain;">
                            <div class="card-body">
                                <h5 class="card-title">${product.title}</h5>
                                <p class="card-text">${product.description.slice(0, 70)}...</p>
                                <p class="card-text my-0"> <span class="fw-bold">Price:</span> $${product.price}</p>
                                <p class="card-text my-0"> <span class="fw-bold">Category:</span> ${product.category}</p>
                                <p class="card-text my-0"> <span class="fw-bold">Rating:</span> ${product.rating.rate} (${product.rating.count} reviews)</p>
                                <a target="_blank" href="productDetails.html?productId=${product.id}" class="btn btn-primary">Vies Details</a>
                            </div>
                        </div>
                    </div>`
                })
            })
}

loadAllProducts();
loadCategories();
