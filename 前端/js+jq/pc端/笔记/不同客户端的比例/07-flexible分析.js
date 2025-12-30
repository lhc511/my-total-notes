(function flexible(window, document) {
    // 获取的html 的根元素
    var docEl = document.documentElement
        // dpr 物理像素比，如果浏览器有该属性则返回属性，没有则返回1  ，在不同的客户端(电脑，手机，各个品牌手机)有不同的
    var dpr = window.devicePixelRatio || 1

    // adjust body font size  设置我们body 的字体大小
    function setBodyFontSize() {
        // 如果页面中有body 这个元素 就设置body的字体大小  根据像素比设置body内的字体大小
        if (document.body) {
            document.body.style.fontSize = (12 * dpr) + 'px'
        } else {
            // 如果页面中没有body 这个元素，则等着 我们页面主要的DOM元素加载完毕再去设置body
            // 的字体大小
            document.addEventListener('DOMContentLoaded', setBodyFontSize)
        }
    }
    setBodyFontSize();

    // set 1rem = viewWidth / 10    设置我们html 元素的文字大小
    function setRemUnit() {
        //docEl为上面得到的html根元素  此处指将浏览器页面分成十等分,横分
        // 代码将根元素字体设为当前视口宽度 (clientWidth) 的 1/10
        // 例如：屏幕宽度 375px → font-size=37.5px → 1rem=37.5px
        var rem = docEl.clientWidth / 10
        docEl.style.fontSize = rem + 'px'
    }

    setRemUnit()

    // reset rem unit on page resize  当我们页面尺寸大小发生变化的时候，要重新设置下rem 的大小
    window.addEventListener('resize', setRemUnit)
    // pageshow 是我们重新加载页面触发的事件
    // 刷新页面会触发load事件，但是火狐浏览器会及那个前一个页面缓存到内存，于是无法触发，所以用pageshow事件
    //pageshow是在页面显示的时候触发,无论是否刷新
    window.addEventListener('pageshow', function(e) {
        // e.persisted 返回的是true 就是说如果这个页面是从缓存取过来的页面(比如火狐)，也需要从新计算一下rem 的大小
        if (e.persisted) {
            setRemUnit()
        }
    })

    // detect 0.5px supports  有些移动端的浏览器不支持0.5像素的写法
    //以下是一个解决方案，让这些移动端支持0.5像素写法(了解干什么就好不用弄太清楚)
    if (dpr >= 2) {
        var fakeBody = document.createElement('body')
        var testElement = document.createElement('div')
        testElement.style.border = '.5px solid transparent'
        fakeBody.appendChild(testElement)
        docEl.appendChild(fakeBody)
        if (testElement.offsetHeight === 1) {
            docEl.classList.add('hairlines')
        }
        docEl.removeChild(fakeBody)
    }
}(window, document))