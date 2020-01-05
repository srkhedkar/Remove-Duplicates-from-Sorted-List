/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::deleteDuplicates(ListNode* A) {
    if (NULL == A)
    {
        return A;
    }

    ListNode* current;
    ListNode* next;

    current = A;
    next = A->next;

    while (next)
    {
        if (current->val == next->val)
        {
            current->next = next->next;
            delete next;
            next = current->next;
        }
        else
        {
            current = current->next;
            next = current->next;
        }        
    }

    return A;
}
