function submit() {
    program = document.getElementById('answer').value;
    var s = document.createElement('script');
    s.innerHTML = program;
    var ele = document.getElementById('result');
    ele.appendChild(s);
}

a = [];


function get_input1() {
    return a[0];
}

function get_input2() {
    return a[1];
}

console.log = function(message) {
    console.log(message);
    return message;
}
