var timer;

function check_email(){
    var email = $(".email-input").val();
    var error_div = $(".error-tips-div");
    var result_div = $(".result-div");
    var load_div = $(".loaders-div");
    var tips_div = $(".tips-div");
    var server_error_div = $(".server-error-tips-div");

    var reg = /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/;

    clearInterval(timer);

    tips_div.css("display","none");
    result_div.css("display","none");
    unresultcss();


    if(email.length > 48)
    {
        error_div.css("display","block");
        return false;
    }
    if(!reg.test(email))
    {
        error_div.css("display","block");
        return false;
    }
    error_div.css("display","none");
    server_error_div.css("display","none");

    $(".loaders-div").css("display","block");
    showslider();


    $.ajax({
        url:"/check/"+email,
        type:"get",
        aysnc:true,
        dataType: "json",
        success:function(data){
            load_div.css("display","none");

            switch(data.status)
            {
                case "1":
                    server_error_div.css("display","block");
                    server_error_div.html("您查询过于频繁，请休息一会...");
                    break;
                case "0":
                    loadtips();
                    resultcss();
                    tips_div.css("display","block");

                    var data = data.data;
                    result_div.css("display","block");
                    $(".grade-span").html(data.grade);

                    var str = "";

                    for(var i in data.decision)
                    {
                        str += data.decision[i] +"<br>";
                    }

                    $(".decision-span").html(str);
                    savecfg();
                    break;
                case "2":
                    error_div.css("display","block");
                    break;
                default:
                    server_error_div.css("display","block");
                    server_error_div.html("sorry，您给服务器提了一个问题....");
                    break;
            }
        }
    })
}


function isEnter(e)
{
    if (e.keyCode == 13){
        check_email();
    }
}


function savecfg(){
    localStorage.email_name = $(".email-input").val();
}

function loadcfg(){
    var email_name = localStorage.email_name;
    $(".email-input").val(email_name);
}


function loadtips(){
    timer = setInterval("gettips()",1000*5);
}


function gettips(){
    var Arr = [
    "大部分互联网账号都采用邮箱注册，邮箱地址是我们验证网络欺诈的第一道关口。",
    "不仅仅是简单地邮箱存在探测，我们还采用了“机器学习”的方式，对邮箱名称进行分析。",
    "互联网上有很多的临时邮箱服务商，坏人们常常利用他们注册很多的垃圾小号。",
    "同盾邮霸比对了同盾所拥有的海量黑名单数据，让坏邮箱无处藏身。",
    "分数越高，邮箱越可信！"
    ];

    var n = Math.floor(Math.random() * Arr.length + 1)-1;
    $(".tips-div .tips-span").html(Arr[n]);
}


function resultcss(){
    $("#wapper").css("background-color","#f5f5f5");
    $(".bg-content-div").css("background-image",'url("/static/image/background.jpg")');
}

function unresultcss(){
    $("#wapper").css("background-color","");

}

function showslider(){
    $(".newslistwraper").Xslider({
        unitdisplayed:1,
        numtoMove:1,
        loop:"cycle",
        dir:"V",
        autoscroll:4000,
        speed:300,
    });
    $("a.abtn").focus(function(){this.blur();});
}
