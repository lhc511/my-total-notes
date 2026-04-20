async function foo () {//默认返回undefined
    console.log("foo function start~")

    console.log("中间代码~")

    console.log("foo function end~")

    // 区别1
    //return的值只决定了res的值，最终还是一个promise对象
    // return '123'
    // return {
    //     then:function (resolve,reject){
    //         resolve('hhhhhhhhh')
    //     }
    // }

    //区别二
    //普通函数代码直接崩溃
    //、异步函数中的异常,会被作为异步函数返回的Promise的reject值的
    throw new Error("error message")
}

//*区别一
//·异步函数的返回值一定是一个Promise
// const promise = foo()
// //此处的res是异步函数最终返回的东西
// //倘若异步函数中返回的是一个实现了then方法的对象(thenable),并且res是then方法中resolve函数的参数
// promise. then(res => {
//     console.log('res:'+res)
//     console.log("promise then function exec")
// })

//区别二，错误抛出区别
//普通函数在抛出异常后会直接崩掉，而异步函数会继续执行后面的代码
//作为reject值被catch捕获
foo().catch(err=>{
    console.log(err)
})
console.log('next=')