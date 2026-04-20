// console.log('‘aaa')
// setTimeout(()=>{
//     console.log('1')
// },1000)
// setTimeout(()=>{
//     console.log('2')
// },2000)
//
// setTimeout(()=>{
//     console.log('3')
// },3000)
// console.log('aaasd')

var x = 0
//题目
function foo(x,y =function(){x=3;console.log(x)}) {
    console.log(x)
    var x = 2
    y()
    console.log(x)
}
foo()
console. log(x)

function throttle(fn, interval,options={leading:true,trailing:false},resultCallback) {
    // leading为true则默认第一次触发，反之相反
    const {leading, trailing} = options
    let lastTime = 0
    let timer = null

    const _throttle = function (...args) {
        const nowTime = new Date().getTime()
        if (lastTime === 0 && leading === false) lastTime = nowTime

        const remainTime = interval - (nowTime - lastTime)
        if (remainTime <= 0) {
            if (timer) {
                clearTimeout(timer)
                timer = null
            }
            fn.apply(this, args)
            lastTime = nowTime
            return
        }
        if (trailing && !timer) {
            timer = setTimeout(() => {
                timer = null
                lastTime = !leading ? 0 : new Date().getTime()
                const result=fn.apply(this, args)
            }, remainTime)
        }
    }
    return _throttle
}