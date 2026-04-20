// request.js
// function requestData(url,) {
//     //、异步请求的代码会被放入到executor中
//     return new Promise((resolve, reject) => {
//         //、模拟网络请求
//         setTimeout(() => {
//             resolve(url)
//         }, 2000);
//     })
// }

// requestData("coderwhy") .then(res => {
//     console.log('传回数据:'+res)
// })

//·1.第一种方案 :· 多次回调/不推荐
//·回调地狱
// requestData("why").then(res => {
//     requestData(res + "aaa").then(res => {
//         requestData(res + "bbb").then(res => {
//             console.log(res)
//         })
//     })
// })


//·2.第二种方案 :· Promise中then的返回值来解决
// requestData("why") . then(res => {
//     console.log(res)
//     return requestData(res + "aaa")
//
// }).then (res => {//此处的res会将上一个then中箭头函数的返回值作为参数传递进来
//     console.log(res)
//     return requestData(res + "bbb")
// }).then (res => {
//     console.log(res)
// })


function requestData(url,) {
    //、异步请求的代码会被放入到executor中
    return new Promise((resolve, reject) => {
        //、模拟网络请求
        setTimeout(() => {
            resolve(url)
        }, 2000);
    })
}

// function* getDepartment() {
//     const user = yield requestData("id")
//     const department = yield requestData(user.departmentId)
// }

////////////////////////////////////////////////////////////////////////////////////////////////
//·3.第三种方案 :· Promise+generator实现
// function* getData() {
//     // requestData函数最终返回一个promise对象，
//     // yield后面的代码会作为next函数调用后最终返回对象中value属性的值，因此value对应一个promise对象
//     const res1 = yield requestData("why")//res1=why
//     const res2 = yield requestData(res1 +"bbb")
//     const res3 = yield requestData(res2 +"ccc")
//     console.log(res3)
// }
//
//
// //手动执行生成器函数
// // const generator = getData()
// // // console.log(generator.next()) //value中存储的是requestData()返回是promise对象
// //
// // //此处的res是上面函数中resolve传来的参数，
// // generator.next().value. then(res => {
// //     //此处next函数中传递的参数会作为上一段next函数执行代码yield的返回值
// //     generator.next(res).value.then(res => {
// //         generator.next(res).value.then(res => {
// //             generator.next(res)
// //         })
// //     })
// // })
//
//工具函数
// function execGenerator (genFn) {
//     const generator = genFn()//此处只会返回一个生成器对象，不会执行生成器内部的代码
//     console.log(generator)
//     //在该函数中逐步执行生成器中的函数
//     function exec(res) {
//         //此处跳到生成器中的函数执行段
//         const result = generator.next(res)//返回一个符合迭代器协议的对象
//         //首次执行时是undefined，之后为requestData的参数(函数参数传递给resolve函数)
//         console.log(res)
//
//         if (result.done) {
//             return result.value
//         }
//         result.value.then(res => {
//             exec(res)//此处递归执行函数直到执行完毕
//         })
//     }
//     exec()
// }
//
// execGenerator(getData)
// // execGenerator(getDepartment)
//
// //·3>·第三方包co自动执行(需要安装)
// const co =require('co')
// co(getData)
//////////////////////////////////////////////////////////////////////////////

//·4.第四种方案:async/await
// function* getData() {
//     // requestData函数最终返回一个promise对象，
//     // yield后面的代码会作为next函数调用后最终返回对象中value属性的值，因此value对应一个promise对象
//     const res1 = yield requestData("why")//res1=why
//     const res2 = yield requestData(res1 +"bbb")
//     const res3 = yield requestData(res2 +"ccc")
//     console.log(res3)
// }
//上面为第三种，
//第三种方案需要工具函数，而第四种方案不需要，，是一种语法糖
async function getData() {
    const res1 = await requestData("why")
    const res2 = await requestData(res1 + "aaa")
    const res3 = await requestData(res2 + "bbb")
    const res4 = await requestData(res3 + "ccc")
    console.log(res4)
}

getData()