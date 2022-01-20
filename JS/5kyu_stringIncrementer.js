const n = 'foo0042'
// foo0042 -> foo0043

function incrementString(strng) {
  let num = ''
  let str = ''
  for (let i = 0; i < strng.length; i++) {
    str = strng.concat(strng[i])
    let table = parseInt(strng[i])
    if (Number.isInteger(table)) {
      num += table
    }
  }
  let result = parseInt(num) || 0
  result += 1
  let size = num.length
  let zeroSize = size - result.toString().length
  let strSize = strng.length - size
  str = strng.slice(0, strSize)

  for (let j = 0; j < zeroSize; j++) {
    str = str.concat('0')
  }

  return str + result
}

incrementString(n)
