/**
* Created by Brett on 2017-03-22.
*/
var criteriaCount = 0;



/***
 * Function:    runQuery
 * Parameters:  requestURL: The URL to run the request against.
 * Purpose: Makes an AJAX call to the given request URL, and then returns the data.
 */
function runQuery(requestURL)
{
    var toReturn = null;
    $.ajax({
        // Setting async to false, so that a) data can be returned from this method and b) we can successfully
        // apply AND/OR filtering later on in this code
        async: false,
        method: 'GET',
        url: requestURL,
        success: function(data, status)
        {
            toReturn = data.results;
        }
    });

    return toReturn;
}

/***
 * Function:    addCriteria
 * Purpose:     Add another criteria box to the form, and increment the criteria count.
 */
function addCriteria()
{
    criteriaCount++;
   $("#filteringForm").append('<div id="filter-entry-' + criteriaCount + '"> ' +
       '<div class="form-group"> <label>Field</label> <select class="form-control" id="field-choice-' + criteriaCount + '" onchange="determineToShowEquality(' + criteriaCount + ')"> ' +
       '<option value="type">Type</option> <option value="amount">Award Amount</option> <option value="date">Date</option> <option value="description">Description</option> </select> </div> <div class="form-group"> ' +
       '<label>Criteria</label> <select class="form-control" id="field-criteria-' + criteriaCount + '"> <option value="gt">></option> <option value="ee" selected>==</option> <option value="lt">' +
       '<</option> </select> </div><div class="form-group" id="filter_values-' + criteriaCount + '"> <label>Value</label> <input type="text" class="form-control" id="field-value-' + criteriaCount + '"> </div> <div class="form-group">' +
       ' <label>Logical Join</label> <input type="radio" name="field-join-' + criteriaCount + '" class="form-control" value="AND" checked>AND <input type="radio" name="field-join-' + criteriaCount + '" class="form-control" value="OR">OR</div><div class="form-group"> ' +
       '<button class="form-control btn btn-info" onclick="addCriteria()"> <span class="glyphicon glyphicon-plus"></span> </button> ' +
       '<button class="form-control btn btn-warning close" id="remove-' + criteriaCount + '" onclick="removeCriteria(' + criteriaCount + ')"> <span aria-hidden="true">&times;</span> </button></div> </div>');
    determineToShowEquality(criteriaCount);
}

// This function is courtesy of:
// http://stackoverflow.com/questions/1584370/how-to-merge-two-arrays-in-javascript-and-de-duplicate-items
function arrayUnique(array)
{
    var a = array.concat();
    for(var i=0; i<a.length; ++i) {
        for(var j=i+1; j<a.length; ++j) {
            if(a[i] === a[j])
                a.splice(j--, 1);
        }
    }

    return a;
}

/***
 * Function:    applyFilter
 * Purpose:     Apply the filters the user has specified to filter data.
 */
