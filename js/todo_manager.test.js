const {addItem,toDoArray,markComplete} = require("./main");

describe("test add item", () => {
    test("addItem('washthedog') === add item washthedog to todo list",() => {
        addItem("washthedog")
        expect(toDoArray).toContainEqual({task:"washthedog",completed:false});
    })
})

describe("test completor", () => {
    test("markComplete('washthedog') === mark washthedog to completed:true",() => {
        markComplete("washthedog")
        expect(toDoArray).toContainEqual({task:"washthedog",completed:true});
    })
})