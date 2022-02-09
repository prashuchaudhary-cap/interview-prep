// A closure is a function that remembers its outer variables and can access them.
// In JavaScript, all functions are naturally closures (there is only one exception "new Function" syntax).

// That is: they automatically remember where they were created using a hidden [[Environment]] property,
// and then their code can access outer variables.


function debounce(func, ms) {
  let timeout;
  return function() {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, arguments), ms);  // Passing all arguments along with the context to another function is called call forwarding.
  };
}


function throttle(func, ms) {

  let isThrottled = false,
    savedArgs,
    savedThis;

  function wrapper() {

    if (isThrottled) { // (2)
      savedArgs = arguments;
      savedThis = this;
      return;
    }

    func.apply(this, arguments); // (1)

    isThrottled = true;

    setTimeout(function() {
      isThrottled = false; // (3)
      if (savedArgs) {
        wrapper.apply(savedThis, savedArgs);
        savedArgs = savedThis = null;
      }
    }, ms);
  }

  return wrapper;
}

// method borrowing when we take a method from an object and call it in the context of another object.
// It is quite common to take array methods and apply them to arguments.
function hash() {
  alert( [].join.call(arguments) ); // 1,2
}


function defer(f, ms) {
  return function() {
    setTimeout(() => f.apply(this, arguments), ms)
  };
}


// If you come from another programming language, then you are probably used to the idea of a "bound this",
// where methods defined in an object always have this referencing that object.

// In JavaScript this is “free”, its value is evaluated at call-time and does not depend on where the method
// was declared, but rather on what object is “before the dot”.

// The concept of run-time evaluated this has both pluses and minuses. On the one hand, function can be reused
// for different objects. On the other hand, the greater flexibility creates more possibilities for mistakes.




// __proto__ is not the same as [[Prototype]]. It’s a getter/setter for it.


// A module code is evaluated only the first time when imported
// If the same module is imported into multiple other places, its code is executed only the first time, then exports are given to all importers.

