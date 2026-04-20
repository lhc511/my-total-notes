

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
//此处在调用时会this进行隐式绑定，即iterator返回的那个对象，但若是箭头函数则会绑定上一层
// iterator.next()
// console.log(iterableObj[Symbol.iterator])
// const iterator=iterableObj[Symbol.iterator]()
// console.log(iterator.next())
// console.log(iterator.next())
// console.log(iterator.next())
// console.log(iterator.next())
//
// const iterator1=iterableObj[Symbol.iterator]()
// console.log(iterator1.next())
// console.log(iterator1.next())
// console.log(iterator1.next())
// console.log(iterator1.next())

//·3.for ... of可以遍历的东西必须是一个可迭代对象
//for ... of本质就是利用迭代器中的next去取值和判断是否符合要求,并调用next

// const obj = {
//     name: "why",
//     age: 18
// }

// for (const item of obj) {//obj is not iterable  报错
for (const item of iterableObj) {
    //会拿到迭代器中数组的每一个元素内容
    console.log(item) //相当于只拿到了迭代器最终返回的对象中的value属性
}