// class Person {} //自定义类本身不是可迭代对象

//.const p1 = new Person()
// const p2 = new Person()
// const p3 = new Person()

//·案例:创建一个教室类,创建出来的对象都是可迭代对象
class Classroom {
    constructor(address, name, students) {
        this.address = address
        this.name = name
        this.students = students
    }

    entry(newStudent) {
        this.students.push(newStudent)
    }
    //自定义类中添加迭代器属性
    [Symbol. iterator] () {
        let index = 0
        return {
            next: () => {
                if (index < this.students.length) {
                    return {done: false, value: this.students[index++]}
                } else {
                    return {done: true, value: undefined}
                }
            },
            //就像是for of 在遍历可迭代对象时会自动调用next属性，在break等退出操作时也会调用调用return
            return: () => {//对迭代器中断的监听
                console.log("迭代器提前终止了~")
                //此处的语法规范在return属性对应函数中也要用return返回的对象
                return {done: true, value: undefined}
            }
        }
    }
}

const classroom= new Classroom("3幢5楼205","计算机教室",["james","kobe","curry","why"])
classroom.entry("lilei")

for (const item of classroom) {
    console.log(item)
    if (item === "why") break  //对迭代器强制停止
}

function Person (){}
//构造函数变成可迭代对象
Person.prototype[Symbol. iterator] = function() {
    //内部与其他的方法一致
}