$(document).ready(function() {

users_list();

setInterval(function () {
    users_list();
    msgs_logs();
}, 10000);


function users_list(){
    var userId = $('.userId').attr("id");
    
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
                item += '<a href="#" id="'+ element.user.id +'" class="list-group-item"><span class="label label-'+ status_class +'">'+ status +'</span> '+ element.user.first_name +'</a>'
            });
            $('.list-group').html(item);
        }
    });

}

function msgs_logs(){
    // get updated msg logs
}

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


$('#send').click(function(){
    var csrfmiddlewaretoken = getCookie('csrftoken');
    var msg = $("#msg").val();
    var fromId = 9;
    var toId = 10;
    if (msg != ""){
        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:8000/api/msgs_logs/',
            data: {csrfmiddlewaretoken, fromId, toId, msg},
            datatype: "json",
            success: function(data){
                
            }
        });
    } else{
        alert("please enter a message !")
    }
});

});