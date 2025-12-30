//await后加表达式
// function requestData() {
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             resolve(222)
//         }, 2000);
//     })
// }
//
// async function foo () {
//     //该结果为函数执行中返回的promise对象中resolve的参数
//     const res = await requestData()
//     // 在等待结束之后执行后面的代码，相当于是在返回的promise对象回调then方法执行
//     //因为在resolve执行后会回调then，而requestData紧跟的并没有写then，但是之后的带代码又要继续执行因此，相当于在then中执行
//     console.log(res)
//
//     const res2 = await requestData()
//     console.log("res2后面的代码",res2)
// }

// await后加其他值 1.普通值 2.thenable对象 3.promise对象
// async function foo () {
//
//     // const res1 = await 123   //res1就是await后跟的值
//     // const res1 = await {
//     //     then: function (resolve, reject) {
//     //         resolve("abc")
//     //     }
//     // }             //res1为resolve中的参数
//     const res1 = await new Promise((resolve) => {
//         resolve("why")
//     })   //resolve中的参数
//     console.log("res1:", res1)
// }


//·3.reject值
function requestData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            reject(111)
        }, 2000);
    })
}


async function foo() {
    //若此函数中的promise状态为reject，那么会将该状态作为整个异步函数promise的状态
    const res1 = await requestData()
    console.log("res1:", res1)
}

//在reject时需要在此处对reject进行捕捉
foo().catch(err=>{
    console.log(err)
})

//对于有async标志的函数最终的返回值一定是一个promise对象
async function foo1(){}
console.log(foo1())//Promise {<fulfilled>: undefined}

