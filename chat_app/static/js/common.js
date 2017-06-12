$(document).ready(function() {

// global variable for user id to be receive msgs
var gUserId = 0;
var userId = $('.userId').attr("id");

// call users list funtion
users_list(userId);

setInterval(function () {
    users_list();
    if (gUserId != 0){
        msgs_logs(userId, gUserId);
    } 
}, 7000);


// get all users list and status on load
function users_list(){
    // ajax get request for users list
    $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:8000/api/users_list/',
        data: {userId},
        datatype: "json",
        success: function(data){
            var item = "";
            var status, status_class = "";
            $.each(data, function(index, element) {
                if (element.status == true){status = "online";status_class="success"}
                else{status = "offline";status_class="warning"}
                item += '<a id="'+ element.user.id +'" class="list-group-item"><span class="label label-'+ status_class +'">'+ status +'</span> '+ element.user.first_name +'</a>'
            });
            $('.list-group').html(item);

            if(gUserId != 0){$("#"+ gUserId).addClass('active');}
        }
    });
}


// get updated msg logs
function msgs_logs(fromId, toId){
    var msg_container = $('#messages');
    $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:8000/api/msgs_logs/',
        data: {fromId, toId},
        datatype: "json",
        success: function(data){
            var item = "";
            var d,direction;
            var options = {weekday: 'short', month: 'long', day: 'numeric', minute: 'numeric', hour: 'numeric'};
            if(data != ""){
                $.each(data, function(index, element) {
                    d = new Date(element.timestamp);
                    if(element.sender == fromId){direction="text-danger"}
                    else{direction="text-primary"}
                    item += '<p class="'+ direction +'">' + element.msg + ' <small> ' + d.toLocaleString('en-US', options) + '</small></p><br>';
                });
            } else{
                item = '<p>No messages yet ! send first msg ?</p>';
            }
            msg_container.html(item);
            msg_container.scrollTop(msg_container.prop("scrollHeight"));
        }
    });
}

// handle user click
$(document).on('click', '.list-group-item', function () {
	gUserId = $(this).attr('id');
    $('.list-group-item').removeClass('active');
    $(this).addClass('active');
    msgs_logs(userId, gUserId);
});

// handle submitting msgs
function handle_post_msg(){
    var csrfmiddlewaretoken = getCookie('csrftoken');
    var msg = $("#msg").val();
    var fromId = userId;
    var toId = gUserId;
    if (msg != ""){
        if(toId != 0){
            // ajax post request for posting new msg
            $.ajax({
                type: 'POST',
                url: 'http://127.0.0.1:8000/api/msgs_logs/',
                data: {csrfmiddlewaretoken, fromId, toId, msg},
                datatype: "json",
                success: function(data){
                    $("#msg").val("");
                    msgs_logs(userId, gUserId);
                }
            });
        } else{
            alert("please choose a user to send ..");
        }
    } else{
        alert("please enter a message !");
    }
}

// click listener for send button
$('#send').click(function(){
    handle_post_msg();
});


// key press listener for "Enter"" key
$('#msg').keypress(function (e) {
    var key = e.which;
    if(key == 13){
        $('#send').click();
        return false;  
    }
});   


// get csrf token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


});
