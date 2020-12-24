$(function () {
    $('img').click(function () {
        console.log('1111');
        $(this).attr('src','/App/getcode/?t='+ Math.random())
    })
})

$('#submit').click(function () {

})