console.log("main.js代码开始运行")
//在加载foo模块时foo中的代码会被执行一次
require("./foo")
//即便多次加载也只会运行一次
require("./foo")
require("./foo")

console.log("main.js代码后续运行")