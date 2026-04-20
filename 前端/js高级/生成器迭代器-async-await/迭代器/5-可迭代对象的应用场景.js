const iterableObj={
    names:["abc", "cba", "nba"],
    [Symbol.iterator]:function (){
        let index=0
        return {
            next: ()=> {
                if (index < this.names.length) {
                    return {done: false, value: this.names[index++]}
                } else {
                    return {done: true, value: undefined}
                }
            }
        }
    }
}

const names = ["abc", "cba", "nba"]
//iterableObj本身就是一个可迭代对象，使用迭代器展开
const newNames =[ ... names, ... iterableObj]
console. log(newNames)

const obj = { name: "why", age: 18 }
// for (const item of obj) {}    //obj作为一个普通对象是不可被for of遍历的

//此处的obj对象用的并不是迭代器方法展开，而是其他方法,ES9(ES2018)中新增的一个特性:特殊处理
const newObj = { ... obj }
console.log(newObj)

// 3.解构语法
const [ name1, name2 ] = names
// const{name, age} ·= obj 不是迭代器，ES9新增的特性，特殊处理

// 4.创建一些其他对象时，
const set1 = new Set(iterableObj)//set内部要传可迭代对象
//通过迭代器获取可迭代对象中的元素并传给定义的变量
console.log(set1)//Set(3) {'abc', 'cba', 'nba'}
// const set2 = new Set(123)//不能传不可迭代对象

// 5.Promise.all
Promise.all(iterableObj).then(res => {
    console. log(res)
})