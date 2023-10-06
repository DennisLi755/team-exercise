const prompt = require("prompt-sync")();

let toDoArray = [];

function addItem(str) {
  return toDoArray.push({ task: str, completed: false });
}
function markComplete(str) {
  let isFound = false;
  for (i = 0; i < toDoArray.length; i++) {
    if (toDoArray[i].task === str) {
      toDoArray[i].completed = true;
      isFound = true;
    }
  }
  if (!isFound) {
    console.log("Item not found");
  }
}
function deleteItem(str) {
  let toBeRemoved = null;
  for (i = 0; i < toDoArray.length; i++) {
    if (toDoArray[i].task === str) {
      toBeRemoved = i;
    }
  }
  if (toBeRemoved != null) {
    console.log(`${str} succesfully deleted`);
    toDoArray.splice(toBeRemoved, 1);
  } else {
    console.log(`${str} not found`);
  }
}

function displayToDoList() {
  for (let item of toDoArray) {
    if (item.completed == true) {
      console.log(`[ᓚᘏᗢ ] ${item.task}`);
    } else {
      console.log(`[] ${item.task}`);
    }
  }
}

function displayMenu() {
  console.log("To-Do Later...Maybe");
  console.log("(>^.^(>");
  console.log("What would you like to do right meow?");
  console.log("1. Add Task");
  console.log("2. Mark Complete");
  console.log("3. Delete Task");
  console.log("4. Quit Program");
}

displayMenu();

while (true) {
  displayToDoList();
  let userInput = prompt("Enter Menu Number: ");
  if (userInput === "4") {
    break;
  } else if (userInput === "1") {
    let taskName = prompt("Enter New Task: ");
    addItem(taskName);
  } else if (userInput === "2") {
    let taskName = prompt("What did you complete? ");
    markComplete(taskName);
  } else if (userInput === "3") {
    let taskName = prompt("Enter the task you want to delete FUREVER: ");
    deleteItem(taskName);
  } else {
    console.log("Invalid Input");
  }
}
console.log("Bye-Bye!");

module.exports = { addItem, toDoArray, markComplete, deleteItem };
