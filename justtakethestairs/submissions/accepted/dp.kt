    import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer
import kotlin.math.min

fun main() {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    var st = StringTokenizer(reader.readLine())
    val N = st.nextToken().toInt()
    val C = st.nextToken().toInt()

    val S = IntArray(N + 1)
    val F = IntArray(N + 1)

    for (i in 1..N) {
        st = StringTokenizer(reader.readLine())
        S[i] = st.nextToken().toInt()
        F[i] = st.nextToken().toInt()
    }

    //Cant use max like in python solution because of wrapping, so just use a large number instead
    val dp = IntArray(N + 1) { 1_000_000_000 }
    dp[0] = 0

    for (i in 1..N) {
        var students = 0
        var mask = 0
        var maxFloor = 0

        for (j in i - 1 downTo 0) {
            students += S[j + 1]
            if (students > C) break

            val floor = F[j + 1]
            mask = mask or (1 shl floor)
            if (floor > maxFloor) maxFloor = floor

            val stops = mask.countOneBits()
            val tripCost = if (i == N) maxFloor + stops
            else maxFloor * 2 + stops

            val totalCost = dp[j] + tripCost
            if (totalCost < dp[i]) dp[i] = totalCost
        }
    }
    print(dp[N])
}
