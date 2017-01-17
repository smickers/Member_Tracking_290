/**
 * Created by COSA on 2017-01-17.
 */
$(document).ready(function(){
    file_field = $('input[name=file_field]');
    file_field.change(function(){
       if(file_field[0].files.length == 1)
       {
           $("#id_file_description").removeAttr("type");
       }
    });
})
