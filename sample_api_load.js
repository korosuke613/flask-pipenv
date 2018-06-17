// DOMを全て読み込んだあとに実行される
$(function () {
    // 「#execute」をクリックしたとき
    $('#execute').click(function () {
        // Ajax通信を開始する
        $.ajax({
            url: 'http://127.0.0.1:5000/api/timecapsule/user',
            type: 'post', // getかpostを指定(デフォルトは前者)
            //dataType: 'json', // 「json」を指定するとresponseがJSONとしてパースされたオブジェクトになる
            data: { // 送信データを指定(getの場合は自動的にurlの後ろにクエリとして付加される)
                id: $('#id').val(),
                name: $('#name').val(),
                address: $('#address').val(),
                mail_address: $('#mail_address').val(),
                password: $('#password').val(),
            }
        })
        // ・ステータスコードは正常で、dataTypeで定義したようにパース出来たとき
        .done(function (response) {
            $('#result').val('成功');
            $('#detail').val(response.message);
        })
        // ・サーバからステータスコード400以上が返ってきたとき
        // ・ステータスコードは正常だが、dataTypeで定義したようにパース出来なかったとき
        // ・通信に失敗したとき
        .fail(function (response) {
            $('#result').val('失敗');
            $('#detail').val(response.data);
        });
    });
});