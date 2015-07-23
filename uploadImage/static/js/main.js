/**
 * Created by Administrator on 2015/7/23.
 */
/**
 * Created by Administrator on 2015/7/22.
 */
require.config({
    baseUrl: "/static/js",
    paths: {
        jquery: 'jquery-1.7.2.min',
        jform: 'jquery.form'
    },
    shim: {
        jform: ['jquery']
    }
});
require(['jform'], function () {
    $(function () {
        console.log('all loaded!');
        var options = {
            success: function (data) {
                alert("上传成功");
                $("#imgDiv").empty();
                $("#imgDiv").html(data);
                $("#imgDiv").show();
            }
        };
        $("#upload_form").ajaxForm(options);
    });
});