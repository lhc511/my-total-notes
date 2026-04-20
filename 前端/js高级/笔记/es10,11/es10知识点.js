// // flat
// const nums = [10, 20,[2,9], [[30, 40], [10, 45]], 78, [55, 88]]
// const newNums = nums. flat()
// console. log(newNums)//[10, 20, 2, 9,[30, 40], [10, 45], 78, 55, 88]
//
// const newNums2 = nums. flat(2)//[10, 20, 2, 9, 30, 40, 10, 45, 78, 55, 88] 降维两次
// console.log(newNums2)

//flatMap 第二个参数是指定的绑定对象
// 2.flatMap的使用
// const nums2=[10,20,30]
// const newNums3 =nums2. flatMap(item => {//此处若返回的依旧是一个数组那便会自动降维
//     return item * 2
// })
// const newNums4 = nums2.map(item => {
//     return item * 2
// })
// console.log(newNums3) //[20, 40, 60]
// console.log(newNums4)//[20, 40, 60]

//-3.flatMap的应用场景
// const messages = ["Hello World", "hello lyh", "my name is coderwhy"]
// const words = messages.map(item => {
//     return item.split(" ")
// })
//
// console. log(words)//[['Hello', 'World'], ['hello', 'lyh'], ['my', 'name', 'is', 'coderwhy']]
//
// const words1 = messages.flatMap(item => {//自动降维一次
//     return item.split(" ")
// })
// console.log(words1)//['Hello', 'World', 'hello', 'lyh', 'my', 'name', 'is', 'coderwhy']

//将entries转化的数组格式转换为对象
// const obj = {
//     name: "why",
//     age: 18,
//     height: 1.88
// }
// const entries = Object.entries(obj)
// console.log(entries)//[['name', 'why'],['age', 18],['height', 1.88]]
//方法1
// const newObj = {}
// for (const entry of entries) {
//     newObj [entry[0]] = entry[1]
// }
//方法2
//-ES10中新增了Object.fromEntries方法
// const newObj = Object. fromEntries(entries)
// console.log(newObj)//{name: 'why', age: 18, height: 1.88}

//-2.Object.fromEntries的应用场景
// URLSearchParams(queryString)是JavaScript中处理URL查询字符串的核心API，其主要作用是将查询字符串解析为可操作的对象，提供便捷的参数管理功能。
// const queryString ='name=why&age=18&height=1.88'
// const queryParams = new URLSearchParams(queryString)
// console.log(queryParams)
// for (const param of queryParams) {//遍历打印出以下三个数组
//     console.log(param)//['name', 'why']，['age', '18']，['height', '1.88']
// }
//
// const paramObj = Object. fromEntries(queryParams) //转化为对象类型
// console. log(paramObj)//{name: 'why', age: '18', height: '1.88'}

//trimStart和trimEnd
const message = "      Hello World          "

console.log(message.trim())//去除全部空格
console.log(message.trimStart())//去除头部空格
console. log(message. trimEnd ())//去除尾部空格
