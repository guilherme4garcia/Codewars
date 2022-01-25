/* 
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

    Only lower case letters will be used (a-z). 
    No punctuation or digits will be included.
    Performance needs to be considered. 
    (not working for this criteria yet...)

*/

function scramble(str1, str2) {
  let table = str1.split('')
  for (let i = 0; i < str2.length; i++) {
    let letter = table.includes(str2[i])
    if (letter) {
      let index = table.indexOf(str2[i])
      table.splice(index, 1)
    }
    if (letter === false) {
      return false
    }
  }
  return true
}
