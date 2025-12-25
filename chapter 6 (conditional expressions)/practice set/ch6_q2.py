sub1 = int(input("Enter the marks of sub1 out of 100: "))
sub2 = int(input("Enter the marks of sub2 out of 100: "))
sub3 = int(input("Enter the marks of sub3 out of 100: "))

total_percentage = (sub1+sub2+sub3)/3

if total_percentage>=40 and sub1>=33 and sub2>=33 and sub3>=33:
    print(f"The student has passed with {total_percentage}.")
else:
    reason_of_failing = []
    if sub1<33:
        reason_of_failing.append(f"Marks of subject 1 is {sub1} which is less than 33")
    if sub2<33:
        reason_of_failing.append(f"Marks of subject 2 is {sub2} which is less than 33")
    if sub3<33:
        reason_of_failing.append(f"Marks of subject 3 is {sub3} which is less than 33")
    if total_percentage<40:
        reason_of_failing.append(f"Total percentage is {total_percentage} which is less than 40")
    print(f"The student has passed away with {total_percentage:.2f}% marks cause of {reason_of_failing}.")


    
