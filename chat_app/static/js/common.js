$(document).ready(function() {

setInterval(function () {
    users_list();
    msgs_logs();
}, 2500);


function users_list(){
    // send ajax requests for updated users list and status
}

function msgs_logs(){
    // get updated msg logs
}

    $('#send').click(function(){
        var msg = $("#msg").val();
        if (msg != ""){
            // post msg
        } else{
            alert("please enter a message !")
        }
    });

});