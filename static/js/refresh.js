$(function(){
    $('#verifycodeChange').css('cursor','pointer').click(function() {
        $('#verifycode').attr('src',$('#verifycode').attr('src')+1)
    });
});
