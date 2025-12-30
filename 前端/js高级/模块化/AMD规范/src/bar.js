//在bar中使用foo模块
define(["foo"], function(foo) {//获得foo中返回的对象的另一种写法

    console.log('--------')
    console.log("bar:", foo)
})

//写法1
// define(function() {
//     // 获取foo模块中返回的对象
//     require(["foo"], function(foo){
//     console.log("bar1:", foo)
//     })
// })