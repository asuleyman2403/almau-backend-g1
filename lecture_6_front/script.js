const BASE_URL = 'http://localhost:8000';

const logCategories = () => {
    const xhr = new XMLHttpRequest();

    xhr.open('GET', `${BASE_URL}/online-shop/categories`);


    xhr.onload = function () {
        if (xhr.status === 200) {
            console.log(JSON.parse(xhr.response));
        }
    }

    xhr.send();
}

logCategories();
