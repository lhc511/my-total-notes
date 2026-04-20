///////////////以下为回调函数//////////////////

setTimeout (()=> {
    console.log("setTimeout")
},1000)

queueMicrotask(() => {
    console.log("queueMicrotask")
})

Promise.resolve() .then(() => {
    console.log("Promise then")
})

//浏览器中维护的队列有两个，一个宏任务队列，一个微任务队列
//规范:在执行任何的宏任务之前,都需要先保证微任务队列已经被清空。即有微任务优先执行微任务，执行完微任务后才会执行宏任务
// 宏任务队列macrotask queue：callback 定时器-ajax-DOM-UI Rendering
// 微任务队列microtask queue：queueMicrotask Promise then

//////////////////////以下为普通函数在调用时直接执行
function foo() {
    console.log("foo")
}

function bar () {
    console.log("bar")
    foo()
}

bar()
console.log("其他代码")

// promise1
// 2
// then1
// queueMicrotask1
// then3
// setTimeout1
// then2
// then4
// setTimeout2