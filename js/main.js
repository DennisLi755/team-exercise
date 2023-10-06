const prompt = require('prompt-sync')();

let toDoArray = [];


function addItem(str) {
  return toDoArray.push({ task: str, completed: false });
}
function markComplete(str) {
  for (i = 0; i < toDoArray.length; i++) {
    if (toDoArray[i].task === str) {
      toDoArray[i].completed = true;
    }
  }
}
function deleteItem(str) {
  let toBeRemoved = null;
  for (i = 0; i < toDoArray.length; i++) {
    if (toDoArray[i].task === str) {
      toBeRemoved = i;
    }
  }
  toDoArray.splice(toBeRemoved, 1);
}

function displayMenu(){
    console.log("To-Do Later...Maybe");
    console.log("(>^.^(>");
    console.log("What would you like to do right meow?")
    console.log("1. Add Task")
    console.log("2. Mark Complete")
    console.log("3. Delete Task")
    console.log("4. Quit Program")
}

displayMenu()

while (true){
    let userInput = prompt('Enter Menu Number: ');
    if (userInput === '4'){
        break
    }
}
console.log('Bye-Bye!')

module.exports = { addItem, toDoArray, markComplete, deleteItem };
