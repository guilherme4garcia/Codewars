const validParentheses = input => {
  let count = 0
  for (let i = 0; i < input.length; i++) {
    if (input[i] === '(') {
      count++
    } else {
      count--
    }
    if (count < 0) {
      count = false
      return count
    }
  }
  return count === 0 ? true : false
}
