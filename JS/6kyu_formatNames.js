const names = [{ name: 'Bart' }, { name: 'Lisa' }]
const test = { name: 'Gui' }
function list(names) {
  let text = ' & '
  let position = names.lenght - 1
  let output = ''

  if (names.length > 1) {
    output = [names.slice(0, position), text, names.slice(position)].join('')
  } else {
    output = names.name
  }
  return output
}

list(names)
