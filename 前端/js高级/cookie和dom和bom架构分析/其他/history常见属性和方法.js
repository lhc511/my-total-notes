const jumpBtn =document.querySelector("#jump")

jumpBtn. onclick = function() {
    // location.href = "./demo.html"

    //name:"coderwhy"会被保存在history.state的属性里面
    //此处会跳转路径但是不会刷新网页，在一些组件中会监察路径的变化而加载对应的组件，比如之后学的vue。
    history. pushState ({name:"coderwhy"}, "", "/detail")//会保存之前的网页
    //history. replaceState ({name: "coderwhy"}, "", "/detail")//不会保存之前的网页
}