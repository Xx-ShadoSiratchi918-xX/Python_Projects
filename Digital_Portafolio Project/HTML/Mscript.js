function validació_del_formulari_() {
    let fname = document.forms["FContacte"]["fname"].value;
    let lname = document.forms["FContacte"]["lname"].value;
    let phone = document.forms["FContacte"]["phone"].value;
    let email = document.forms["FContacte"]["email"].value;
    let message = document.forms["FContacte"]["msg"].value;

    if (lname == "" || num == "") {
        alert("Sisplau, Emplenar tots els camps requerits :P");
        return false;
    } else {
        alert("Les dades en el formulari se han enviat correctament ;}")
        return true;

    }
}


function validar_numeros_generats() {
    document.getElementById("num1").value = Math.floor(Math.random() * 100) + 1;
    document.getElementById("num2").value = Math.floor(Math.random() * 100) + 1;
}

function validar_formulari_exercicis() {
    let num1 = parseInt(document.forms["MActivities"]["num1"].value);
    let num2 = parseInt(document.forms["MActivities"]["num2"].value);
    let resultat = parseInt(document.forms["MActivities"]["result"].value);

    console.log(num1)
    console.log(num2)
    console.log(resultat)

    if (num1 + num2 == resultat) {
        alert("¡Felicitats! La suma es correcte ;D");
        return true;
    } else {
        alert("¡Estàs equivocat! La suma es incorrecte '-.-");
        return false;
    }
}