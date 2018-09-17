//自定义js文件

//help页通知区域条目的点击事件
function c_h(t) {
    t.siblings('.li_c').toggleClass("hidden");
    if (t.children(".ico").children().attr("class") === "fa fa-lg fa-hand-o-right") {
        t.children(".ico").children().attr("class", "fa fa-lg fa-hand-o-down");
    }
    else {
        t.children(".ico").children().attr("class", "fa fa-lg fa-hand-o-right");
    }
    t.parent().siblings().children('.li_c').addClass("hidden");
    t.parent().siblings().children('.main').children(".ico").children().attr("class", "fa fa-lg fa-hand-o-right");
}


//notice页通知区域条目的点击事件
function c_n(t) {
    t.siblings('.msg').children().first().toggleClass("hidden");
    if (t.children(".ico").children().attr("class") === "fa fa-lg fa-hand-o-right") {
        t.children(".ico").children().attr("class", "fa fa-lg fa-hand-o-down");
    }
    else {
        t.children(".ico").children().attr("class", "fa fa-lg fa-hand-o-right");
    }
    t.parent().siblings().children('.li_c').addClass("hidden");
    t.parent().siblings().children('.main').children(".ico").children().attr("class", "fa fa-lg fa-hand-o-right");
}