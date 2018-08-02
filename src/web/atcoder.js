function submit() {
    program = document.getElementById('answer').value;
    var s = document.createElement('script');
    s.innerHTML = program;
    var ele = document.getElementById('result');
    ele.appendChild(s);
    var req = new XMLHttpRequest();
    req.open('get', 'https://www.google.co.jp', true);
    req.send(null);
    req.onload = function() {
        console.log(req.responseText);
    }
}

var a = [];


function get_input1() {
    return a[0];
}

function get_input2() {
    return a[1];
}
