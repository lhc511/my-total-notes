// request.js
// function requestData(url, successCallback, failtureCallback) {
//     // 模拟网络请求
//     setTimeout(() => {
//     // 拿到请求的结果
//     //url传入的是coderwhy,请求成功
//         if (url === "coderwhy") {
//             //成功
//             let names = ["abc", "cba", "nba"]
//             successCallback(names)
//         } else {//·否则请求失败
//             //失败
//             let errMessage = "请求失败,url错误"
//             failtureCallback(errMessage)
//         }
//     }, 3000);
// }
// // index.js
// requestData("qaaaa", (res) => {
//     console.log(res)
// }, (err) => {
//     console.log(err)
// })

///////////////////////////////// promise进行重构

function foo() {
    // Promise  此处的箭头函数作为参数传递并且会自动执行
    return new Promise ((resolve,reject)=>{
        // 执行resolve函数回调then方法/或then方法的第二个参数
        resolve('success')//此处的参数会传递给下面then的参数

        //执行reject函数时回调catch方法
        // reject('false')
    })
}
const fooPromise=foo() //相当于是promise对象
// then方法传入的回调函数,会在Promise执行resolve函数时,被回调
//then方法传入的回调函数两个回调函数:
//>第一个回调函数,会在Promise执行resolve函数时,被回调
//>第二个回调函数,会在Promise执行reject函数时,被回调
fooPromise.then((res)=>{
    console.log(res)
},(err) =>{
    console.log(err)
})

//catch方法传入的回调函数,会在Promise执行reject函数时,被回调
// fooPromise.catch(()=>{
// })

///////////////////////////////////////////////////////////////////////////

//-传入的这个函数在其内部会立即执行,被称之为 executor
//->resolve:回调函数,在成功时,回调resolve函数
//>reject:回调函数,在失败时,回调reject函数

// const promise = new Promise( (resolve,reject) => {
//     // console.log("promise传入的函数被执行了")
//     resolve()
// })
//
// promise.then(() => {
//
// })
//
// promise.catch(() => {
//
// })
