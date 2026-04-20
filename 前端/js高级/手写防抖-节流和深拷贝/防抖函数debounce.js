//方案1
// function debounce(fn,delay){//该函数由inputEl.oninput进行监听
//     let timer=null
//     return function (...args) {//inputEl.oninput实际执行的函数，其中的参数就是坚挺的事件对象
//         if(timer) {
//             clearTimeout(timer)
//         }
//
//         timer=setTimeout(()=>{
//             fn.apply(this,args)//第二个参数是一个数组，里面的参数会作为执行函数(此处为fn)的参数
//         },delay)
//     }
//
// }

//方案二
//immediate：true表示立即执行一次，false表示默认(与上面一样)
//此处debounce函数只在绑定的时候调用一次，之后执行的都是返回的函数，因此timer和isInvoke都只定义一次，之后只存在于闭包当中
//并在闭包当中随着执行函数中代码的操作而改变
// function debounce(fn,delay,immediate=false,resultCallback) {
//     let timer = null
//     let isInvoke = false
//
//     const _debounce = function (...args) {
//         if (timer) {
//             clearTimeout(timer)
//         }
//
//         if (immediate && !isInvoke) {
//             const result=fn.apply(this, args)
//             if (resultCallback) resultCallback(result)
//             isInvoke = true
//         } else {
//             timer = setTimeout(() => {
//                 const result=fn.apply(this, args)
//                 if (resultCallback) resultCallback(result)//如果有，则执行传入的函数
//                 isInvoke = false
//             }, delay)
//         }
//     }
//
//     //、封装取消功能
//     _debounce.cancel = function () {
//         if (timer) clearTimeout(timer)
//         timer = null
//         isInvoke = false
//     }
//     return _debounce
// }

//promise返回目标函数的返回值
function debounce(fn,delay,immediate=false,resultCallback) {
    let timer = null
    let isInvoke = false

    const _debounce = function (...args) {
        return new Promise((resolve,reject)=> {
            if (timer) {
                clearTimeout(timer)
            }

            if (immediate && !isInvoke) {
                const result = fn.apply(this, args)
                if (resultCallback) resultCallback(result)
                resolve(result)
                isInvoke = true
            } else {
                timer = setTimeout(() => {
                    const result = fn.apply(this, args)
                    if (resultCallback) resultCallback(result)
                    resolve(result)
                    isInvoke = false
                }, delay)
            }
        })
    }

    //、封装取消功能
    _debounce.cancel = function () {
        if (timer) clearTimeout(timer)
        timer = null
        isInvoke = false
    }
    return _debounce
}
