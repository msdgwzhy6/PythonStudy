/**
 * Created by yutianran on 16/4/2.
 */
function calc(BMI) {
    if (BMI < 18.5) {
        res = "偏瘦"
    } else if (BMI >= 18.5 && BMI < 25) {
        res = "正常体重"
    } else if (BMI >= 25 && BMI < 30) {
        res = "偏胖"
    } else if (BMI >= 30 && BMI < 35) {
        res = "轻度肥胖"
    } else if (BMI >= 35 && BMI < 40) {
        res = "中度肥胖"
    } else (BMI >= 40)
    {
        res = "重度肥胖"
    }
    return res
}
