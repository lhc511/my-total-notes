
console. log("script start")

// 业务代码
// setTimeout本身和其他函数一样都是同步的，一般说的异步是指的setTimeout中传入的function函数
//比如，此处的function函数会在setTimeout调用后一秒执行，因此为异步函数
setTimeout(function() {
    console.log('aaa')

},1000)
console. log("script end")