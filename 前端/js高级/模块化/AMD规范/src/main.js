//此处的require是调用的require.js的库
require.config({//这个是在浏览器上运行的，在node控制台上无法使用
    paths: {//将要关联的文件进行注册
        foo: "foo", //此处是相对于index.html进行查找
        bar: "bar"
    }
})


//["foo"]通过require加载某一个具体的模块，拿到该模块后会执行一个回调函数
//并且会把加载模块中返回导出的值放到回调函数的参数中
// bar中的返回值是undefined，但是在加载代码块的时候会先执行一遍,所以bar在前面
require(["foo","bar"], function(foo) {
    console.log("main:", foo)
})

//输出
// --------
// bar: {name: 'why', age: 18, sum: ƒ}
// main: {name: 'why', age: 18, sum: ƒ