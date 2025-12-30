//只能对对象进行继承，以为是要给原型对象进行赋值，只能是对象{}
var obj = {
    name: "why",
    age: 18
}
//-原型式继承函数
function createObject(o) {
    var newObj = {}
    //将newObj的原型对象设置为传进来的 o 对象(此处为obj对象)
    Object.setPrototypeOf(newObj, o)
    return newObj//实际上是返回了一个空对象
}


function createObject2(o) {
    function Fn(name) {}
    Fn.prototype = o
    var newObj = new Fn()//构造函数创建的对象，__proto__指向构造函数的对象原型
    return newObj
}


var info = createObject(obj)//创建并返回空对象{}，并使该对象的原型(__proto__)指向obj对象
//在新规中提供了内置函数
var info=Object.create(obj)//是实现相同效果    {}
var info = createObject2(obj)

console.log(info)//{}
console. log(info.__proto__)//{name: 'why', age: 18}