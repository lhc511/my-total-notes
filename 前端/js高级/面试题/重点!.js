async function bar () {
    console.log("22222")//此处在执行bar函数时会直接打印
    return new Promise((resolve) => {
        resolve()//执行bar时直接执行promise中的函数，即执行resolve函数
    })
}

async function foo () {
    // 在async异步函数中默认代码会直接执行
    console.log("111111")

    //在await后面的 值/表达式 相当于promise对象中调用了resolve(结果)
    //此处为resolve(bar函数返回结果/即undefined) 也可以是一个值/对象等
    await bar()//直接执行bar中的代码
    // 由于bar函数在上面先执行，即执行了promise对象的resolve函数，
    // 因此在下方执行的代码都会被看作在then方法中执行
    console.log("33333")//即将改行代码放在微任务队列中，会在主线程执行完毕后再次执行
}

foo()//直接执行其中的代码
console. log("444444")//此处是主线程中的代码
// 111111
// 22222
// 444444
// 33333