function applyFilter()
{
    var all_records = [];
    var curr_records = [];
    //var currRecord = 0;
    const BASE_REQUEST_URL = "http://127.0.0.1:8000/api-root/grievance_award/filter/?";
    var next_join = "OR";
    $("#grievance-award-table-data").html("");
    for (var i = 0; i <= criteriaCount; i++)
    {
        var request_url = BASE_REQUEST_URL;
            // Run a query right now on the current criteria and combine it with
            // the previous results
            if ($("#field-choice-" + i).val() === "date")
            {
                // Determine if less than, greater than, or equals was selected
                switch($("#field-criteria-" + i).val())
                {
                    case 'gt':
                        request_url += 'min_date=' + convertDateFormat($("#field-value-" + i).val());
                        break;
                    case 'lt':
                        request_url += 'max_date=' + convertDateFormat($("#field-value-" + i).val());
                        break;
                    default:
                        request_url += 'date=' + convertDateFormat($("#field-value-" + i).val());
                        break;
                }
                curr_records = runQuery(request_url);
            }
            // Check for an empty description
            else if ($("#field-choice-" + i).val() === "description")
            {
                console.log($("#field-value-" + i).val());
                if($("#field-value-" + i).val() != null)
                {
                    request_url += "empty_desc_filter=True";
                    curr_records = runQuery(request_url);
                }
                else
                {
                    request_url += "description__contains=" + $("#field-value" + i).val();
                    curr_records = runQuery(request_url);
                }
                console.log(request_url);
            }
            else if ($("#field-choice-" + i).val() === "type")
            {
                // Run three queries: one on first name, one on middle name, and one on last name
                // Next, combine them with an OR
                if($("#field-value-" + i).val() == 7)
                {
                    request_url += "case__caseType=" + $("#field-value-" + i).val();
                }
                else
                {
                    request_url += "policy=" + $("#field-value-" + i).val();
                }

                curr_records = runQuery(request_url);
            }
            else if ($("#field-choice-" + i).val() ==="amount")
            {
                // Determine if less than, greater than, or equals was selected
                switch($("#field-criteria-" + i).val())
                {
                    case 'gt':
                        request_url += 'min_amount=' + $("#field-value-" + i).val();
                        break;
                    case 'lt':
                        request_url += 'max_amount=' + $("#field-value-" + i).val();
                        break;
                    default:
                        request_url += 'awardAmount=' + $("#field-value-" + i).val();
                        break;
                }
                curr_records = runQuery(request_url);
            }
            else
            {
                // If no other conditions have been met, just run the query
                request_url += $("#field-choice-" + i).val() + "=" + $("#field-value-" + i).val();
                curr_records = runQuery(request_url);
            }

            // Determine how to combine all of our arrays depending on the join type selected
            if (next_join === "OR")
            {
                all_records = combineArraysOR(all_records, curr_records);
            }
            else
            {
                all_records = combineArraysAND(all_records, curr_records);
            }
        next_join = $("[name=field-join-" + i + "]:checked").val();
    }

    // Now display the result
    filterTable(all_records);
}

/***
 * Function:    combineArraysAND
 * Purpose:     Combine two given arrays with an AND operator based on contact log IDs.
 * @param arrayOne - The first array
 * @param arrayTwo - the second array
 * @returns {Array} - the arrays combined with an AND
 */
function combineArraysAND(arrayOne, arrayTwo)
{
    var result_array = [];
    for(var i = 0; i < arrayOne.length; i++)
    {
        var found = false;
        for(var j = 0; j < arrayTwo.length && !found; j++)
        {
            if (arrayOne[i].id === arrayTwo[j].id)
            {
                found = true;
                result_array.push(arrayOne[i]);
            }
        }
    }

    return result_array;
}

/***
 * Function:    combineArraysOR
 * Purpose:     Combine two given arrays with an OR operator.
 * @param arrayOne - The first array
 * @param arrayTwo - the second array
 * @returns {Array} - the arrays combined with an OR
 */
function combineArraysOR(arrayOne, arrayTwo)
{
    var result_array = arrayOne;

    // Loop through all items in the second array
    for (var i = 0; i < arrayTwo.length; i++)
    {
        var found = false;
        // Check to see if it exists in the first array
        for (var j = 0; j < arrayOne.length && !found; j++)
        {
            // If it exists, quit looping
            found = arrayTwo[i].id === arrayOne[j].id;
        }

        // If it wasn't found, add the item to the array
        if (!found)
        {
            result_array.push(arrayTwo[i]);
        }
    }

    // Return our new results
    return result_array;
}

/***
 * Function:    formatDate
 * Purpose:     Given a date in the form YYYY-MM-DD, format and return it in the form DD-MMM-YYYY.
 * @param toFormat
 * @returns {string}
 */
function formatDate(toFormat)
{
    var monthNames = [
        "Jan", "Feb", "Mar",
        "Apr", "May", "Jun", "Jul",
        "Aug", "Sep", "Oct",
        "Nov", "Dec"
      ];

    // Grab the year, month, and date
    var year = toFormat.substring(0, 4);
    var monthIndex = parseInt(toFormat.substring(6, 9));
    var date = toFormat.substring(8, 11);

    // Put together the new date and return it
    var toReturn = date + ", " + monthNames[monthIndex - 1] + ". " + year;
    return toReturn;
}

