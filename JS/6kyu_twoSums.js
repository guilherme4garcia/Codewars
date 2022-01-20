const numb = [1, 2, 3]
const target = 4

function twoSum(numb, target) {
  let result = null
  let sum = null
  numb.forEach((element, index) => {
    for (let i = 0; i < numb.length; i++) {
      if (index != i) {
        sum = element + numb[i]
        if (sum === target) {
          result = [i, index]
        }
      }
    }
  })
  return result
}

twoSum(numb, target)
