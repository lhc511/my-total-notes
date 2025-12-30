define(function() {//define是AMD的导出方式
    const name = "why"
    const age = 18

    function sum(num1, num2) {
        return num1 + num2
    }

    return {
        name,
        age,
        sum
    }
})