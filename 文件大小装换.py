import tkinter as tk

def convert_size(size_bytes, unit=None):
    """
    将文件大小从字节转换为更大单位（如KB、MB、GB、TB、PB、EB、ZB、YB、BB、NB、DB等）
    :param size_bytes: 文件大小（以字节为单位）
    :param unit: 要转换的单位，默认为None，自动选择最适合的单位
    :return: 转换后的字符串
    """
    units = {"B": 0, "KB": 1, "MB": 2, "GB": 3, "TB": 4, "PB": 5, "EB":6, "ZB": 7, "YB": 8, "BB": 9, "NB": 10, "DB": 11,}
    if unit is not None and unit not in units:
        raise ValueError(f"Invalid unit: {unit}")

    if unit:
        target_unit = units[unit]
    else:
        target_unit = max(units.values())

    size = size_bytes
    for i in range(target_unit):
        size /= 1024

    return f"{size:.2f} {list(units.keys())[int(target_unit)]}"

def get_file_size():
    """
    从输入框中获取文件大小，并将其转换为用户指定的单位
    """
    file_size_str = file_size_entry.get()
    try:
        file_size_bytes = int(file_size_str)
    except ValueError:
        result_label.config(text="无效请重新输入")
        return

    # 调用 convert_size 函数进行单位转换
    converted_size = convert_size(file_size_bytes, unit=unit_var.get())

    # 更新结果标签
    result_label.config(text=f"文件大小为: {converted_size}")

# 创建窗口并添加部件
window = tk.Tk()
window.title("文件大小计算器")

file_size_label = tk.Label(window, text="请输入文件大小(字节/b):")
file_size_label.pack()

file_size_entry = tk.Entry(window)
file_size_entry.pack()

unit_frame = tk.Frame(window)
unit_frame.pack()

unit_var = tk.StringVar()
unit_var.set("B")

b_radio = tk.Radiobutton(unit_frame, text="B", variable=unit_var, value="B")
kb_radio = tk.Radiobutton(unit_frame, text="KB", variable=unit_var, value="KB")
mb_radio = tk.Radiobutton(unit_frame, text="MB", variable=unit_var, value="MB")
gb_radio = tk.Radiobutton(unit_frame, text="GB", variable=unit_var, value="GB")
tb_radio = tk.Radiobutton(unit_frame, text="TB", variable=unit_var, value="TB")
pb_radio = tk.Radiobutton(unit_frame, text="PB", variable=unit_var, value="PB")
eb_radio = tk.Radiobutton(unit_frame, text="EB", variable=unit_var, value="EB")
zb_radio = tk.Radiobutton(unit_frame, text="ZB", variable=unit_var, value="ZB")
yb_radio = tk.Radiobutton(unit_frame, text="YB", variable=unit_var, value="YB")
bb_radio = tk.Radiobutton(unit_frame, text="BB", variable=unit_var, value="BB")
nb_radio = tk.Radiobutton(unit_frame, text="NB", variable=unit_var, value="NB")
db_radio = tk.Radiobutton(unit_frame, text="DB", variable=unit_var, value="DB")

b_radio.pack(side="left")
kb_radio.pack(side="left")
mb_radio.pack(side="left")
gb_radio.pack(side="left")
tb_radio.pack(side="left")
pb_radio.pack(side="left")
eb_radio.pack(side="left")
zb_radio.pack(side="left")
yb_radio.pack(side="left")
bb_radio.pack(side="left")
nb_radio.pack(side="left")
db_radio.pack(side="left")

convert_button = tk.Button(window, text="确认", command=get_file_size)
convert_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()