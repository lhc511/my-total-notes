async function async1 () {
    console.log('async1 start')//直接执行
    await async2();
    console.log('async1 end')//加到微任务队列
}

async function async2 () {
    console.log('async2')//直接执行
}

console. log('script start')

setTimeout(function () {
    console.log('setTimeout')//宏任务队列中执行
},0)

async1();

new Promise (function (resolve) {
    console.log('promise1')//直接执行
    resolve();
}) . then (function () {
    console.log('promise2')//微任务队列
})


console. log('script end')//直接执行

// script start
// async1 start
// async2
// promise1
// script end
// async1 end
// promise2
// setTimeout