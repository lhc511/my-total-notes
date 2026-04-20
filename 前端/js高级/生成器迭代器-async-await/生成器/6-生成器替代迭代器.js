//、迭代器
// function createArrayIterator(arr) {
//     let index = 0
//     return {
//         next: function () {
//             if (index < arr.length) {
//                 return {done: false, value: arr[index++]}
//             } else {
//                 return {done: true, value: undefined}
//             }
//         }
//     }
// }
//
// const names =["abc", "cba", "nba"]
// const namesIterator = createArrayIterator(names)
//
// console.log(namesIterator.next())
// console.log(namesIterator.next())
// console.log(namesIterator.next())
// console. log(namesIterator.next())

//生成器替代迭代器
// function* createArrayIterator(arr) {
//     //第1种写法
//     // for (const item of arr){
//     //     yield item
//     // }
//
//     //第二种写法
//     // let index = 0
//     // yield arr[index++] //{done: false, value: "abc".}
//     // yield arr [index++] //{done: false, value: "abc"}
//     // yield arr [index++] // { done: false, value: "abc"}
//
//     // 第三种 yield* 可迭代对象
//     yield* arr //调用next时自动遍历传入的数组/可迭代对象，每一个next返回一个对象(符合迭代器协议)
// }
//
// const names =["abc", "cba", "nba"]
// const namesIterator = createArrayIterator(names)
//
// console.log(namesIterator.next())
// console.log(namesIterator.next())
// console.log(namesIterator.next())
// console. log(namesIterator.next())


//·2.创建一个函数,·这个函数可以迭代一个范围内的数字
//10 20
//迭代器的写法
// function createRangeIterator(start, end) {
//     let index = start
//     return {
//         next: function () {
//             if (index < end) {
//                 return {done: false, value: index++}
//             } else {
//                 return {done: true, value: undefined}
//             }
//         }
//     }
// }

//生成器写法
// function* createRangeIterator(start, end) {
//     let index=start
//     while (index<end){
//         yield index++//yield对函数的执行进行暂停控制
//     }
// }
//
//
// const rangeIterator = createRangeIterator(10, 20)
// console.log(rangeIterator.next())
// console.log(rangeIterator.next())
// console.log(rangeIterator.next())
// console.log(rangeIterator.next())
// console.log(rangeIterator.next())


//自定义类的生成器写法
class Classroom {
    constructor(address, name, students) {
        this.address = address
        this.name = name
        this.students = students//此处传入的是一个数组
    }

    entry(newStudent) {
        this.students.push(newStudent)
    }

    foo =()=>{
        console.log("foo function")
    };

    //自定义类中添加迭代器属性
    // [Symbol. iterator] =function* () {
    //     yield* this.students
    // }
    //此处和上面的一样，只是写法不同
    *[Symbol. iterator](){
        yield* this.students
    }
}

const classroom = new Classroom("3", "1102", ["abc", "cnba"])
classroom.foo()
for(const item of classroom){//此处迭代的对象取决于类中对迭代器的定义中迭代的目标对象(此处为传入的数组)
    console.log(item)
}