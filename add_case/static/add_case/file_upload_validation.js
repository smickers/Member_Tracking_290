/**
 * Created by COSA on 2017-02-02.
 */
$(document).ready(function(){
    var file_field = $('input[name=file_field]');
    var desc = $('input[name=file_description]');
    //unselect any files when the page loads
    file_field[0].value = null;


    // Hide the cancel upload button until the user submits the form
    $("#cancel_upload").hide();


    // This method contains the main logic for validation
    description_handler(file_field, desc);

    // Call the main logic every time the file selected changes
    file_field.change(function(){
        description_handler(file_field, desc);
    });




    // Show a cancel upload button when the user clicks Submit
     $("input[type=submit]").click(function(){
         if(file_field[0].files.length > 0)
         {
             $("#cancel_upload").show();
         }



     });
     $("#cancel_upload").click(function(){
         //have to clear out files before refreshing or else upload just restarts
         //and the page is never refreshed
         file_field[0].value = "";
         window.location.reload();

     });


})
/*
function:   description_handler
Purpose:    When a file is selected and less than the maximum size of 500mb(524288000 bytes)
            the description field will show. If the size is larger than 500mb, error will be
            displayed
Params:     file_field  the input text box for the file description

 */
function description_handler(file_field, desc)
{

    //if user selected some files
    if(file_field[0].files.length > 0)
    {
        //display an error message if the file exceeds the file storage limit
        if (file_field[0].files[0].size > 524288000) {
            //append an error message
            $("#id_file_description").before("<p style='color:red' id='file_error'>File has been removed. File is larger than the allowed maximum size. </p>");

            file_field[0].value = "";

            $(desc).hide();
        }
        else {
            $(desc).show();

            //if no error hide the error field
            if($("#file_error").length > 0);
            {
                $("#file_error").hide();
            }

            if($("button[type=submit]").attr('disabled')!= undefined)
            {
                $("button[type=submit]").removeAttr('disabled')
            }
            desc.siblings().removeAttr("hidden");
            desc.removeAttr("type");
        }
    }
    //no files are present for upload so hide description title and input
    else
    {
        desc.siblings().attr("hidden", "");
        desc.attr("type", "hidden");

        $("#file_error").hide();
    }


}
