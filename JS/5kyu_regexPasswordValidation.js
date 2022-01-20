function validate(password) {
  return (
    //At least six characters long
    /^[A-Za-z0-9]{6,}$/.test(password) &&
    // contains a uppercase letter
    /[A-Z]+/.test(password) &&
    // contains a lowercase letter
    /[a-z]+/.test(password) &&
    // contains a number
    /[0-9]+/.test(password)
  )
}

/* 
function validate(password) {
  return /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]{6,}$/.test(password);
} 
*/
