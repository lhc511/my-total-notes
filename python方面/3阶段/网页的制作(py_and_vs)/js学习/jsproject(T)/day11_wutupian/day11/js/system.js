// 使用封装的方式处理每个页面的逻辑
var index = {}
index.nav = {
    html: function (i) {
        var newul = "<ul id='sub_nav'>"
        newul += "<li><a href=''>Python</a></li>"
        newul += "<li><a href=''>Python Web</a></li>"
        newul += "<li><a href=''>爬虫</a></li>"
        newul += "<li><a href=''>人工智能</a></li>"
        newul += "<li><a href=''>JS实例索引</a></li>"
        newul += "</ul>"
        var HTML = '<div id="nav">'
        HTML += '<div class="con">'
        HTML += '<div class="log">'
        HTML += '        个人博客'
        HTML += '    </div>'
        HTML += '    <ul>'
        HTML += (i == 1) ? '<li><a href="index.html" class="focus">网站首页</a></li>' : '<li><a href="index.html">网站首页</a></li>'
        HTML += (i == 2) ? '<li><a href="list.html" class="focus">文章列表</a>' + newul + '</li>' : '<li><a href="list.html">文章列表</a></li>'
        HTML += (i == 3) ? '<li><a href="pics.html" class="focus">我的相册</a></li>' : '<li><a href="pics.html">我的相册</a></li>'
        HTML += (i == 4) ? '<li><a href="" class="focus">时间轴</a></li>' : '<li><a href="">时间轴</a></li>'
        HTML += (i == 5) ? '<li><a href="" class="focus">留言</a></a></li>' : '<li><a href="">留言</a></a></li>'
        HTML += (i == 6) ? '<li><a href="" class="focus">关于我</a></li>' : '<li><a href="">关于我</a></li>'
        HTML += (i == 7) ? '<li><a href="send.html" class="focus">发表博客</a></li>' : '<li><a href="send.html">发表博客</a></li>'
        HTML += '    </ul>'
        HTML += '    <div class="act">'
        HTML += '        <a href="login.html">登录</a>'
        HTML += '        <a href="">注册</a>'
        HTML += '    </div>'
        HTML += '</div>'
        HTML += '</div>'
        return HTML;
    }
}
index.box = {
    html: function (url, title, p) {
        var HTML = '<div class="box">'
        HTML += '<div class="title">' + title + '</div>'
        HTML += '<img src="' + url + '" width="365" height="216" alt="">'
        HTML += '<p>' + p + '</p>'
        HTML += '</div>';
        return HTML;
    }
}
index.list = {
    html: function (title, tip) {
        var HTML = '<div class="title">'
        HTML += '<div class="ltip">'
        HTML += title
        HTML += '</div>'
        HTML += '<div class="rtip">'
        HTML += tip
        HTML += '</div>'
        HTML += '</div>'
        return HTML;
    },
    conn: function (title, imgurl, p1, num) {
        var HTML = '<div class="ccon" data-scroll-reveal="bottom 10px 3 3">'
        HTML += '<div class="cctip">' + title + '</div>'
        HTML += '<div class="ccframe">'
        HTML += '<figure>'
        HTML += '<img width="300" src="' + imgurl + '" alt="">'
        HTML += '</figure>'
        HTML += '<div class="ccright">'
        HTML += '<p>' + p1 + '</p>'
        HTML += '<div class="info">' + num + '已阅读</div>'
        HTML += '</div>'
        HTML += '</div>'
        HTML += '</div>'
        return HTML;
    },
    imgs: function (imgurl) {
        var HTML = '<figure data-scroll-reveal="bottom 10px 3 3">'
        HTML += '<img width="300" src="' + imgurl + '" alt="">'
        HTML += '</figure>'
        return HTML;
    }
}
index.send = {
    random: function (l) {
        var _n = "";
        for (var i = 0; i < l; i++) {
            _n += Math.floor(Math.random() * 10)
        }
        return _n;
    }
}
index.pics = {
    html: function (imgurl, p1) {
        var HTML = '<div class="item">'
        HTML += '<figure>'
        HTML += '<img width="270" src="' + imgurl + '" alt="">'
        HTML += '</figure>'
        HTML += '<p>' + p1 + '</p>'
        HTML += '</div>';
        return HTML;
    }

}