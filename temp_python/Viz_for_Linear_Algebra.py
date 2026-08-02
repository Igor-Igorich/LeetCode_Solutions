import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 1. Задаем базисные векторы
# Правая тройка (Стандартный декартов базис: e1, e2, e3)
a_right = np.array([1, 0, 0])  # Оси X
b_right = np.array([0, 1, 0])  # Оси Y
c_right = np.array([0, 0, 1])  # Оси Z

# Левая тройка (Меняем местами первые два вектора: b, a, c)
a_left = np.array([0, 1, 0])
b_left = np.array([1, 0, 0])
c_left = np.array([0, 0, 1])

# Проверка знака определителя (ориентации)
det_right = np.linalg.det(np.column_stack((a_right, b_right, c_right)))
det_left = np.linalg.det(np.column_stack((a_left, b_left, c_left)))

# 2. Создаем шаблон для отрисовки 3D-векторов (стрелок)
def add_vector_3d(fig, start, end, color, name, row, col):
    # Рисуем линию (тело вектора)
    fig.add_trace(go.Scatter3d(
        x=[start[0], end[0]], y=[start[1], end[1]], z=[start[2], end[2]],
        mode='lines', line=dict(color=color, width=6), name=name, showlegend=True if row==1 and col==1 else False
    ), row=row, col=col)
    
    # Рисуем конус (наконечник вектора)
    fig.add_trace(go.Cone(
        x=[end[0]], y=[end[1]], z=[end[2]],
        u=[end[0]-start[0]], v=[end[1]-start[1]], w=[end[2]-start[2]],
        colorscale=[[0, color], [1, color]], showscale=False, sizemode='absolute', sizeref=0.15
    ), row=row, col=col)

# 3. Настраиваем субплоты (2 сцены рядом)
fig = make_subplots(
    rows=1, cols=2,
    specs=[[{'type': 'scene'}, {'type': 'scene'}]],
    subplot_titles=(
        f"Правая тройка (Положительная)<br>det(A) = {det_right:+.1f}",
        f"Левая тройка (Отрицательная)<br>det(A) = {det_left:+.1f}"
    )
)

# Строим Правую тройку (Столбец 1)
add_vector_3d(fig, [0,0,0], a_right, 'red', 'Вектор 1 (a)', 1, 1)
add_vector_3d(fig, [0,0,0], b_right, 'green', 'Вектор 2 (b)', 1, 1)
add_vector_3d(fig, [0,0,0], c_right, 'blue', 'Вектор 3 (c)', 1, 1)

# Строим Левую тройку (Столбец 2)
add_vector_3d(fig, [0,0,0], a_left, 'red', 'Вектор 1 (a)', 1, 2)
add_vector_3d(fig, [0,0,0], b_left, 'green', 'Вектор 2 (b)', 1, 2)
add_vector_3d(fig, [0,0,0], c_left, 'blue', 'Вектор 3 (c)', 1, 2)

# 4. Оформление осей и общего макета
scene_config = dict(
    xaxis=dict(range=[-0.2, 1.2], title='X', backgroundcolor="rgb(240, 240, 240)"),
    yaxis=dict(range=[-0.2, 1.2], title='Y', backgroundcolor="rgb(230, 230, 230)"),
    zaxis=dict(range=[-0.2, 1.2], title='Z', backgroundcolor="rgb(220, 220, 220)"),
    aspectmode='cube'
)

fig.update_layout(
    title_text="Визуализация ориентации базисов в ℝ³",
    title_x=0.5,
    width=1100, height=600,
    scene=scene_config,
    scene2=scene_config,
    template="plotly_white"
)

# Отображаем график в браузере
fig.show()