var button = document.getElementsByClassName("update-cart");

for (var i = 0; i < button.length; i++) {
    button[i].addEventListener('click', function() {
        var ProductPrice = this.dataset.price
        var ProductTitle = this.dataset.title

        if (user === 'AnonymousUser') {
            console.log("user is not permitted !")
        } else {
            console.log("price:", ProductPrice, "title:", ProductTitle)
        }
    })
}