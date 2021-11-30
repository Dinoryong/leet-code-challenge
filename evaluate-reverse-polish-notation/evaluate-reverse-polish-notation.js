
// Written by @jamesernator James Browning

const OPERATORS = ["+", "-", "/", "*"];

var evalRPN = function(tokens) {
    const stack = [];

    for (const token of tokens) {
        if (!OPERATORS.includes(token)) {
            stack.push(Number(token));
            continue;
        }

        const number2 = stack.pop();
        const number1 = stack.pop();

        switch (token) {
            case "+": {
                stack.push(number1 + number2);
                break;
            } case "-": {
                stack.push(number1 - number2);
                break;
            } case "/": {
                stack.push(Math.trunc(number1 / number2));
                break;
            } case "*": {
                stack.push(number1 * number2);
                break;
            }
        }
    }

    return stack.pop();
};