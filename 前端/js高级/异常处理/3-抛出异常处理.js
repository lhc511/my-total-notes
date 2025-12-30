function foo() {
    throw "foo error message~"
}

function bar () {
    try{
        foo()
    }catch (err){
        console.log(err)
    }finally{
        console.log('must执行')
    }

}

function test() {
    bar ()
}

function demo(){
    test()
}

demo()
console.log('aaaaaaaaaaaaaaaaaaaaaaaaa')