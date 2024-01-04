const loadUsers = () => {
  fetch("https://fakestoreapi.com/users")
    .then((res) => res.json())
    .then((users) => {
      const userListContainer = document.getElementById("userListContainer");

      users.forEach((user) => {
        const userCard = document.createElement("div");
        userCard.className = "card mb-3";

        userCard.innerHTML = `
            <div class="card-body">
                <h5 class="card-title">${user.name.firstname} ${user.name.lastname}</h5>
                <p class="card-text"><strong>Email:</strong> ${user.email}</p>
                <p class="card-text"><strong>Username:</strong> ${user.username}</p>
                 <a href="singleUser.html?id=${user.id}" class="btn btn-primary">Details</a>
                
            </div>
        `;

        userListContainer.appendChild(userCard);
      });
    });
};



const loadSingleUser = () => {
    const params = new URLSearchParams(window.location.search).get("id");
    
    fetch(`https://fakestoreapi.com/users/${params}`)
    .then((res) => res.json())
    .then((user) => {
        const userCard = document.getElementById("userCard");
        userCard.innerHTML = `
            <div class="card mb-3">
                <div class="card-body">
                    <h5 class="card-title">${user.name.firstname} ${user.name.lastname}</h5>
                    <p class="card-text"><strong>Email:</strong> ${user.email}</p>
                    <p class="card-text"><strong>Username:</strong> ${user.username}</p>
                    <p class="card-text"><strong>Phone:</strong> ${user.phone}</p>
                    <p class="card-text"><strong>Address:</strong> ${user.address.city}, ${user.address.street}, ${user.address.number}, ${user.address.zipcode}</p>
                    <p class="card-text"><strong>Latitude:</strong> ${user.address.geolocation.lat}</p>
                    <p class="card-text"><strong>Longitude:</strong> ${user.address.geolocation.long}</p>
                </div>
            </div>
        `;
    })
}


loadSingleUser();
loadUsers();