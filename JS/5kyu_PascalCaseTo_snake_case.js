function toUnderscore(string) {
  if (string[0] != undefined) {
    string = string[0].toLowerCase() + string.slice(1)
  }
  let result = ''
  for (let index = 0; index < string.length; index++) {
    if (Number.parseInt(string[index])) {
      result += string[index]
    } else if (string[index] === string[index].toUpperCase()) {
      result += '_' + string[index].toLowerCase()
    } else {
      result += string[index]
    }
  }

  return result.toString()
}
