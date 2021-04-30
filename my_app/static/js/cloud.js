$(document).ready(function(){

    document.getElementById("addFolder").onclick = function() {addDirectory()};
    function addDirectory() {
        if (document.getElementById("FolderInput").value.trim() != ''){
            var xhttp = new XMLHttpRequest();
            xhttp.open("GET", "/cloud/addFolder/"+document.getElementById("FolderInput").value.trim(), false);
            xhttp.send();
            if (xhttp.responseText == "ko")
                $("#FolderInput").addClass("alert-danger")
            else {
                document.getElementById("FolderInput").value = "";
                console.log("noce");
                location.reload();
            }
        }
        else
            $("#FolderInput").addClass("alert-danger")
    }




    // document.getElementById("downloadFolder").onclick = function() {downloadDirectory()};
    // function downloadDirectory() {
    //      console.log("hi there");
    // //     $("#loadModal").modal('toggle');
    // }

    // $( "#downloadFolderButton" ).click(function() {
    //     console.log("hi there");
    // });
    //     var xhttp = new XMLHttpRequest();
    //     var xhttpZip = new XMLHttpRequest();
    //     xhttp.open("GET", "/cloud/downloadFolder/", true);
    //     xhttp.send();
    //     // $('#errorModal').addClass('d-block');
    //     if (xhttp.responseText == "ko")
    //         console.log("Error");
    //     else {
    //         // console.log(xhttp.responseText);
    //         // xhttpZip.open("GET", "/cloud/downloadZip/"+xhttp.responseText, false);
    //         // xhttpZip.send();
    //     }
    // }


});