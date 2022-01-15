function solution(ball, order) {

    var answer = [];
    const ballLenght = ball.length

    let check = 0;
    var ball = [...ball];
    var order = [...order];

    while (true) {
        console.log("while Start !!!")
        if (ball[0] === order[check]) {
            answer.push(order[check]);
            a = ball.indexOf(order[check])
            b = order.indexOf(order[check])
            ball.splice(a, 1);
            order.splice(b, 1);
            check = 0
        }
        else if (ball[ball.length - 1] === order[check]) {
            answer.push(order[check]);
            a = ball.indexOf(order[check])
            b = order.indexOf(order[check])
            ball.splice(a, 1);
            order.splice(b, 1);
            check = 0
        }
        else {
            check += 1
        }
        console.log(answer);

        if (answer.length === ballLenght) {
            break
        }

    }
    return answer;
}

const ball = [1, 2, 3, 4, 5, 6]
const order = [6, 2, 5, 1, 4, 3]

solution(ball, order)