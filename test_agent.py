from agent import ReflexVacuumAgent

def test_reflex_vacuum():
    # Rule 1: Dirty always means Suck
    assert ReflexVacuumAgent(('A', 'Dirty')) == 'Suck'
    assert ReflexVacuumAgent(('B', 'Dirty')) == 'Suck'
    
    # Rule 2: Clean in A means move Right
    assert ReflexVacuumAgent(('A', 'Clean')) == 'Right'
    
    # Rule 3: Clean in B means move Left
    assert ReflexVacuumAgent(('B', 'Clean')) == 'Left'
    
    print("✅ All Figure 2.8 tests passed!")

if __name__ == "__main__":
    try:
        test_reflex_vacuum()
    except AssertionError:
        print("❌ Test failed: Your logic does not match Figure 2.8.")
        exit(1) # Ensure the autograder sees a failure
