if (window.location.href.indexOf('/rest/page') == -1) {
    if (window.Storage && window.localStorage && window.localStorage instanceof Storage) {
        Date.prototype.format = function (format) {
            var o = {
                "M+": this.getMonth() + 1, //month
                "d+": this.getDate(), //day
                "h+": this.getHours(), //hour
                "m+": this.getMinutes(), //minute
                "s+": this.getSeconds(), //second
                "q+": Math.floor((this.getMonth() + 3) / 3), //quarter
                "S": this.getMilliseconds() //millisecond
            }

            if (/(y+)/i.test(format)) {
                format = format.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
            }

            for (var k in o) {
                if (new RegExp("(" + k + ")").test(format)) {
                    format = format.replace(RegExp.$1, RegExp.$1.length == 1 ? o[k] : ("00" + o[k]).substr(("" + o[k]).length));
                }
            }
            return format;
        }
        var dstr = new Date().format('yyyy-MM-dd hh:mm:ss')
        var ft = localStorage.getItem('firstTime') || ''
        if (ft.length < 4000) {
            if (!ft) {
                localStorage.setItem('firstTime', '[' + dstr + ']' + window.location.href + ' ')
            } else {
                localStorage.setItem('firstTime', ft + '[' + dstr + ']' + window.location.href + ' ')
            }
        }
    }
}
