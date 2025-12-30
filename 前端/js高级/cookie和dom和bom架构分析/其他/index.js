//之后在系统学习，用django的思想来看待
// const Koa = import('koa');
// const Router = import('koa-router');

const app=new Koa()
const testRouter=new Router()

//koa的代码和django类似
//、登录接口
testRouter.get('/',(ctx, next)=> {
//·maxAge对应毫秒
    ctx.cookies.set("name", "why", {
        maxAge: 60 * 1000
    })
    ctx.body = "test";//在浏览器网页上输入test
})

testRouter.get('/', (ctx, next) =>{
//·读取cookie
const value = ctx.cookies.get('name');//拿到cookies中设置的键name的值
ctx.body = "你的cookie是"+value;//
});

app.use(testRouter.routes());
app.use(testRouter.allowedMethods());

app.listen(8080, () =>{
console.log("服务器启动成功~");
})

testRouter.get('/demo', (ctx, next) => {
//·读取cookie
    const value = ctx.cookies.get('name');
    ctx.body = "你的cookie是" + value;
});
app.use(testRouter.routes());
app.use(testRouter.allowedMethods());

app.listen(8080, () => {
    console.log("服务器启动成功~");
})