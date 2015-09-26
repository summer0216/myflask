/**
 * Created by lewis on 15-9-26.
 */
define(['domReady!','bootstrap','text!./update_pro.html'], function (domReady,bootstrap,update_pro) {
    $('body').append(update_pro);
    $("#submit_edit_project").click(function () {
        var formdata = new FormData(document.forms.namedItem("project_edit"));
        $.ajax({
            type: "POST",
            url: "/update/project/",
            data: formdata,
            cache: false,
            contentType: false,    //告诉jQuery不要去设置Content-Type请求头
            processData: false,    //告诉jQuery不要去处理发送的数据
            success: function (data) {
                $("#update_pro").modal("hide");
                alert(data.message);
            },
            error: function (xhr) {
                alert("Search Fail:" + xhr.statusText + xhr.status);
            }
        });
    });
    return{
        run: function (pro_no,pro_name,pro_description) {
            $("#pro_no").val(pro_no);
            $("#pro_name").val(pro_name);
            $("#pro_description").val(pro_description);
            $("#update_pro").modal();
        }
    }
});