function suggestion() {
    console.log('Suggestion');
    var textarea = document.getElementById("input");
    var input = textarea.value; 

    var params = {
        'input': input
    }
    fetch(
        "/gpt-2",
        {
            method: "GET",
            params: params
        }
    )
    .then(response => {
        console.log(response.status);
        if (response.status == 200){
            return response;
        }
        else{
            throw Error("Failed");
        }
    })
    .then(response => response.json())
    .then(response => {
        var items = document.getElementsByClassName("item");
        items[0].innerHTML = response.text();
        console.log('Success');
    })
    .catch(e => { // Error
        console.log('Error');
        var item = document.getElementsByClassName("item")[0];
        item.innerHTML=e;
    })
}