const spanEl =document.querySelector(".span")

spanEl.addEventListener("click", (event) => {
    console.log("span元素被点击:", event)
    console.log("事件的类型:", event.type)
    console.log("事件的元素:", event.target, event.currentTarget)
    console.log("事件发生的位置:", event.offsetX, event.offsetY)
})

const divEl = document.querySelector(".container")

divEl.addEventListener("click", (event) => {
    console.log("div元素被点击:", event.target, event.currentTarget)
})

// 常见的方法
// preventDefault
const aEl= document.querySelector("a")
aEl.addEventListener("click", (event) => {
    event.preventDefault()//阻止a标签的默认跳转行为
})

// stopPropagation：在冒泡和捕获中调用，阻止事件的进一步传递
