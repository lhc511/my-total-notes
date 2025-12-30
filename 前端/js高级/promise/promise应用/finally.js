const promise = new Promise((resolve, reject) => {
// resolve("resolve message")
    reject("reject message")
})
//finally没有参数，并在最后一定会被执行
promise.then(res => {
    console.log("res:", res)
}) . catch(err => {
    console.log("err:", err)
}) . finally(() => {
    console.log("finally code execute")
})