//此处定义的也是全局变量，在同一个html文件中和其他js一起引用时可能会引起命名冲突
// var name = "why"
// var isFlag = false

//解决方法 变成一个自执行函数，因为函数有局部作用域，所以在函数内部就能够避免冲突
(function () {
    var name = "why"
    var isFlag = false
})()