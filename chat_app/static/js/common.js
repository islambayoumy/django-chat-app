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

    $('#send').click(function(){
        var msg = $("#msg").val();
        if (msg != ""){
            ///
        } else{
            alert("please enter a message !")
        }
    });

});