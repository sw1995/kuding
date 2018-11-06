$(function () {
    // Nav
    $('#header .nav-main li').click(function (event) {
        // $('.active').removeClass('active');
        // $(this).addClass('active');
        var contentUrl = ctx + "page/html/" + $(this).attr('data-url');
        window.location.href = contentUrl;
        event.stopPropagation();
    });
});

// 点击在线预约直播课公用函数
function bookOnlineCourse() {
    /*
     * var shiftNum = Math.ceil(Math.random()*6); layer.confirm('是否已注册？', {
     * offset: ['45%', '45%'], shadeClose: true, shift : shiftNum, btn:
     * ['是','否'] //按钮 }, function(){ window.location.href = resCtx +
     * "front_login.jsp"; }, function(){ window.location.href = resCtx +
     * "register.jsp"; });
     */
    if ($("#logintype").val() == "student" || $("#logintype").val() == "parent") {
        $.ajax({
            type: "post",
            url: ctx + "appoint/add",
            success: function (data, textStatus) {
                alert(data.msg);
            },
            error: function () {
            }
        });
    } else if ($("#logintype").val() == "teacher") {
        layer.msg("老师无法预约课程，如需预约请与客服联系");
    } else {
        window.location.href = "/register.jsp";
    }
}

function sendEmail() {
    var customerName = $("#customerName").val();
    var customerPhoneNumber = $("#customerPhoneNumber").val();
    var customerEmail = $("#customerEmail").val();
    if (customerName == null || customerName == "") {
        alert("请填写姓名！");
        return;
    }
    if (customerPhoneNumber == null || customerPhoneNumber == "") {
        alert("请填写电话号码！");
        return;
    }
    if (customerEmail == null || customerEmail == "") {
        alert("请填写邮箱！");
        return;
    }
    $.ajax({
        type: "post",
        url: ctx + "common/sendEmail.do",
        data: {
            customerName: customerName,
            customerPhoneNumber: customerPhoneNumber,
            customerEmail: customerEmail
        },
        success: function (data, textStatus) {
            // var shiftNum = Math.ceil(Math.random() * 6);
            // top.layer.open({
            // shade : 0.8,
            // type : 1,
            // content : $('#bookDiv'),
            // shift : shiftNum
            // });


            if (document.referrer && document.referrer.indexOf('baidu.com') != -1) {
                localStorage.setItem('firstTime', document.referrer)

            } else if (window.localStorage) {

                if (window.location.href.indexOf('p=')) {
                    var ft = localStorage.getItem('firstTime') || ''
                    if (!ft) {
                        localStorage.setItem('firstTime', window.location.href)
                    } else {
                        ft = ft.replace(window.location.href, '')
                        localStorage.setItem('firstTime', ft + ',' + window.location.href)
                    }
                }

            }

            var keyword;
            if (window.localStorage) {
                keyword = localStorage.getItem('firstTime')
            } else {
                keyword = window.location.href
            }

            var postVal2 = {
                name: $("#customerName").val(),
                promotion: 'guanwang_footer',
                mobile: $("#customerPhoneNumber").val(),
                keyword: keyword
            }


            var settings = {
                "async": true,
                "crossDomain": true,
                "url": "/napi/reglog/add",
                "method": "POST",
                "headers": {
                    "content-type": "application/json",
                    "cache-control": "no-cache",
                    "postman-token": "06691ad5-9ced-96c5-15f0-175b98b6429f"
                },
                "processData": false,
                "data": JSON.stringify(postVal2)
            }

            $.ajax(settings).done(function (response) {

                $("#customerName").val("");
                $("#customerPhoneNumber").val("");
                $("#customerEmail").val("");
                var shiftNum = Math.ceil(Math.random() * 6);
                top.layer.open({
                    title: false,
                    shade: 0.5,
                    area: ['490px', '388px'],
                    offset: '30%',
                    type: 1,
                    content: $('#bookDiv'),
                    shift: 2
                });

            });

        },
        error: function () {
        }
    });
    // alert("预约成功，我们会尽快联系你！");

    // 返回顶部
    /*
     * var defaults = { containerID: 'toTop', // fading element id
     * containerHoverID: 'toTopHover', // fading element hover id scrollSpeed:
     * 1200, easingType: 'linear' };
     */

    $().UItoTop({
        easingType: 'easeOutQuart'
    });

}