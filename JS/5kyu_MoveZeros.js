const inp = [false, 1, 0, 1, 2, 0, 1, 3, 'a']

function moveZeros(input) {
  let arr = []
  let count = 0
  input.map((element, index) => {
    if (element !== 0) {
      arr.push(element)
    } else {
      count++
    }
  })

  for (let i = 0; i < count; i++) {
    arr.push(0)
  }
  return arr
}

/* moveZeros([false, 1, 0, 1, 2, 0, 1, 3, 'a']) // returns[false,1,1,2,1,3,"a",0,0]
 */

moveZeros(inp)
