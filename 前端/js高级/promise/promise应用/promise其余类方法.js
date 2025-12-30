//reject方法
// const promise = Promise. reject("rejected message")
// // 相当于
// const promise2 = new Promise((resolve, reject) => {
//     reject("rejected message")
// })

//注意:无论传入什么值都是一样的/没有想resolve一样的三种区别，都会将值直接传给下面的失败状态方法
// const promise = Promise.reject(new Promise(()=>{}))
//
// promise.then(res => {
//     console.log("res:", res)
// }) . catch(err => {
//     console.log("err:", err)
// })

// all方法
//创建多个Promise
// const p1 = new Promise((resolve, reject) => {
//     setTimeout(()=>{
//         resolve(11111)
//     },1000)
//
// })
// const p2 = new Promise((resolve, reject) => {
//     setTimeout(()=>{
//         // resolve(222)
//         reject(222)
//     },2000)
// })
// const p3 = new Promise((resolve, reject) => {
//     setTimeout(()=>{
//         resolve(333)
//     },3000)
// })
// //、需求 :· 所有的Promise都变成fulfilled时,再拿到结果
// //·意外:在拿到所有结果之前,有一个promise变成了rejected,那么整个promise是rejected(后续不再执行)
// Promise.all([p2,p1, p3,"aaaa"]).then(res => {
//     console. log(res)//[222, 11111, 333, 'aaaa']
// }).catch(err=>{
//     console.log('err:'+err)//err:222
// })

// allSettled方法
//创建多个Promise
// const p1 = new Promise((resolve, reject) => {
//     setTimeout(()=>{
//         resolve(11111)
//     },1000)
//
// })
// const p2 = new Promise((resolve, reject) => {
//     setTimeout(()=>{
//         // resolve(222)
//         reject(222)
//     },2000)
// })
// const p3 = new Promise((resolve, reject) => {
//     setTimeout(()=>{
//         resolve(333)
//     },3000)
// })
//
// //allSettled；该方法不会经过catch，只会在所有promise对象的状态设置好之后返回每一个对象的状态和值/原因
// Promise.allSettled([p1,p2, p3]).then(res => {
//     console.log(res)
//         // [{ status: 'fulfilled', value: 11111 },
//         // { status: 'rejected', reason: 22222 },
//         // { status: 'fulfilled', value: 33333 }]
// }) .catch(err => {
//     console.log(err)
// })

// race方法
//创建多个Promise
// const p1 = new Promise((resolve, reject) => {
//     setTimeout(()=>{
//         resolve(11111)
//     },1000)
//
// })
// const p2 = new Promise((resolve, reject) => {
//     setTimeout(()=>{
//         // resolve(222)
//         reject(222)
//     },2000)
// })
// const p3 = new Promise((resolve, reject) => {
//     setTimeout(()=>{
//         resolve(333)
//     },3000)
// })
//
// //·race: 竞技/竞赛
// //·只要有一个Promise变成fulfilled状态,那么就结束，将最快执行的值作为返回的结果
// Promise.race([p1, p2, p3]).then(res => {//res: 11111
//     console.log("res:", res)
// }) .catch(err => {
//
// })

// any方法
// 创建多个Promise
const p1 = new Promise((resolve, reject) => {
    setTimeout(()=>{
        // resolve(11111)
        reject(222)
    },1000)

})
const p2 = new Promise((resolve, reject) => {
    setTimeout(()=>{
        // resolve(222)
        reject(222)
    },2000)
})
const p3 = new Promise((resolve, reject) => {
    setTimeout(()=>{
        // resolve(333)
         reject(222)
    },3000)
})

//any方法：会返回一个最快的成功状态(resolve)的值(参数)/至少等一个resolve的结果,若全部失败则返回即抛错err: AggregateError: All promises were rejected即抛错
Promise.any([p1, p2, p3]).then(res => {
    console.log("res:", res)
}).catch(err => {
    console.log("err:", err)//err: AggregateError: All promises were rejected
    console.log("err:", err.errors)//那到错误的内容 [222, 222, 222] 此三个是上面reject中传的参数
})