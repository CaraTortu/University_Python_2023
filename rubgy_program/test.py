from user import User
from stadium import Stadium

def TEST_display_all_seats() -> bool:
    test_stadium = Stadium()
    should_output = "    1 2 3 4 5 6 7 8\n--------------------\n1 | O O O O O O O O \n2 | O O O O O O O O \n3 | O O O O O O O O \n4 | O O O O O O O O \n5 | O O O O O O O O \n"

    return should_output == test_stadium.__str__()

def TEST_register() -> bool:
    test_user = User("Javier")

    return test_user.name == "Javier"

def TEST_verify_ticket() -> bool:
    test_stadium = Stadium()
    test_user = User("Javier")
    
    # Create ticket
    test_ticket = test_stadium.add_ticket(0, 0, test_user)

    # Check that the ticket exists and is not checked in 
    return test_stadium.verify_ticket(test_ticket) == (True, False)

def TEST_check_in() -> bool:
    test_stadium = Stadium()
    test_user = User("Javier")
    
    # Create ticket
    test_ticket = test_stadium.add_ticket(0, 0, test_user)

    # Check in ticket (Should return true since it hasnt been checked in yer)
    check_in_unchecked_ticket = test_stadium.check_in_ticket(test_ticket)
    
    # Try to check it again (Should return False since its already checked in)
    check_in_checked_ticket = test_stadium.check_in_ticket(test_ticket)

    # Try to check in invalid ticket (Should return False)
    check_in_invalid_ticket = test_stadium.check_in_ticket("INVALID")

    # Check if all the previous stated conditions are correct
    return check_in_unchecked_ticket and not check_in_invalid_ticket and not check_in_checked_ticket


def run_all_tests():
    # initial setup
    print("[i] RUNNING ALL TESTS:")
    total_passed = 0
    total_tests = 4

    total_passed += TEST_display_all_seats()
    total_passed += TEST_register()
    total_passed += TEST_verify_ticket()
    total_passed += TEST_check_in()

    # print results
    print(f"[i] Total passed: {total_passed}/{total_tests}")

