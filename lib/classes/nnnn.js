function findingUnpairedElement(A) {
    let unpaired = 0;

    
    for (let i = 0; i < A.length; i++) {
        unpaired ^= A[i];
    }

    return unpaired;
}

// Test case
const A = [9, 3, 9, 3, 9, 7, 9];
console.log(findingUnpairedElement(A)); // Output: 7