/***
 * Function:    filterTable
 * Purpose:     Add new data to the table according to the passed-in data.
 * @param newData - The data to be added.
 */
function filterTable(newData)
{
    $("#grievance-award-table-data").html("");
    newData.forEach(function(item, index)
    {
        var id = item.id;
        var amount = item.awardAmount;
        var date = formatDate(item.date);
        var description = item.description;
        var rowToAdd = "<tr><td>" + id + "</td><td>" + amount + "</td><td>" + date + "</td><td>" + description + '</td><td><a href="/grievance/detail/' + id + '">[View]</a></td><td><a href="/grievance/edit/' + id + '">[Edit]</a></td></tr>';

        $("#grievance-award-table-data").append(rowToAdd);
    });
}

/***
 * Function:    removeCriteria
 * Purpose:     Removes criteria with the given number from the table.
 * @param num - The criteria ID/row to remove.
 */
function removeCriteria(num)
{
    // Remove the entire row of filtering
    $("#filter-entry-" + num).remove();

    // Decrement the IDs of inputs that occur after
    for (var i = num + 1; i <= criteriaCount; i++)
    {
        // Decrement filter-entry
        $("#filter-entry-" + i).attr('id', 'filter-entry-' + (i - 1));
        // Decrement field-choice
        $("#field-choice-" + i).attr('id', 'field-choice-' + (i - 1));
        // Decrement field-criteria
        $("#field-criteria-" + i).attr('id', 'field-criteria-' + (i - 1));
        // Decrement field-value
         $("#field-value-" + i).attr('id', 'field-value-' + (i - 1));
        // Decrement field-join
        $("#field-join-" + i).attr('id', 'field-join-' + (i - 1));
        // Change the onclick value + ID of the onclick button
        $("#remove-" + i).attr('id', 'remove-' + (i - 1));
        $("#remove-" + (i - 1)).attr('onclick', 'removeCriteria(' + (i - 1) + ')');
    }

    // Decrement criteria count
    criteriaCount--;
}

/***
 * Function:    determineToShowEquality
 * Purpose:     Determine whether or not to show the equality select box for a specific field based
 *              on its current value.
 * @param elem - the element to look at
 */
function determineToShowEquality(elem)
{
    if ($("#field-choice-" + elem).val() == "date" || $("#field-choice-" + elem).val() == "amount")
    {
        // Show the entire div that the equality selector is in - which happens
        // to be the parent of the field-choice select element
        $("#field-criteria-" + elem).parent().show();
        $("#field-value-" + elem).remove();
        $("#filter_values-" + elem).append('<input type="text" class="form-control" id="field-value-' + elem + '" name="field-value-' + elem + '">');
    }
    else if($("#field-choice-" + elem).val() == "type")
    {
        $("#field-criteria-" + elem).parent().hide();
        $("#field-value-" + elem).remove();
        $("#filter_values-" + elem).append("<select class='form-control' id='field-value-" + elem + "'></select>");
        $("#field-value-" + elem).append("<option value='7'>Member</option><option value='6'>Policy</option>");
    }
    else
    {
        $("#field-criteria-" + elem).parent().hide();
        $("#field-value-" + elem).remove();
        $("#filter_values-" + elem).append('<input type="text" class="form-control" id="field-value-' + elem + '">');
    }
}

// This function is courtesy of:
// http://stackoverflow.com/questions/17445585/javascript-convert-string-into-date-with-format-dd-mmm-yyyy-i-e-01-jun-2012
function convertDateFormat(enteredDate)
{
    var dateToReturn = new Date(enteredDate);
    // Convert the date to a string in the form DD/MM/YYYY, and then
    // change all the slashes to hyphens
    return dateToReturn.toLocaleDateString("en-CA");
}

$(document).ready(function()
{
    // Hide the equality selector for the first criteria by default
    determineToShowEquality(0);
})