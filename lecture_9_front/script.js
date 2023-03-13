const BASE_URL = 'http://localhost:8000'

const getBlogs = () => {
    const xhr = new XMLHttpRequest();

    xhr.open('GET', `${BASE_URL}/blogs`);


    xhr.onload = () => {
        if (xhr.status == 200) {
            console.log(xhr.response);
        }
    }

    xhr.send();
}

getBlogs();
