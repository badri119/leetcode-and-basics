// FizzBuzz
/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function (n) {
  let result = [];

  for (let i = 1; i < n + 1; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      result.push("FizzBuzz");
    } else if (i % 3 == 0) {
      result.push("Fizz");
    } else if (i % 5 == 0) {
      result.push("Buzz");
    } else {
      result.push(i.toString());
    }
  }
  return result;
};

// Palindrime Number:
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  if (x < 0) {
    return false;
  }
  x = x.toString();
  let pointerLeft = 0;
  let pointerRight = x.length - 1;

  while (pointerLeft <= pointerRight) {
    if (x[pointerLeft] === x[pointerRight]) {
      pointerLeft += 1;
      pointerRight -= 1;
    } else {
      return false;
    }
  }
  return true;
};

//Palindrime String:
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  let string = "";

  for (i = 0; i < s.length; i++) {
    if (s[i].match(/^[a-zA-Z0-9]+$/)) {
      string += s[i].toLowerCase();
    }
  }

  left = 0;
  right = string.length - 1;

  while (left <= right) {
    if (string[left] === string[right]) {
      left += 1;
      right -= 1;
    } else {
      return false;
    }
  }
  return true;
};
