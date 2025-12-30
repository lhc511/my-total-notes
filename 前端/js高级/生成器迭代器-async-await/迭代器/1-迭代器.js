// 编写的一个迭代器
// const iterator = {
//     next: function () {
//         return {done: true, value: 123}
//     }
// }


//、数组
const names = ["abc", "cba", "nba"]

// 创建一个迭代器对象来访问数组  能找到元素done为false，找不到为true
let index=0
const namesIterator = {
    next: function () {
        // return {done: false, value: "abc"}
        // return {done: false, value: "cba"}
        // return {done: false, value: "nba"}
        // return {done: true, value: undefined}
        if(index<names.length){
            return {done:false,value:names[index++]}
        }else {
            return {done:true,value:undefined}
        }
    }
}
//通过属性找到函数存储地址，然后通过 () 调用
console.log(namesIterator.next())
console.log(namesIterator.next())
console.log(namesIterator.next())
console. log(namesIterator.next())
console.log(namesIterator.next())
