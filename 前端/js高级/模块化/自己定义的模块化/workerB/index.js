// 此处var定义的是全局变量 ，在b.js文件中依旧可以使用变量
// var name = "why"
// var age = 18
// var isFlag = true

var moduleB=(function (){
    var name = "why"
    var age = 18
    var isFlag = true

    //将要暴露的变量返回出去
    return {
        name:name,
        isFlag:isFlag
    }
})()