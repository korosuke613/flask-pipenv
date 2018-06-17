// DOMを全て読み込んだあとに実行される

$(function () {

    // 「#execute」をクリックしたとき

    $('#execute').click(function () {

        // Ajax通信を開始する

        $.ajax({

            url: 'http://ec2-13-113-63-24.ap-northeast-1.compute.amazonaws.com:5000/api/timecapsule/event',

            type: 'post', // getかpostを指定(デフォルトは前者)

            //dataType: 'json', // 「json」を指定するとresponseがJSONとしてパースされたオブジェクトになる

            data: { // 送信データを指定(getの場合は自動的にurlの後ろにクエリとして付加される)

                user_id: $('#user_id').val(),

                delivery_date: $('#delivery_date').val(),

                info: $('#info').val(),

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