
//针对log页面定义对象
let log={
    dt:"2025-5-29",
    enddt:"2025-5-30",
    update:"2025-5-29",
    anchor:"李海川"
};
//由对象派生业务逻辑
//可以先理解为起一个叫log.submit的变量名
// check和autohide都是里面的方法函数名称
// 例:和function check(参数){}一样
log.submit={
    check:function (v){
        return v === "";
    },
    autohide:function (obj){
        setTimeout(function (){
            obj.hide();
        },2000);
    }
};

let $form=$("form");
let $username=$("#username");
let $password=$("#password");
let $err1=$("#err1");
let $err2=$("#err2");
let $btn=$(".btn>input");
//绑定按钮的单击事件
$(function (){
    $form.on("submit",function (){
            //用户名和密码都不为空
        if($username.val()!==""&&$password.val()!==""){
            return true;
        }
        if($username.val()===""){
            $err1.show();
            //两秒后自动隐藏
            log.submit.autohide($err1);
        }
        if($password.val()===""){
            $err2.show();
            log.submit.autohide($err2);
        }
        return false;
    })
})


//定义一个基于列表页的业务逻辑
let lst={
    template:function (title,picture,subtitle,describe){
        let HTML="";
        HTML= "<div class=\"item\">" +
                    "<div class=\"title\">" +
                        "<h3>"+title+"</h3>" +
                    "</div>"+
                    "<div class=\"con\">" +
                        "<div class=\"cleft\">"+
                            "<img src="+picture+" alt=\"\">" +
                        "</div>"+
                        "<div class=\"cright\">" +
                            "<p class=\"ptop\">" +subtitle+ "</p>" +
                            "<p class=\"pbottom\">"+describe+"</p>" +
                        "</div>" +
                    "</div>" +
                "</div>";
        return HTML;
    }
}

// let HTML=lst.template("Python语言在人工智能(AI)中的优势",
//     "imgs/b05.jpg",
//     "本文讨论了Python语言在AI领域的优势与运用,谁会成为AI和大数据的第一开发语言？这本以是一个不需要争论的问题，如果说三年前，Matlab、Scala、R、Java...",
//     "皮皮璐 学无止境 2018-5-13 34567阅读 9999")

//在所有文件中寻找 id是list 并且后代为 list类 的位置在这个位置上添加css代码

let arrData=[
    {
        title:"Python语言在人工智能(AI)中的优势",
        picture:"imgs/b05.jpg",
        subtitle:"本文讨论了Python语言在AI领域的优势与运用,谁会成为AI和大数据的第一开发语言？这本以是一个不需要争论的问题，如果说三年前，Matlab、Scala、R、Java...",
        describe:"皮皮璐 学无止境 2018-5-13 34567阅读 9999"
    },
    {
        title:"Web的优势",
        picture:"imgs/c.jpg",
        subtitle:"数据的第一开发语言？这本以是一个不，如果说三年前，Matlab、Scala、R、Java...",
        describe:"李海川 学无止境 2018-5-13 34567阅读 9999"
    },
    {
        title:"c++语言在人工智能(AI)中的优势",
        picture:"imgs/banner01.jpg",
        subtitle:"本文讨论了Python语言在AI领域的优势与运用,谁会成为AI和大数据的第一开发语言？这本以是一个不需要争论的问题，如果说三年前，Matlab、Scala、R、Java...",
        describe:"皮皮璐 学无止境 2018-5-13 34567阅读 9999"
    }
];

for(let i=0;i<arrData.length;i++){
    let _HTML=lst.template(arrData[i].title,arrData[i].picture,arrData[i].subtitle,arrData[i].describe);
    $("#list .list").append(_HTML);
}

/////////////////////定义图片相册的业务逻辑对象
let pics={
    template:function (url,num,title){
            let HTML="<div class=\"item\">" +
                "        <div class=\"imgs\">" +
                "            <img src=\"" +url+ "\" alt=\"\">" +
                "            <div class=\"tip\">喜欢 | "+ num +"</div>" +
                "        </div>" +
                "        <div class=\"title\">" +
                "                <h3>"+title+"</h3>" +
                "        </div>" +
                "    </div>";
                return HTML;
        }
}

//定义一个包含三个对象内容的图片数组
let arrPics=[
    {url:"imgs/a.jpg",num:223,title:"python文件打开报错"},
    {url:"imgs/b04.jpg",num:260,title:"Web文件打开报错"},
    {url:"imgs/banner01.jpg",num:200,title:"ahdahdaohdaw报错"}
];

for(let i=0;i<arrPics.length;i++){
    let _HTML=pics.template(arrPics[i].url,arrPics[i].num,arrPics[i].title);
    $("#pics").append(_HTML);
}