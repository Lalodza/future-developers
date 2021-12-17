/*
 * Haz depositado a tu cuenta bancaria una cantidad especifica de dinero(deposit)
 * cada año tu saldo incrementa a la misma tasa de crecimiento (rate)
 * asumiendo que no haces depositos adicionales
 * averigua cuanto tiempo le tomaria a tu dinero superar un umbral especifico (threshold).
 * 
 * Ejemplo:
 * 
 * Para:
 * deposit = 100
 * rate = 20
 * threshold = 170
 *  la salida debe de ser
 * depositProfit(deposit, rate, threshold) = 3
 * 
 * Cada año la cantidad de dinero en tu cuenta crece 20%
 * asi que con los años el saldo quedaria de la siguiente manera:
 * 
 * -year 0: 100
 * -year 1: 120
 * -year 2: 144
 * -year 3: 172.8
 */

function depositProfit(deposit, rate, threshold) {
    let count = 0
    const growthRate = rate * 0.01

    while (deposit < threshold) {
        let interest = deposit * growthRate
        console.log('currently in the account ${deposit}' )
        deposit = deposit + interest
        count++
    }
    return count
}

const result = depositProfit(100, 20, 170)
console.log(result)