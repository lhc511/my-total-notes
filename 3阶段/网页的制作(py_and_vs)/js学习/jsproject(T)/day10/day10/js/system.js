// 使用封装的方式处理每个页面的逻辑
var index = {}
index.nav = {
    html: function (i) {
        var HTML = '<div id="nav">'
        HTML += '<div class="con">'
        HTML += '<div class="log">'
        HTML += '        个人博客'
        HTML += '    </div>'
        HTML += '    <ul>'
        HTML += (i == 1) ? '<li><a href="index.html" class="focus">网站首页</a></li>' : '<li><a href="index.html">网站首页</a></li>'
        HTML += (i == 2) ? '<li><a href="" class="focus">文章列表</a></li>' : '<li><a href="">文章列表</a></li>'
        HTML += (i == 3) ? '<li><a href="" class="focus">我的相册</a></li>' : '<li><a href="">我的相册</a></li>'
        HTML += (i == 4) ? '<li><a href="" class="focus">时间轴</a></li>' : '<li><a href="">时间轴</a></li>'
        HTML += (i == 5) ? '<li><a href="" class="focus">留言</a></a></li>' : '<li><a href="">留言</a></a></li>'
        HTML += (i == 6) ? '<li><a href="" class="focus">关于我</a></li>' : '<li><a href="">关于我</a></li>'
        HTML += (i == 7) ? '<li><a href="" class="focus">发表博客</a></li>' : '<li><a href="">发表博客</a></li>'
        HTML += '    </ul>'
        HTML += '    <div class="act">'
        HTML += '        <a href="">登录</a>'
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