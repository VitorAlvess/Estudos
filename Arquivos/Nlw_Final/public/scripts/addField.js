//procurar o botão

document.querySelector("#add-time")
.addEventListener("click", cloneField)
//quando clicar no botão
function cloneField() {

    //duplicar os campos
    const newFieldContainer = document.querySelector(".schedule-item").cloneNode(true)

    //cleam //Pegar os campos
    const fields = newFieldContainer.querySelectorAll("input")

    // para cada campo limpar
    fields.forEach(function(field) {
         //pegar o field do momento e limpa
        field.value = ""
    })



    //colocar na página
    document.querySelector("#schedule-items").appendChild(newFieldContainer)
}