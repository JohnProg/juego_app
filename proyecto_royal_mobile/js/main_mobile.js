$(document).on('ready',init());

function init(){
    var prevSelection = "tab1";
    $("#navbar ul li").live("click", function clickTab(){
        var newSelection = $(this).children("a").attr("data-tab-class");
        $("."+prevSelection).addClass("ui-screen-hidden");
        $("."+newSelection).removeClass("ui-screen-hidden");
        prevSelection = newSelection;
    });
    $('#form_login_app').on('submit', login_function);
    $("#log_in").live("click", login_function);

}

function login_function (event){
    event.preventDefault();
    var url = '/mobile/login_buyer/';
    $.ajax({
        url: url,
        data: {
            password: $('#password').val(),
            email: $('#username').val()
        },
        type: 'POST',
        dataType: 'json',
        success: function (data) {
            console.log(data.status);
            if (data.status === 'OK') {
                $.mobile.navigate( "#pagina2" );
                getInventoryItems();
            }
            else{
                $('.overlay').fadeIn().children().addClass('effect_in_out');
            }
        }
    });
}

function getInventoryItems(){
    var url = '/mobile/inventory/';
    $.ajax({
       url: url,
       type: 'GET',
       dataType: 'json',
       success: function(data){
            console.log('Data successfully received')
       }
    });
}