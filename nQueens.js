class QueenPosition {
    constructor(rowIndex, columnIndex) {
        this.rowIndex = rowIndex
        this.columnIndex = columnIndex
    }

    get leftDiagonal() {
        return this.rowIndex - this.columnIndex
    }

    get rigthDiagonal() {
        return this.rowIndex + this.columnIndex
    }
}

function isSafe(queensPositions, rowIndex, columnIndex) {
    const newQueenPosition = new QueenPosition(rowIndex, columnIndex)

    for (let queenIndex = 0; queenIndex < queensPositions.length; queenIndex++) {
        const currentQueenPosition = queensPositions[queenIndex]

        if (
            currentQueenPosition &&
            (
                newQueenPosition.columnIndex === currentQueenPosition.columnIndex ||
                newQueenPosition.rowIndex === currentQueenPosition.rowIndex ||
                newQueenPosition.leftDiagonal === currentQueenPosition.leftDiagonal ||
                newQueenPosition.rigthDiagonal === currentQueenPosition.rigthDiagonal
            )
        ) {
            return false
        }
    }
    return true
}

function allQueensSet(queensPositions) {
    return queensPositions.every(position => position !== null)
}

function nQueensRecursive(solutions, previousQueensPositions, queensCount, columnIndex) {
    const queenPositions = [...previousQueensPositions].map(queenPosition => {
        return !queenPosition ? queenPosition : new QueenPosition(queenPosition.rowIndex, queenPosition.columnIndex)
    })

    if (allQueensSet(queenPositions)) {
        solutions.push(queenPositions)
        return true
    }

    for (let rowIndex = 0; rowIndex < queensCount; rowIndex ++) {
        if (isSafe(queenPositions, rowIndex, columnIndex)) {
            queenPositions[rowIndex] = new QueenPosition(rowIndex, columnIndex)

            nQueensRecursive(solutions, queenPositions, queensCount, columnIndex + 1)

            queenPositions[rowIndex] = null
        }
    }
    return false 
}

function nQueens(queensCount) {
    const queenPositions = Array(queensCount).fill(null)
    const solutions = []

    nQueensRecursive(solutions, queenPositions, queensCount, 0)

    return solutions
}

const results = nQueens(4)
console.log(results)
