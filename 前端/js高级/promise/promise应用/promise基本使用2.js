function requestData(url, successCallback, failtureCallback) {
    // 对象中的参数在传参时会放到constructor里面，若是寒=函数则是一个立即执行函数
    return new Promise((resolve, reject) => {
        // 模拟网络请求
        setTimeout(() => {
            // 拿到请求的结果
            //url传入的是coderwhy,请求成功
            if (url === "coderwhy") {
                //成功
                let names = ["abc", "cba", "nba"]
                resolve(names)
            } else {//·否则请求失败
                //失败
                let errMessage = "请求失败,url错误"
                reject(errMessage)
            }
        }, 1500);
    })
}

//index.js
const promise = requestData("coderwhy")
//then方法传入的回调函数两个回调函数:
//>第一个回调函数,会在Promise执行resolve函数时,被回调
//>第二个回调函数,会在Promise执行reject函数时,被回调
promise.then((res) => {
    console.log('success',res)
},(err) =>{
    console.log('false',err)
})

// promise.catch(() =>{
//     console.log('false')
// })