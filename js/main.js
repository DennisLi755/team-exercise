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

module.exports = { addItem, toDoArray, markComplete, deleteItem };
