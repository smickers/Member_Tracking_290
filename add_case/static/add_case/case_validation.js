// get a reference of the Case Type field
var case_type_field = document.getElementById("id_caseType");

// listen to changes of the case type select box values
case_type_field.addEventListener('change', update_additional_mem);
function update_additional_mem(){
    var case_type_val = case_type_field.options[case_type_field.selectedIndex].value;

    //selects additional member parent element
    var additional_mem_field = document.getElementById("id_additionalMembers").parentNode;
    //selects additional non-member parent element
    var additional_nonmem_field = document.getElementById("id_additionalNonMembers").parentNode;
    //checks to see if the caseType's value is an empty string or a value of 7(which is GRIEVANCE-INDIVIDUAL
    var griev_check =  ( case_type_val == 7 ) || (case_type_val=="");

    //hides additional member and additional non-member field
    additional_mem_field.hidden = griev_check;
    additional_nonmem_field.hidden = griev_check;
}

update_additional_mem()//Execute this function on startup
