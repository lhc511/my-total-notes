function throttle(fn, interval,options={leading:true,trailing:false},resultCallback) {
    // leading为true则默认第一次触发，反之相反
    const {leading, trailing} = options
    let lastTime = 0
    let timer = null

    const _throttle = function (...args) {
        const nowTime = new Date().getTime()
        console.log('时间差:',interval - (nowTime - lastTime))

        //节流时在第一次不触发函数的执行
        if (lastTime === 0 && leading === false) lastTime = nowTime//此处之后使得remainTime大于零
        console.log('::',lastTime)//将上一次事件触发的时刻赋值给lastTime,当leading为false时,由执行处2来执行事件

        //**********函数执行处1**********只在leading为true时第一次执行一次，之后都由执行处2来处理事件
        //当leading为true时:第一次:传入的数字-(很大的数字-0) 符合条件，因此第一次会立即执行
        const remainTime = interval - (nowTime - lastTime)
        if (remainTime <= 0) {
            if (timer) {
                clearTimeout(timer)//取消在节流期间因事件触发而添加的定时器
                timer = null
            }

            fn.apply(this, args)
            lastTime = nowTime
            return  //此处已经触发函数，不需要加定时器，否则后面依旧会添加定时器导致重复执行
        }

        //**********函数执行处2********此处时是leading为true的第一次以后的后续执行和为false的所有执行的主要处理过程

        //!timer:一次执行和下一次执行期间触发的事件,并且没有定时器(即防止定时器多次重复设置)
        //若在下一次没有触发事件则自动触发一次(即自动执行最后一次)
        if (trailing && !timer) {
            //此处的定时器是在上下一次期间设置的，因此当手动触发下一次事件时(除非恰好等于10秒上面才会清除定时器,一般不可能)
            //因此在 下一次触发和手动触发 的理想时间 的间隔 定时器就会触发

            timer = setTimeout(() => {//在等待remainTime后才会执行其中代码(即事件出发函数)
                //在下一次手动触发前将定时器和初始时间清空
                timer = null

                //leading为false时不立即执行，并lastTime置零 此处为下一次手动事件触发做准备
                lastTime = !leading ? 0 : new Date().getTime()//将此次节流事件触发的时间交给lastTime
                console.log('节流期间:'+lastTime)
                fn.apply(this, args)//执行事件
                // const result=fn.apply(this, args)
                // resolve(result)//promise返回方法

            }, remainTime)//会在remainTime的时间后自动触发一次，即每一次在理想时间执行.以5s为例例:0,5,10...
            //remainTime是触发事件时的时刻到目标时刻所需的时间
        }

        _throttle.cancel = function () {
            if (timer) clearTimeout(timer)
            timer = null
            lastTime = 0
        }
    }
    return _throttle
}