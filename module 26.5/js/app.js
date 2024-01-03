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

loadCategories();
