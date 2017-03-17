/**
 * Created by Brett on 2017-03-15.
 */
$(document).ready( function() {
    var page = 1;
    var data_each_page = 30;
    var end_point_url = "/api-root/member/filter/?limit=30&" ;
    var temp_endpoint = end_point_url;
    var form_no = 0;

    // Hiding the option for a range of dates until an initial date has been selected.
    $("#id_max_bDay_year").hide();
    $("#id_max_bDay_day").hide();
    $("#id_max_bDay_month").hide();
    $("label[for='id_max_bDay_day']").hide();

    // On change handler, if the user selects a year, it shows the other select boxes to make a range of dates.
    $("#id_min_bDay_year").change($("#id_min_bDay_year").val() > 0 || $("#id_min_bDay_year").val() != null ? function(){
        $("#id_max_bDay_year").show();
        $("#id_max_bDay_day").show();
        $("#id_max_bDay_month").show();
        $("label[for='id_max_bDay_day']").show();
    }: false);

    // Hiding the option for a range of dates until an initial date has been selected.
    $("#id_max_hDay_year").hide();
    $("#id_max_hDay_day").hide();
    $("#id_max_hDay_month").hide();
    $("label[for='id_max_hDay_day']").hide();

    // On change handler, if the user selects a year, it shows the other select boxes to make a range of dates.
    $("#id_min_hDay_year").change($("#id_min_hDay_year").val() > 0 || $("#id_min_hDay_year").val() != null ? function(){
        $("#id_max_hDay_year").show();
        $("#id_max_hDay_day").show();
        $("#id_max_hDay_month").show();
        $("label[for='id_max_bDay_day']").show();
    }: false);

    // Clearing out our default values
    $("#form").find(':input').val("");

    /*
        This is my brilliant function to clone the form and append the clone to the end of the form container.
     */
    $("#moreFilters").click(function(){
        form_no++;  // Increment the number of forms.

        // Getting the source form to be cloned.
        var source = $("#form");
        // On the first go around, we append a hr to separate our forms.
        form_no == 1 ? source.append("<hr />") : false;
        // Clone the form.
        var clone = source.clone();

        // Add the form number to the id of each input tag.
        clone.find(':input').attr('id', function(i, val){
            return val + form_no;
        });

        // Clearing out the each input.
        clone.find(':input').val("");

        // Adding it to the form container
        clone.appendTo("#form_container");
    });

    /*
        This function performs our filtering. It builds a url with each parameter required and passes it into our
        ajax function.
     */
    $("#filter").click(function(){
        // If the form_no is greater than 0 (this is an OR case), we don't want to limit our results to the initial 30.
        // We also hide the show more button
        if(form_no > 0) {
            temp_endpoint = "/api-root/member/filter/?";
            $("#show_more").hide();
        }
        else // Otherwise, we don't care. Show the button and keep the 30 at a time.
        {
            temp_endpoint = end_point_url;
            $("#show_more").show();
        }

        // Some fancy variables to be used to build some date strings
        var minBday = null;
        var maxBday = null;
        var minHday = null;
        var maxHday = null;

        // These if blocks check to see if the dates are filled out, if so, we build a date string
        if($("#id_min_bDay_year").val() != null)
        {
            if($("#id_min_bDay_month").val() != null && $("#id_min_bDay_day").val() !=null)
            {
                var minBdayDate = new Date($("#id_min_bDay_year").val(), $("#id_min_bDay_month").val(),$("#id_min_bDay_day").val());
                minBday = minBdayDate.getFullYear() + "-" + (minBdayDate.getMonth()) + "-" +minBdayDate.getDate();
            }
            else if($("#id_min_bDay_month").val() != null)
            {
                minBday = $("#id_min_bDay_year").val() + "-" + $("#id_min_bDay_month").val() + "-1";
            }
            else
            {
                minBday =  $("#id_min_bDay_year").val() + "-1-1";
            }
        }

        // These if blocks check to see if the dates are filled out, if so, we build a date string
        if($("#id_max_bDay_year").val() != null)
        {
            if($("#id_max_bDay_month").val() != null && $("#id_max_bDay_day").val() !=null)
            {
                var maxBdayDate = new Date($("#id_max_bDay_year").val(), $("#id_max_bDay_month").val(),$("#id_max_bDay_day").val());
                maxBday = maxBdayDate.getFullYear() + "-" + (maxBdayDate.getMonth()) + "-" +maxBdayDate.getDate();
            }
            else if($("#id_max_bDay_month").val() != null)
            {
                maxBday = $("#id_max_bDay_year").val() + "-" + $("#id_max_bDay_month").val() + "-30";
            }
            else
            {
                maxBday =  $("#id_max_bDay_year").val() + "-12-30";
            }
        }
        else if (minBday != null)   // If the user selected a min date but not a max date range
        {
            /*
                In here we check to see what values were chosen in the min range and create a date string based on
                what the user has entered
             */
            if($("#id_min_bDay_day").val() != null)
            {
                maxBday = minBday;
            }
            else if ($("#id_min_bDay_month").val() != null)
            {
                var day = $("#id_min_bDay_month").val() % 2 == 0 ? 31: 30;
                $("#id_min_bDay_month").val() == 2 ? day = 28: day = day;
                maxBday = $("#id_min_bDay_year").val() + "-" + $("#id_min_bDay_month") + "-" + day;
            }
            else
            {
                maxBday = $("#id_min_bDay_year").val() + "-12-31";
            }
        }

        // These if blocks check to see if the dates are filled out, if so, we build a date string
        if($("#id_min_hDay_year").val() != null)
        {
            if ($("#id_min_hDay_month").val() != null && $("#id_min_hDay_day").val() != null) {
                var minHdayDate = new Date($("#id_min_hDay_year").val(), $("#id_min_hDay_month").val(), $("#id_min_hDay_day").val());
                minHday = minHdayDate.getFullYear() + "-" + (minHdayDate.getMonth()) + "-" + minHdayDate.getDate();
            }
            else if ($("#id_max_bDay_month").val() != null) {
                minHday = $("#id_min_hDay_year").val() + "-" + $("#id_min_hDay_month").val() + "-1";
            }
            else {
                minHday = $("#id_min_hDay_year").val() + "-1-1";
            }
        }

        // These if blocks check to see if the dates are filled out, if so, we build a date string
        if($("#id_max_hDay_year").val() != null)
        {
            if ($("#id_max_hDay_month").val() != null && $("#id_max_hDay_day").val() != null) {
                var maxHdayDate = new Date($("#id_max_hDay_year").val(), $("#id_max_hDay_month").val(), $("#id_max_hDay_day").val());
                maxHday = maxHdayDate.getFullYear() + "-" + (maxHdayDate.getMonth()) + "-" + maxHdayDate.getDate();
            }
            else if ($("#id_max_bDay_month").val() != null) {
                maxHday = $("#id_max_hDay_year").val() + "-" + $("#id_max_hDay_month").val() + "-30";
            }
            else {
                maxHday = $("#id_max_hDay_year").val() + "-12-30";
            }
        }
        else if (minHday != null)// If the user selected a min date but not a max date range
        {
            /*
                In here we check to see what values were chosen in the min range and create a date string based on
                what the user has entered
             */
            if($("#id_min_hDay_day").val() != null)
            {
                maxHday = minHday;
            }
            else if ($("#id_min_bHay_month").val() != null)
            {
                var day = $("#id_min_bHay_month").val() % 2 == 0 ? 31: 30;
                $("#id_min_bHay_month").val() == 2 ? day = 28: day = day;
                maxHday = $("#id_min_hDay_year").val() + "-" + $("#id_min_bHay_month") + "-" + day;
            }
            else
            {
                maxHday = $("#id_min_hDay_year").val() + "-12-31";
            }
        }

        // This lovely block of code checks to see if each input field has a value in it. If they do, we add that to our string.
        // If they don't, we just ignore them. I used false in this case just because I can.
        $('#id_memberID').val() > 0 ? temp_endpoint += "memberID=" + encodeURIComponent($('#id_memberID').val())+ "&" : false;
        $('#id_firstName').val().length > 0 ? temp_endpoint += "firstName__contains=" + encodeURIComponent($('#id_firstName').val())+ "&" : false;
        $('#id_middleName').val().length > 0 ? temp_endpoint += "middleName__contains=" + encodeURIComponent($('#id_middleName').val())+ "&": false;
        $('#id_lastName').val().length > 0 ? temp_endpoint += "lastName__contains=" + encodeURIComponent($('#id_lastName').val())+ "&": false;
        $('#id_socNum').val() > 0 ? temp_endpoint += "socNum__contains=" + encodeURIComponent($('#id_socNum').val())+ "&": false;
        $('#id_city').val().length > 0 ? temp_endpoint += "city__contains=" + encodeURIComponent($('#id_city').val())+ "&": false;
        $('#id_mailAddress').val().length > 0 ? temp_endpoint += "mailAddress__contains=" + encodeURIComponent($('#id_mailAddress').val())+ "&": false;
        $('#id_mailAddress2').val().length > 0 ? temp_endpoint += "mailAddress2__contains=" + encodeURIComponent($('#id_mailAddress2').val())+ "&": false;
        $('#id_pCode').val().length > 0 ? temp_endpoint += "pCode__contains=" + encodeURIComponent($('#id_pCode').val())+ "&": false;
        $('#id_hPhone').val().length > 0 ? temp_endpoint += "hPhone__contains=" + encodeURIComponent($('#id_hPhone').val())+ "&": false;
        $('#id_campus').val() != null ? temp_endpoint += "campus__contains=" + encodeURIComponent($('#id_campus').val())+ "&": false;
        $('#id_jobType').val() != null ? temp_endpoint += "jobType__contains=" + encodeURIComponent($('#id_jobType').val())+ "&": false;
        $('#id_committee').val().length > 0 ? temp_endpoint += "committee__contains=" + encodeURIComponent($('#id_committee').val())+ "&": false;
        $('#id_membershipStatus').val() != null ? temp_endpoint += "membershipStatus__contains=" + encodeURIComponent($('#id_membershipStatus').val())+ "&": false;
        $('#id_programChoice').val().length > 0 ? temp_endpoint += "programChoice__contains=" + encodeURIComponent($('#id_programChoice').val())+ "&": false;
        (minHday != null ) ? temp_endpoint += "min_hDay=" + encodeURIComponent(minHday)+ "&": temp_endpoint += '';
        (maxHday != null ) ? temp_endpoint += "max_hDay=" + encodeURIComponent(maxHday)+ "&": temp_endpoint += '';
        (minBday != null ) ? temp_endpoint += "min_bDay=" + encodeURIComponent(minBday)+ "&": temp_endpoint += '';
        (maxBday != null ) ? temp_endpoint += "max_bDay=" + encodeURIComponent(maxBday)+ "&": temp_endpoint += '';
        $('#id_gender').val() != null ? temp_endpoint += "gender=" + encodeURIComponent($('#id_gender').val()) + "&": false;
        // Make our ajax call to our API
        console.log(temp_endpoint);
        ajax_call(temp_endpoint);

        // If we have multiple fields, we use this loop. We build a new url for each form and the results are added on to our
        // table.
        for(var i = 1; i <= form_no; i++)
        {
            // Some fancy variables to be used to build some date strings
            var minBday = null;
            var maxBday = null;
            var minHday = null;
            var maxHday = null;
            // These if blocks check to see if the dates are filled out, if so, we build a date string
            if($("#id_min_bDay_year" +i).val() != null && $("#id_min_bDay_month"+i).val() != null && $("#id_min_bDay_day"+i).val() !=null)
            {
                var minBdayDate = new Date($("#id_min_bDay_year"+i).val(), $("#id_min_bDay_month"+i).val(),$("#id_min_bDay_day"+i).val());
                minBday = minBdayDate.getFullYear() + "-" + (minBdayDate.getMonth()) + "-" +minBdayDate.getDate();
            }
            if($("#id_max_bDay_year"+i).val() != null && $("#id_max_bDay_month"+i).val() != null && $("#id_max_bDay_day"+i).val() !=null)
            {
                var maxBdayDate = new Date($("#id_max_bDay_year"+i).val(), $("#id_max_bDay_month"+i).val(),$("#id_max_bDay_day"+i).val());
                maxBday = maxBdayDate.getFullYear()+ "-" + (maxBdayDate.getMonth()) + "-" +maxBdayDate.getDate();
            }
            if($("#id_min_hDay_year"+i).val() != null && $("#id_min_hDay_month"+i).val() != null && $("#id_min_hDay_day"+i).val() !=null)
            {
                var minHdayDate = new Date($("#id_min_hDay_year"+i).val(), $("#id_min_hDay_month"+i).val(),$("#id_min_hDay_day"+i).val());
                minHday =  minHdayDate.getFullYear()+ "-" + (minHdayDate.getMonth()) + "-" +minHdayDate.getDate();
            }
            if($("#id_max_hDay_year"+i).val() != null && $("#id_max_hDay_month"+i).val() != null && $("#id_max_hDay_day"+i).val() !=null)
            {
                var maxHdayDate = new Date($("#id_max_hDay_year"+i).val(), $("#id_max_hDay_month"+i).val(),$("#id_max_hDay_day"+i).val());
                maxHday = maxHdayDate.getFullYear() + "-" + (maxHdayDate.getMonth()) + "-" +maxHdayDate.getDate();
            }
            // Building our url with the parameters again.
            temp_endpoint = "/api-root/member/filter/?";
            $('#id_memberID'+i).val() > 0 ? temp_endpoint += "memberID=" + encodeURIComponent($('#id_memberID'+i).val())+ "&" : false;
            $('#id_firstName'+i).val().length > 0 ? temp_endpoint += "firstName__contains=" + encodeURIComponent($('#id_firstName'+i).val())+ "&" : false;
            $('#id_middleName'+i).val().length > 0 ? temp_endpoint += "middleName__contains=" + encodeURIComponent($('#id_middleName'+i).val())+ "&": false;
            $('#id_lastName'+i).val().length > 0 ? temp_endpoint += "lastName__contains=" + encodeURIComponent($('#id_lastName'+i).val())+ "&": false;
            $('#id_socNum'+i).val() > 0 ? temp_endpoint += "socNum__contains=" + encodeURIComponent($('#id_socNum'+i).val())+ "&": false;
            $('#id_city'+i).val().length > 0 ? temp_endpoint += "city__contains=" + encodeURIComponent($('#id_city'+i).val())+ "&": false;
            $('#id_mailAddress'+i).val().length > 0 ? temp_endpoint += "mailAddress__contains=" + encodeURIComponent($('#id_mailAddress'+i).val())+ "&": false;
            $('#id_mailAddress2'+i).val().length > 0 ? temp_endpoint += "mailAddress2__contains=" + encodeURIComponent($('#id_mailAddress2'+i).val())+ "&": false;
            $('#id_pCode'+i).val().length > 0 ? temp_endpoint += "pCode__contains=" + encodeURIComponent($('#id_pCode'+i).val())+ "&": false;
            $('#id_hPhone'+i).val().length > 0 ? temp_endpoint += "hPhone__contains=" + encodeURIComponent($('#id_hPhone'+i).val())+ "&": false;
            $('#id_campus'+i).val() != null  ? temp_endpoint += "campus__contains=" + encodeURIComponent($('#id_campus'+i).val())+ "&": false;
            $('#id_jobType'+i).val() != null ? temp_endpoint += "jobType__contains=" + encodeURIComponent($('#id_jobType'+i).val())+ "&": false;
            $('#id_committee'+i).val().length > 0 ? temp_endpoint += "committee__contains=" + encodeURIComponent($('#id_committee'+i).val())+ "&": false;
            $('#id_membershipStatus'+i).val() != null ? temp_endpoint += "membershipStatus__contains=" + encodeURIComponent($('#id_membershipStatus'+i).val())+ "&": false;
            $('#id_programChoice'+i).val().length > 0 ? temp_endpoint += "programChoice__contains=" + encodeURIComponent($('#id_programChoice'+i).val())+ "&": false;
            (minHday != null ) ? temp_endpoint += "min_hDay=" + encodeURIComponent(minHday)+ "&": temp_endpoint += '';
            (maxHday != null ) ? temp_endpoint += "max_hDay=" + encodeURIComponent(maxHday)+ "&": temp_endpoint += '';
            (minBday != null ) ? temp_endpoint += "min_bDay=" + encodeURIComponent(minBday)+ "&": temp_endpoint += '';
            (maxBday != null ) ? temp_endpoint += "max_bDay=" + encodeURIComponent(maxBday)+ "&": temp_endpoint += '';
            $('#id_gender'+i).val() != null ? temp_endpoint += "gender=" + encodeURIComponent($('#id_gender'+i).val()) + "&": false;
            // ajax call to api again.
            console.log(temp_endpoint);
            ajax_call(temp_endpoint);
        }

        $('#list_member')[0].innerHTML = "";


    });

    // This grabs another 30 results from our API. This could also be done by saving the 'next' value from the response.
    $("#show_more").click(function(){
        ajax_call(temp_endpoint+"offset=" + data_each_page*page);
        page++;
    });

    /*
        Function:   ajax_call
        Params:     end_url - the url of our API with all of the params included
        Purpose:    To make an ajax call to the backend and append the results to our table of members
     */
    function ajax_call(end_url){
        $.ajax({
            url: end_url,
            success: function(data){
                // Looping through our results, creating a table row element and with some member info, then appending it
                // to the table
                data.results.forEach(function(e){
                    var ele = $('<tr></tr>');
                    ele.append(
                        "<td><a href='/member/" + e.id + "'>" + e.firstName + " " + e.lastName + "</a></td>"
                    );
                    ele.append(
                        $("<td></td>").text(e.gender)
                    );
                    ele.append(
                        $("<td></td>").text(e.memberID)
                    );
                    ele.append(
                        $("<td></td>").text(e.city)
                    );
                    ele.append(
                        $("<td></td>").text(e.pCode)
                    );
                    ele.append(
                        $("<td></td>").text(e.bDay)
                    );
                    ele.append(
                        $("<td></td>").text(e.campus)
                    );

                    // Appending the element to the table
                    $('#list_member').append(ele);
                });

                // If this is the all the data we're getting, we hide our show more button from the user.
                if( data.next == null)
                {
                    $("#show_more").hide();
                }
                // Clearing out any duplicate results in the table. Duplicates can happen in the OR cases.
                removeDuplicateRows($('#list_member'));
            }
        });
    }

    // This function removes any duplicate rows that might pop up.
    function removeDuplicateRows($table){
        function getVisibleRowText($row){
            return $row.find('td:visible').text().toLowerCase();
        }

        $table.find('tr').each(function(index, row){
            var $row = $(row);
            $row.nextAll('tr').each(function(index, next){
                var $next = $(next);
                if(getVisibleRowText($next) == getVisibleRowText($row))
                    $next.remove();
            })
        });
    }

    // Loading our initial results.
    ajax_call(temp_endpoint);
});