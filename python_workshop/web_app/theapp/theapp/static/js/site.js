$(document).ready(function () {
    $(".btn.show_users").click(function () {
        $.get('/api/active_user_count').then(function (e) {
            $("#user_count").text("User count: " + e.count);
        })

    })
});