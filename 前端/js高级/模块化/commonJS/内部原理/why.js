// module. exports = {
//     name: "why",
//     age: 18,
//     foo: function () {
//         console.log("foo函数~")
//     }
// }

//exports方法导出数据
const name ="why"
const age = 18
function sum(num1, num2) {
    return num1 + num2
}
//、第二种导出方式
exports.name = name
exports.age = age
exports.sum = sum