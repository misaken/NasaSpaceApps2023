function square(number)
{
    return number * number;
}

// function getQuestion()
// {
//     let qst = document.getElementById('question');
// }

var qst;

function onClick()
{
    qst = document.getElementById('question').value;
    document.querySelector('.balloon1-top').innerHTML = qst;
}

//qst = document.getElementById('question').value;

var random = Math.random();

document.write("<h1>javascriptから喋ってます</h1>");
var a = 2;
var b = square(a);

document.write("<h1>");
if (random <= 0.5)
{
    document.write(a + ", ");
    document.write(random);
}
else
{
    document.write(b + ", ");
    document.write(random);
}
document.write(qst);
document.write("</h1>");
