const loginBtn = document.querySelector("button")
console.log(loginBtn)
loginBtn.onclick = function() {
    localStorage.setItem("name", "localStorage")
    sessionStorage.setItem("name", "sessionStorage")
}