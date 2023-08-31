$(document).ready(function () {
    $('.correctBox').on('click', function (event) {

        $.ajax({
            url: toggleCorrectUrl,
            method: 'POST',
            data: {

            },
        });
    });
});