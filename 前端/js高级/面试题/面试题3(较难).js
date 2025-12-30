//return一个普通值
//两个resolve在主线程中优先执行
// Promise.resolve().then(() => {//加入微队列
//     console.log(0);
//     // return Promise.resolve(4)
//     return 4 //作resolve的参数传给下面的then
//
// //打印0的微队列第一个执行，在第一个微队列任务执行后该then才会执行，因此此处的then作为第三个微队列
// }) . then ((res) => {
//     console.log(res)
// })
//
// Promise.resolve().then(() => {//加入微队列
//     //此处resolve执行后会将.后的then放入微队列，作为微队列中第二位
//     console.log(1);
// }) . then ( () => {
//     console.log(2);
// }) . then (() => {
//     console.log(3);
// }) . then (() => {
//     console.log(5);
// }) . then (() => {
//     console.log(6);
// })

// 打印顺序，0 1 4 2 3 5 6

//return一个thenable对象，
// Promise.resolve().then(() => {
//     console.log(0);
//
//     return {//对于一个thenable对象会将此处的then执行的函数推到下一次微任务中
//         then: function (resolve) {
//             resolve(4)
//         }
//     }
//
// }) . then ((res) => {
//     console.log(res)
// })
//
// Promise.resolve().then(() => {
//     console.log(1);
// }) . then ( () => {
//     console.log(2);
// }) . then (() => {
//     console.log(3);
// }) . then (() => {
//     console.log(5);
// }) . then (() => {
//     console.log(6);
// })

//打印结果:0 1 2 4 3 5 6

//推迟的原因：当返回的不是一个普通值时其内部可以能有耗时/复杂的代码，为了不影响
// 后续执行，所以会进行适当推迟防止阻塞，实际开发不会有那么多then不停调用，在执行完推迟后的基本上就没有了


//return一个promise对象
//、不是普通的值,多加一次微任务，此处因为是promise对象，所以推后一次
//、Promise.resolve(4),多加一次微任务   调用了一次resolve，再推后一次
//·一共多加两次微任务
Promise.resolve() .then(() => {
    console.log(0);
    return Promise.resolve(4)

}) . then ((res) => {
    console.log(res)
})

Promise.resolve().then(() => {
    console.log(1);
}) . then ( () => {
    console.log(2);
}) . then (() => {
    console.log(3);
}) . then (() => {
    console.log(5);
}) . then (() => {
    console.log(6);
})
// 0
// 1
// 2
// 3
// 4
// 5
// 6