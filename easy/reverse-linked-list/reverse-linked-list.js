/**
 * Definition for singly-linked list.

 */
function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
 var reverseList = function(head) {
    prevNode = null
    curNode = head

    while(curNode != null){
        nextNode = curNode.next
        curNode.next = prevNode
        prevNode = curNode
        curNode = nextNode
    }

    return prevNode
};