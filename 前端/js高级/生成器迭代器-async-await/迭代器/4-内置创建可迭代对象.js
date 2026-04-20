//创建一些原生的对象时
const names = ["abc", "cba", "nba"]

console. log(names[Symbol.iterator])

const iterator1 = names[Symbol. iterator] ()//通过调用内部的函数返回了一个可迭代对象
//通过该对象调用next方法
// console.log(iterator1.next())
// console.log(iterator1.next())
// console.log(iterator1.next())
// console. log(iterator1.next())
// console.log('*************')

for (const item of names) {
    console.log(item)
}
//Map/Set
const set = new Set()
set.add(10)
set.add(100)
set. add(1000)

for (const item of set) {
    console.log(item)
}
console.log('**********')

//函数中arguments也是一个可迭代对象
function foo(x, y, z) {
    console.log(arguments [Symbol.iterator])
    for (const arg of arguments) {
        console.log(arg)
    }
}

foo(10,20, 30)