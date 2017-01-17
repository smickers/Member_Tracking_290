/**
 * Created by COSA on 2017-01-17.
 */
$(document).ready(function(){
    file_field = $('input[name=file_field]');
    showDescription(file_field);


    file_field.change(function(){
        showDescription(file_field);
    });
})
/*
function:   showDescription
Purpose:    When a file is selected and less than the maximum size of 500mb(524288000 bytes)
            the description field will show. If the size is larger than 500mb, error will be
            displayed
Params:     file_field  the input text box for the file description

 */
function showDescription(file_field)
{
    if(file_field[0].files.length == 1 && file_field[0].files[0].size < 524288000)
    {
        $("#id_file_description").removeAttr("type");
        $("#id_file_description").before("<label class='control-label' for='id_file_description'>Description</label></br>");
    }
    else
    {
        $("#id_file_description").before("<p style='color:red' id='file_error'>File is larger than the allowed maximum size</p>");
    }
    //remove error message if there are 1 or 0 files uploaded, and max size is not exceeded
    if(file_field[0].files.length == 0 || (file_field[0].files.length == 1 && file_field[0].files[0].size < 524288000) )
    {
        $("#file_error").remove();
    }
}
