/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
 var maxDepth = function(root) {
    return maxDepthResults(root);
};

const maxDepthResults = function(root){
    if(!root){
        return 0;
    }
    if(!root.left && !root.right){
        return 1
    }

    const maxLeft = maxDepth(root.left);
    const maxRight = maxDepth(root.right);

    return Math.max(maxLeft, maxRight) + 1;
};