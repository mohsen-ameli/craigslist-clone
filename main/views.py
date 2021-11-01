import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from requests.compat import quote_plus

craigslist = "https://toronto.craigslist.org/d/for-sale/search/sss?query={}"


def home(request):
    return render(request, "main/base.html")


def search(request):
    searching = request.POST.get("q")
    # fianl_url = craigslist.format(quote_plus(searching))
    fianl_url = (
        # f"https://toronto.craigslist.org/search/sss?query={quote_plus(searching)}",
        f"https://toronto.craigslist.org/d/for-sale/search/sss?query={searching}"
    )
    responce = requests.get(fianl_url)
    data = responce.text
    soup = BeautifulSoup(data, features="html.parser")

    post_listing = soup.find_all("li", {"class": "result-row"})

    # Empty list
    final_listing = []

    for post in post_listing:
        # Heading
        post_heading = post.find(class_="result-title").text

        # Url
        post_url = post.find("a").get("href")

        # Price
        if post.find(class_="result-price"):
            post_price = post.find(class_="result-price").text
        else:
            post_price = "N/A"

        # Image
        if post.find(class_="result-image").get("data-ids"):
            image = post.find("a", {"class": "result-image gallery"})["data-ids"]
            image_url = image.split(":")[1].split(",")[0]
            post_img = f"https://images.craigslist.org/{image_url}_300x300.jpg"
        else:
            post_img = "https://craigslist.org/images/peace.jpg"

        # Appending everything to the empty list.
        final_listing.append((post_heading, post_price, post_url, post_img))

    template_name = "main/new_search.html"
    context = {
        "search": searching,
        "posts": final_listing,
    }
    return render(request, template_name, context)
