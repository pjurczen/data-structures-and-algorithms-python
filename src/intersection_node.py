def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    lenA: int = 0
    tmpA = headA
    while tmpA is not None:
        lenA += 1
        tmpA = tmpA.next
    lenB: int = 0
    tmpB = headB
    while tmpB is not None:
        lenB += 1
        tmpB = tmpB.next
    diff: int = lenB - lenA
    # B is longer
    while diff > 0:
        headB = headB.next
        diff -= 1
    # A is longer
    while diff < 0:
        headA = headA.next
        diff += 1
    while headA is not None:
        if headA is headB:
            return headA
        headA = headA.next
        headB = headB.next
    return None
