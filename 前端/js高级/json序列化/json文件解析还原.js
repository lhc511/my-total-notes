const JSONString ='{"name":"why","age":18,"friends":{"name":"kobe"},"hobbies":["篮球","足球"]}'
//parse函数的第二个参数是一个操作函数，可以对一些属性进行操作
const info = JSON.parse(JSONString, (key, value) => {
    if (key === "age") {
        return value - 1
    }
    return value
})
console. log(info)