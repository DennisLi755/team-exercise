const {addItem,toDoArray} = require("./main");

// describe("test adding items", () => {
//     test("addItem('washthedog') === add item washthedog to todo list",() => {
//         addItem("washthedog")
//         expect(toDoArray).toContain("washthedog");
//     })
// })
describe("test todolist", () => {
    test("addItem('washthedog') === add item washthedog to todo list",() => {
        addItem("washthedog")
        expect(toDoArray).toContain({task:"washthedog",completed:false});
    })
})