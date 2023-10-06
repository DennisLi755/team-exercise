let toDoArray = [];

function addItem(str){
    return toDoArray.push({task:str, completed:false})
}

module.exports = {addItem,toDoArray}