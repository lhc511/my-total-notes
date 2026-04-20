// 转成Promise对象
function foo() {
    const obj = {name: "why"}
    return new Promise((resolve) => {
        resolve(obj)
    })
}

foo().then(res => {
    console.log("res:", res)
})



// Promise.resolve() 接收一个值作为参数，如果该值本身就是 Promise 对象，则直接返回；
// 如果非 Promise 对象（如普通对象、数值或字符串），它会将其包装成一个已解决的 Promise 对象，结果值即为原始值。
// value：可以是任何 JavaScript 值，包括对象、数组、函数或原始类型（如字符串或数字）。
// 类方法Promise,resolve
const promise = Promise.resolve ({ name: "why" })
//·相当于
// const promise2 = new Promise((resolve, reject) => {
//      resolve ({ name: "why" })
// })


// 状态变更：调用 resolve(value) 将 Promise 从 pending 状态转变为 fulfilled（已完成）。
// 值存储：value 被存储在 Promise 的内部属性 [[PromiseResult]] 中，成为该 Promise 的永久解决值
// [[PromiseResult]] 是 Promise 的内部私有属性，用于存储 Promise 的最终结果值（成功解决值或失败原因）。它是 Promise 机制的核心组成部分

promise.then(res => {
    console.log("res:", res)
})