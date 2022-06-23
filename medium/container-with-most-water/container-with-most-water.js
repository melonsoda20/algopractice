/**
 * Function that will return max area from a list of array
 *
 * @param {Array<number>} height Array to iterate
 * @returns {number}  max area results
 */

var maxArea = function(height) {
    if(height.length < 2){
        return 0
    }
    maxAreaResult = 0
    let leftPointer = 0
    let rightPointer = height.length - 1

    while(leftPointer < rightPointer){
        minHeight = Math.min(height[leftPointer], height[rightPointer])
        areaLength = rightPointer - leftPointer
        curAreaResult = minHeight * areaLength
        maxAreaResult = Math.max(curAreaResult, maxAreaResult)

        if(minHeight == height[leftPointer]){
            leftPointer += 1
        }
        else{
            rightPointer -= 1
        }
    }

    return maxAreaResult
};

heightData = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = maxArea(heightData)

console.log(result)
