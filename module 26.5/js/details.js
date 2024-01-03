const getparams = () => {
  const param = new URLSearchParams(window.location.search).get("productId");

  fetch(`https://fakestoreapi.com/products/${param}`)
    .then((res) => res.json())
    .then((json) => {
      const productsContainer = document.getElementById("product-details");
      productsContainer.innerHTML += `

            <div class="row g-0">
                <div class="col-md-4">
                    <img src="${json.image}" class="img-fluid rounded-start" alt="Product Image">
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h2 class="card-title">${json.title}</h2>
                        <p class="card-text">${json.description}</p>
                        <p class="card-text">Price: $${json.price}</p>
                        <p class="card-text">Category: ${json.category}</p>
                        <p class="card-text">Rating: ${json.rating.rate} (${json.rating.count} reviews)</p>
                        <a href="#" class="btn btn-primary">Add to Cart</a>
                    </div>
                </div>
            </div>
                `;
    });
};

getparams();
