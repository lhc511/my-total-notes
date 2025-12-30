//·1.常见的属性
// console. log(window. screenX)
// console. log(window. screenY)
//
// window. addEventListener("scroll", () => {
//     console.log(window.scrollX, window.scrollY)
// })

// console.log(window.outerHeight)//整个浏览器的高度
// console.log(window. innerHeight)//窗口页面中内容显示的高度
//
// //·2.常见的方法
// const scrollBtn = document.querySelector("#scroll")
//
// scrollBtn.onclick = function() {
//     window.scrollTo({top: 2000})
// }

//.2.close
//window. close()   //关掉当前窗口

//.3.open  打开新页面  _self：在当前页面打开新页面(覆盖当前页面)
// window. open("https://www.baidu.com","_self")

//·3.常见的事件
// window. onload = function() {
//     console.log("window窗口加载完毕~")
// }
//
// window.onfocus = function() {
//     console.log("window窗口获取焦点~")
// }
//
// window.onblur = function() {
//     console.log("window窗口失去焦点~")
// }

const hashChangeBtn = document. querySelector("#hashchange")
window. onhashchange = function() {
    console.log("hash发生了改变")
}

hashChangeBtn.onclick = function() {
    location.hash = "aaaa"
}