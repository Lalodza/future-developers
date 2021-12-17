/*
 *Dado un arreglo de cadenas regresar otro que
 *que contenga solo las cadenas mas largas
 *
 * Ejemplo:
 * para:
 * inputArray  = ["aba", "aa", "ad", "vcd", "aba"]
 * 
 * la salida debe de ser:
 * allLongestString(inputArray) = ["aba", "vcd", "aba"]
 */

function allLongestString(inputArray) {
    let longestSize = -1
    const result = []

    for (let i = 0; i < inputArray.length; i++) {
        if (inputArray[i].length > longestSize) {
            longestSize = inputArray[i].length
        }
    }

    for (let i = 0; i < inputArray.length; i++) {
        if (inputArray[i].length === longestSize) {
            result.push(inputArray[i])
        }
    }
    return result
}

const inputArray = ["aba", "qwerty", "aa", "ad", "vcd", "aba"]
const result = allLongestString(inputArray)
console.log(result)