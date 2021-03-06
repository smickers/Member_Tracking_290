/**
 * Created by cst237 on 3/16/17.
 */
var xhr = undefined;
var upload_button = undefined;
var fileSelect = undefined;
var stop_upload = undefined;
var confirm_button_y = undefined;
var confirm_button_n = undefined;
var json_members = undefined;
var url_upload = undefined;
var url_xlsx_json = undefined;
var list_members = undefined;
var json_to_members = undefined;
var pk_to_file = undefined;


var BulkCreate = {
    init: function(url_file_endpoint, url_xlsx_to_json, json_to_members_in){
        xhr = new XMLHttpRequest();
        upload_button = document.getElementById('upload_button');
        fileSelect = document.getElementById("file-select");
        // stop_upload = document.getElementById("stop_upload");
        confirm_button_y = $('#submit_json_y');
        confirm_button_n = $('#submit_json_n');
        json_members = undefined;
        list_members = $('#list_members');
        url_upload = url_file_endpoint;
        url_xlsx_json = url_xlsx_to_json;
        json_to_members = json_to_members_in;
         $('#confirmation').hide();
        BulkCreate.bindEvents();
    },


    bindEvents: function(){

        confirm_button_n.click( function(e){
            $("#progress").empty();
            $('#list_members').empty();
            $('#confirmation').hide();
            $("#success").hide();
            fileSelect.value = "";
        });

        confirm_button_y.click(function(e){
            e.preventDefault();
            xhr.open('POST', json_to_members , false);
            xhr.setRequestHeader("Content-Type", "application/json");
            // Set up a handler for when the request finishes.
            xhr.onload = function () {
                //JSON sent
              if (xhr.status !== 500) {
                var json_response = JSON.parse(this.responseText);
                $("#success").show();
                $("#success").html('<h3>Successfully created' + json_response.count + ' members </h3> ');
                console.log(json_response);
                $("#progress").empty();
                $('#list_members').empty();
                $('#confirmation').hide();
                fileSelect.value = "";
              }
            };
            xhr.send( JSON.stringify({pk: pk_to_file} ));
        });
        upload_button.addEventListener('click', function(event){
            event.preventDefault() ;
            var files = fileSelect.files;
            var formData = new FormData();
            formData.append('file', files[0]);
            // Set up the request.
            xhr.upload.addEventListener('progress',function(oEvent){
              if (oEvent.lengthComputable) {
                var percentComplete = oEvent.loaded / oEvent.total;
                document.getElementById("progress").innerHTML =  (percentComplete * 100) + "%";
              } else {
                document.getElementById("progress").innerHTML =  'unknown';
              }
            });

            xhr.open('POST', url_upload , true);
            xhr.setRequestHeader('Content-Disposition', 'attachment; filename='+files[0].name);
            // Set up a handler for when the request finishes.
            xhr.onload = function () {
                // File(s) uploaded.
              if (xhr.status === 201) {
                  var json_response = JSON.parse(this.responseText);
                  var event = new CustomEvent('uploaded_valid_fl', {'detail': json_response.id });
                  pk_to_file = json_response.id;
                upload_button.dispatchEvent(event);
              }
            };
            xhr.send(formData);
        });

        upload_button.addEventListener('uploaded_valid_fl', function(e){
            var xhr = new XMLHttpRequest();
            xhr.open('GET', url_xlsx_json + e.detail + "?format=json", true);
            xhr.onload = function () {
              if (xhr.status === 200) {
                BulkCreate.createTable( JSON.parse(this.responseText) ) ;
              }
            };
            xhr.send();
        });
    },

    createTable: function (json_members_temp) {
        list_members.empty();
        json_members = json_members_temp;
        var ele = $('<thead></thead>');
        ele.append($('<th>First Name</th>'));
        ele.append($('<th>Middle Name</th>'));
        ele.append($('<th>Last Name</th>'));
        ele.append($('<th>Department</th>'));
        ele.append($('<th>Campus</th>'));
        ele.append($('<th>Employee Status</th>'));
        ele.append($('<th>Position Title</th>'));
        list_members.append(ele);
        var tbody = $('<tbody></tbody>');
        json_members_temp.Result.forEach(function (val) {
            var ele = $('<tr></tr>');
            ele.append($("<td></td>").text(val.firstName));
            ele.append($("<td></td>").text(val.middleName));
            ele.append($("<td></td>").text(val.lastName));
            ele.append($("<td></td>").text(val.department));
            ele.append($("<td></td>").text(val.campus));
            ele.append($("<td></td>").text(val.employeeStatus));
            ele.append($("<td></td>").text(val.posTitle));
            tbody.append(ele);
        });
        list_members.append(tbody);
        $('#confirmation').show();
        // BulkCreate.bindEvents();
    }

};


