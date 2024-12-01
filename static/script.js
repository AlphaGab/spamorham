document.addEventListener("DOMContentLoaded", function() {
   
        const inputText = document.getElementById("text")
        const button = document.querySelector("button");
        const div = document.getElementById("result-container")
        button.addEventListener("click", function(){
            const textValue = inputText.value;
            fetch('/predict',{
                method:'POST',
                headers:{
                    'Content-Type':'application/json',
                },
                body:JSON.stringify({text:textValue}),

            }).then(response=>response.json())
            .then(data=>{
                clearDiv(div)
                div.appendChild(createPNode(data.prediction))
            })
            })
        })

function createPNode(text){

const para = document.createElement("p");
para.classList.add("text-center")
const node = document.createTextNode(text);
para.appendChild(node); 
return para
}
function clearDiv(divElement){
    
    divElement.innerHTML =" "
}