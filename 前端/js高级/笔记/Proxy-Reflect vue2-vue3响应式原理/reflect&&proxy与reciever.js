// const obj = {
//     name: "why",
//     age: 18
// }
//
// const objProxy = new Proxy(obj, {
//     get: function (target, key, receiver) {
//         return Reflect.get(target, key)
//     },
//     set: function (target, key, newValue, receiver) {
//         const result=Reflect.set(target, key, newValue)//reflect在设置后会返回布尔类型来表示成功和失败
//         if (result) {}
//         else {
//         }
//
//         // target[key]=newValue  //此处还是对原对象尽行直接操作  用了reflect后便可以避免这种情况，前面一样
//     }
// })
// objProxy.name = "kobe"
// console. log(objProxy.name)

//receiver
const obj = {
    _name: "why",
    get name() {
        //在代理对象有receiver参数后，此处this指向代理对象，因此this._name会触发代理对象的get函数
        return this._name
    },
    set name(newValue) {
        this._name = newValue

    }
}

const objProxy = new Proxy(obj, {
    get: function (target, key,receiver) {
        //若无receiver参数则先通过obj对象中的get函数再访问obj中的name属性，最终this绑定到obj原对象对象
        //与代理对象的需求目的不符，加入receiver可以使this指向代理对象
        console.log("get方法被访问", key, receiver)

        // console.log(receiver === objProxy)  //true

        //receiver就是代理对象，并作为this传到原对象中，使this指向代理对象，通过代理对象获取值时触发此处get函数，
        //在通过reflect调用原对象obj获取值时通过调用this(代理对象)又触发一次此处的代理对象的get函数，所以打印两次
        return Reflect.get(target, key,receiver)
    },
    set: function (target, key, newValue) {
        Reflect.set(target, key, newValue)
    }
})
obj.name = "kobe"
console. log(objProxy.name)