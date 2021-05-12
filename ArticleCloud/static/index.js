function suggestion() {
    console.log('Suggestion');
    var textarea = document.getElementById("input");
    var input = textarea.value; 

    var formData = new FormData(); 
    formData.append("input", input );
    fetch(
        "/gpt-2",
        {
            method: "POST",
            body:formData
        }
    )
    .then(response => {
        if (response.status == 200){
            return response;
        }
        else{
            throw Error("Failed");
        }
    })
    .then(response => {
        var items = document.getElementsByClassName("item");
        const resolvedProm = Promise.resolve(response.text()); // items = response.text();
        let thenProm = resolvedProm.then(value => {
            items[0].innerHTML = value;
            console.log(items);
        });
    })
    .catch(e => { // Error
        console.log('Error');
        var item = document.getElementsByClassName("item")[0];
        item.innerHTML=e;
    })
}