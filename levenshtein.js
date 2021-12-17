function levenshteinDistance(a, b) {
    // Create Empty Matrix
    const distanceMatrix = Array(a.length + 1).
        fill (null).
        map(() => Array(b.length + 1).fill(null))

        // fill fisrt row
        for (let i = 0; i <= b.length; i++) {
            distanceMatrix[0][i] = i
        }

        // fill fisrt column
        for (let j = 0; j <= a.length; j++) {
            distanceMatrix[j][0] = j
        }
        
        // Calculate distances
        
        for (let i = 1; i <= a.length; i++){
            for (let j = 1; j <= b.length; j++){
                const indicator = a[i - 1] === b[j - 1] ? 0 : 1
                
                distanceMatrix[i][j] = Math.min(
                    distanceMatrix[i][j - 1] + 1, //insert
                    distanceMatrix[i - 1][j] + 1, //delete
                    distanceMatrix[i - 1][j - 1] + indicator, //replace or nothing
                    )
                }
            }
            
            console.log(distanceMatrix)
            // return distance value
}
levenshteinDistance('casas', 'cosa')
