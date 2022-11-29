const form = document.querySelector("form")

form.addEventListener('submit', e =>  {
    if (!form.checkValidity()){
        e.preventDefault()
    }
    form.classList.add('was-validated')
})

function addIngredientElement() {
    const element = document.getElementById("ingredientList");
    var IG = document.createElement('div');
    var IGT = document.createElement('div');
    var I1 = document.createElement('input');
    var I2 = document.createElement('input');
    var I3 = document.createElement('select');
    var O1 = document.createElement('option');
    var O2 = document.createElement('option');
    var O3 = document.createElement('option');
    var O4 = document.createElement('option');
    var O5 = document.createElement('option');
    var O6 = document.createElement('option');
    IG.className = "input-group";
    IGT.className = 'input-group-text';
    I1.className = 'form-control';
    I2.className = 'form-control';
    I3.className = 'form-control custom-select';
    I1.type = 'text';
    I2.type = 'number';
    I1.placeholder = 'Add an Ingredient';
    I2.placeholder = 'Quantity';
    O1.selected;
    O1.innerHTML = 'Choose a Unit';
    O2.value = 'C';
    O2.innerHTML = 'Cup';
    O3.value ='OZ';
    O3.innerHTML = 'Ounce';
    O4.value = 'LB';
    O4.innerHTML = 'Pound';
    O5.value = 'TB';
    O5.innerHTML = 'Tablespoon';
    O6.value = 'TS';
    O6.innerHTML = 'Teaspoon';
    I3.appendChild(O1);
    I3.appendChild(O2);
    I3.appendChild(O3);
    I3.appendChild(O4);
    I3.appendChild(O5);
    I3.appendChild(O6);
    IG.append(IGT);
    IG.append(I1);
    IG.append(I2);
    IG.append(I3)
    
    element.append(IG);
}