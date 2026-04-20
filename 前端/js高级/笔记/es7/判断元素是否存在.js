//对内容是否存在的判断
// const names = ["abc", "cba", "nba", "mba",NaN]
//
// if (names. indexOf("cba") !== -1) {  //!== -1则包含
//     console.log("包含abc元素")
// }
// // ES7 ES2016
// if (names.includes("cba",0)) {//零是指从第0个元素开始判断
//     console.log("包含abc元素")
// }
// if (names. indexOf(NaN) !== -1) {//老方法判断不出来NaN
//     console.log("包含NaN")  //没有输出
// }
// if (names. includes(NaN) ) {//新版本可以判断
//     console.log("包含NaN")
// }

//新增的指数运算符
const result1= Math.pow(3,3)
// ES7: **
const result2 = 3 ** 3
console.log(result1, result2)