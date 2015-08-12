def isPalindrome(head):
    rev=None
    jump1=jump2=head
    while jump2 and jump2.next:
        jump2=jump2.next.next
        rev,rev.next,jump1=jump1,rev,jump1.next
    if jump2:
        jump1=jump1.next
    while rev and rev.val==jump1.val:
        rev=rev.next
        jump1=jump1.next
    return rev
    
