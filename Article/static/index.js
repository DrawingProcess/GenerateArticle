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
        var contexts = document.getElementsByClassName("context");
        const resolvedProm = Promise.resolve(response.text()); // contexts = response.text();
        let thenProm = resolvedProm.then(value => {
            contexts[0].innerHTML = value;
            console.log(contexts);
        });
    })
    .catch(e => { // Error
        console.log('Error');
        var context = document.getElementsByClassName("context")[0];
        context.innerHTML=e;
    })
}