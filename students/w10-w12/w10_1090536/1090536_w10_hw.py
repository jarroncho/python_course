import tensorflow as tf
from datetime import datetime
import os
# 定義一個簡單的函數來加三個數字
@tf.function
def add_three_numbers(num1, num2, num3):
    return (num1 + num2) + num3

# 為 TensorBoard 建立摘要寫入器
log_directory = "logs/" + datetime.now().strftime("%Y%m%d-%H%M%S")
summary_writer = tf.summary.create_file_writer(log_directory)

# 使用 tf.summary.trace_on 來追蹤圖表
tf.summary.trace_on(graph=True, profiler=True)

# 使用範例值呼叫函數
value1 = tf.constant(3.0, dtype=tf.float32)
value2 = tf.constant(4.0, dtype=tf.float32)
value3 = tf.constant(5.0, dtype=tf.float32)

sum_result = add_three_numbers(value1, value2, value3)

# 使用 tf.summary.trace_export 將圖表儲存到 TensorBoard
with summary_writer.as_default():
    tf.summary.trace_export(name="graph_trace_1", step=0, profiler_outdir=log_directory)

# 印出結果
print(f'{value1.numpy()}、{value2.numpy()} 和 {value3.numpy()} 的總和是：{sum_result.numpy()}')
full_path = os.path.abspath(log_directory)
print(full_path)


# 若要啟動 TensorBoard，請在終端機中使用以下命令：
# tensorboard --logdir=實際的日誌目錄路徑
# 將 "實際的日誌目錄路徑" 替換為你的日誌目錄的實際路徑。
