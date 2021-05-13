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

function GenerateWordcloud(){
    console.log('Generating..');
    var items = document.getElementsByClassName("item");
    for (let index = 1; index <= 4; index++) {
        image_src = "static/images/graph0" + index + ".png";
        console.log(image_src);
        items[index - 1].innerHTML = "<img src=image_src width='100'/>";
    }
}
function GetNews(){
    console.log('Get News..');
    var contexts = document.getElementsByClassName("context");
    var select = document.getElementsByClassName("selection");
    var contextExists = document.getElementsByClassName("context").length;
    var selectExists = document.getElementsByClassName("selection").length;
    console.log(contextExists);
    console.log(selectExists);

    if (!contextExists || !contexts[0].innerHTML){ // context가 있는지? && context의 값이 있는지?
        alert('Generate Context!');
    }
    else if (!selectExists || !select[0].innerHTML){
        alert('Select WordCloud!');
    }
    else {
        location.href="/news";
    }

}
function selection(image) {
    var select = document.getElementsByClassName("selection");
    console.log(image);
    select = image;
}