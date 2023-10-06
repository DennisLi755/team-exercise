let toDoArray = [];

function addItem(str){
    return toDoArray.push({task:str, completed:false})
}
function markComplete(str){
    for(i=0;i<toDoArray.length;i++){
        if(toDoArray[i].task===str){
            toDoArray[i].completed = true
        }
    }
}

module.exports = {addItem,toDoArray,markComplete}