/**
 * Function that will return 2 index of from input num where the summed values is equal to targetNum
 *
 * @param {Array<number>} inputNum Array to search from.
 * @param {number} targetNum Targget Number value
 * @returns {Array<number>}  Array filled with two indexes of the correct numbers.
 */
function twoSum(inputNum, targetNum){
    if (inputNum.length < 2){
        return null
    }

    const valueMapTable = new Map()

    for (let i = 0; i < inputNum.length; i++){
        let desiredValue = targetNum - inputNum[i]
        if(valueMapTable.has(desiredValue)){
            return [valueMapTable.get(desiredValue), i]
        }
        else{
            valueMapTable.set(inputNum[i], i)
        }
    }
    return null
}


const inputNum = [2, 3, 5]
const targetNum = 8

console.log(twoSum(inputNum, targetNum))
