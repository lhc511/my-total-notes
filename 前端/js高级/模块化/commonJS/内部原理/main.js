const why = require("./why.js")
//第一种方式
// console. log (why)

//源码
module. exports = {
    name: name
}
exports = module. exports

//第二种方式
console. log(why.name)
console. log(why.age)
console.log(why.sum(20,30))

//·这种代码不会进行导出
//exports .= {
// name,
//age,
//sum
// }

//此处也无法导出，因为在原来的module.exports添加了数据后又指向了一个新的空对象
//基本不使用
// exports.name = name
// exports. age = age
// exports. sum = sum

//只用下面方法
module.exports={}

//、最终能导出的一定是module,exports