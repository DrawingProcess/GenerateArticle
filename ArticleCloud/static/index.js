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
        image_src = "/source/graph0" + index + ".png";
        console.log(image_src);
        items[index - 1].innerHTML = "<img src=image_src width:40% height:20% />";
    }
}
function GetNews(){
    console.log('Get News..');
    var contexts = document.getElementsByClassName("context");
    console.log(contexts[0].innerHTML);
    var contextExists = document.getElementsByClassName("context").length;
    var selectExists = document.getElementsByClassName("selection").length;
    console.log(contextExists);
    console.log(selectExists);

    if (!contextExists || !contexts[0].innerHTML){
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
    select = image;
    clearSelect();
}

function clearSelect() {
    var items = document.getElementsByClassName("item");
    for (let index = 0; index < items.length; index++) {
        items[index].innerHTML = "";
    }
}