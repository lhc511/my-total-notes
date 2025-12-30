function divClick() {
    console.log("div元素被点击")
}

const divEl = document.querySelector(".box")

divEl. onclick =function() {
    console.log("div元素被点击3")
}

//.DOM2
divEl.addEventListener("click", () => {
console.log("div元素被点击4")
})
divEl.addEventListener("click", () => {
console.log("div元素被点击5")
})
divEl. addEventListener("click", () => {
    console.log("div元素被点击6")
})